# Dog Breed Classifier

This is a Flask web application that allows users to upload an image of a dog and predicts the breed of the dog using a pre-trained model.

## Features

- Upload an image of a dog
- Predict the breed of the dog using a pre-trained model
- Display the predicted breed on the web page

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. **Clone the Repository**:

git clone https://github.com/Sc02/Dog_breed_classifier
cd Dog_breed_classifier


2. **Create a Virtual Environment**:

python -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate


3. **Install Dependencies**:

Install the required Python packages using `pip`:
   
pip install -r requirements.txt


4. **Download the Model File**:

   Ensure the model file `dog_breed_classifier.h5` is in the project directory. If it's not included in the repository, you may need to download it separately and place it in the project directory.

## Running the Application

1. **Start the Flask App**:
python app.py


2. **Access the Application**:

Open your web browser and go to `http://127.0.0.1:5000/` to access the application.

## Project Structure

- **app.py**: The main Flask application file.
- **requirements.txt**: List of dependencies.
- **Procfile**: Specifies the command to run the app (used for deployment).
- **dog_breed_classifier.h5**: The pre-trained model file.
- **static/**: Directory containing static files (e.g., CSS).
- **templates/**: Directory containing HTML templates.
