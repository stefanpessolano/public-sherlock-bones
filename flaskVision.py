from flask import Flask, render_template, request, redirect, url_for
import vision 
import os 

app = Flask(__name__)

info = []

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]

            if image.filename == "":
                return redirect(request.url)

            info = vision.upload(image.stream)

            return render_template('results.html',info=info)
    return render_template('home.html')


if __name__ == '__main__':
    app.run()