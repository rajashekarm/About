import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")


# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hey!, I am Raj :wave:")
    st.title("Aspiring Python devoloper")
    st.write(
"As a third-year electrical and electronics engineering student, I am driven to explore the world of software development. While my electrical core provides me with a strong foundation, I am also learning data structures and algorithms (DSA) using Python to further enhance my skills in the software field. "

" With a hardworking and productive attitude, I am constantly seeking opportunities to learn and grow. As the chairperson of a student club, I have gained invaluable experience in leadership, teamwork, and communication - skills that I believe will be essential in any future role. "

    )
    st.write("[Know more about me>](https://www.linkedin.com/in/rajashekar-m-1739501b1)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Positions of Responsibility")
        st.write("##")
        st.write(
            """
           1. Founding Chairperson of BMSCE IEEE SSIT
           2. Secretary of School students union 
           3. Member at BMSCE Upagraha and Bullz EV
            """
        )
        st.write("[LinkedIn >](https://www.linkedin.com/in/rajashekar-m-1739501b1/)")



# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
   
    with text_column:
        st.subheader("empty rn")
        st.write(
            """
         1. Adanced Battery Management and Diagnostic System for Smart Grid Infrastructure
            """
        )
       


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
