import streamlit as st
st.set_page_config(layout="wide")
from streamlit_option_menu import option_menu
from app_page1 import introduction_page
from app_page2 import about_the_dataset
from app_page33_copy import heart_disease_prediction_page
# from app_page4 import chatbot_page

def main():
    # Pastikan session_state punya key default
    if "selected_page" not in st.session_state:
        st.session_state["selected_page"] = "Introduction"

    # Sidebar menu
    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=["Introduction", "Informasi Edukasi", "Deteksi Kardiovaskular", "Chatbot"],
            icons=['house', 'database', 'heart', 'robot'],
            menu_icon="cast",
            default_index=["Introduction", "Informasi Edukasi", "Deteksi Kardiovaskular", "Chatbot"].index(
                st.session_state["selected_page"]
            )
        )
        # Simpan nilai menu terakhir yang diklik user
        if selected != st.session_state["selected_page"]:
            st.session_state["selected_page"] = selected
            st.rerun()

    # --- Load page sesuai pilihan ---
    if st.session_state["selected_page"] == "Introduction":
        introduction_page()
    elif st.session_state["selected_page"] == "Informasi Edukasi":
        about_the_dataset()
    elif st.session_state["selected_page"] == "Deteksi Kardiovaskular":
        heart_disease_prediction_page()
    # elif st.session_state["selected_page"] == "Chatbot":
    #     chatbot_page()

if __name__ == "__main__":
    main()
