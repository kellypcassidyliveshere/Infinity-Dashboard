from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__, template_folder='.')
UPLOAD_FOLDER = 'uploads'

# Create the uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/')
def dashboard():
    return render_template('infinitylink.html')

@app.route('/programs.html')
def programs():
    return render_template('programs.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'certificate' not in request.files:
        return "No file part", 400
    
    file = request.files['certificate']
    program_name = request.form.get('program_name', 'unknown')

    if file.filename == '':
        return "No selected file", 400

    if file:
        # Save file with Program Name prefix
        filename = f"{program_name}_{file.filename}"
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return f"<h1>Success!</h1><p>{program_name} certificate saved.</p><a href='/programs.html'>Back to Programs</a>"

@app.route('/admin-vault')
def admin_vault():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('admin-vault.html', files=files)

if __name__ == '__main__':
    # Switching to 8082 to avoid the port conflict
    app.run(host='0.0.0.0', port=8082)
