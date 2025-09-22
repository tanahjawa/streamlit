import streamlit as st
st.set_page_config(layout="wide")
from streamlit_option_menu import option_menu
from app_page1 import introduction_page
from app_page2 import about_the_dataset
from app_page33_copy import heart_disease_prediction_page
# from app_page4 import chatbot_page
# st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️", layout="wide")


def main():
    
    # Sidebar menu
    with st.sidebar:
        selected = option_menu(
            menu_title=None, 
            options=["Introduction", "Informasi Edukasi", "Deteksi Kardiovaskular", "Chatbot"], 
            icons=['house', 'database', 'heart', 'robot' ], 
            menu_icon="cast", 
            default_index=2)
        
        st.markdown("### Connect with me")
        
        # Adding icons for GitHub and LinkedIn
        github_url = "https://github.com/jessih828"
        linkedin_url = "https://www.linkedin.com/in/hsieh-jessica/"

        # URLs for the icons
        github_icon = "https://cdn-icons-png.flaticon.com/512/25/25231.png"
        linkedin_icon = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
        
        # Display icons with adjusted size using HTML
        st.markdown(f'<a href="{github_url}" target="_blank"><img src="{github_icon}" width="30" height="30"></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{linkedin_url}" target="_blank"><img src="{linkedin_icon}" width="30" height="30"></a>', unsafe_allow_html=True)

    # Load the selected page
    if selected == "Introduction":
        introduction_page()
    elif selected == "Informasi Edukasi":
        about_the_dataset()
    elif selected == "Deteksi Kardiovaskular":
        heart_disease_prediction_page()
    elif selected == "Chatbot":
        chatbot_page()

if __name__ == "__main__":
    main()

    #"#0e2059"