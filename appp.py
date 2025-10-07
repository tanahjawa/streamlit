import streamlit as st
st.set_page_config(layout="wide")
from streamlit_option_menu import option_menu
from app_page1 import introduction_page
from app_page2 import about_the_dataset
from app_page33_copy import heart_disease_prediction_page
# from app_page4 import chatbot_page

def main():
    
    # Sidebar menu
    with st.sidebar:
        selected = option_menu(
            menu_title=None, 
            options=["Introduction", "Informasi Edukasi", "Deteksi Kardiovaskular", "Chatbot"], 
            icons=['house', 'database', 'heart', 'robot'], 
            menu_icon="cast", 
            default_index=2
        )

        # Spacer supaya GitHub ke bawah
        st.sidebar.markdown("<br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
        
        # GitHub icon di bawah
        github_url = "https://github.com/tanahjawa"
        github_icon = "https://cdn-icons-png.flaticon.com/512/25/25231.png"
        st.sidebar.markdown(
            f'<div style="position: fixed; bottom: 30px;">'
            f'<a href="{github_url}" target="_blank">'
            f'<img src="{github_icon}" width="30" height="30">'
            f'</a></div>', unsafe_allow_html=True
        )

    # Load the selected page
    if selected == "Introduction":
        introduction_page()
    elif selected == "Informasi Edukasi":
        about_the_dataset()
    elif selected == "Deteksi Kardiovaskular":
        heart_disease_prediction_page()
    # elif selected == "Chatbot":
    #     chatbot_page()

if __name__ == "__main__":
    main()
