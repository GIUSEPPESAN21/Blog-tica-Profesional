import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Optimizando con Dignidad | Ética Profesional",
    page_icon="⚙️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilos CSS adicionales para darle un toque más de "artículo"
st.markdown("""
    <style>
    .justified-text {
        text-align: justify;
    }
    .quote-box {
        background-color: #f0f7ff;
        border-left: 5px solid #0066cc;
        padding: 15px;
        font-style: italic;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado Principal
st.title("⚙️ Optimizando con Dignidad")
st.subheader("La Revolución Ética de la Ingeniería Industrial en la Era de las Capacidades")
st.info("**Audiencia Objetivo:** Alta Dirección de Operaciones y Estudiantes Universitarios de Ingeniería.")

st.divider()

# Introducción
st.header("Introducción: El algoritmo incompleto de la productividad")
st.markdown("""
<div class="justified-text">
Durante décadas, la ingeniería industrial ha sido definida como la ciencia de la optimización. Tradicionalmente, se nos enseña a medir el éxito mediante indicadores estrictos de rendimiento y reducción de costos. Sin embargo, cuando reducimos la organización a una mera máquina de maximizar beneficios, el sistema queda incompleto.

Como señalan <strong>Adela Cortina y Emilio Martínez</strong>, la actividad profesional no puede desvincularse de su dimensión moral sin perder su legitimidad social. Si tratamos a las personas como meros insumos, caemos en la instrumentalización. En este espacio exploraremos un nuevo paradigma: <strong>la optimización centrada en la dignidad humana</strong>.
</div>
""", unsafe_allow_html=True)

# Sección 1
st.header("1. El 'Bien Interno' de la Ingeniería Industrial")
st.markdown("""
Para comprender la ética de nuestra profesión, debemos recuperar la distinción aristotélica entre *bienes internos* y *bienes externos*:

* **Bienes externos:** Dinero, poder, estatus o utilidad neta de la planta.
* **Bienes internos:** La meta social que da sentido a la profesión; en nuestro caso, crear sistemas de trabajo que armonicen la viabilidad técnica con el bienestar humano.
""")

st.markdown("""
<div class="quote-box">
"Cuando un director de operaciones sacrifica la salud física de sus operarios para aumentar un margen de ganancia a corto plazo, está corrompiendo la profesión. La verdadera excelencia radica en diseñar procesos donde la eficiencia sea el vehículo para la dignificación."
</div>
""", unsafe_allow_html=True)

# Sección 2
st.header("2. Más allá de Taylor: El Trabajador como Fin en Sí Mismo")
st.markdown("""
<div class="justified-text">
El taylorismo clásico trató de convertir al obrero en una extensión de la máquina. La <strong>ética deontológica de Kant</strong> dinamita esta perspectiva al recordarnos que las cosas tienen precio, pero las personas tienen dignidad.

En la ingeniería industrial moderna, esto nos exige una <em>ergonomía proactiva</em>, el diseño de <em>sistemas sociotécnicos</em> que eviten la alienación, y una <em>automatización ética</em> que libere al humano de tareas peligrosas en lugar de desecharlo ciegamente.
</div>
""", unsafe_allow_html=True)

# Sección 3
st.header("3. Del OEE a las 'Capacidades' (Martha Nussbaum)")
st.markdown("""
En su obra *Crear capacidades*, **Martha Nussbaum** critica a quienes miden el progreso solo a través del PIB. Esta crítica aplica a los directores que evalúan el éxito solo a través de la rentabilidad o el indicador OEE (Efectividad Total de los Equipos).

Proponemos transitar hacia un **Índice de Capacidades Industriales**, midiendo qué es realmente capaz de hacer y ser cada trabajador. Algunas de las capacidades centrales aplicadas a la industria son:
""")

# Tabla de capacidades usando datos de Streamlit
import pandas as pd
data = {
    "Capacidad (Nussbaum)": ["Vida y Salud Corporal", "Sentidos y Pensamiento", "Razón Práctica"],
    "Aplicación en Dirección Industrial": [
        "Espacios libres de riesgos; ergonomía preventiva e integral.", 
        "Capacitación continua; filosofía Kaizen y mejora continua.", 
        "Autonomía y empoderamiento en la toma de decisiones del puesto."
    ]
}
df = pd.DataFrame(data)
# Ocultamos el índice de la tabla para que se vea más limpia
st.dataframe(df, hide_index=True, use_container_width=True)

# Sección 4
st.header("4. Ética Discursiva en Decisiones Estratégicas")
st.markdown("""
<div class="justified-text">
Ante reestructuraciones o despidos por automatización, la <strong>Ética del Discurso de Habermas</strong> establece que una decisión solo es válida si cuenta con el consenso de los afectados. El ingeniero ético no impone desde su escritorio; facilita mesas de diálogo con operarios, sindicatos y comunidades, equilibrando la convicción técnica con la responsabilidad social.
</div>
""", unsafe_allow_html=True)

# Conclusión
st.header("Conclusión")
st.success("**Optimizamos procesos para que la vida florezca, no para que la dignidad se deprecie.** \n\nIntegrar la ética no es caridad corporativa, es la única estrategia viable para la sostenibilidad. Para los estudiantes, el reto es diseñar sistemas donde la tecnología potencie la libertad.")

st.divider()

# Referencias (Usamos un 'expander' para que no ocupe tanto espacio visual, pero esté presente)
with st.expander("📚 Referencias Bibliográficas (APA 7)"):
    st.markdown("""
    * Cortina, A., & Martínez Navarro, E. (2001). *Ética*. Ediciones Akal.
    * Correa Casanova, M., & Martínez Becerra, P. (Eds.). (2010). *La riqueza ética de las profesiones*. RIL Editores.
    * Nussbaum, M. C. (2012). *Crear capacidades: Propuesta para el desarrollo humano*. Paidós.
    * Sen, A. (2000). *Desarrollo y libertad*. Editorial Planeta.
    * Kant, I. (2012). *Fundamentación para una metafísica de las costumbres*. Alianza Editorial.
    """)

# Footer
st.caption("© 2026 Proyecto Final Ética Profesional - UNIMINUTO. Desarrollado en Python con Streamlit.")
