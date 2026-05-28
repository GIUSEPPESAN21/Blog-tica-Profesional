import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title="Optimizando con Dignidad | Ética en Ingeniería",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    /* Importar fuente moderna de Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Ocultar barra lateral y controles nativos para un look de "Sitio Web" */
    [data-testid="collapsedControl"] { display: none; }
    [data-testid="stSidebar"] { display: none; }
    header[data-testid="stHeader"] { background: transparent; }
    
    /* Hero Banner Principal */
    .hero-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
        padding: 3.5rem 2rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        position: relative;
        overflow: hidden;
    }
    
    /* Efecto de brillo de fondo en el banner */
    .hero-banner::after {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%);
        transform: rotate(30deg);
        pointer-events: none;
    }

    .hero-title { font-size: 3.5rem; font-weight: 800; margin-bottom: 0.5rem; letter-spacing: -1px; line-height: 1.2; }
    .hero-subtitle { font-size: 1.3rem; font-weight: 300; color: #cbd5e1; margin-bottom: 1.5rem; }
    
    /* Tarjetas de Contenido (Cards) */
    .glass-card {
        background: #ffffff;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        border: 1px solid #f1f5f9;
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    }
    
    /* Tipografía de Texto */
    .text-justify { text-align: justify; line-height: 1.8; color: #475569; font-size: 1.15rem; }
    .gradient-text { background: linear-gradient(90deg, #2563eb, #7c3aed); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800; }
    
    /* Citas Destacadas */
    .custom-quote {
        border-left: 5px solid #3b82f6;
        background: #eff6ff;
        padding: 1.5rem 2rem;
        border-radius: 0 12px 12px 0;
        font-style: italic;
        color: #1e3a8a;
        margin: 2rem 0;
        font-size: 1.2rem;
        box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.03);
    }

    /* Estilos Premium para las Pestañas (Tabs) */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 0.5rem;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        gap: 4px;
        border: 1px solid #e2e8f0;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px !important;
        padding: 0.8rem 1rem !important;
        transition: all 0.3s ease;
        border: none;
        color: #64748b;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: #f8fafc !important;
        color: #0f172a !important;
        font-weight: 800 !important;
        box-shadow: inset 0 -3px 0 0 #2563eb;
    }
    
    /* Estilo del Expander Académico */
    .st-emotion-cache-18ni7ap { border: 1px solid #e2e8f0; border-radius: 12px; background-color: white; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-banner">
    <div class="hero-title">⚙️ Optimizando con Dignidad</div>
    <div class="hero-subtitle">La Revolución Ética de la Ingeniería Industrial en la Era de las Capacidades</div>
    <span style="background: rgba(255,255,255,0.2); padding: 8px 16px; border-radius: 20px; font-size: 0.9rem; font-weight: 600; backdrop-filter: blur(5px);">
        Para: Alta Dirección de Operaciones y Estudiantes de Ingeniería
    </span>
</div>
""", unsafe_allow_html=True)

with st.expander("🎓 Información Académica - Proyecto Final (Clic para expandir)", expanded=False):
    st.markdown("""
    <div style="padding: 10px; border-radius: 8px; background-color: #f8fafc;">
    """, unsafe_allow_html=True)
    col_a, col_b, col_c = st.columns([1, 2, 2])
    with col_a:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Uniminuto_logo.svg/1200px-Uniminuto_logo.svg.png", width=140)
    with col_b:
        st.markdown("**Materia:** Ética Profesional")
        st.markdown("**NRC:** 10-84364")
        st.markdown("**Semestre:** 2026-1")
    with col_c:
        st.markdown("**Docente:** LUIS ALEXANDER APONTE ROJAS")
        st.markdown("**Estudiante:** [ESCRIBE TU NOMBRE COMPLETO AQUÍ]") 
        st.markdown("**Institución:** Corporación Universitaria Minuto de Dios")
    st.markdown("</div>", unsafe_allow_html=True)

st.write("") # Espaciador

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "1. Problema Actual", 
    "2. El Bien Interno", 
    "3. Kant y Ergonomía", 
    "4. Índice de Capacidades", 
    "5. Simulador Ético",
    "6. Conclusiones"
])

with tab1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<h2>El algoritmo incompleto de la productividad</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.3, 1], gap="large")
    with col1:
        st.markdown("""
        <div class="text-justify">
        Históricamente, la ingeniería industrial ha sido conceptualizada como la disciplina de la optimización estricta. En el entorno corporativo, el éxito gerencial se mide a través de la maximización del rendimiento, la reducción de mermas y la compresión de costos operativos (OEE, ROI, KPIs de eficiencia).
        <br><br>
        No obstante, cuando el ecosistema organizacional se reduce a un modelo matemático puramente transaccional, la ecuación queda gravemente incompleta. Apoyándonos en los postulados de <strong>Adela Cortina y Emilio Martínez</strong>, sostenemos que ninguna actividad profesional puede desvincularse de su dimensión moral sin perder su legitimidad social.
        <br><br>
        Tratar al capital humano como un mero insumo estadístico conduce a la instrumentalización sistemática. Proponemos a la Alta Dirección un cambio de paradigma: <span class="gradient-text">la optimización centrada en la dignidad humana como base de la sostenibilidad operativa.</span>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.image("https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="La Industria 4.0 exige un liderazgo profundamente ético.", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<h2>Aristóteles en la Planta de Producción</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="text-justify">
    La ética profesional rescata la diferenciación aristotélica fundamental entre <em>bienes internos</em> y <em>bienes externos</em>. La crisis de muchas corporaciones contemporáneas radica en el sacrificio sistémico de su propósito fundacional en aras de acumular métricas financieras a corto plazo.
    </div><br>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.success("### 🛡️ Bienes Internos (El Fin)")
        st.write("**La meta social que legitima a la ingeniería industrial:**")
        st.markdown("""
        * ✅ Crear ecosistemas de trabajo seguros y ergonómicos.
        * ✅ Armonizar la viabilidad técnica con el desarrollo integral del trabajador.
        * ✅ Innovar tecnológicamente para facilitar la existencia humana.
        """)
    with c2:
        st.warning("### 💰 Bienes Externos (Los Medios)")
        st.write("**Lo que se obtiene como consecuencia (pero no justifica el todo):**")
        st.markdown("""
        * ⚠️ Utilidad operativa y márgenes netos de rentabilidad.
        * ⚠️ Posicionamiento de mercado y valor de la acción.
        * ⚠️ Estatus corporativo y bonos de la gerencia.
        """)

    st.markdown("""
    <div class="custom-quote">
    "Corromper la profesión ocurre cuando un Director de Operaciones vulnera la salud física de sus colaboradores para cumplir la meta trimestral del OEE. La excelencia profesional consiste en diseñar procesos donde la eficiencia sea el vehículo para el bienestar colectivo."
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<h2>Más allá de Taylor: El Trabajador como Fin en Sí Mismo</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="text-justify mb-4">
    El paradigma de la administración científica del siglo XX (Taylorismo) asumió al operario como una extensión mecánica, sustituible y exenta de capacidad volitiva. La <strong>ética deontológica de Immanuel Kant</strong> deconstruye esta visión mediante el imperativo categórico: <em>"Las cosas tienen precio y son intercambiables; las personas tienen dignidad y valor absoluto"</em>.
    <br><br>
    La ingeniería moderna debe materializar este principio filosófico en tres áreas críticas de diseño operacional:
    </div>
    """, unsafe_allow_html=True)
    
    col_k1, col_k2, col_k3 = st.columns(3)
    with col_k1:
        st.info("#### 🧍 Ergonomía Proactiva")
        st.write("Cese del diseño de estaciones de trabajo que generen enfermedades musculoesqueléticas a mediano plazo. La ética exige mitigar el riesgo desde los planos de ingeniería.")
    with col_k2:
        st.info("#### 🧠 Sistemas Sociotécnicos")
        st.write("Estructuración de líneas de ensamble que prevengan la alienación cognitiva. El diseño debe permitir autonomía y el fomento del desarrollo intelectual (Kaizen).")
    with col_k3:
        st.info("#### 🤖 Automatización Ética")
        st.write("La implementación de IA y robótica no debe enfocarse exclusivamente en la liquidación de nóminas, sino en la eliminación de tareas monótonas, sucias y peligrosas.")
    st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<h2>Del utilitarismo de métricas al 'Enfoque de Capacidades'</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="text-justify mb-4">
    Martha Nussbaum y Amartya Sen exponen las falacias de medir el desarrollo de una nación exclusivamente mediante el PIB. Transpolando esta teoría a la gerencia, medir el éxito de una planta solo con el <strong>OEE</strong> oculta realidades operativas de precarización.
    Proponemos sustituir el modelo rígido por un <strong>Índice de Capacidades Industriales (ICI)</strong>.
    </div>
    """, unsafe_allow_html=True)
    
    # Tabla usando markdown limpio para mejor estilo con nuestro CSS
    st.markdown("""
    | Capacidad Central (M. Nussbaum) | Traducción a la Dirección Industrial Operativa |
    | :--- | :--- |
    | **1. Vida, Salud Corporal e Integridad** | Ambientes con cero exposición a tóxicos; prevención de fatiga crónica; políticas contra acoso. |
    | **2. Sentidos, Imaginación y Pensamiento** | Planes de carrera técnicos; libertad de expresión para proponer rediseños de procesos. |
    | **3. Razón Práctica** | Empoderamiento (Empowerment); que el operario participe en la organización de su propia labor. |
    | **4. Afiliación y Entorno** | Respeto absoluto al derecho de asociación; fomento de redes de apoyo interdepartamental. |
    """, unsafe_allow_html=True)
    
    st.caption("Nota Estratégica: La aplicación de este marco genera altos niveles de retención de talento y disminuye drásticamente el ausentismo, haciendo de la ética una ventaja competitiva rentable.")
    st.markdown('</div>', unsafe_allow_html=True)

with tab5:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<h2>🎮 Simulador de Toma de Decisiones Estratégicas</h2>", unsafe_allow_html=True)
    st.markdown("Evalúe su criterio gerencial frente a un escenario operativo real. Seleccione su curso de acción para obtener retroalimentación fundamentada.")
    
    st.error("**El Caso: 'Vibraciones en la Línea de Ensamblaje B'**", icon="🚨")
    st.markdown("""
    **Contexto:** Usted asume como Director de Operaciones. Descubre que la maquinaria de la Línea B genera una frecuencia de vibración *justo en el límite legal*. Sin embargo, un estudio privado de ingeniería biomédica indica que, a largo plazo, causará micro-lesiones nerviosas irreversibles en sus operarios. 
    Cambiar los motores solucionaría el problema, pero reduciría la rentabilidad del trimestre en un 12%, anulando los bonos de cumplimiento de la junta y el suyo propio.
    """)
    
    opcion = st.radio(
        "**Como líder corporativo, ¿qué determinación toma?**",
        ["Seleccione una estrategia para ver el análisis ético...",
         "A) Estrategia Utilitarista: Mantener la maquinaria. Es legalmente defendible y mi deber principal es asegurar el dividendo financiero.", 
         "B) Estrategia de Evasión: Ocultar el estudio biomédico y aumentar la velocidad de rotación del personal para que los síntomas tarden en manifestarse.", 
         "C) Estrategia Ética-Discursiva (Habermas): Convocar a los representantes, exponer el hallazgo transparentemente y detener la línea para invertir en nuevos motores."]
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if opcion.startswith("A)"):
        st.warning("❌ **Alerta Ética:** Su decisión es legal, pero inmoral. Está instrumentalizando al capital humano como medio para un fin financiero (violación deontológica de Kant) y priorizando un 'bien externo' sobre el propósito genuino de la profesión.")
    elif opcion.startswith("B)"):
        st.error("❌ **Falla Ética Crítica:** Ha incurrido en dolo por omisión. Viola la ética del discurso al negar información vital a los afectados y destruye activamente la 'Salud Corporal' (capacidad central de Nussbaum).")
    elif opcion.startswith("C)"):
        st.success("✅ **Liderazgo Excepcional:** Resolución congruente con la ética profesional. Actúa como facilitador a través de la Ética del Discurso, protegiendo la dignidad humana y asegurando la sostenibilidad reputacional a largo plazo.")
        st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

with tab6:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<h2>Conclusión Estratégica</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #f0fdf4; border-left: 5px solid #22c55e; padding: 20px; border-radius: 8px; margin-bottom: 30px;">
    <strong style="font-size: 1.2rem; color: #166534;">Optimizamos procesos operativos para que la vida prospere, no para depreciar la dignidad.</strong><br><br>
    <span style="color: #15803d; line-height: 1.6;">La convergencia entre la ética profesional y la ingeniería industrial no representa una limitante para la competitividad, sino el estándar evolutivo de la Industria 4.0. Las organizaciones que ignoran el componente humano y filosófico en el diseño de sus operaciones enfrentan riesgos catastróficos de rotación, demandas y colapso reputacional. El verdadero desafío es equilibrar la exactitud matemática con la responsabilidad de cuidar la red humana.</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    st.markdown("### 📚 Referencias Bibliográficas (Normas APA 7.ª Edición)")
    st.markdown("""
    <div style="padding-left: 20px; text-indent: -20px; line-height: 1.8; color: #475569;">
    Correa Casanova, M., & Martínez Becerra, P. (Eds.). (2010). <em>La riqueza ética de las profesiones</em>. RIL Editores.<br>
    Cortina, A., & Martínez Navarro, E. (2001). <em>Ética</em>. Ediciones Akal.<br>
    Kant, I. (2012). <em>Fundamentación para una metafísica de las costumbres</em> (R. R. Aramayo, Trad.). Alianza Editorial. (Obra original publicada en 1785).<br>
    Nussbaum, M. C. (2012). <em>Crear capacidades: Propuesta para el desarrollo humano</em>. Paidós.<br>
    Sen, A. (2000). <em>Desarrollo y libertad</em>. Editorial Planeta.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 0.9rem;'>Desarrollado en Python & Streamlit Framework | Interfaz Frontend Avanzada</p>", unsafe_allow_html=True)
