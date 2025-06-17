
import streamlit as st
from spell_core import load_dictionary, suggest

st.set_page_config(page_title="Spell Checker", layout="centered")
st.title("🔍 Spell Checker (DP-based)")

dictionary = load_dictionary("words.txt")

word = st.text_input("Enter a word to check:", "")

if st.button("Check Spelling"):
    if not word.strip():
        st.warning("Please enter a word.")
    else:
        suggestions = suggest(word, dictionary)
        st.subheader("Did you mean:")
        for i, suggestion in enumerate(suggestions, 1):
            st.write(f"{i}. {suggestion}")
