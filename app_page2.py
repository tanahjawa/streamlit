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




    # ---------- Sidebar ----------
    st.sidebar.title("📚 Menu")
    menu = st.sidebar.radio("Pilih Halaman:", ["Informasi Edukatif"], key="menu_radio")


    # ---------- Halaman ----------
    if menu == "Informasi Edukatif":
        st.title("🧪 Informasi Edukatif")

        # Tabs
        tab1, tab2, tab3 = st.tabs(["🫀 Tekanan Darah", "🧬 Kolesterol", "🍬 Gula Darah"])

        # ===============================
        # TAB TEKANAN DARAH
        # ===============================
        with tab1:
            st.subheader("📌 Edukasi Tekanan Darah")
            st.markdown("""
            [Tekanan darah](https://medlineplus.gov/highbloodpressure.html#:~:text=What%20is%20blood%20pressure?,and%20a%20diastolic%20of%2080.) adalah tenaga dorongan darah pada dinding pembuluh arteri. Setiap kali jantung berdetak, darah dipompa masuk ke arteri untuk mengalir ke seluruh tubuh. 
            Dua nilai utama yang perlu diperhatikan adalah **sistolik** dan **diastolik**:
            
            - **Sistolik (angka atas)**. [Tekanan sistolik](https://www.alodokter.com/seperti-ini-cara-membaca-hasil-pemeriksaan-tekanan-darah) menggambarkan besarnya tekanan darah pada dinding arteri setelah jantung berkontraksi 
            Nilai Tekanan darah sistolik tercatat saat bunyi [Korotkoff](https://www.physio-pedia.com/Sphygmomanometer?utm_source=chatgpt.com) pertama terdengar.
            - **Diastolik (angka bawah)**. [Tekanan diastolik](https://www.alodokter.com/seperti-ini-cara-membaca-hasil-pemeriksaan-tekanan-darah) mencerminkan tekanan ketika jantung berada dalam fase relaksasi. 
            Nilai tekanan diastolik [tercatat](https://www.physio-pedia.com/Sphygmomanometer?utm_source=chatgpt.com) ketika bunyi tersebut hilang.
            
            Penting mengetahui kedua nilai karena keduanya saling terkait. Jika salah satunya terlalu tinggi atau rendah, hal ini bisa menjadi tanda masalah kesehatan dan perlu evaluasi lebih lanjut, baik untuk kondisi hipertensi maupun hipotensi.
            """)

            st.markdown("""
            Berdasarkan kategori yang diakui oleh American Heart Association (dikutip melalui [EatingWell](https://www.eatingwell.com/low-blood-pressure-symptoms-8580291)), berikut adalah rentang tekanan darah:
            """)
            
            st.subheader("📊 Kategori Tekanan Darah")
            st.markdown("""
            <table style="width:100%; border-collapse: collapse; border-radius: 10px; overflow: hidden; border:1px solid #ddd;">
                <tr style="background-color:#fce8eb;">
                    <th style="padding:8px; border:1px solid #ddd;">Kategori</th>
                    <th style="padding:8px; border:1px solid #ddd;">Sistolik (mmHg)</th>
                    <th style="padding:8px; border:1px solid #ddd;">Diastolik (mmHg)</th>
                </tr>
                <tr><td style='padding:8px; border:1px solid #ddd;'>Hipotensi</td><td style='padding:8px; border:1px solid #ddd;'>Kurang dari 90</td><td style='padding:8px; border:1px solid #ddd;'>Kurang dari 60</td></tr>
                <tr><td style='padding:8px; border:1px solid #ddd;'>Normal</td><td style='padding:8px; border:1px solid #ddd;'>90 – 119</td><td style='padding:8px; border:1px solid #ddd;'>60 – 79</td></tr>
                <tr><td style='padding:8px; border:1px solid #ddd;'>Meningkat</td><td style='padding:8px; border:1px solid #ddd;'>120 – 129</td><td style='padding:8px; border:1px solid #ddd;'>Kurang dari 80</td></tr>
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
                    [Kolesterol](https://my.clevelandclinic.org/health/articles/11920-cholesterol-numbers-what-do-they-mean) adalah lemak penting bagi tubuh untuk berbagai fungsi, namun jika berlebihan dapat menumpuk di dinding arteri, merusak lapisan pembuluh darah, dan membentuk plak aterosklerotik dan bisa meningkatkan risiko penyakit jantung.""")
                    st.write("""
                    Berikut beberapa kategori kolesterol yang perlu diketahui, yaitu:
                    - **Kolesterol Total**. Jumlah keseluruhan kolesterol yang beredar dalam darah seseorang.
                    - **HDL (High Density Lipoprotein)**. Kolesterol baik, membantu membersihkan kolesterol jahat.
                    - **LDL (Low Density Lipoprotein)**. Kolesterol jahat, menumpuk di pembuluh darah.
                    - **Trigliserida**. Lemak cadangan energi, jika tinggi dapat memicu penyakit metabolik.
                    """)

                    st.markdown("""
                    Berdasarkan [Cleveland Clinic](https://my.clevelandclinic.org/health/articles/11920-cholesterol-numbers-what-do-they-mean), berikut nilai kategori kolesterol:
                    """)


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
                                <a href="https://www.ncbi.nlm.nih.gov/books/NBK542294/" target="_blank">
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
            st.write("""
            Glukosa darah atau [gula darah](https://medlineplus.gov/bloodglucose.html#:~:text=What%20is%20blood%20glucose?,The%20typical%20targets%20are:) merupakan gula utama yang terdapat dalam darah dan menjadi sumber energi utama bagi tubuh. Ketika kadar glukosa meningkat, pankreas diberi sinyal untuk melepaskan insulin. Insulin adalah hormon yang membantu glukosa masuk ke dalam sel agar dapat digunakan sebagai energi. 
            """)
            st.write("""
            Apa itu diabetes? [diabetes](https://medlineplus.gov/bloodglucose.html#:~:text=What%20is%20blood%20glucose?,The%20typical%20targets%20are:) adalah penyakit ketika kadar glukosa darah terlalu tinggi akibat tubuh tidak cukup menghasilkan insulin atau tidak dapat menggunakannya dengan baik. Kondisi ini menyebabkan glukosa menumpuk di dalam darah dan, jika dibiarkan, dapat menimbulkan komplikasi serius, sehingga pengendalian kadar gula darah menjadi sangat penting.
            """)

            st.markdown("""
            Berdasarkan [nutrisense](https://www.nutrisense.io/blog/blood-sugar-level-charts), berikut nilai kategori gula darah untuk dewasa:
            """)

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

            st.subheader("📊 Kategori Gula Darah Normal Untuk Dewasa dengan [Diabetes](https://northwestclinic.org/normal-blood-sugar-levels-chart/)")
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
if __name__ == "__main__":
    about_the_dataset()