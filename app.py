from flask import Flask, request, render_template, url_for 
import qrcode
from PIL import Image
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=["POST", "GET"])
def result():
    if request.method == "POST":
        input = request.form
        data = input["text-input"]
        filename = input["filename-input"]

        # Convert
        qr = qrcode.QRCode(
                version = 5,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size = 10,
                border = 5
                )

        # adding data
        qr.add_data(data)
        img = qr.make_image(fill="black", back_color="white")

        # saving result
        img.save(filename)

        return render_template('result.html', )


if __name__ == "__main__":
    app.run(debug=True)