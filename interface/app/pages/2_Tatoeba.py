# Import streamlit and pandas
import streamlit as st
import pandas as pd
from datetime import datetime
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from db import get_data, get_collection


st.set_page_config(page_title="Tatoeba", page_icon=":smiley:")

#### Authentication ####

#### Variables ####
data = get_data()
collection = get_collection()
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
    st.session_state.index += 1
    if st.session_state.index < nrows:
        st.session_state.eng_sentence_input = data["eng_sentence"][
            st.session_state.index
        ]
        st.session_state.ckb_sentence_input = data["ckb_sentence"][
            st.session_state.index
        ]
        st.session_state.eng_id = data["eng_id"][st.session_state.index]
        st.session_state.ckb_id = data["ckb_id"][st.session_state.index]
    else:
        st.session_state.index -= 1
        st.error("No more sentences!")


def save():
    try:
        authentication_status = st.session_state.authentication_status
    except:
        authentication_status = False

    if authentication_status:
        eng_sentence = st.session_state.eng_sentence_input
        ckb_sentence = st.session_state.ckb_sentence_input
        eng_id = st.session_state.eng_id
        ckb_id = st.session_state.ckb_id
        filter = {"eng_id": int(eng_id), "ckb_id": int(ckb_id)}
        update = {
            "$set": {
                "eng_sentence": eng_sentence,
                "ckb_sentence": ckb_sentence,
                "reviewed": True,
                "updated_at": datetime.now(),
            },
            "$addToSet": {"reviewed_by": "anonymous"},
        }
        collection.update_one(filter, update, upsert=True)
        st.toast(f"""{eng_sentence} - {ckb_sentence}!""", icon="✅")
    else:
        st.error("Please login to save sentences!")


def prev_row():
    if st.session_state.index > 0:
        st.session_state.index -= 1
        st.session_state.eng_sentence_input = data["eng_sentence"][
            st.session_state.index
        ]
        st.session_state.ckb_sentence_input = data["ckb_sentence"][
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

st.session_state.eng_id = data["eng_id"][st.session_state.index]
st.session_state.ckb_id = data["ckb_id"][st.session_state.index]

sentence_one_input = st.text_input(
    f"English sentence {str(st.session_state.eng_id)}",
    value=data["eng_sentence"][st.session_state.index],
    key="eng_sentence_input",
)
ckb_sentence_input = st.text_input(
    f"Kurdish sentence {st.session_state.ckb_id}",
    value=data["ckb_sentence"][st.session_state.index],
    key="ckb_sentence_input",
)


col1, col2, col3 = st.columns(3)

col1.button("Prev", on_click=prev_row)
col2.button("Save", on_click=save)
col3.button("Next", on_click=next_row)
