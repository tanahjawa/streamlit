import streamlit as st
import pandas as pd
import joblib
import gdown
import os
import numpy as np
from scipy.stats import boxcox
from sklearn.preprocessing import StandardScaler

# Load model dan scaler
MODEL_PATH = "stacking5.pkl"
SCALER_PATH = "scaler5.pkl"

# link Google Drive (file di set "Anyone with the link" -> "Viewer")
MODEL_URL = "https://drive.google.com/uc?id=1zYe3jM3U4_bovpx-_dJkUPjn0poHQwd9"
SCALER_URL = "https://drive.google.com/uc?id=1quPoXkwtTJzt4IrztItNmPzUvM_mUr9X"

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        gdown.download(MODEL_URL, MODEL_PATH, quiet=False)
    with open(MODEL_PATH, "rb") as f:
        return joblib.load(f)

@st.cache_resource
def load_scaler():
    if not os.path.exists(SCALER_PATH):
        gdown.download(SCALER_URL, SCALER_PATH, quiet=False)
    with open(SCALER_PATH, "rb") as f:
        return joblib.load(f)

model = load_model()
scaler = load_scaler()

# Fungsi kategori probabilitas
def prob(prediction_proba):
    # Pastikan prediction_proba dalam skala 0–1
    if prediction_proba < 0.10:
        return 'rendah'
    elif prediction_proba < 0.50:
        return 'sedang'
    else:
        return 'tinggi'


