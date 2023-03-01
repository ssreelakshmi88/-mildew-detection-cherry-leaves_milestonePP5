import streamlit as st

# This class generates multiple streamlit pages


class MultiPage:
    """ This class generates multiple Streamlit pages
    """

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
        )

    def add_page(self, title, func) -> None:
        """ Adds title"""
        self.pages.append({"title": title, "function": func})

    def run(self):
        """Add title and menu names"""
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages,
                                format_func=lambda page: page['title'])
        page['function']()
