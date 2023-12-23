import streamlit as st

st.set_page_config(page_title="Home", page_icon=":smiley:")

st.write(
    """
         # English - Central Kurdish Sentence Pairs
         This is a Python project that downloads and processes sentence pairs in English and Central Kurdish (Soranî) from the [Tatoeba](https://tatoeba.org/en/downloads) project. The Tatoeba project is a large database of sentences and translations. This project uses the [pandas](https://pandas.pydata.org/) library to manipulate the data and the [streamlit](https://streamlit.io/) library to create a web app for reviewing the sentence pairs.
         """
)
st.sidebar.success("Hello World!")
