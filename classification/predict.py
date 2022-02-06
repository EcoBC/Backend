import cv2
import numpy as np
import os

# Image Recycling Prediction Model
def predict(rawImage, file_extension, model):
    filename = "image" + file_extension
    with open(filename, "wb") as f:
        f.write(rawImage)
    image = cv2.imread(filename)
    os.remove(filename)
    image = cv2.resize(image,(224,224))
    image = np.array(image, dtype=np.float32)
    image = image/255
    image = np.expand_dims(image, axis=0) # None,224,224,3
    class_dict = {0:"can", 1:"chips_packets", 2:"paper_bag", 3:"plastic_bottle"}
    x = model.predict(image)
    argmax = np.argmax(x[0])
    mx = max(x[0])
    sum = np.sum(x)
    accuracy = (mx/sum)*100
    predicted_dict = {"item":class_dict[argmax], "certainty": accuracy/100}
    return predicted_dict