def heart_disease_prediction_page():
    st.title("Prediksi Risiko Kardiovaskular")
    st.markdown("""
    Aplikasi ini membantu Anda mengetahui **perkiraan risiko kardiovaskular** berdasarkan data kesehatan dasar.  
    """)

    st.header("🔎 Masukkan Faktor Risiko Kesehatan")

    # ================= INPUT DATA =================
    with st.expander("👤 Data Pribadi", expanded=True):
        age = st.slider('Umur (tahun)', 18, 90, 50)
        gender = st.selectbox('Jenis Kelamin', ('Laki-laki', 'Perempuan'))
        height = st.slider('Tinggi Badan (cm)', 100, 250, 170)
        weight = st.slider('Berat Badan (kg)', 30, 200, 70)

    # ================= TEKANAN DARAH =================
    if "show_details_bp" not in st.session_state:
        st.session_state.show_details_bp = False
    if "expand_bp" not in st.session_state:
        st.session_state.expand_bp = False

    def toggle_details_bp():
        st.session_state.show_details_bp = not st.session_state.show_details_bp
        st.session_state.expand_bp = True

    # ================= KONDISI KLINIS =================
    st.subheader("🩺 Kondisi Klinis")
    st.markdown("""
    Bagian ini berisi data hasil pemeriksaan medis dasar seperti tekanan darah, kolesterol, dan gula darah. Jika Anda belum memiliki hasil tes terbaru, Anda tetap bisa memilih kategori yang paling mendekati kondisi saat ini. Sebagai panduan, silakan lihat **tabel kategori** di bawah ini, atau gunakan tombol **Lihat Detail** untuk informasi gejala yang lebih lengkap.

    """)

    with st.expander("🩸 Tekanan Darah", expanded=st.session_state.expand_bp):
        bp_input = st.text_input("Masukkan nilai tekanan darah (contoh: 120/80)", value="", placeholder="Contoh Format: 120/80")
        try:
            ap_hi, ap_lo = map(int, bp_input.split("/"))
        except:
            ap_hi, ap_lo = 120, 80
            if bp_input:
                st.error("⚠️ Format salah. Gunakan format misal: 120/80")

        # 🆕 Tambahkan penjelasan singkat di sini
        st.info(
            "ℹ️ Inputkan nilai tekanan darah terkini (setelah tes). Jika belum ada, gunakan tombol **Lihat Detail Tekanan Darah** atau **Tabel Kategori Tekanan Darah** untuk menentukan nilainya."
        )

        button_label_bp = "🔽 Tutup Detail Tekanan Darah" if st.session_state.show_details_bp else "📌 Lihat Detail Tekanan Darah"
        st.button(button_label_bp, on_click=toggle_details_bp, key="btn_bp")

        if st.session_state.show_details_bp:
            st.subheader("🖊️ Masukkan Hasil Pemeriksaan")
            st.markdown("""
            """)            
            st.markdown("""
                <div style="padding:12px; background-color:#f7fbff; border-left:5px solid #4da4ff; border-radius:8px;">
                    <p><b>ℹ️ Gejala Umum Berdasarkan Kategori:</b></p>
                    <p>Jika Anda <b>belum memiliki hasil pemeriksaan tekanan darah</b>, Anda dapat menggunakan <b>gejala-gejala umum</b> sebagai panduan awal untuk memilih kategori yang paling sesuai. Misalnya, jika kondisi Anda menggambarkan tekanan darah normal, maka Anda bisa mengisi nilai dalam rentang normal contoh: 110/70 atau 115/75.</p>
                    <p><b>Normal (90–119 / 60–79 mmHg):</b></p>
                <ul>
                    <li>Tidak ada gejala khusus.</li>
                    <li>Jika merasa pusing ringan di dahi/kening, biasanya disebabkan oleh kurang tidur, stres, atau dehidrasi ringan.</li>
                </ul>

                <p><b>Di atas normal / Pra-Hipertensi (120–129 / <80 mmHg):</b></p>
                <ul>
                    <li>Biasanya tidak ada gejala yang spesifik.</li>
                    <li>Tingkatkan kewaspadaan karena kondisi ini dapat berkembang menjadi hipertensi jika tidak dikelola dengan baik.</li>
                    <li>Contoh gejala ringan: terasa cepat lelah atau mudah lelah saat aktivitas ringan.</li>
                </ul>
                <p><b>Sangat tidak normal / Hipertensi (≥130 / ≥80 mmHg, termasuk Tahap 1, Tahap 2, dan Krisis ≥180 / ≥120 mmHg):</b></p>
                <ul>
                    <li>Sakit kepala parah</li>
                    <li>Nyeri dada</li>
                    <li>Pusing</li>
                    <li>Kesulitan bernafas</li>
                    <li>Mual atau muntah</li>
                    <li>Penglihatan kabur atau perubahan penglihatan</li>
                    <li>Kecemasan atau kebingungan</li>
                    <li>Berdengung di telinga</li>
                    <li>Mimisan</li>
                    <li>Irama jantung tidak normal</li>
                </ul>

                <p><b>Disclaimer:</b> Jika sudah melakukan tes, utamakan nilai hasil tes Anda...</i>
                </div>
                """, unsafe_allow_html=True)

        st.subheader("📌 Tekanan Darah")
        st.markdown("""
        Berikut adalah kategori tekanan darah menurut American Heart Association (dikutip dari [EatingWell](https://www.eatingwell.com/low-blood-pressure-symptoms-8580291)):
        """)
        st.subheader("📊 Kategori Tekanan Darah")
        st.markdown("""
        <table style="width:100%; border-collapse: collapse; border-radius: 10px; overflow: hidden; border:1px solid #ddd;">
            <tr style="background-color:#fce8eb;">
                <th style="padding:8px; border:1px solid #ddd;">Kategori</th>
                <th style="padding:8px; border:1px solid #ddd;">Sistolik (mmHg) angka atas</th>
                <th style="padding:8px; border:1px solid #ddd;">Diastolik (mmHg) angka bawah</th>
            </tr>
            <tr><td>Hipotensi (Rendah)</td><td>Kurang dari 90</td><td>Kurang dari 60</td></tr>
            <tr><td>Normal</td><td>90 – 119</td><td>60 – 79</td></tr>
            <tr><td>Meningkat</td><td>120 – 129</td><td>Kurang dari 80</td></tr>
            <tr><td>Hipertensi Tahap 1</td><td>130 – 139</td><td>80 – 89</td></tr>
            <tr><td>Hipertensi Tahap 2</td><td>≥ 140</td><td>≥ 90</td></tr>
            <tr><td>Krisis Hipertensi (Darurat)</td><td>> 180</td><td>> 120</td></tr>
        </table>
        """, unsafe_allow_html=True)



    # ================= KOLESTEROL =================
    if "show_details_chol" not in st.session_state:
        st.session_state.show_details_chol = False
    if "expand_chol" not in st.session_state:
        st.session_state.expand_chol = False

    def toggle_details_chol():
        st.session_state.show_details_chol = not st.session_state.show_details_chol
        st.session_state.expand_chol = True

    with st.expander("🥓 Kolesterol", expanded=st.session_state.expand_chol):
        cholesterol = st.selectbox('Level Kolesterol', ('Normal', 'Di atas normal', 'Sangat tinggi'))

        st.info(
            "ℹ️ Jika sudah ada hasil tes kolesterol, cocokkan nilainya dengan tabel di bawah. Jika belum ada, gunakan tombol **Lihat Detail Kolesterol** atau **Tabel Kategori Kolesterol** untuk menentukan kategori."
        )

        button_label_chol = "🔽 Tutup Detail Kolesterol" if st.session_state.show_details_chol else "📌 Lihat Detail Kolesterol"
        st.button(button_label_chol, on_click=toggle_details_chol, key="btn_chol")

        if st.session_state.show_details_chol:
            st.markdown("""
            <br>
            <div style="padding:12px; background-color:#fff7f7; border-left:5px solid #ff4d6d; border-radius:8px;">
                <p>ℹ️ Kolesterol biasanya tidak menimbulkan gejala, sehingga diperlukan tes darah untuk mengetahui kategori sebenarnya.
                <br>Jika Anda belum melakukan tes, Anda tetap bisa pilih kategori sesuai kondisi, misalnya kolesterol agak tinggi. Nanti aplikasi akan memperkirakan berapa persen tingkat risikonya, dengan mempertimbangkan data lainnya.</p>
            """, unsafe_allow_html=True)

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
                <td>Kurang dari 40 (pria), > 50 (wanita)</td>
                <td>Lebih dari 500</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)

    # ================= GULA DARAH =================
    if "show_details_gluc" not in st.session_state:
        st.session_state.show_details_gluc = False
    if "expand_gluc" not in st.session_state:
        st.session_state.expand_gluc = False

    def toggle_details_gluc():
        st.session_state.show_details_gluc = not st.session_state.show_details_gluc
        st.session_state.expand_gluc = True

    with st.expander("🍬 Gula Darah", expanded=st.session_state.expand_gluc):
        gluc = st.selectbox('Level Gula Darah', ('Normal', 'Di atas normal', 'Sangat tinggi'))

        st.info(
            "ℹ️ Jika sudah ada hasil tes gula darah, cocokkan nilainya dengan tabel di bawah. Jika belum ada, gunakan tombol **Lihat Detail Gula Darah** atau **Tabel Kategori Gula Darah** untuk menentukan kategori."
        )

        button_label_gluc = "🔽 Tutup Detail Gula Darah" if st.session_state.show_details_gluc else "📌 Lihat Detail Gula Darah"
        st.button(button_label_gluc, on_click=toggle_details_gluc, key="btn_gluc")

        if st.session_state.show_details_gluc:
            st.markdown("""
                <div style="padding:12px; background-color:#f7fbff; border-left:5px solid #4da4ff; border-radius:8px;">
                    <p><b>ℹ️ Catatan Tambahan:</b></p>
                    <p><b>Gejala gula darah di atas normal (prediabetes):</b></p>
                    <p>Kondisi di atas normal atau prediabetes terjadi saat kadar gula darah lebih tinggi dari normal, tetapi belum cukup tinggi untuk disebut diabetes. Biasanya tidak menimbulkan gejala yang jelas, namun beberapa orang dapat mengalami:</p>
                <ul>
                    <li>Buang air kecil dalam jumlah banyak</li>
                    <li>Rasa haus yang berlebihan</li>
                    <li>Merasa lelah</li>
                    <li>Sering lapar</li>
                    <li>Mulut kering</li>
                    <li>Penurunan berat badan</li>
                    <li>Penglihatan kabur</li>
                    <li>Infeksi berulang (misalnya, infeksi saluran kemih, infeksi kulit)</li>
                    <li>Luka (luka sayat, lecet) yang sembuhnya lambat</li>
                </ul>
                    <p><b>Hiperglikemia (Gula Darah Tinggi atau sangat tidak normal)</b></p>
                    <p>Gejala-gejala yang "sangat tidak normal" ini menunjukkan peningkatan gula darah yang cepat dan parah, yang memerlukan perhatian medis segera. </p>

                <ul>
                    <li>Mual dan muntah: Merasa mual dan muntah</li>
                    <li>Sakit perut: Nyeri di perut, terutama pada anak-anak. </li>
                    <li>Bau napas buah : Napas yang berbau seperti permen buah pir atau buah manis lainnya. </li>
                    <li>Mengantuk dan kebingungan: Merasa mengantuk, kesulitan untuk tetap terjaga, atau kesulitan berkonsentrasi. </li>
                    <li>Pernapasan atau detak jantung cepat: Bernapas lebih cepat dari biasanya atau detak jantung lebih cepat dari normal. </li>
                    <li>Kehadiran keton : Tingginya kadar keton dalam urin atau darah. </li>
                </ul>
                </div>
                """, unsafe_allow_html=True)

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

    # ================= KEBIASAAN =================
    with st.expander("🚬 Kebiasaan & Aktivitas", expanded=False):
        smoke = st.selectbox('Apakah Anda Merokok?', ('Tidak', 'Ya'))
        alco = st.selectbox('Apakah Anda Mengonsumsi Alkohol?', ('Tidak', 'Ya'))
        active = st.selectbox('Apakah Anda Aktif Secara Fisik?', ('Tidak', 'Ya'))

    # ================= PROSES DATA =================
    opt_lambda = 0.15
    def boxcox_transform(x, lmbda):
        return np.log(x) if lmbda == 0 else (x ** lmbda - 1) / lmbda

    age_box = boxcox_transform(age, opt_lambda)
    bmi = weight / ((height / 100) ** 2)
    pulse_pressure = ap_hi - ap_lo
    mean_ap = (ap_hi + 2 * ap_lo) / 3

    chol_map = {
        'Normal': 'cholesterol_normal',
        'Di atas normal': 'cholesterol_above_normal',
        'Sangat tinggi': 'cholesterol_well_above_normal'
    }
    gluc_map = {
        'Normal': 'gluc_normal',
        'Di atas normal': 'gluc_above_normal',
        'Sangat tinggi': 'gluc_well_above_normal'
    }

    chol_encoded = {key: False for key in chol_map.values()}
    chol_encoded[chol_map[cholesterol]] = True
    gluc_encoded = {key: False for key in gluc_map.values()}
    gluc_encoded[gluc_map[gluc]] = True

    input_data = {
        'age_box': [age_box],
        'gender': [1 if gender == 'Laki-laki' else 0],
        'weight': [weight],
        'smoke': [1 if smoke == 'Ya' else 0],
        'alco': [1 if alco == 'Ya' else 0],
        'active': [1 if active == 'Ya' else 0],
        'pulse_pressure': [pulse_pressure],
        'map': [mean_ap],
        'bmi': [bmi],
        **{key: [val] for key, val in chol_encoded.items()},
        **{key: [val] for key, val in gluc_encoded.items()}
    }

    ordered_columns = [
        'age_box', 'gender', 'weight', 'smoke', 'alco', 'active',
        'pulse_pressure', 'map', 'bmi',
        'cholesterol_above_normal', 'cholesterol_normal', 'cholesterol_well_above_normal',
        'gluc_above_normal', 'gluc_normal', 'gluc_well_above_normal'
    ]

    features = pd.DataFrame(input_data)
    for col in ordered_columns:
        if col not in features.columns:
            features[col] = 0
    features = features[ordered_columns]

    scaler = load_scaler()
    model = load_model()

    # ================= HASIL PREDIKSI =================
    if scaler and model:
        num_cols = ['age_box', 'gender', 'weight', 'smoke', 'alco', 'active', 'pulse_pressure', 'map', 'bmi']
        features[num_cols] = scaler.transform(features[num_cols])

        prediction_proba = model.predict_proba(features)
        probability = prediction_proba[0][1] * 100
        risk_level = prob(prediction_proba[0][1])

        st.subheader("📊 Hasil Prediksi Risiko Kardiovaskular")
        if risk_level == "rendah":
            color, level = "#4FB783", "Risiko Rendah"
        elif risk_level == "sedang":
            color, level = "#005A9C", "Risiko Sedang"
        else:
            color, level = "#A91D3A", "Risiko Tinggi"

        st.markdown(
            f"<span style='color:{color}; font-weight:bold;'>Probabilitas Anda terkena risiko kardiovaskular adalah {probability:.2f}% ({level})</span>",
            unsafe_allow_html=True
        )

        # --- Pesan berdasarkan kategori risiko ---
        if risk_level == "rendah":
            st.info("✅ Risiko sangat kecil / jarang terjadi. Terus pertahankan gaya hidup sehat dengan menjaga pola makan, rutin berolahraga, dan menghindari stres berlebihan. Nilai ini menunjukkan kemungkinan pasien mengalami gangguan kardiovaskular berdasarkan prediksi model, bukan hasil diagnosis medis langsung.")

        elif risk_level == "sedang":
            st.warning("⚠️ Risiko sedang / kemungkinan mulai meningkat. Disarankan untuk mulai memperhatikan kebiasaan sehari-hari seperti mengurangi konsumsi garam, berhenti merokok, dan menjaga berat badan ideal. Lakukan pemeriksaan rutin agar dapat memantau kondisi jantung lebih baik. Nilai ini menunjukkan kemungkinan pasien mengalami gangguan kardiovaskular berdasarkan prediksi model, bukan hasil diagnosis medis langsung.")

        else:  # tinggi
            st.error("🚨 Risiko tinggi / sangat mungkin terjadi. Segera konsultasikan dengan tenaga medis atau dokter spesialis jantung untuk pemeriksaan lebih lanjut. Terapkan gaya hidup sehat secara konsisten dan hindari faktor risiko seperti merokok, konsumsi alkohol, serta kurangnya aktivitas fisik. Nilai ini menunjukkan kemungkinan pasien mengalami gangguan kardiovaskular berdasarkan prediksi model, bukan hasil diagnosis medis langsung.")


        # ================= PENJELASAN NILAI RISIKO =================
        st.markdown("")
        if "show_info_qrisk" not in st.session_state:
            st.session_state.show_info_qrisk = False

        def toggle_qrisk_info():
            st.session_state.show_info_qrisk = not st.session_state.show_info_qrisk

        button_label_qrisk = "📖 Baca Penjelasan Nilai Risiko" if not st.session_state.show_info_qrisk else "🔽 Tutup Penjelasan"
        st.button(button_label_qrisk, on_click=toggle_qrisk_info)

        if st.session_state.show_info_qrisk:
            st.markdown("""
            Risiko kardiovaskular menggambarkan kemungkinan seseorang mengalami penyakit jantung atau pembuluh darah seperti **serangan jantung** atau **stroke** dalam jangka waktu tertentu.

            > “It’s important to note that your risk of developing CVD is never zero and regardless of other risk factors, your risk naturally increases the older you get.”  
            > — *Winchmore Hill Practice* <a href='https://www.winchmorehillpractice.nhs.uk/2021/09/08/cardiovascular-risk-score-qrisk2-patient-information-leaflet/' target='_blank' style='text-decoration:none;'>🔗</a>

            💡 **Artinya:**  
            Risiko terkena penyakit kardiovaskular **tidak pernah benar-benar nol**, karena sistem jantung dan pembuluh darah bekerja terus-menerus sepanjang hidup.  
            Selama jantung berdetak dan darah mengalir, risiko gangguan selalu ada — walaupun sangat kecil.

            ---

            🩺 **Jika hasil menunjukkan risiko yang sangat rendah (misalnya di bawah 1% seperti 0,99%)**  
            👉 Itu berarti peluang mengalami serangan jantung atau stroke dalam 10 tahun ke depan **sangat kecil**.  
            Namun, **risiko kecil bukan berarti nol**.

            🔸 **Perhatikan juga sinyal tubuh:**  
            Kadang muncul gejala ringan seperti:  
            - Kepala terasa berat atau pusing di bagian depan dekat mata 🧠  
            - Mudah lelah atau kurang fokus  
            - Jantung berdebar ringan setelah minum kopi  

            Biasanya hal ini **tidak berbahaya**, tapi bisa disebabkan oleh:  
            - Kurang tidur 😴  
            - Stres berlebih 😣  
            - Konsumsi kafein berlebihan ☕

            Gejala seperti ini hanyalah bentuk **“alarm” alami dari tubuh**, tanda bahwa sistem kardiovaskular sedang beradaptasi dan butuh istirahat.

            ---

            **📊 Kategori Risiko (QRISK2 – 10 tahun ke depan):**

            | Kategori Risiko | Rentang QRISK2 | Penjelasan |
            |------------------|----------------|-------------|
            | 🟢 **Rendah** | `< 10%` | Kurang dari 1 dari 10 orang berisiko mengalami serangan jantung atau stroke dalam 10 tahun. |
            | 🟡 **Sedang** | `10–20%` | Sekitar 1–2 dari 10 orang berisiko mengalami serangan jantung atau stroke dalam 10 tahun. |
            | 🔴 **Tinggi** | `> 20%` | Lebih dari 2 dari 10 orang berisiko mengalami serangan jantung atau stroke dalam 10 tahun. |

            ---

            🔹 **Kesimpulan:**  
            Tidak ada risiko 0%. Semua orang memiliki risiko kardiovaskular, hanya saja tingkatnya bisa **sangat rendah**.  
            Bahkan gejala ringan seperti **kepala terasa cenut-cenut** bisa menjadi tanda kecil dari sistem pembuluh darah yang memberi sinyal, meskipun belum tentu berbahaya.
            """, unsafe_allow_html=True)

        st.markdown(
            """
            <hr style="margin-top: 25px; margin-bottom: 10px;">
            <div style="text-align: center; color: black; font-size: 16px; font-style: italic;">
                ⚠️ Nilai tersebut menunjukkan tingkat risiko kardiovaskular berdasarkan <b>prediksi model</b>, 
                bukan <b>diagnosis medis</b>.
            </div>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    heart_disease_prediction_page()
