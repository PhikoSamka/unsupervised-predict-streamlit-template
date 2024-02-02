"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model


# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# Set the page width
st.set_page_config(layout="wide",page_title="OUR PAGE")

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_selection = option_menu(None, ["Home", "About us", "Recommender System", 'Dashboard','Solution Overview','Contact us'], 
    icons=['house', 'people-fill', "diagram-3-fill",'graph-up', 'telephone-inbound-fill'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
	    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "#fafafa", "font-size": "13px"}, 
        "nav-link": {"font-size": "15.6px", "text-align": "left", "margin":"0px", "--hover-color": "#253D5B"},
        "nav-link-selected": {"background-color": "#253D5B"},
    })

    #Home page
    if page_selection == "Home":
        lottie_coding = 'https://lottie.host/08e9e42b-1db7-49b9-83f5-df148a67a24e/k9COL6xBc1.json'
        
        with st.container():
            st.write("---")
            right_column, center_column, right_column = st.columns([1.25, 4.7, 4.5])


            with center_column:
                st.title("Name of the company")
                st.write("##")
                st.subheader("This is where the subheading goes with our slogan")
                st.write(
                    """Catchy paragraph to grab viewers eyes: Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                      Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi 
                      ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit 
                      in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
                        occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim 
                        id est laborum.
                    """
                )
            with center_column:

                subscribe_letter = """<form style="display: flex; align-items: center;">
                                    <input type="email" placeholder="signmeupnow@here.com" required style="margin-right: 15px; margin-left: 0px; margin-top:15px;" >
                                    <button type="submit" style="padding: 11px 20px; margin-left: 0px">Subscribe</button>
                                </form>"""
                st.markdown(subscribe_letter, unsafe_allow_html=True)

                #use local css file
                def local_css(file_name):
                        with open(file_name) as f:
                            st.markdown(f"<style>{f.read()}</styel>", unsafe_allow_html=True)
                
                local_css('style/style.css')

            with right_column:
                st_lottie(lottie_coding, height=400, key="coding")


    #About Us Page
    if page_selection == "About us":
        st.write("---")
        st.title("Meet the team, mission, and vision")
        st.write("Describe your winning approach on this page")
        contact_form = """
        <h4>For more information please contact us...</h4>
        <form action="https://formsubmit.co/your@email.com" method="POST">
        <input type="text" name="name", placeholder="Your name" required>
        <input type="email" name="email", placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
        </form>

        """

        st.markdown(contact_form, unsafe_allow_html=True)

        #use local css file
        def local_css(file_name):
                with open(file_name) as f:
                    st.markdown(f"<style>{f.read()}</styel>", unsafe_allow_html=True)
        
        local_css('style/style.css')


    
    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    # page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        st.write("---")
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
                    

    #Analytics/Dashboard page
    if page_selection == "Dashboard":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    #Solution overview page
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    #Contact us page
    if page_selection == "Contact us":
        st.write("---")

        contact_form = """
        <h4>For more information please contact us...</h4>
        <form action="https://formsubmit.co/your@email.com" method="POST">
        <input type="text" name="name", placeholder="Your name" required>
        <input type="email" name="email", placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
        </form>

        """

        st.markdown(contact_form, unsafe_allow_html=True)

        #use local css file
        def local_css(file_name):
                with open(file_name) as f:
                    st.markdown(f"<style>{f.read()}</styel>", unsafe_allow_html=True)
        
        local_css('style/style.css')

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
