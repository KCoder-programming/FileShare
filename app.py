__version__ = 'v1.0.0'

from flask import Flask, render_template, request, redirect
from os import path, listdir, makedirs, remove
from qrcode import make
from werkzeug.utils import secure_filename
from urllib.parse import unquote
from threading import Thread
from time import sleep
import webview
import socket
import sys


def get_local_ipv4_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return path.join(sys._MEIPASS, relative_path)
    return path.join(path.abspath("."), relative_path)

def run_app(ip):
    app.run(port=5000, host=ip)


app = Flask(__name__, static_folder=get_resource_path("static"), template_folder=get_resource_path("templates"))

@app.route('/')
def home():
    folder = get_resource_path(path.join("static", "uploaded_files"))
    if not path.exists(folder):
        makedirs(folder)
    files = listdir(folder)

    local_ip = request.url_root

    # Generate QR Code
    qr = make(local_ip, border=1, error_correction=1)
    qr.save(get_resource_path(path.join("static", "qr.png")), format="PNG")

    return render_template("base.html", files=files, local_ip=local_ip)

@app.route('/delete/<file>')
def delete(file):
    filename = secure_filename(unquote(file))

    full_path = get_resource_path(path.join("static", "uploaded_files", filename))

    if path.exists(full_path):
        remove(full_path)
        return redirect('/')
    else:
        return(f"The file '{file}' does not exist.<br><a href='/'>Home</a>")  

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/upload')
def upload():
    return render_template("upload.html")

@app.route('/upload/submit', methods = ["POST"])
def upload_submit():
    files = request.files.getlist('file')
    for file in files:
        if file and file.filename !="":
            filename = secure_filename(file.filename)
            name, ext = path.splitext(filename)
            counter = 1
            while path.exists(get_resource_path(path.join("static", "uploaded_files", filename))):
                filename = f"{name}({counter}){ext}"
                counter += 1
            file.save(get_resource_path(path.join("static", "uploaded_files", filename)))
    return redirect('/')

if __name__=="__main__":
    ip = get_local_ipv4_address()
    Thread(target=run_app, daemon=True, args=(ip,)).start()

    sleep(1)
    webview.create_window('FileShare', f"http://{ip}:5000/")
    webview.start(icon=get_resource_path(path.join("static", "icon.ico")), gui='edgechromium')