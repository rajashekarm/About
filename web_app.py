import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

#function to get online json animation
url = requests.get(
	"https://lottie.host/5e3a65e8-9118-4eb8-9a09-4e211003a6b3/C83zLG4OD1.json")
# Creating a blank dictionary to store JSON file, as their structure is similar to Python Dictionary
url_json = dict()

if url.status_code == 200:
	url_json = url.json()
else:
	print("Error in the URL")

        

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/

st.set_page_config(page_title="Raj Webpage", page_icon=":tada:", layout="wide")

#importing animations without json
dotlottie_file_path = 'https://lottie.host/5bbd35b9-6047-44d5-b2cc-bd4da907da0a/xUb5gtrDEa.lottie'



# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")


# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hey!:wave:, I am Raj 🙌")
    st.header(" An Aspiring Python developer ")
    st.write(
" With a hardworking and productive attitude, I am constantly seeking opportunities to learn and grow. As the chairperson of a student club, I have gained invaluable experience in leadership, teamwork, and communication - skills that I believe will be essential in any future role. "
    )
    st.write("[LinkedIn>](https://www.linkedin.com/in/rajashekar-m-1739501b1)")

# ---- WHAT I DO ----
with st.container():
st.write("---")
st.header("Positions of Responsibility")
st.write("##")
st.write(
            """
    1. Founding Chairperson- IEEE Society on Social Implications of Technology, BMSCE (Nov 2022 - March '23)
    
        * Presided a team of around more than 30 members in organizing about 12+ events in a span of 5 months.
        * Demonstrated ability to work collaboratively to lead successful events, to name a few Fauji talks and Verbattle
    
    2. Global SAC Volunteer- IEEE Society on Social Implications of Technology
    
    * Responsible for the smooth conduction of events.
         
    3. Secretary of School Union while in 7th class(2014-15)
    
    * Won my first ever election and was responsible for arranging School assembly every day.
         
    4. Co-ordinator in PhaseShift- BMSCE's annual tech symposium
    
    * Conducted an exciting event called 'Big Daddy', where each and every participant had fun.
         
    5. Member of Power sub-system at Upagraha- The Satellite club of BMSCE
    
    * Responsible for the battery charging control circuit in the sub-system.
         
    6. Member at EV Bullz Racing- Formula student club of BMSCE
    
    * Responsible for building the Battery Management System.
         
            """
        )


# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
   
    with text_column:
        st.write(
            """
        1.[Cricket Outcome Predictor: Unveiling Victory with Machine Learning](https://victory-predictor-raj.streamlit.app) 
        * Developed a machine learning-based Victory Predictor application for IPL matches.
        * Utilized Python, Streamlit, and Scikit-Learn for project development.
        * Predicted winning probabilities for IPL teams using logistic regression.
        * Designed an interactive and visually appealing user interface.
        * Conducted data preprocessing and deployed the application successfully.

        2.Battery management and diagnostic system
        * Conducted extensive research on state of charge (SoC) and health(SoH), cell balancing, and other relevant topics
            Working on Active cell balancing circuit for BMS
            
        2.Arduino based Morse Code Generator for Encoded communication
        * A mini project to encode any character in two different durations of signals called Dots and Dashes which can be used in
            Defense and other sectors
            """
        )
       


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/rajashekarm2003@gmail.com" method= "Post">
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
    with st.container():
        st.write("[Insta>](https://www.instagram.com/its_rajshekar_m/)")
        st.write("That's all for now :)")

