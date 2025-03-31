
import streamlit as st
import joblib
import numpy as np

# Cargar el modelo entrenado
model = joblib.load("modelo_ayuda_medica.pkl")

st.title("Evaluador de Ayuda Médica")
st.write("Introduce los datos de la persona para saber si recibirá financiación médica.")

# Formulario de entrada de datos
historial_medico = st.selectbox("Historial Médico", [0, 1, 2, 3])
diagnostico_actual = st.selectbox("Diagnóstico Actual", [1, 2, 3, 4])
costo_tratamiento = st.number_input("Costo del Tratamiento", min_value=0)
beneficio_potencial = st.selectbox("Beneficio Potencial", [1, 2, 3])
indice_capacidad = st.selectbox("Índice de Capacidad Financiera", [1, 2, 3])
cobertura_seguro = st.slider("Cobertura de Seguro", 0.0, 1.0, 0.5)
numero_dependientes = st.number_input("Número de Dependientes", min_value=0, step=1)

if st.button("Evaluar"):
    datos = np.array([[historial_medico, diagnostico_actual, costo_tratamiento,
                       beneficio_potencial, indice_capacidad, cobertura_seguro,
                       numero_dependientes]])
    resultado = model.predict(datos)[0]
    if resultado == 1:
        st.success("✅ Tiene derecho a financiación médica.")
    else:
        st.error("❌ No tiene derecho a financiación médica.")
