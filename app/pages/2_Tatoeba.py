# Import streamlit and pandas
import streamlit as st
import pandas as pd
from eng_ckb import Tatoeba

st.set_page_config(page_title="Tatoeba", page_icon=":smiley:")

#### Authentication ####

#### Variables ####
tb = Tatoeba()
data = tb.get_data()
nrows = len(data)

usernames = data["ckb_username"].unique().tolist()

with st.sidebar:
    st.multiselect(
        "Filter by users",
        ["All"] + usernames,
        ["All"],
    )
    st.button("Filter")


#### Functions ####
def next_row():
    # Increment the index by one
    st.session_state.index += 1
    # Check if the index is within the range of the dataframe
    if st.session_state.index < nrows:
        # Update the text input values with the sentences from the next row
        st.session_state.sentence_one_input = data["eng_sentence"][
            st.session_state.index
        ]
        st.session_state.sentence_two_input = data["ckb_sentence"][
            st.session_state.index
        ]
    else:
        # Display a message if the index exceeds the range
        st.error("No more sentences!")


def save():
    try:
        authentication_status = st.session_state.authentication_status
    except:
        authentication_status = False

    if authentication_status:
        eng_sentence = st.session_state.sentence_one_input
        ckb_sentence = st.session_state.sentence_two_input
        st.toast(f"""{eng_sentence} - {ckb_sentence}!""", icon="✅")
    else:
        st.error("Please login to save sentences!")


def prev_row():
    if st.session_state.index > 0:
        st.session_state.index -= 1
        st.session_state.sentence_one_input = data["eng_sentence"][
            st.session_state.index
        ]
        st.session_state.sentence_two_input = data["ckb_sentence"][
            st.session_state.index
        ]

    else:
        st.error("Index zero hase no previous!")


#### Main ####
st.title("Sentence pairs in English-Central Kurdish (Soranî) - 2023-12-22")
st.write(
    "This is a demo app for reviewing [Tatoeba](https://tatoeba.org/en/downloads) sentence pairs."
)

if "index" not in st.session_state:
    st.session_state.index = 0

sentence_one_input = st.text_input(
    "Sentence one",
    value=data["eng_sentence"][st.session_state.index],
    key="sentence_one_input",
)
sentence_two_input = st.text_input(
    "Sentence two",
    value=data["ckb_sentence"][st.session_state.index],
    key="sentence_two_input",
)

col1, col2, col3 = st.columns(3)

col1.button("Prev", on_click=prev_row)
col2.button("Save", on_click=save)
col3.button("Next", on_click=next_row)
