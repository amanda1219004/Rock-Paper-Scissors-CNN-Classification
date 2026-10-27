import streamlit as st
import prediction 

page = st.sidebar.selectbox(
    'Select Page',
    ('Main', 'Prediction')
)

if page == 'Main':

    st.title('Rock Paper Scissor Hand Gesture Classification')
    st.write(
        '''
        This application uses a Convolutional Neural Network (CNN)
        to classify hand gesture images into three classes:
        Paper, Rock, and Scissors. 
        '''
    )

else :
    prediction.run()
