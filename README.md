# Dog breed classifier

This project aims to classify images of dogs into their respective breeds using a Convolutional Neural Network (CNN) built with TensorFlow and Keras. The model is trained on a dataset of dog images and can predict the breed of a given dog image.
Can distinguish between 11 breeds of dogs, namely: Beagle, Boxer, Bulldog, Dachshund, German Shepherd, Golden Retriever, Husky, Labrador Retriever, Poodle, Rottweiler, and Yorkshire Terrier with a *0.92 accuracy* and *0.249 loss*
(more breeds can be added with sufficient data)

### Key Features

- **Convolutional Neural Network (CNN)**: Utilizes a CNN architecture with multiple convolutional and pooling layers to extract features from images.
- **Multi-Class Classification**: Capable of classifying images into one of several dog breeds.
- **Data Augmentation**: Employs data augmentation techniques to improve model generalization and performance.
- **Model Training and Evaluation**: Includes scripts for training the model on a dataset and evaluating its performance.
- **Prediction**: Provides functionality to predict the breed of a dog from a new image using the trained model.

### Technologies Used

- **TensorFlow and Keras**: For building and training the deep learning model.
- **OpenCV**: For image processing and augmentation.
- **NumPy**: For numerical operations and data manipulation.
- **Matplotlib**: For visualizing training progress and results.

### Dataset

The dataset used for training the model consists of images of dogs categorized by breed. 
It was found on Kaggle and more images were added to it : https://www.kaggle.com/datasets/khushikhushikhushi/dog-breed-image-dataset

### Model Architecture

The CNN model architecture includes the following layers:

- **Convolutional Layers**: Extract spatial features from the input images.
- **Max-Pooling Layers**: Reduce the spatial dimensions and retain important features.
- **Dropout Layers**: Prevent overfitting by randomly setting a fraction of input units to zero during training.
- **Fully Connected Layers**: Combine the extracted features to make final predictions.
- **Softmax Output Layer**: Outputs a probability distribution over the dog breed classes.
