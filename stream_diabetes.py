#Load model sav
import pickle
#membuat codingan streamlit
import numpy as np
import streamlit as st
import base64


# import background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('background.jpg')

#load save model
model = pickle.load(open('diabetes_model.sav', 'rb'))
#judul web
# Path atau URL ke logo
logo_url = "https://images.vexels.com/content/175854/preview/diabetes-awareness-ribbon-drop-badge-sticker-6e51cf.png"

# HTML dan CSS untuk posisi logo
st.markdown(
    f"""
    <style>
    .logo-container {{
        display: flex;
        justify-content: center; /* Posisi tengah */
        align-items: center;
        height: 100px; /* Atur tinggi sesuai kebutuhan */
    }}
    </style>
    <div class="logo-container">
        <img src="{logo_url}" alt="Logo" width="140">
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("<h2 style='text-align: center;'>Aplikasi Prediksi Penyakit Diabetes Menggunakan Algoritma Logistic Regression</h2>",
            unsafe_allow_html=True)

#Membuat Form Input
col1, col2 = st.columns(2)
with col1:
  Pregnancies = st.number_input ('Input Nilai Pregnancies',value=0.0, format="%1f")
  Glucose = st.number_input ('Input Nilai Glucose',value=0.0, format="%1f")
  BloodPressure = st.number_input ('Input Nilai Blood Pressure',value=0.0, format="%1f")
  SkinThickness = st.number_input ('Input Nilai Skin Thickness',value=0.0, format="%1f")
with col2:
  Insulin = st.number_input ('Input Nilai Insulin',value=0.0, format="%1f")
  BMI = st.number_input ('Input Nilai BMI',value=0.0, format="%1f")
  DiabetesPedigreeFunction = st.number_input ('Input Nilai Diabetes Pedigree Function',value=0.0, format="%1f")
  Age = st.number_input ('Input Nilai Age',value=0.0, format="%1f")

#code untuk prediksi
diab_diagnosis =''

#membuat button prediksi
if st.button('**Test Prediksi Diabetes**', type="primary"):
  diab_prediction = model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
  if(diab_prediction[0] == 1):
    diab_diagnosis = '**Pasien Terkena Diabetes**'
    st.error(diab_diagnosis)
  else:
    diab_diagnosis = '**Pasien Tidak Terkena Diabetes**'
    st.success(diab_diagnosis)

