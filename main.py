import streamlit as st
import random

# Configuración visual de la App
st.set_page_config(page_title="Plan Flor del Consuelo", page_icon="🥗")
st.title("🍎 Planificador de Dieta: Flor del Consuelo")

# --- BASE DE DATOS (Filtrada: SE EXCLUYEN alimentos con asterisco *) ---
alimentos = {
    "AOAV (Proteína)": ["Clara de huevo (2 pzas)", "Frijol/Lenteja/Soya (1/2 taza)", "Queso Panela (40g)", "Requesón (3 cdas)", "Queso Oaxaca (30g)", "Pollo sin piel (30g)", "Pescado blanco (40g)"],
    "Cereales": ["Elote desgranado (1/2 taza)", "Papa cocida (1/2 pza)", "Tortilla de maíz (1 pza)", "Tostada horneada (1 pza)"],
    "Verduras": ["Calabacita", "Chayote", "Jitomate", "Lechuga", "Nopal", "Pepino", "Zanahoria", "Champiñón", "Betabel", "Brócoli"],
    "Frutas": ["Manzana", "Pera", "Papaya", "Melón", "Plátano", "Sandía", "Fresa", "Mango", "Naranja"],
    "Grasas": ["Aceite Vegetal (1 cdita)", "Aguacate (1/3 pza)", "Nuez sin sal (7 mitades)"]
}

# --- LÓGICA DE DISTRIBUCIÓN POR TIEMPO DE COMIDA ---
def generar_menu():
    st.subheader("📋 Menú Generado para Hoy")
    
    # Desayuno: 1 AOAV, 1 Cereal, 1/2 Verdura, 1/2 Fruta, 1/2 Grasa (según notas manuales)
    with st.expander("🌅 DESAYUNO"):
        st.write(f"**Proteína:** {random.choice(alimentos['AOAV (Proteína)'])}")
        st.write(f"**Cereal:** {random.choice(alimentos['Cereales'])}")
        st.write(f"**Vegetal/Fruta:** {random.choice(alimentos['Verduras'])} y {random.choice(alimentos['Frutas'])}")
        st.info("💊 Tomar: Yakult Light + 1/2 Complejo B + 1/2 Ácido Fólico")

    # Comida: 2 AOAV, 1 Cereal, 1/2 Verdura, 1/2 Fruta, 1/2 Grasa
    with st.expander("☀️ COMIDA"):
        st.write(f"**Proteína:** {', '.join(random.sample(alimentos['AOAV (Proteína)'], 2))}")
        st.write(f"**Cereal:** {random.choice(alimentos['Cereales'])}")
        st.write(f"**Complementos:** {random.choice(alimentos['Verduras'])} y {random.choice(alimentos['Frutas'])}")
        st.info("🥤 Incluir: 1/2 bote de Ensure Advance")

    # Cena: 1 AOAV, 1 Cereal, 1/2 Verdura, 1/2 Fruta, 1/2 Grasa
    with st.expander("🌙 CENA"):
        st.write(f"**Proteína:** {random.choice(alimentos['AOAV (Proteína)'])}")
        st.write(f"**Cereal:** {random.choice(alimentos['Cereales'])}")
        st.write(f"**Ligero:** {random.choice(alimentos['Frutas'])}")
        st.info("🥤 Incluir: 1/2 bote de Ensure Advance")

if st.button('🎲 Generar Nuevas Combinaciones'):
    generar_menu()

# --- RECOMENDACIONES GENERALES ---
st.sidebar.header("⚠️ Indicaciones Médicas")
st.sidebar.write("- **Líquidos totales:** 1200 ml/día")
st.sidebar.write("- **Suplementos:** 2 botes de Ensure Advance al día")
st.sidebar.write("- **Evitar:** Refrescos, embutidos y enlatados")
