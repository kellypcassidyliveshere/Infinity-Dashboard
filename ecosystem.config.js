module.exports = {
  apps: [
    {
      name: "Infinity-Link-App",
      script: "python",
      args: "-m http.server 8083",
      cwd: "/data/data/com.termux/files/home/infinity-dashboard",
      watch: true
    },
    {
      name: "Foundation-Project-Web",
      script: "python",
      args: "-m http.server 8080",
      cwd: "/data/data/com.termux/files/home/official_foundation_site",
      watch: true
    },
    {
      name: "Cloudflare-Tunnel",
      script: "cloudflared",
      args: "tunnel run --protocol http2 infinity-bridge-v2",
      watch: false
    }
  ]
};
