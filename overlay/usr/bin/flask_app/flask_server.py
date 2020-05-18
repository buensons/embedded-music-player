from flask import Flask, render_template
import os
from flask import jsonify, request, send_file, flash, redirect
from werkzeug.utils import secure_filename
from os.path import isfile, join
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
FILE_DIR = "/music/"
ERROR = False
authenticated = False

def allowed_file(filename):
    return '.' in filename and '/' not in filename

@app.route('/files')
def load_files():
    return jsonify([f for f in os.listdir(FILE_DIR) if isfile(join(FILE_DIR, f))])

@app.route('/download', methods=['POST'])
def get_file():
    try:
        file = request.form.get("file")
        return send_file(FILE_DIR + file, as_attachment=True, attachment_filename=file)
    except Exception as e:
        return str(e)

@app.route('/delete', methods=['POST'])
def remove_file():
    try:
        file = request.form.get("file")
        os.remove(FILE_DIR + file)
        return redirect("/admin")
    except Exception as e:
        return str(e)

@app.route("/login", methods=['POST'])
def login():
    user = request.form.get('user')
    password = request.form.get('password')

    global authenticated

    if(user == 'admin' and password == 'admin'):
        authenticated = True
        return redirect("/admin")
    else:
        return redirect("/")

@app.route("/logout")
def logout():
    global authenticated
    authenticated = False
    return redirect("/")

@app.route('/admin')
def admin():
    if(authenticated):
        global ERROR
        return render_template('loggedin.html', error = ERROR)
    else:
        return redirect("/")

@app.route('/')
def splash_page():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if(authenticated):
        global ERROR

        if 'file' not in request.files:
            ERROR = True
            return redirect("/admin")

        file = request.files['file']

        if file.filename == '':
            ERROR  = True
            return redirect("/admin")

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(FILE_DIR, filename))
            ERROR = False
        
        return redirect("/admin")
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8080)




