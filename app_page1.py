import streamlit as st

def introduction_page():
    # --- Judul Utama ---
    st.markdown("""
    <div style='text-align:center;'>
        <h1 style='color:#002C54;'>Deteksi Dini Risiko Kardiovaskular</h1>
        <p style='font-size:18px;'>Aplikasi ini membantu Anda memahami risiko penyakit kardiovaskular dan memberikan informasi penting seputar jantung dan pembuluh darah.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])  

    with col3:
        st.image("heart2.png", width=400)
        st.markdown(
            """
            <div style="text-align: center; font-size: 14px;">
                Sumber: 
                <a href="https://www.healthdirect.gov.au/circulatory-system" 
                target="_blank" 
                style="color: #0066cc; text-decoration: none;">
                Healthdirect
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

        # --- 🔘 Tombol Menuju Halaman Deteksi Kardiovaskular ---
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🩺 Menuju Halaman Deteksi Kardiovaskular", use_container_width=True):
            st.session_state["selected_page"] = "Deteksi Kardiovaskular"
            st.rerun()

    # --- Garis Pemisah ---
    st.markdown("<hr style='border:1px solid #e63946'>", unsafe_allow_html=True)

    # --- Konten Informasi ---
    st.markdown("""
    Istilah **kardiovaskular** berasal dari gabungan dua kata, yaitu:
    - *Kardio* yang berarti jantung  
    - *Vaskular* yang berarti pembuluh darah
    """)
    st.write("""
    Dengan demikian, kardiovaskular secara keseluruhan merujuk pada sistem jantung dan pembuluh darah dalam tubuh manusia.
    """)

    with st.expander("📌 Apa Itu Penyakit Kardiovaskular?", expanded=True):
        st.write("""
        Penyakit kardiovaskular mencakup berbagai kondisi yang menyerang jantung dan pembuluh darah, termasuk akibat faktor risiko seperti tekanan darah tinggi, pola hidup tidak sehat, diabetes, obesitas, dan faktor genetik.
        """)

    with st.expander("💡 Jenis-Jenis Penyakit Kardiovaskular", expanded=True):
        st.markdown("""
        <ul style='font-size:16px;'>
            <li><b>Penyakit Jantung Koroner:</b> Penyempitan arteri koroner yang bisa menyebabkan nyeri dada dan serangan jantung.</li>
            <li><b>Serangan Jantung:</b> Terhenti aliran darah ke jantung secara mendadak.</li>
            <li><b>Stroke:</b> Darah tidak mengalir ke otak, bisa akibat penyumbatan atau pecahnya pembuluh darah.</li>
            <li><b>Kondisi Lainnya:</b> Aritmia, Penyakit Aorta, Kardiomiopati, Penyakit Jantung Bawaan, Trombosis Vena Dalam & Emboli Paru, Gagal Jantung, Penyakit Katup Jantung, Perikarditis, Penyakit Jantung Rematik, Penyakit Pembuluh Darah, Penyakit Arteri Perifer, Penyakit Serebrovaskular, Penyakit Chagas.</li>
        </ul>
        """, unsafe_allow_html=True)

    with st.expander("⚠️ Gejala Umum", expanded=True):
        st.markdown("""
        <ul style='font-size:16px;'>
            <li>Nyeri atau tekanan di dada</li>
            <li>Lelah berlebihan saat aktivitas ringan</li>
            <li>Sesak napas</li>
            <li>Nyeri menjalar ke lengan, leher, rahang, bahu, atau punggung</li>
            <li>Perubahan detak jantung</li>
            <li>Pusing, lemas, atau mati rasa di tangan/kaki</li>
            <li>Pembengkakan di tangan, kaki, atau pergelangan</li>
            <li>Gejala lain seperti batuk, demam ringan, atau ruam</li>
        </ul>
        """, unsafe_allow_html=True)

    with st.expander("🩺 Cara Diagnosis", expanded=True):
        st.markdown("""
        <ul style='font-size:16px;'>
            <li><b>Tes darah:</b> Cek kolesterol, gula darah, dan penanda peradangan</li>
            <li><b>Tes stres:</b> Fungsi jantung saat aktivitas fisik</li>
            <li><b>Rontgen dada:</b> Kondisi jantung dan paru-paru</li>
            <li><b>EKG & Ekokardiogram:</b> Aktivitas listrik dan struktur jantung</li>
            <li><b>CT scan, MRI, EBCT:</b> Visualisasi detail jantung dan pembuluh darah</li>
            <li><b>Kateterisasi & angiografi:</b> Melihat aliran darah di arteri jantung</li>
        </ul>
        """, unsafe_allow_html=True)

    with st.expander("🥗 Cara Pencegahan", expanded=True):
        st.markdown("""
        <ul style='font-size:16px;'>
            <li>Makan sehat dan seimbang</li>
            <li>Olahraga rutin minimal 30 menit sehari</li>
            <li>Menjaga berat badan ideal</li>
            <li>Berhenti merokok</li>
            <li>Batasi konsumsi alkohol</li>
            <li>Kelola stres dengan baik</li>
        </ul>
        """, unsafe_allow_html=True)

    with st.expander("📊 Angka Penting Tubuh", expanded=True):
        st.markdown("""
        <ul style='font-size:16px;'>
            <li>Tekanan darah</li>
            <li>Kolesterol</li>
            <li>Gula darah</li>
        </ul>
        <p style='font-size:14px;'>Mengetahui angka-angka ini membantu menilai risiko kardiovaskular.</p>
        """, unsafe_allow_html=True)

    with st.expander("💊 Pengobatan", expanded=True):
        st.markdown("""
        <ul style='font-size:16px;'>
            <li>Perubahan gaya hidup (makan sehat, olahraga, berhenti merokok, kurangi alkohol)</li>
            <li>Obat-obatan (tekanan darah, kolesterol, pengencer darah)</li>
            <li>Alat bantu jantung (pacu jantung/ICD)</li>
            <li>Tindakan medis (stent, bypass, perbaikan katup jantung)</li>
        </ul>
        """, unsafe_allow_html=True)

    # --- Sumber ---
    st.markdown(
        """
        <hr style="border:1px solid #e63946;">
        <p style="font-size:12px; text-align:center;">
            Sumber: 
            <a href="https://world-heart-federation.org/what-is-cvd/" 
            target="_blank" 
            style="color:#0066cc; text-decoration:none;">
            World Heart Federation
            </a>
        </p>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    introduction_page()
