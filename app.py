from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os

app = Flask(__name__)

# Load the model
model = load_model('dog_breed_classifier.h5')
categories = ["Beagle", "Boxer", "Bulldog", "Dachshund", "German Shepherd", "Golden Retriever", "Husky", "Labrador Retriever", "Poodle", "Rottweiler", "Yorkshire Terrier"]

def prepare_image(filepath, img_size=70):
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (img_size, img_size))
    new_array = new_array.reshape(-1, img_size, img_size, 1)
    new_array = new_array / 255.0
    return new_array

def predict_breed(filepath):
    prepared_image = prepare_image(filepath)
    prediction = model.predict(prepared_image)
    breed_index = np.argmax(prediction)
    breed_name = categories[breed_index]
    return breed_name

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        filepath = os.path.join('uploads', file.filename)
        file.save(filepath)
        breed_name = predict_breed(filepath)
        return breed_name

if __name__ == "__main__":
    app.run(debug=True)