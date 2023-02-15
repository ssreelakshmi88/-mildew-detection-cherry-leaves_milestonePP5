import streamlit as st
from app_pages.multi_page import MultiPage

# load pages scripts

from app_pages.page_project_summary import page_project_summary_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_leaves_visualizer import page_leaves_visualizer_body
from app_pages.page_ml_performance import page_ml_performance_body
from app_pages.page_mildew_detector import page_mildew_detector_body


app = MultiPage(app_name="Cherry Leaves Mildew Detection")


app.add_page("Project Summary", page_project_summary_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("Cherry Leaf Visualizer", page_leaves_visualizer_body)
app.add_page('Mildew Detector', page_mildew_detector_body)
app.add_page('ML Performance Metric', page_ml_performance_body)

app.run()
