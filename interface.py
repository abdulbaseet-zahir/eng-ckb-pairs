# Import streamlit and pandas
import streamlit as st
import pandas as pd
from tatoeba.tatoeba import Tatoeba

tb = Tatoeba()

# Load the .tsv file into a pandas dataframe
data_path = "Sentence pairs in English-Central Kurdish (Soranî) - 2023-12-22"
data = tb.get_data()

st.title("Sentence pairs in English-Central Kurdish (Soranî) - 2023-12-22")
st.write("This is a demo app for reviewing sentence pairs.")
st.write("The data is from the [Tatoeba](https://tatoeba.org/en/downloads) project.")

# Get the number of rows in the dataframe
nrows = len(data)

# Create a variable to store the current index
if "index" not in st.session_state:
    st.session_state.index = 0


# Create a function to go to the next row
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
    pass


def prev_row():
    # Increment the index by one
    if st.session_state.index > 0:
        st.session_state.index -= 1
        # Update the text input values with the sentences from the next row
        st.session_state.sentence_one_input = data["eng_sentence"][
            st.session_state.index
        ]
        st.session_state.sentence_two_input = data["ckb_sentence"][
            st.session_state.index
        ]

    else:
        st.error("Index zero hase no previous!")


# Create two text input widgets for the sentences
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

container = st.container(border=True)
# Create two columns with equal width
col1, col2, col3 = st.columns(
    3,
)


col3.button("Next -->", on_click=next_row)
col2.button("Save", on_click=save())
col1.button("<-- Previous", on_click=prev_row)
