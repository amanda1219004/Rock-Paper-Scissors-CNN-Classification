import os
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import gdown

folder_base = os.path.dirname(
    os.path.abspath(__file__)
)
                                        #path
model_path = os.path.join(
    folder_base,
    'rps_model.keras'
)

@st.cache_resource
def load_my_model():
    

    # URL Google Drive file
    drive_url = "https://drive.google.com/file/d/1yunbIiiwwPTnsyJ3r-QfJe0jqelSkTzK/view?usp=sharing"
    local_path = "nama_model.keras"

    # download hanya kalau file belum ada
    if not os.path.exists(local_path):
        gdown.download(drive_url, local_path, quiet=False)

    model = tf.keras.models.load_model(local_path)
    return model
model = load_my_model()

class_labels = [
    'paper',
    'rock',                                         #class labels
    'scissors'
]

def run():

    st.title(
        'Rock Paper Scissors Prediction'
    )

    st.write(
        '''
        Upload an image of a hand gesture
        to predict whether it is Paper,
        Rock, or Scissors.
        '''
    )

   
    uploaded_file = st.file_uploader(
        'Upload Image',                             #upload image
        type=['jpg', 'jpeg', 'png']
    )


    if uploaded_file is not None:

        
        image = Image.open(
            uploaded_file                       # Load image
        ).convert('RGB')

        st.subheader(
            'Uploaded Image'
        )                                               #display image

        st.image(
            image,
            width=300
        )

        image_resized = image.resize(
            (150, 150)
        )

        image_array = np.array(
            image_resized                           #preprocessin image
        ).astype('float32')

        image_array = (
            image_array / 255.0
        )

        image_array = np.expand_dims(
            image_array,
            axis=0
        )

                                                    # Prediction
        prediction = model.predict(
            image_array,
            verbose=0
        )[0]

        predicted_index = np.argmax(
            prediction
        )

        predicted_class = class_labels[
            predicted_index
        ]

        confidence = prediction[
            predicted_index
        ]

        st.success(
            f'Prediction: {predicted_class.upper()}'    #result
        )

if __name__ == '__main__':
    run()