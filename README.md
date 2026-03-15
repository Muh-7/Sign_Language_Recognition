# Real-Time Sign Language Recognition using MobileNetV3

A real-time **Sign Language Recognition System** built using **Python, OpenCV, TensorFlow, and MobileNetV3**.

The system detects hand gestures from a webcam and classifies them into **sign language digits (0–10)** in real time.

This project demonstrates how **Computer Vision and Deep Learning** can be used to enable communication through hand gestures.

Sign language recognition systems aim to bridge the communication gap between hearing-impaired individuals and others by automatically interpreting hand gestures using machine learning models. :contentReference[oaicite:0]{index=0}

---

# Project Demo

The system works in real time using a webcam.

Pipeline:

Camera → ROI Detection → Segmentation → Preprocessing → MobileNet Model → Prediction → Display Result

Example predictions:

0 → zero  
1 → one  
2 → two  
3 → three  
4 → four  
5 → five  
6 → six  
7 → seven  
8 → eight  
9 → nine  
10 → ten  

---

# Features

• Real-time gesture recognition  
• Hand segmentation using OpenCV  
• Custom dataset collected using webcam  
• Deep learning classification model  
• Transfer learning using MobileNetV3  
• Data augmentation for better generalization  

---

# Dataset

A custom dataset was created manually using a webcam.

## Data Collection Process

1. Define a **Region Of Interest (ROI)**.
2. Place the hand inside the ROI.
3. Press **SPACE** to capture an image.
4. Press **ENTER** to switch to the next sign.
5. Repeat for all gestures.

## Dataset Statistics

Number of classes: **11**

Classes:
0,1,2,3,4,5,6,7,8,9,10

Images per class:
500 images → left hand
500 images → right hand

Total images per class: 1000 images

Total dataset size: 11000 images

Data augmentation was applied to increase dataset diversity and improve model performance.

---

# Model

The system uses **MobileNetV3 with transfer learning**.

MobileNetV3 is a lightweight convolutional neural network designed for efficient image recognition tasks and real-time applications. :contentReference[oaicite:1]{index=1}

## Training configuration
Optimizer: Adam
Learning Rate: 0.0001
Loss Function: categorical_crossentropy
Epochs: 3 – 15

---

# Technologies Used

Python  
OpenCV  
TensorFlow / Keras  
NumPy  
Matplotlib  

OpenCV is widely used for real-time computer vision applications such as gesture recognition and video processing. :contentReference[oaicite:2]{index=2}

---

# Project Pipeline
Camera Input
    ↓
Region Of Interest (ROI)
    ↓
Background Subtraction
    ↓
Hand Segmentation
    ↓
Image Preprocessing
    ↓
MobileNetV3 Model
    ↓
Gesture Prediction
    ↓
Display Result

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/sign-language-recognition.git

pip install -r requirements.txt

python main.py
```
Controls:
```
SPACE → capture image
ENTER → change sign class
ESC → exit
```

sign-language-recognition
│
├── dataset
│   ├── train
│   └── test
│
├── model
│   └── mobilenet_model.h5
│
├── sign_language.ipynb
│
├── main.py
│
└── README.md

# Future Improvements

• Add alphabet recognition (A–Z)
• Add dynamic gesture recognition
• Support full sign language words
• Deploy as a web or mobile application

Author

Muhammad Alsehoum

Computer Engineering Student
AI & Machine Learning Enthusiast
Python Developer
<<<<<<< HEAD

=======
>>>>>>> 3b4c77591b3c87ad6a846c86559e5ef5d0acf72c
