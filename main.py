import cv2
import numpy as np
import tensorflow as tf



model = tf.keras.models.load_model("model/sign_language_model.h5")

#labels
classes = {
0:"zero",
1:"one",
2:"two",
3:"three",
4:"four",
5:"five",
6:"six",
7:"seven",
8:"eight",
9:"nine",
10:"ten"
}

# ROI Region of interest
TOP = 50
RIGHT = 350
BOTTOM = 300
LEFT = 600



cap = cv2.VideoCapture(0)

print("Camera started...")

while True:

    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame,1)

    
    cv2.rectangle(frame,(RIGHT,TOP),(LEFT,BOTTOM),(0,255,0),2)

    roi = frame[TOP:BOTTOM, RIGHT:LEFT]

    # preprocessing
    img = cv2.resize(roi,(224,224))
    img = img.astype("float32")/255.0
    img = np.expand_dims(img,axis=0)

    # prediction
    preds = model.predict(img,verbose=0)
    class_id = np.argmax(preds)
    label = classes[class_id]

    
    cv2.putText(frame,
                "Prediction: "+label,
                (10,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2)

    cv2.imshow("Sign Language Recognition",frame)

    key = cv2.waitKey(1) & 0xFF

    if key == 27:   # ESC
        break

cap.release()
cv2.destroyAllWindows()
