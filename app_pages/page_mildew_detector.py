import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_predictions_probabilities
)


def page_mildew_detector_body():
    """
    This function shows mildew detector page

    """

    st.header("Powdery Mildew Detection")
    st.success(
        f"**Business Requirement 2**\n"
        f" The client is interested in predicting whether or not a cherry leaf"
        f" contains powdery mildew")

    st.write('---')

    st.info(
        f"* Download a set of leaves containing both powdery mildew or healthy leaves for live prediction. "
        f" Images can be downloaded from [kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves)"
    )
    st.write(
        f"**Upload a clear picture of a cherry leaf for live predictions. You may select more than one.**"
    )
    images_buffer = st.file_uploader(' ',
                                     accept_multiple_files=True)

    st.write(
        f" Click the **Make Prediction** button for prediction results"
    )
    predict_button = st.button("Make Prediction")

    if predict_button:
        make_live_predict(images_buffer)
