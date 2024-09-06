from flask import Flask, render_template, request, send_file
import cv2
import numpy as np
from skimage import exposure, restoration
from PIL import Image
import io

app = Flask(__name__)

def enhance_contrast(image):
    """ Apply adaptive histogram equalization to enhance contrast. """
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    return cv2.cvtColor(limg, cv2.COLOR_Lab2BGR)

def reduce_noise(image):
    """ Apply Non-Local Means denoising. """
    return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

def process_image(file):
    """ Process the uploaded image. """
    in_memory_file = io.BytesIO(file.read())
    image = np.array(Image.open(in_memory_file))

    # Stage 1: Contrast Enhancement
    image = enhance_contrast(image)

    # Stage 2: Noise Reduction
    image = reduce_noise(image)

    return image

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        processed_image = process_image(file)
        in_memory_output = io.BytesIO()
        Image.fromarray(processed_image).save(in_memory_output, format='PNG')
        in_memory_output.seek(0)
        return send_file(in_memory_output, mimetype='image/png', as_attachment=True, download_name='enhanced_image.png')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
