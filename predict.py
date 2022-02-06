import cv2
import numpy as np
import json
model = tf.keras.models.load_model("drive/MyDrive/recycle_dataset/model.h5")
image = cv2.imread('drive/MyDrive/recycle_dataset/Can/can020.jpg')
image = cv2.resize(image,(224,224))
image = np.array(image, dtype=np.float32)
image = image/255
image = np.expand_dims(image, axis=0) # None,224,224,3
class_dict = {0:"can", 1:"chips_packets", 2:"paper_bag", 3:"plastic_bottle"}
# print(class_dict)
x = model.predict(image)
print(x)
argmax = np.argmax(x[0])
# print(np.argmax(x[0]))
# print(max(x[0]))
mx = max(x[0])
sum = np.sum(x)
accuracy = (mx/sum)*100
predicted_dict = {"item":class_dict[argmax], "certainity": accuracy/100}
predicted_json = json.dumps(predicted_dict, indent = 4)
print(predicted_json)