import streamlit as st
import random

# Título de la App
st.set_page_config(page_title="Plan Flor del Consuelo", page_icon="🥗")
st.title("🍎 Planificador de Dieta Post-Op")

# --- BASE DE DATOS FILTRADA (SIN ASTERISCOS) ---
# Se excluyen alimentos marcados con precaución (*) en las fotos
alimentos = {
    "AOAV": ["Clara de huevo", "Alubias/Lentejas", "Soya texturizada", "Queso Panela", "Requesón", "Pollo (sin piel)", "Pescado blanco"],
    "Cereales": ["Elote desgranado", "Papa cocida", "Tortilla de maíz", "Tostada horneada"],
    "Verduras": ["Acelga", "Berenjena", "Betabel", "Brócoli", "Calabacita", "Chayote", "Chilacayote", "Chile poblano", "Zanahoria"],
    "Frutas": ["Ciruela", "Durazno", "Fresa", "Manzana", "Melón", "Naranja", "Papaya", "Pera", "Piña", "Plátano", "Sandía", "Uva"],
    "Grasas": ["Aceite Vegetal", "Aguacate", "Nuez (sin sal)"]
}

# --- LÓGICA DE PORCIONES POR MEAL ---
def generar_menu():
    st.subheader("📋 Menú Recomendado")
    
    # Distribución: 1 AOAV, 1 Cereal, 1/2 Verdura, 1/2 Fruta, 1/2 Grasa (según tabla)
    col1, col2, col3 = st.columns(3)
    
    for col, meal in zip([col1, col2, col3], ["Desayuno", "Comida", "Cena"]):
        with col:
            st.markdown(f"**{meal}**")
            st.write(f"• {random.choice(alimentos['AOAV'])}")
            st.write(f"• {random.choice(alimentos['Cereales'])}")
            st.write(f"• {random.choice(alimentos['Verduras'])} (1/2 taza)")
            st.write(f"• {random.choice(alimentos['Frutas'])} (1/2 taza)")
            st.info("🥤 + 1/2 Ensure Advance")

if st.button('🔄 Generar Combinación'):
    generar_menu()

st.sidebar.warning("⚠️ Líquidos totales permitidos: 1200 ml/día.")
st.sidebar.info("Medicinas: Yakult, Complejo B y Ácido Fólico.")
