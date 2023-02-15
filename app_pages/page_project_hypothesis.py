import streamlit as st


def project_hypothesis_page_body():
    """ Function to display project hypothesis page """

    st.header("### Project Hypothesis and Validation")

    st.info(
        f"* 1 - Cherry Leaves infected with powdery mildew have white, powdery spots or "
        f"patches on the top side of  leaves or on plant stems."
        f" 2 -The powdery surface growth gradually spreads to cover the entire"
        f" leaf, including the undersides, until the plant looks like it's "
        f"dusted with white powder.\n"
        f" 3- We believe that these types of features should be sufficient"
        f" to differentiate a healthy leaf and an infected "
        f" leaf.\n"
        f" 4- The ML model will be able to distinguish between a healthy cherry leaf "
        f" and an infected cherry leaf with at least 97% accuracy.\n"
    )

    st.success(
        f"* 1- We believe that Cherry leaves infected with powdery mildew have a white colour/ lighter "
        f"blotches in the leaf and also distorted edges  making them appear significantly different from healthy leaf. \n"

        f"* 2- An Image Montage shows the evident difference "
        f"between both kinds of leaves.\n"

        f" 3 - Average Image, Variability Image and Difference confirmed the hypothesis "
        f" showing color difference within the center of each leaf image however; "
        f" there were no patterns to identify them by shape."

        f" 4 - ML pipeline performance was evaluated and it differentiates a healthy leaf and an infected leaf "
        f" with at least 97% accuracy.\n\n"
    )
