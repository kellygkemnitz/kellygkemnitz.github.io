import streamlit as st
import streamlit.components.v1 as components
from st_social_media_links import SocialMediaIcons

st.set_page_config(
    page_title="kellykemnitz.com",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

with open('static/streamlit_app/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title('Welcome to my website')
st.write('First time deploying a streamlit app')

st.header('About Me')

col1, col2, col3 = st.columns(3)

with col1:
    st.write(
        """
        I am a software quality assurance engineer by trade, but exploring career alternatives.
        """
    )
    
    st.markdown(f'##### Kelly Kemnitz')
    st.markdown(f'##### Wichita, KS')

    social_media_links = [
        'https://www.linkedin.com/in/kellykemnitz/',
        'https://github.com/kellygkemnitz/'
    ]

    social_media_icons = SocialMediaIcons(social_media_links)
    st.markdown(f'{social_media_icons.render()}')

    
    with open('static/resume.pdf', 'rb') as file:
        st.download_button(
            label = 'Download my Resume',
            data = file,
            file_name = 'resume.pdf',
            mime = 'application/pdf'
        )

with col3:
    st.image('static/img/profile.png', width=360)



st.header('Projects', divider='grey')
st.write('Here are some of my recent projects')
st.write('- [Project 1](https://github.com/kellygkemnitz/kellygkemnitz.github.io): This website!')
st.write('- [Project 2](https://github.com/kellygkemnitz/latex-resume-to-flask): An app that automates resume creation using LaTeX')


        
