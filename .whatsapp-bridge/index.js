const { default: makeWASocket, useMultiFileAuthState } = require("@whiskeysockets/baileys");
const qrcode = require("qrcode-terminal");

async function startInfinityBridge() {
    const { state, saveCreds } = await useMultiFileAuthState('auth_info');
    
    const sock = makeWASocket({
        auth: state,
        printQRInTerminal: false // We will handle the QR manually for Termux
    });

    sock.ev.on('creds.update', saveCreds);

    sock.ev.on('connection.update', (update) => {
        const { connection, qr } = update;
        
        // This draws the QR code manually so you can see it in Termux
        if(qr) {
            console.log("SCAN THIS QR CODE WITH WHATSAPP:");
            qrcode.generate(qr, {small: true});
        }
        
        if(connection === 'open') {
            console.log("Infinity Link Bridge is ONLINE!");
        }
    });

    sock.ev.on('messages.upsert', async m => {
        const msg = m.messages[0];
        if (!msg.key.fromMe && msg.message?.conversation?.toLowerCase() === 'menu') {
            const menu = "🍹 *Juice Bar Menu* 🍹\n1. Kaleb Moon\n2. Maia Gold\n3. Ruby Rush\n4. Hulk Mode (Matcha/Pistachio)\n\nWelcome to The Foundation Project!";
            await sock.sendMessage(msg.key.remoteJid, { text: menu });
        }
    });
}

startInfinityBridge();
