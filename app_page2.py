import streamlit as st
import pandas as pd
import re
# from app_page2 import about_the_dataset  # Tidak ada set_page_config di sini


def about_the_dataset():
    # ---------- Helper: Klasifikasi ----------
    def klasifikasi_td(sistolik: int, diastolik: int):
        if sistolik > 180 or diastolik > 120:
            return ('🚨 Krisis Hipertensi', "Segera cari pertolongan medis darurat!")
        elif sistolik >= 140 or diastolik >= 90:
            return ('❌ Hipertensi Tahap 2', "Konsultasi dengan dokter, periksa secara rutin.")
        elif 130 <= sistolik <= 139 or 80 <= diastolik <= 89:
            return ('⚠️ Hipertensi Tahap 1', "Kurangi garam, olahraga teratur, kontrol berat badan.")
        elif 120 <= sistolik <= 129 and diastolik < 80:
            return ('⚠️ Meningkat (Pre-Hipertensi)', "Tetap waspada, perhatikan pola makan dan gaya hidup.")
        elif sistolik < 90 or diastolik < 60:
            if sistolik < 70 or diastolik < 40:
                return ('🚨 Hipotensi Berat', "Segera ke IGD, risiko syok.")
            else:
                return ('❗ Hipotensi', "Konsultasi dokter, perbanyak cairan, cek penyebab.")
        elif 90 <= sistolik <= 119 and 60 <= diastolik <= 79:
            return ('✅ Normal', "Pertahankan gaya hidup sehat.")
        else:
            return ("⚠️ Tidak dapat ditentukan", "Pastikan input benar.")




    # # ---------- Sidebar ----------
    # st.sidebar.title("📚 Menu")
    # menu = st.sidebar.radio("Pilih Halaman:", ["Informasi Edukatif"], key="menu_radio")


    st.title("🧪 Informasi Edukatif")

    # Tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🫀 Tekanan Darah", 
        "🧬 Kolesterol", 
        "🍬 Gula Darah", 
        "🚬 Merokok", 
        "🍷 Alkohol", 
        "🏃‍♂️ Aktivitas"
    ])

    # ===============================
    # TAB TEKANAN DARAH
    # ===============================
    with tab1:
        st.subheader("📌 Edukasi Tekanan Darah")
        st.markdown("""
        <p>
        <a href='https://medlineplus.gov/highbloodpressure.html#:~:text=What%20is%20blood%20pressure?,and%20a%20diastolic%20of%2080.' 
        target='_blank' style='color:#1a73e8; text-decoration:none;'>Tekanan darah</a> 
        adalah tenaga dorongan darah pada dinding pembuluh arteri. Setiap kali jantung berdetak, darah dipompa masuk ke arteri untuk mengalir ke seluruh tubuh. 
        Dua nilai utama yang perlu diperhatikan adalah <b>sistolik</b> dan <b>diastolik</b>:
        </p>

        <ul>
        <li><b>Sistolik (angka atas)</b>. 
        <a href='https://www.alodokter.com/seperti-ini-cara-membaca-hasil-pemeriksaan-tekanan-darah' 
        target='_blank' style='color:#1a73e8; text-decoration:none;'>Tekanan sistolik</a> 
        menggambarkan besarnya tekanan darah pada dinding arteri setelah jantung berkontraksi. 
        Nilai tekanan darah sistolik tercatat saat bunyi 
        <a href='https://www.physio-pedia.com/Sphygmomanometer?utm_source=chatgpt.com' 
        target='_blank' style='color:#1a73e8; text-decoration:none;'>Korotkoff</a> 
        pertama terdengar.
        </li>

        <li><b>Diastolik (angka bawah)</b>. 
        <a href='https://www.alodokter.com/seperti-ini-cara-membaca-hasil-pemeriksaan-tekanan-darah' 
        target='_blank' style='color:#1a73e8; text-decoration:none;'>Tekanan diastolik</a> 
        mencerminkan tekanan ketika jantung berada dalam fase relaksasi. 
        Nilai tekanan diastolik 
        <a href='https://www.physio-pedia.com/Sphygmomanometer?utm_source=chatgpt.com' 
        target='_blank' style='color:#1a73e8; text-decoration:none;'>tercatat</a> 
        ketika bunyi tersebut hilang.
        </li>
        </ul>
        """, unsafe_allow_html=True)


        st.markdown("""
        <p><b>American Heart Association</b> 
        (<a href='https://www.heart.org/en/health-topics/high-blood-pressure/the-facts-about-high-blood-pressure' 
        target='_blank' 
        style='color:#1a73e8; text-decoration:none;'>AHA</a>) 
        telah memperbarui batas normal tekanan darah — jika sebelumnya nilai 
        <b>120/80 mmHg</b> dianggap normal, kini tekanan darah dikatakan 
        <b>normal bila berada di bawah 120/80 mmHg</b>.</p>

        > Dengan demikian, tekanan sistolik **120 mmHg** sudah termasuk dalam kategori **pra-hipertensi (elevated blood pressure)**, yaitu tahap awal peningkatan tekanan darah yang perlu diwaspadai agar tidak berkembang menjadi hipertensi.

        Berdasarkan kategori terbaru dari **American Heart Association (AHA)**, berikut adalah rentang tekanan darah:
        """, unsafe_allow_html=True)
        
        st.subheader("📊 Kategori Tekanan Darah")
        st.markdown("""
        <table style="width:100%; border-collapse: collapse; border-radius: 10px; overflow: hidden; border:1px solid #ddd;">
            <tr style="background-color:#fce8eb;">
                <th style="padding:8px; border:1px solid #ddd;">Kategori</th>
                <th style="padding:8px; border:1px solid #ddd;">Sistolik (mmHg)</th>
                <th style="padding:8px; border:1px solid #ddd;">Diastolik (mmHg)</th>
            </tr>
            <tr>
                <td style='padding:8px; border:1px solid #ddd;'>
                    <a href='https://www.heart.org/en/health-topics/high-blood-pressure/the-facts-about-high-blood-pressure/low-blood-pressure-when-blood-pressure-is-too-low' 
                    target='_blank' 
                    style='color:#1a73e8; text-decoration:none;'>
                    Hipotensi
                    </a>
                </td>
                <td style='padding:8px; border:1px solid #ddd;'>Kurang dari 90</td>
                <td style='padding:8px; border:1px solid #ddd;'>Kurang dari 60</td>
            </tr>
            <tr><td style='padding:8px; border:1px solid #ddd;'>Normal</td><td style='padding:8px; border:1px solid #ddd;'>90 – 119</td><td style='padding:8px; border:1px solid #ddd;'>60 – 79</td></tr>
            <tr><td style='padding:8px; border:1px solid #ddd;'>Meningkat (pra-hipertensi)</td><td style='padding:8px; border:1px solid #ddd;'>120 – 129</td><td style='padding:8px; border:1px solid #ddd;'>Kurang dari 80</td></tr>
            <tr><td style='padding:8px; border:1px solid #ddd;'>Hipertensi Tahap 1</td><td style='padding:8px; border:1px solid #ddd;'>130 – 139</td><td style='padding:8px; border:1px solid #ddd;'>80 – 89</td></tr>
            <tr><td style='padding:8px; border:1px solid #ddd;'>Hipertensi Tahap 2</td><td style='padding:8px; border:1px solid #ddd;'>≥ 140</td><td style='padding:8px; border:1px solid #ddd;'>≥ 90</td></tr>
            <tr><td style='padding:8px; border:1px solid #ddd;'>Krisis Hipertensi</td><td style='padding:8px; border:1px solid #ddd;'>> 180</td><td style='padding:8px; border:1px solid #ddd;'>> 120</td></tr>
        </table>
        """, unsafe_allow_html=True)

        st.markdown("---")

        # --------- Input Tekanan Darah (1 kolom saja) ----------
        st.subheader("🖊️ Masukkan Hasil Pemeriksaan")
        st.markdown("""
        **Contoh:** `120/80 mmHg` 
        - **120** = **Sistolik (nilai atas)**  
        - **80** = **Diastolik (nilai bawah)**  
        Masukkan dalam format **angka atas/angka bawah**.
        """)

        satu_kolom = st.text_input(
            "Tekanan Darah (contoh: 120/80)",
            placeholder="Masukkan nilai, contoh: 120/80",
            key="td_satu_kolom"
        )

        cek_td = st.button("✅ Cek Hasil Tekanan Darah", key="cek_td_button_single")

        sistolik_val, diastolik_val = None, None

        if cek_td:
            if not satu_kolom:
                st.warning("⚠️ Harap isi nilai tekanan darah dalam format contoh: 120/80.")
            else:
                cleaned = re.sub(r"\s|mmhg|MMHG|MmHg", "", satu_kolom)
                parts = cleaned.split("/")
                if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
                    st.error("❌ Format salah. Gunakan format: angka atas/angka bawah (contoh: 120/80).")
                else:
                    sistolik_val = int(parts[0])
                    diastolik_val = int(parts[1])

        # --------- Tampilkan hasil jika ada nilai valid ----------
        if sistolik_val is not None and diastolik_val is not None:
            kategori, rekomendasi = klasifikasi_td(sistolik_val, diastolik_val)

            hasil_html = f"""
            <table style="width:100%; border-collapse: collapse; border-radius: 10px; overflow: hidden;">
                <tr style="background-color:#f2f2f2;">
                    <th style="padding:8px; border:1px solid #ddd;">Parameter</th>
                    <th style="padding:8px; border:1px solid #ddd;">Hasil</th>
                    <th style="padding:8px; border:1px solid #ddd;">Kategori</th>
                </tr>
                <tr>
                    <td style="padding:8px; border:1px solid #ddd;">Tekanan Darah</td>
                    <td style="padding:8px; border:1px solid #ddd;">{sistolik_val}/{diastolik_val} mmHg</td>
                    <td style="padding:8px; border:1px solid #ddd;">{kategori}</td>
                </tr>
            </table>
            <p><b>💡 Rekomendasi:</b> {rekomendasi}</p>
            """
            st.markdown(hasil_html, unsafe_allow_html=True)


    # ===============================
    # TAB KOLESTEROL
    # ===============================
    with tab2:
        st.subheader("📌 Edukasi Kolesterol")
        st.write("""
        <p>
        <a href='https://my.clevelandclinic.org/health/articles/11920-cholesterol-numbers-what-do-they-mean' 
        target='_blank' style='color:#1a73e8; text-decoration:none;'>Kolesterol</a> 
        adalah lemak penting bagi tubuh untuk berbagai fungsi, namun jika berlebihan dapat menumpuk di dinding arteri, merusak lapisan pembuluh darah, dan membentuk plak aterosklerotik dan bisa meningkatkan risiko penyakit jantung.
        </p>
        """, unsafe_allow_html=True)
        st.write("""
        Berikut beberapa kategori kolesterol yang perlu diketahui, yaitu:
        - **Kolesterol Total**. Jumlah keseluruhan kolesterol yang beredar dalam darah seseorang.
        - **HDL (High Density Lipoprotein)**. Kolesterol baik, membantu membersihkan kolesterol jahat.
        - **LDL (Low Density Lipoprotein)**. Kolesterol jahat, menumpuk di pembuluh darah.
        - **Trigliserida**. Lemak cadangan energi, jika tinggi dapat memicu penyakit metabolik.
        """)
        st.write("""
        <p>Berdasarkan
        <a href='https://my.clevelandclinic.org/health/articles/11920-cholesterol-numbers-what-do-they-mean' 
        target='_blank' style='color:#1a73e8; text-decoration:none;'>Cleveland Clinic</a> 
        berikut nilai kategori kolesterol:
        </p>
        """, unsafe_allow_html=True)

        # ✅ Tambahkan Tabel Kategori Kolesterol

        st.subheader("📊 Kategori Kolesterol")
        st.markdown("""
        <table style="width:100%; border-collapse: collapse; border-radius: 10px; overflow: hidden; border:1px solid #ddd;">
            <tr style="background-color:#fce8eb;">
                <th style="padding:8px; border:1px solid #ddd;">Kategori</th>
                <th style="padding:8px; border:1px solid #ddd;">Kolesterol Total (mg/dL)</th>
                <th style="padding:8px; border:1px solid #ddd;">Kolesterol LDL (mg/dL)</th>
                <th style="padding:8px; border:1px solid #ddd;">Kolesterol HDL (mg/dL)</th>
                <th style="padding:8px; border:1px solid #ddd;">
                    <a href='https://www.ncbi.nlm.nih.gov/books/NBK542294' 
                    target='_blank' style='color:#1a73e8; text-decoration:none;'>
                        Trigliserida puasa (mg/dL)
                    </a>
                </th>
            </tr>
            <tr>
                <td>Normal</td>
                <td>Kurang dari 200</td>
                <td>Kurang dari 100</td>
                <td>Lebih dari 60</td>
                <td>Kurang dari 150</td>
            </tr>
            <tr>
                <td>Di atas normal</td>
                <td>200 – 239</td>
                <td>100 – 159</td>
                <td>40 – 59 (pria), 50 – 59 (wanita)</td>
                <td>150 hingga 499</td>
            </tr>
            <tr>
                <td>Sangat tidak normal</td>
                <td>Lebih dari 240</td>
                <td>Lebih dari 160</td>
                <td>Kurang dari 40 (pria), < 50 (wanita)</td>
                <td>Lebih dari 500</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)


        st.markdown("---")

        # ✅ Input Kolesterol
        st.subheader("🖊️ Masukkan Hasil Pemeriksaan")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            kol_total = st.text_input("Kolesterol Total", placeholder="mg/dL")
        with col2:
            ldl = st.text_input("LDL", placeholder="mg/dL")
        with col3:
            hdl = st.text_input("HDL", placeholder="mg/dL")
            gender = st.selectbox("Jenis Kelamin (HDL)", ["Pria", "Wanita"])
        with col4:
            trigliserida = st.text_input("Trigliserida", placeholder="mg/dL")


        cek_kol = st.button("✅ Cek Hasil Kolesterol")
        if cek_kol:
            if not any([kol_total, ldl, hdl, trigliserida]):
                st.warning("⚠️ Harap isi minimal satu nilai pemeriksaan kolesterol.")
            else:
                try:
                    hasil_html = """
                    <table style="width:100%; border-collapse: collapse; border-radius: 10px; overflow: hidden;">
                        <tr style="background-color:#f2f2f2;">
                            <th style="padding:8px; border:1px solid #ddd;">Parameter</th>
                            <th style="padding:8px; border:1px solid #ddd;">Hasil</th>
                            <th style="padding:8px; border:1px solid #ddd;">Kategori</th>
                        </tr>
                    """
                    # Kolesterol Total
                    if kol_total:
                        val = int(kol_total)
                        kategori = ""
                        color = "black"  # default

                        if val < 200:
                            kategori = "✅ Normal"
                            color = "green"
                        elif 200 <= val <= 239:
                            kategori = "⚠️ Di atas normal"
                            color = "orange"
                        else:  # >= 240
                            kategori = "❌ Sangat tidak normal"
                            color = "red"

                        hasil_html += f"<tr><td style='padding:8px;border:1px solid #ddd;'>Kolesterol Total</td><td style='padding:8px;border:1px solid #ddd;'>{val}</td><td style='padding:8px;border:1px solid #ddd;color:{color};'>{kategori}</td></tr>"

                    # LDL
                    if ldl:
                        val = int(ldl)
                        kategori = ""
                        color = "black"  # default

                        if val < 100:
                            kategori = "✅ Normal"
                            color = "green"
                        elif 100 <= val <= 159:
                            kategori = "⚠️ Di atas normal"
                            color = "orange"
                        else:  # >= 160
                            kategori = "❌ Sangat tidak normal"
                            color = "red"

                        hasil_html += f"<tr><td style='padding:8px;border:1px solid #ddd;'>LDL</td><td style='padding:8px;border:1px solid #ddd;'>{val}</td><td style='padding:8px;border:1px solid #ddd;color:{color};'>{kategori}</td></tr>"

                    # HDL (dengan jenis kelamin)
                    if hdl and gender:
                        val = int(hdl)
                        kategori = ""
                        color = "black"  # default

                        if gender == "Pria":
                            if val < 40:
                                kategori = "❌ Sangat tidak normal"
                                color = "red"
                            elif 40 <= val <= 59:
                                kategori = "⚠️ Abnormal (rendah)"
                                color = "orange"
                            else:  # >= 60
                                kategori = "✅ Normal"
                                color = "green"

                        elif gender == "Wanita":
                            if val < 50:
                                kategori = "❌ Sangat tidak normal"
                                color = "red"
                            elif 50 <= val <= 59:
                                kategori = "⚠️ Abnormal (rendah)"
                                color = "orange"
                            else:  # >= 60
                                kategori = "✅ Normal"
                                color = "green"

                        hasil_html += f"<tr><td style='padding:8px;border:1px solid #ddd;'>HDL ({gender})</td><td style='padding:8px;border:1px solid #ddd;'>{val}</td><td style='padding:8px;border:1px solid #ddd;color:{color};'>{kategori}</td></tr>"


                    # Trigliserida
                    if trigliserida:
                        val = int(trigliserida)
                        kategori = ""
                        color = "black"  # default

                        if val < 150:
                            kategori = "✅ Normal"
                            color = "green"
                        elif 150 <= val <= 499:
                            kategori = "⚠️ Di atas normal"
                            color = "orange"
                        else:  # >= 500
                            kategori = "❌ Sangat tidak normal"
                            color = "red"

                        hasil_html += f"<tr><td style='padding:8px;border:1px solid #ddd;'>Trigliserida</td><td style='padding:8px;border:1px solid #ddd;'>{val}</td><td style='padding:8px;border:1px solid #ddd;color:{color};'>{kategori}</td></tr>"

                    hasil_html += "</table>"
                    st.markdown(hasil_html, unsafe_allow_html=True)
                except ValueError:
                    st.error("❌ Masukkan hanya angka yang valid.")

    # ===============================
    # TAB GULA DARAH
    # ===============================
    with tab3:
        st.subheader("📌 Edukasi Gula Darah")

        st.markdown("""
        <p style='padding-left:20px; text-align:justify; line-height:1.6;'>
        Glukosa darah atau <a href='https://medlineplus.gov/bloodglucose.html#:~:text=What%20is%20blood%20glucose?,The%20typical%20targets%20are:' 
        target='_blank' style='color:#1a73e8; text-decoration:none; font-weight:500;'>gula darah</a> 
        merupakan <b>gula utama</b> yang terdapat dalam darah dan menjadi <b>sumber energi utama</b> bagi tubuh.  
        Ketika kadar glukosa meningkat, pankreas diberi sinyal untuk melepaskan hormon <b>insulin</b>.  
        Insulin berfungsi membantu glukosa masuk ke dalam sel agar dapat digunakan sebagai energi.
        </p>

        <p style='padding-left:20px; text-align:justify; line-height:1.6;'>
        Apa itu <a href='https://medlineplus.gov/bloodglucose.html#:~:text=What%20is%20blood%20glucose?,The%20typical%20targets%20are:' 
        target='_blank' style='color:#1a73e8; text-decoration:none; font-weight:500;'>diabetes</a>?  
        Diabetes adalah kondisi ketika kadar glukosa darah terlalu tinggi karena tubuh 
        <b>tidak cukup menghasilkan insulin</b> atau <b>tidak dapat menggunakannya dengan efektif</b>.  
        Akibatnya, glukosa menumpuk dalam darah dan berisiko menimbulkan berbagai komplikasi serius, 
        sehingga <b>pengendalian kadar gula darah sangat penting</b>.
        </p>

        <p style='padding-left:20px; text-align:justify; line-height:1.6;'>
        Berdasarkan <a href='https://www.nutrisense.io/blog/blood-sugar-level-charts' 
        target='_blank' style='color:#1a73e8; text-decoration:none; font-weight:500;'>Nutrisense</a>, 
        berikut adalah rentang nilai kategori gula darah untuk orang dewasa.
        </p>
        """, unsafe_allow_html=True)

        # ✅ Tambahkan Tabel Kategori Gula Darah
        st.subheader("📊 Kategori Gula Darah Untuk Dewasa")
        st.markdown("""
        <table style="width:100%; border-collapse: collapse; border-radius: 10px; overflow: hidden; border:1px solid #ddd; text-align:center;">
            <tr style="background-color:#fce8eb;">
                <th style="padding:8px; border:1px solid #ddd;">Kategori</th>
                <th style="padding:8px; border:1px solid #ddd;">Nilai Puasa (mg/dL)<br><small>Setelah 8 jam tidak makan</small></th>
                <th style="padding:8px; border:1px solid #ddd;">Nilai 2 Jam Setelah Makan (mg/dL)</th>
            </tr>
            <tr style="background-color:#f9f9f9;">
                <td style="padding:8px; border:1px solid #ddd;">Normal/Optimal</td>
                <td style="padding:8px; border:1px solid #ddd;">70 – 90</td>
                <td style="padding:8px; border:1px solid #ddd;">Kurang dari 140</td>
            </tr>
            <tr style="background-color:#ffffff;">
                <td style="padding:8px; border:1px solid #ddd;">Pra-Diabetes</td>
                <td style="padding:8px; border:1px solid #ddd;">100 – 125</td>
                <td style="padding:8px; border:1px solid #ddd;">140 – 180</td>
            </tr>
            <tr style="background-color:#f9f9f9;">
                <td style="padding:8px; border:1px solid #ddd;">Diabetes</td>
                <td style="padding:8px; border:1px solid #ddd;">≥ 126</td>
                <td style="padding:8px; border:1px solid #ddd;">Lebih dari 200</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)

        st.markdown("""
        <h3 style='margin-bottom:10px;'>
        📊 Kategori Gula Darah Normal Untuk Dewasa dengan 
        <a href='https://northwestclinic.org/normal-blood-sugar-levels-chart/' 
        target='_blank' 
        style='color:#1a73e8; text-decoration:none; font-weight:600;'>Diabetes</a>
        </h3>
        """, unsafe_allow_html=True)
        st.markdown("""
        <table style="width:100%; border-collapse: collapse; border-radius: 10px; overflow: hidden; border:1px solid #ddd; text-align:center;">
            <tr style="background-color:#fce8eb;">
                <th style="padding:8px; border:1px solid #ddd;">Waktu Pemeriksaan</th>
                <th style="padding:8px; border:1px solid #ddd;">Kisaran Target untuk Penderita Diabetes (mg/dL)</th>
            </tr>
            <tr style="background-color:#f9f9f9;">
                <td style="padding:8px; border:1px solid #ddd;">Puasa</td>
                <td style="padding:8px; border:1px solid #ddd;">80 – 130</td>
            </tr>
            <tr style="background-color:#ffffff;">
                <td style="padding:8px; border:1px solid #ddd;">1-2 jam setelah makan</td>
                <td style="padding:8px; border:1px solid #ddd;">Kurang dari 180</td>
            </tr>
            <tr style="background-color:#f9f9f9;">
                <td style="padding:8px; border:1px solid #ddd;">Sebelum tidur</td>
                <td style="padding:8px; border:1px solid #ddd;">100 – 140</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)



        st.markdown("---")

        # ✅ Input gula darah
        st.subheader("🖊️ Masukkan Hasil Pemeriksaan")
        col1, col2, col3 = st.columns(3)
        with col1:
            gd_puasa = st.text_input("Gula Darah Puasa", placeholder="mg/dL")
        with col2:
            gd_2jam = st.text_input("Gula Darah 2 Jam Setelah Makan", placeholder="mg/dL")
        with col3:
            gd_sewaktu = st.text_input("Gula Darah Sewaktu", placeholder="mg/dL")

        cek_gd = st.button("✅ Cek Hasil Gula Darah")
        if cek_gd:
            if not any([gd_puasa, gd_2jam, gd_sewaktu]):
                st.warning("⚠️ Harap isi minimal salah satu nilai pemeriksaan gula darah.")
            else:
                try:
                    hasil_html = """
                    <table style="width:100%; border-collapse: collapse; border-radius: 10px; overflow: hidden;">
                        <tr style="background-color:#f2f2f2;">
                            <th style="padding:8px; border:1px solid #ddd;">Parameter</th>
                            <th style="padding:8px; border:1px solid #ddd;">Hasil</th>
                            <th style="padding:8px; border:1px solid #ddd;">Kategori</th>
                        </tr>
                    """
                    if gd_puasa:
                        val = int(gd_puasa)
                        if val < 100:
                            kategori = "✅ Normal"; color = "green"
                        elif 100 <= val <= 125:
                            kategori = "⚠️ Prediabetes"; color = "orange"
                        else:
                            kategori = "❌ Diabetes"; color = "red"
                        hasil_html += f"<tr><td style='padding:8px;border:1px solid #ddd;'>Puasa</td><td style='padding:8px;border:1px solid #ddd;'>{val}</td><td style='padding:8px;border:1px solid #ddd;color:{color};'>{kategori}</td></tr>"

                    if gd_2jam:
                        val = int(gd_2jam)
                        if val < 140:
                            kategori = "✅ Normal"; color = "green"
                        elif 140 <= val <= 199:
                            kategori = "⚠️ Prediabetes"; color = "orange"
                        else:
                            kategori = "❌ Diabetes"; color = "red"
                        hasil_html += f"<tr><td style='padding:8px;border:1px solid #ddd;'>2 Jam Setelah Makan</td><td style='padding:8px;border:1px solid #ddd;'>{val}</td><td style='padding:8px;border:1px solid #ddd;color:{color};'>{kategori}</td></tr>"

                    if gd_sewaktu:
                        val = int(gd_sewaktu)
                        if val < 200:
                            kategori = "✅ Normal"; color = "green"
                        else:
                            kategori = "❌ Diabetes"; color = "red"
                        hasil_html += f"<tr><td style='padding:8px;border:1px solid #ddd;'>Sewaktu</td><td style='padding:8px;border:1px solid #ddd;'>{val}</td><td style='padding:8px;border:1px solid #ddd;color:{color};'>{kategori}</td></tr>"
                    hasil_html += "</table>"
                    
                    st.markdown(hasil_html, unsafe_allow_html=True)

                except ValueError:
                    st.error("❌ Masukkan hanya angka yang valid.")
    
    # ===============================
    # TAB MEROKOK
    # ===============================
    with tab4:
        st.subheader("📌 Dampak Merokok")
        st.markdown("""
        1. **Peningkatan Risiko Hipertensi**  
        Nikotin merangsang sistem saraf simpatik → melepaskan hormon adrenalin → meningkatkan denyut jantung dan tekanan darah. <a href='https://pmc.ncbi.nlm.nih.gov/articles/PMC3755365/' target='_blank' style='text-decoration:none;'>🔗</a>

        2. **Kolesterol Tinggi**  
        Zat kimia dalam rokok menyebabkan penyempitan pembuluh darah & meningkatkan kadar kolesterol jahat (LDL). <a href='https://healthmatch.io/cholesterol/does-smoking-cause-high-cholesterol#what-is-cholesterol' target='_blank' style='text-decoration:none;'>🔗</a>

        3. **Penyakit Jantung & Stroke**  
        Rokok merusak pembuluh darah → memicu penyumbatan arteri. <a href='https://www.emc.id/id/care-plus/pengaruh-rokok-terhadap-gangguan-pembuluh-darah-tepi' target='_blank' style='text-decoration:none;'>🔗</a>

        4. **Risiko Diabetes**  
        Nikotin membuat sel kurang responsif terhadap insulin → kadar gula darah sulit terkendali. <a href='https://www.cdc.gov/tobacco/campaign/tips/diseases/diabetes.html' target='_blank' style='text-decoration:none;'>🔗</a>
        """, unsafe_allow_html=True)

        st.warning("⚠️ Tidak ada tingkat merokok yang aman — berhenti merokok sepenuhnya adalah pilihan terbaik.")

        # Tambahan Tips Berhenti Merokok
        st.markdown("### 🚭 Tips Berhenti Merokok")
        st.info("""
        Berikut beberapa langkah yang dapat membantu Anda berhenti merokok:
        
        - 🎯 **Tetapkan Tekad**: Buat komitmen kuat untuk berhenti.  
        - 🗑️ **Buat Rencana**: Buang semua rokok & korek dari sekitar Anda.  
        - 🍬 **Pengganti Sehat**: Gunakan permen karet, permen bebas gula, atau lakukan aktivitas fisik.  
        - 👨‍👩‍👧 **Cari Dukungan**: Minta bantuan keluarga, teman, atau tenaga ahli.  
        - 💊 **Gunakan Terapi**: Pertimbangkan *Nicotine Replacement Therapy* (NRT) atau obat dari dokter.  
        - 🚫 **Hindari Pemicu**: Jauhi alkohol, kafein, atau suasana yang mendorong untuk merokok.  
        - 🧹 **Bersihkan Lingkungan**: Hilangkan bau rokok dari rumah, mobil, dan barang pribadi.  
        """)

        # Tambahkan link sumber dengan tampilan cantik
        st.markdown("""
        <div style="padding: 12px; border-radius: 10px; background-color: #e6f7ff; border: 1px solid #91d5ff; text-align: center;">
            🔗 Untuk tips lebih lanjut, baca di 
            <a href="https://www.klikdokter.com/info-sehat/kesehatan-umum/cara-efektif-berhenti-merokok" target="_blank" style="color: #0066cc; font-weight: bold; text-decoration: none;">
            Klikdokter - Cara Efektif Berhenti Merokok
            </a>
        </div>
        """, unsafe_allow_html=True)

        
    # ===============================
    # TAB ALKOHOL
    # ===============================
    with tab5:
        st.subheader("📌 Dampak Alkohol")
        st.markdown("""
        Konsumsi alkohol berlebihan dapat memengaruhi kesehatan jantung:

        1. **Tekanan Darah Tinggi**  
        Semakin tinggi konsumsi alkohol, semakin tinggi pula tekanan darah; bahkan konsumsi sedang yang teratur dapat meningkatkan tekanan darah, sehingga pembatasan alkohol direkomendasikan untuk mengelola hipertensi. <a href='https://www.palmerlakerecovery.com/alcohol-abuse-and-addiction/impact-on-cardiovascular-health/' target='_blank' style='text-decoration:none;'>🔗</a>

        2. **Risiko Stroke**  
        Konsumsi alkohol yang terbatas berpotensi memberikan efek perlindungan terhadap risiko stroke, namun konsumsi berlebihan meningkatkan risiko stroke iskemik (akibat penyumbatan pembuluh darah otak) dan stroke hemoragik (akibat pecahnya pembuluh darah). <a href='https://www.palmerlakerecovery.com/alcohol-abuse-and-addiction/impact-on-cardiovascular-health/' target='_blank' style='text-decoration:none;'>🔗</a>

        3. **Risiko Serangan Jantung**  
        Konsumsi alkohol berlebihan, terutama pesta minuman keras, dapat menyebabkan peningkatan tekanan darah akut, yang membebani jantung dan dapat memicu serangan jantung. <a href='https://www.palmerlakerecovery.com/alcohol-abuse-and-addiction/impact-on-cardiovascular-health/' target='_blank' style='text-decoration:none;'>🔗</a>
        """, unsafe_allow_html=True)


        # Tambahan Tips Berhenti Alkohol
        st.markdown("### 💡 Tips Berhenti Minum Alkohol")
        st.info("""
        Berikut beberapa langkah yang dapat membantu Anda berhenti minum alkohol:
        
        - 🧹 **Detoksifikasi**: Membersihkan tubuh dari pengaruh alkohol.  
        - 👥 **Dukungan Sosial**: Mencari bantuan dari orang terdekat atau kelompok seperti *Alcoholics Anonymous*.  
        - 💬 **Terapi & Konseling**: Mendapatkan bimbingan profesional untuk mengatasi kecanduan.  
        - 🩺 **Konsultasi Medis**: Berkonsultasi dengan dokter untuk bantuan obat-obatan jika diperlukan.  
        - 🏃 **Gaya Hidup Sehat**: Rutin berolahraga dan menjaga pola hidup sehat.  
        - 🎨 **Kegiatan Positif**: Isi waktu luang dengan hobi baru.  
        - 🚫 **Hindari Pemicu**: Jauhi lingkungan yang mendorong keinginan untuk minum.  
        """)

        # Card khusus untuk pesan utama
        st.markdown("""
            <div style="padding:15px; border-radius:12px; background-color:#e6f4ea; border:1px solid #a3d9a5; margin-top:15px; text-align:center;">
            ⚠️ <b>Batasi konsumsi alkohol, utamakan gaya hidup sehat untuk melindungi jantung.</b><br><br>
            ✅ <span style="color:#0f5132; font-weight:bold;">Pilihan terbaik untuk kesehatan adalah tidak mengonsumsi alkohol sama sekali.</span>
        </div>
        """, unsafe_allow_html=True)

        # Link sumber tambahan
        st.markdown("""
        <div style="padding: 12px; border-radius: 10px; background-color: #e6f7ff; border: 1px solid #91d5ff; text-align: center; margin-top:15px;">
            Untuk tips lebih lanjut, baca di 
            <a href="https://ciputrahospital.com/cara-mengatasi-kecanduan-alkohol/" target="_blank" style="color: #0066cc; font-weight: bold; text-decoration: none;">
            Ciputra Hospital - Cara Mengatasi Kecanduan Alkohol
            </a>
        </div>
        """, unsafe_allow_html=True)


    # ===============================
    # TAB AKTIVITAS
    # ===============================
    with tab6:
        st.subheader("📌 Pentingnya Aktivitas Fisik")
        st.markdown("""
        Aktivitas fisik sangat penting untuk menjaga kesehatan jantung & metabolisme:
        
        - ✅ Meningkatkan fungsi kardiovaskular  
        - ✅ Menurunkan tekanan darah  
        - ✅ Meningkatkan kolesterol HDL (baik)  
        - ✅ Mengatur kadar gula darah  
        - ✅ Menurunkan risiko obesitas & peradangan  
        - ✅ Meningkatkan kesehatan mental  
        
        🔗 <a href='https://ukhealthcare.uky.edu/wellness-community/blog/essential-role-exercise-cardiovascular-wellness' target='_blank' style='text-decoration:none;'>Sumber</a>
        """, unsafe_allow_html=True)
        
        st.info("🏋️ Latihan angkat beban terbukti membantu kontrol gula darah pada penderita diabetes tipe 2.")

if __name__ == "__main__":
    about_the_dataset()