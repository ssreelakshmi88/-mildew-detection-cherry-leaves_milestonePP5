import streamlit as st


def project_hypothesis_page_body():
    """ Function to display project hypothesis page """

    st.header("Project Hypothesis and Validation")

    st.info(
        f"* Cherry Leaves infected with powdery mildew have white, "
        f" powdery spots or "
        f" patches on the top side of  leaves or on plant stems.\n"
        f"* The powdery surface growth gradually spreads to cover the entire"
        f" leaf, including the undersides, until the plant looks like it's "
        f" dusted with white powder.\n"
        f"* We believe that these types of features should be sufficient"
        f" to differentiate a healthy leaf from an infected "
        f" leaf.\n"
        f"* The ML model will be able to distinguish "
        f" between a healthy cherry leaf and an infected cherry leaf "
        f" with at least 97% accuracy.\n"
    )

    st.success(
        f"* We believe that Cherry leaves infected with "
        f" powdery mildew have a white colour/ lighter "
        f" blotches in the leaf and also distorted edges "
        f" making them appear significantly different from healthy leaf. \n"

        f"* An Image Montage shows the evident difference "
        f"between both kinds of leaves.\n"

        f"* Average Image, Variability Image and Difference "
        f" confirmed the hypothesis "
        f" showing color difference within the center of each leaf image "
        f" however; there were no clear patterns to identify them by shape.\n"

        f"* ML pipeline performance was evaluated and it differentiates "
        f" a healthy leaf and an infected leaf "
        f" with at least 97% accuracy.\n\n"
    )
