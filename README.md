# Feynman Diagrams Classification

## Introduction
Feynman diagrams are fundamental tools in particle physics, representing subatomic interactions within the Standard Model framework. Understanding these diagrams is essential for studying electromagnetic, weak, and strong interactions. However, analyzing them can be challenging, especially for students learning quantum field theory.

This project aims to develop a machine learning model capable of classifying six types of Feynman diagrams. The goal is to assist students and researchers in recognizing and understanding these diagrams more effectively.

## Features
- **Machine Learning Classification**: Uses a neural network model to classify Feynman diagrams.
- **Image Processing**: Utilizes TensorFlow and Keras for image preprocessing and augmentation.
- **Web Deployment**: Supports TensorFlow.js for browser-based inference.

## Installation
To run this project, install the necessary dependencies:

```sh
pip install tensorflow keras tensorflowjs numpy pandas matplotlib scikit-learn pillow
```

If using Google Colab, mount Google Drive to access data:

```python
from google.colab import drive
drive.mount('/content/drive')
```

## Usage
1. Prepare the dataset of Feynman diagrams.
2. Train the model using TensorFlow and Keras.
3. Evaluate model performance and fine-tune hyperparameters.
4. Convert the trained model to TensorFlow.js format for deployment.

Run the notebook step-by-step to execute each phase of the classification process.

## Technologies Used
- Python
- TensorFlow & Keras
- Scikit-learn
- Matplotlib
- TensorFlow.js