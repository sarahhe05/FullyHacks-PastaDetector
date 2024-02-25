from keras.models import load_model  # TensorFlow is required for Keras to work
from keras.utils import img_to_array
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

#Model Code

model = load_model('converted_keras/keras_model.h5')

# Preparing and pre-processing the image
def preprocess_img(img_path):
    op_img = Image.open(img_path)
    img_resize = op_img.resize((224, 224))
    img2arr = img_to_array(img_resize) / 255.0
    img_reshape = img2arr.reshape(1, 224, 224, 3)
    return img_reshape
# Load the labels
class_names = open("D:/Code/FullyHacks/converted_keras/labels.txt", "r").readlines()
# Predicting function
def predict_result(predict):
    pred = model.predict(predict)
    class_index = np.argmax(pred[0], axis=-1)
    class_name = class_names[class_index]
    confidence_score = pred[0][class_index]
    return class_name, confidence_score