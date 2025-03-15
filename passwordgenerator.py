import streamlit as st
import random
import string
def generate_password(length,use_digits,use_special):
    characters=string.ascii_letters
    if use_digits:characters+= string.digits
    if use_special:characters+=string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


st.title("password generator")
length = st.slider("select password length" ,min_value=6 ,max_value=32,
value=12)
use_digits=st.checkbox("include digits")
use_special =st.checkbox("include special characters")
password = "" 
if st.button("generate password"):
    password=generate_password(length ,use_digits, use_special)
st.write(f"generated password:`{password}`")
st.write("------------")
st.write("build with ❤️ by [ASMA memon](https://github.com/asmabibi97)")

