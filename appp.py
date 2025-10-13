import streamlit as st
from streamlit_option_menu import option_menu
from app_page1 import introduction_page
from app_page2 import about_the_dataset
from app_page33_copy import heart_disease_prediction_page
# from app_page4 import chatbot_page

# Konfigurasi halaman
st.set_page_config(layout="wide")

# 🌈 Tambahkan CSS agar menu tetap horizontal di layar kecil
st.markdown("""
    <style>
    /* Pastikan container menu bisa di-scroll horizontal */
    div[data-testid="stHorizontalBlock"] {
        overflow-x: auto;
        white-space: nowrap;
    }
    /* Biar scroll-nya halus dan tanpa scrollbar jelek */
    div[data-testid="stHorizontalBlock"]::-webkit-scrollbar {
        height: 6px;
    }
    div[data-testid="stHorizontalBlock"]::-webkit-scrollbar-thumb {
        background: #ccc;
        border-radius: 10px;
    }
    /* Biar elemen menu tidak patah ke bawah */
    div[data-testid="stHorizontalBlock"] > div {
        display: inline-block !important;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    # Menu navigasi horizontal di atas
    selected = option_menu(
        menu_title=None,
        options=["Introduction", "Informasi Edukasi", "Deteksi Kardiovaskular", "Chatbot"],
        icons=['house', 'database', 'heart', 'robot'],
        orientation="horizontal",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "#2c3e50", "font-size": "20px"},
            "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#4CAF50", "color": "white"},
        }
    )

    # Load halaman sesuai menu yang dipilih
    if selected == "Introduction":
        introduction_page()
    elif selected == "Informasi Edukasi":
        about_the_dataset()
    elif selected == "Deteksi Kardiovaskular":
        heart_disease_prediction_page()
    elif selected == "Chatbot":
        st.info("Chatbot belum tersedia.")
        # chatbot_page()

    # --- GitHub icon di kanan bawah ---
    github_url = "https://github.com/tanahjawa"
    github_icon = "https://cdn-icons-png.flaticon.com/512/25/25231.png"
    st.markdown(
        f"""
        <div style='position: fixed; bottom: 20px; right: 25px;'>
            <a href="{github_url}" target="_blank">
                <img src="{github_icon}" width="35" height="35" title="Kunjungi GitHub">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
