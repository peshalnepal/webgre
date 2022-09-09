from tkinter import W
from requests import session
import streamlit as st
import json
import random
from PIL import Image

with open('vince_pic_thesaurus.json') as f:
    flashcard = json.load(f)

st.set_page_config(
    page_title="GRE Vocab",
    page_icon="🕹️",
    layout="centered"
)

def next_func():
    rand = random.randint(0, total_words - 1)
    st.session_state.key = flashcard_list[rand]

    st.title(st.session_state.key)
    st.write("\n")
    
def meaning_func():
    st.title(st.session_state.key)
    st.write(f"meaning : {flashcard[st.session_state.key]['definition']}")

    st.write("\n")

    mean, syno, anto = st.tabs(["Meanings", "Synonyms", "Antonyms"])
    with mean:
        image_name = 'images/' + st.session_state.key + '.png'
        image = Image.open(image_name)
        st.image(image, width=400)

    with syno:
        try:
            synonyms = flashcard[st.session_state.key]['synonyms']
            tabs = st.tabs(synonyms)
            for n,tab in enumerate(tabs):
                with tab:
                    st.write(f"meaning : {flashcard[synonyms[n]]['definition']}")
                    image_name = 'images/' + synonyms[n] + '.png'
                    image = Image.open(image_name)
                    st.image(image, width=400)
        except:
            st.write("No Synonyms")

    with anto:
        try:
            antonyms = flashcard[st.session_state.key]['antonyms']
            taba = st.tabs(antonyms)
            for m,tab in enumerate(taba):
                with tab:
                    st.write(f"meaning : {flashcard[antonyms[m]]['definition']}")
                    image_name = 'images/' + antonyms[m] + '.png'
                    image = Image.open(image_name)
                    st.image(image, width=400)
        except:
            st.write("No Antonyms")
        
    
flashcard_list = list(flashcard)
total_words = len(flashcard)

if 'key' not in st.session_state:
    rand = random.randint(0, total_words - 1)
    st.session_state.key = flashcard_list[rand]
    st.title(st.session_state.key)
    st.write("\n")

col1, col2 = st.columns(2)
with col1:
    st.button("Meaning", on_click=meaning_func)
with col2:
    st.button("Next", on_click=next_func)
