import os
from dotenv import load_dotenv
import yaml
from yaml.loader import SafeLoader
import streamlit as st
import streamlit_authenticator as stauth

st.set_page_config(page_title="Home", page_icon=":smiley:")

st.write(
    """
         # English - Central Kurdish Sentence Pairs
         This is a Python project that downloads and processes sentence pairs in English and Central Kurdish (Soranî) from the [Tatoeba](https://tatoeba.org/en/downloads) project. The Tatoeba project is a large database of sentences and translations. This project uses the [pandas](https://pandas.pydata.org/) library to manipulate the data and the [streamlit](https://streamlit.io/) library to create a web app for reviewing the sentence pairs.
         """
)


load_dotenv()
CONFIG_PATH = os.getenv("CONFIG_PATH")

st.write("## Account")


with open(CONFIG_PATH) as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["preauthorized"],
)

tab1, tab2 = st.tabs(["Login", "Register"])

with tab1:
    authenticator.login("Login", "main")

    if st.session_state["authentication_status"]:
        st.write(f'### Welcome **{st.session_state["name"]}**')
        authenticator.logout("Logout", "main", key="login_key")
    elif st.session_state["authentication_status"] is False:
        st.error("Username/password is incorrect")
    elif st.session_state["authentication_status"] is None:
        st.warning("Please enter your username and password")

with tab2:
    if st.session_state["authentication_status"]:
        st.write(f'### Welcome **{st.session_state["name"]}**')
        authenticator.logout("Logout", "main", key="register_key")
    else:
        try:
            if authenticator.register_user("Register user", preauthorization=False):
                st.success("User registered successfully")
                with open(CONFIG_PATH, "w") as file:
                    yaml.dump(config, file, default_flow_style=False)
        except Exception as e:
            st.error(e)
