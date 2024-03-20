from pyngrok import ngrok
import streamlit as st
import pandas as pd
import tensorflow as tf
## from PLT import Image
import numpy as np
from IPython.display import display, Image

from keras.models import load_model

data_cat = ['apple',
 'banana',
 'beetroot',
 'bell pepper',
 'cabbage',
 'capsicum',
 'carrot',
 'cauliflower',
 'chilli pepper',
 'corn',
 'cucumber',
 'eggplant',
 'garlic',
 'ginger',
 'grapes',
 'jalepeno',
 'kiwi',
 'lemon',
 'lettuce',
 'mango',
 'onion',
 'orange',
 'paprika',
 'pear',
 'peas',
 'pineapple',
 'pomegranate',
 'potato',
 'raddish',
 'soy beans',
 'spinach',
 'sweetcorn',
 'sweetpotato',
 'tomato',
 'turnip',
 'watermelon']


st.title("Image classifier using machine learning")
st.text("upload an image to classify")

model =load_model('Model.h5')


uploaded_file = st.file_uploader("choose an image...",type="jpg")

if uploaded_file is not None:
    ##img = Image.open(uploaded_file)
    ##display(Image(filename= uploaded_file))

    st.image(uploaded_file,caption="uploaded image")
    if st.button("Predict"):
        img_width = 180
        img_height = 180
        image = tf.keras.utils.load_img(uploaded_file, target_size=(img_height, img_width))
        img_arr = tf.keras.utils.array_to_img(image)
        img_bat = tf.expand_dims(img_arr, 0)
        predict = model.predict(img_bat)
        score = tf.nn.softmax(predict)
        st.write('Veg/Fruit in image is {} with accuracy of {:0.2f}'.format(data_cat[np.argmax(score)], np.max(score) * 100))




