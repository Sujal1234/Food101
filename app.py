# import gdown

# url = 'https://drive.google.com/file/d/1ZGEnLM7KD0DrzsR1Cj_0-2PIrFB2uYdj/view?usp=sharing'
# output = "MobileNetV2Tuned.keras"

# gdown.download(url, output, quiet=False)

import streamlit as st
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

IMG_SIZE = (224, 224)

def predict(image_file, model):
  img = image.load_img(image_file, target_size=IMG_SIZE)
  img = image.img_to_array(img)
  img = img / 255.0
  img = np.expand_dims(img, axis=0)

  class_names = {0: 'burger', 1: 'butter naan', 2: 'chai', 3: 'chapati', 4: 'chole bhature', 5: 'dal makhani', 6: 'dhokla', 7: 'fried rice', 8: 'idli', 9: 'jalebi', 10: 'kadhai paneer', 11: 'kathi roll', 12: 'kulfi', 13: 'masala dosa', 14: 'momos', 15: 'paani puri', 16: 'pakode', 17: 'pav bhaji', 18: 'pizza', 19: 'samosa'}

  prediction = model.predict(img)

  predicted_class = class_names[np.argmax(prediction)]
  confidence = np.max(prediction) * 100
  return (confidence, predicted_class)

saved_model = keras.models.load_model("MobileNetV2Tuned.keras")

st.title('Upload an Indian food image')
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    conf, pred = predict(uploaded_image, saved_model)

    st.write(f"I am {conf:.2f}% sure that this is {pred}.")
