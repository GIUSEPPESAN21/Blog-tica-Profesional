import streamlit as st
import pandas as pd
import time

# Configuración inicial de la página (Debe ser el primer comando)
st.set_page_config(
    page_title="Optimizando con Dignidad | Ética en Ingeniería",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed" # Ocultamos el sidebar por defecto
)

st.markdown("""
    <style>
    /* Ocultar el botón del sidebar y el sidebar completo para forzar navegación superior */
    [data-testid="collapsedControl"] { display: none; }
    [data-testid="stSidebar"] { display: none; }
    
    /* Estilos para tipografía y contenedores */
    .main-title { font-size: 2.8rem; font-weight: 800; color: #0f172a; margin-bottom: 0px; }
    .sub-title { font-size: 1.4rem; font-weight: 400; color: #475569; margin-bottom: 30px; }
    .justified-text { text-align: justify; font-size: 1.15rem; line-height: 1.7; color: #334155; }
    .quote-box { background-color: #f8fafc; border-left: 6px solid #2563eb; padding: 25px; font-style: italic; margin: 20px 0; border-radius: 0 8px 8px 0; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .highlight { color: #2563eb; font-weight: 700; }
    
    /* Personalización de las pestañas (Tabs) de Streamlit para que parezcan un menú de navegación */
    .stTabs [data-baseweb="tab-list"] { gap: 8px; background-color: #f1f5f9; padding: 10px 10px 0 10px; border-radius: 10px 10px 0 0; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: transparent; border-radius: 8px 8px 0 0; gap: 4px; padding-top: 10px; padding-bottom: 10px; font-weight: 600; }
    .stTabs [aria-selected="true"] { background-color: #ffffff; color: #2563eb; border-bottom: 3px solid #2563eb; }
    </style>
""", unsafe_allow_html=True)

# Cabecera principal
st.markdown('<p class="main-title">⚙️ Optimizando con Dignidad</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">La Revolución Ética de la Ingeniería Industrial en la Era de las Capacidades</p>', unsafe_allow_html=True)

# Panel desplegable para la información académica (Limpio y no invasivo)
with st.expander("🎓 Información Académica - Proyecto Final de Ética Profesional", expanded=False):
    col_a, col_b, col_c = st.columns([1, 2, 2])
    with col_a:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Uniminuto_logo.svg/1200px-Uniminuto_logo.svg.png", width=120)
    with col_b:
        st.markdown("**Materia:** Ética Profesional")
        st.markdown("**NRC:** 10-84364")
        st.markdown("**Semestre:** 2026-1")
    with col_c:
        st.markdown("**Docente:** LUIS ALEXANDER APONTE ROJAS")
        st.markdown("**Estudiante(s):** [ESCRIBE TU NOMBRE COMPLETO AQUÍ]") 
        st.markdown("**Institución:** Corporación Universitaria Minuto de Dios")

st.divider()

# Menú de Navegación Principal
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "1. Contexto y Problema", 
    "2. Aristóteles en la Planta", 
    "3. Kant y la Ergonomía", 
    "4. Índices y Capacidades", 
    "5. Simulador Ético",
    "6. Conclusión y APA 7"
])

with tab1:
    st.markdown("### El algoritmo incompleto de la productividad")
    
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("""
        <div class="justified-text">
        Históricamente, la ingeniería industrial ha sido conceptualizada como la disciplina de la optimización estricta. En el entorno académico y corporativo, el éxito gerencial se mide a través de la maximización del rendimiento, la reducción de mermas y la compresión de costos operativos.
        <br><br>
        No obstante, cuando el ecosistema organizacional se reduce a un modelo matemático puramente transaccional, la ecuación queda gravemente incompleta. Apoyándonos en los postulados de <strong>Adela Cortina y Emilio Martínez</strong>, sostenemos que ninguna actividad profesional puede desvincularse de su dimensión moral sin perder su legitimidad social.
        <br><br>
        Tratar al capital humano como un mero insumo estadístico conduce a la instrumentalización sistemática. Este documento interactivo plantea un cambio de paradigma para la Alta Dirección: <span class="highlight">la optimización centrada en la dignidad humana como base de la sostenibilidad operativa.</span>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.image("https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="La Industria 4.0 exige un liderazgo ético.", use_container_width=True)

with tab2:
    st.markdown("### El 'Bien Interno' de la Ingeniería Industrial")
    st.markdown("""
    <div class="justified-text">
    La ética profesional, desde la óptica de Adela Cortina, rescata la diferenciación aristotélica fundamental entre <em>bienes internos</em> y <em>bienes externos</em>. La crisis de muchas corporaciones contemporáneas radica en el sacrificio sistémico de su propósito fundacional en aras de acumular métricas financieras a corto plazo.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.info("#### 🛡️ Bienes Internos (El Fin)")
        st.write("La meta social que legitima a la ingeniería industrial:")
        st.markdown("""
        - Crear ecosistemas de trabajo seguros y ergonómicos.
        - Armonizar la viabilidad técnica con el desarrollo integral del trabajador.
        - Innovar tecnológicamente para facilitar la existencia, no para precarizarla.
        """)
    with c2:
        st.warning("#### 💰 Bienes Externos (Los Medios)")
        st.write("Lo que se obtiene como consecuencia, pero que no justifica el todo:")
        st.markdown("""
        - Utilidad operativa y márgenes netos.
        - Posicionamiento de mercado y valor de la acción.
        - Estatus corporativo de la gerencia.
        """)

    st.markdown("""
    <div class="quote-box">
    "Corromper la profesión ocurre cuando un Director de Operaciones vulnera la salud física de sus colaboradores para cumplir la meta trimestral del OEE. La excelencia profesional (Areté) consiste en diseñar arquitecturas de procesos donde la eficiencia sea un vehículo para el bienestar colectivo."
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("### Más allá de Taylor: El Trabajador como Fin en Sí Mismo")
    st.markdown("""
    <div class="justified-text">
    El paradigma de la administración científica del siglo XX (Taylorismo) asumió al operario como una extensión mecánica, sustituible y exenta de capacidad volitiva. La <strong>ética deontológica de Immanuel Kant</strong> deconstruye esta visión mediante el imperativo categórico: <em>"Las cosas tienen precio y son intercambiables; las personas tienen dignidad y valor absoluto"</em>.
    <br><br>
    La ingeniería moderna debe materializar este principio filosófico en tres áreas críticas de diseño operacional:
    </div><br>
    """, unsafe_allow_html=True)
    
    col_k1, col_k2, col_k3 = st.columns(3)
    with col_k1:
        st.markdown("#### 🧍 Ergonomía Proactiva")
        st.write("Cese del diseño de estaciones de trabajo que generen enfermedades musculoesqueléticas a mediano plazo. La ética exige mitigar el riesgo desde los planos de ingeniería, eliminando la concepción del trabajador como 'material desechable'.")
    with col_k2:
        st.markdown("#### 🧠 Sistemas Sociotécnicos")
        st.write("Estructuración de líneas de ensamble que prevengan la alienación cognitiva. El diseño debe permitir autonomía, rotación inteligente, y el fomento del desarrollo intelectual en la planta (ej. Círculos de Calidad / Kaizen).")
    with col_k3:
        st.markdown("#### 🤖 Automatización Ética")
        st.write("La implementación de Robótica e Inteligencia Artificial no debe enfocarse exclusivamente en la liquidación de nóminas, sino en la eliminación de tareas 'Dull, Dirty, and Dangerous' (monótonas, sucias y peligrosas).")

with tab4:
    st.markdown("### Del utilitarismo de métricas al 'Enfoque de Capacidades'")
    st.markdown("""
    <div class="justified-text">
    Martha Nussbaum y Amartya Sen exponen las falacias de medir el desarrollo de una nación exclusivamente mediante el PIB. Transpolando esta teoría a la gerencia, medir el éxito de una planta solo con el <strong>OEE (Eficiencia General de los Equipos)</strong> oculta realidades operativas de precarización.
    Proponemos un <strong>Índice de Capacidades Industriales (ICI)</strong>, donde la eficiencia esté supeditada a las "capacidades centrales" del ser humano.
    </div><br>
    """, unsafe_allow_html=True)
    
    st.markdown("#### Matriz de Transición Ética-Operativa")
    data = {
        "Capacidad Central (M. Nussbaum)": [
            "1. Vida, Salud Corporal e Integridad", 
            "2. Sentidos, Imaginación y Pensamiento", 
            "3. Razón Práctica", 
            "4. Afiliación y Entorno"
        ],
        "Traducción a la Dirección Industrial": [
            "Ambientes con cero exposición a tóxicos; políticas estrictas contra el acoso laboral.", 
            "Planes de carrera técnicos; libertad de expresión para proponer rediseños de procesos.", 
            "Empoderamiento (Empowerment); que el operario participe en la organización de su labor.",
            "Respeto absoluto al sindicalismo legal; fomento de redes de apoyo interdepartamental."
        ]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, hide_index=True, use_container_width=True)
    
    st.caption("Nota: La aplicación de este marco genera altos niveles de retención de talento y disminuye drásticamente el ausentismo, haciendo de la ética una ventaja competitiva.")

with tab5:
    st.markdown("### 🎮 Simulador de Toma de Decisiones Estratégicas")
    st.markdown("Evalúe su criterio gerencial frente a un escenario operativo real. Seleccione su curso de acción para obtener retroalimentación fundamentada en los marcos teóricos abordados.")
    
    st.error("**El Caso de la 'Línea de Ensamblaje B'**")
    st.markdown("""
    **Contexto:** Usted asume como Director de Operaciones. Descubre que la maquinaria de la Línea B genera una frecuencia de vibración que está *justo en el límite legal de las normas estatales*. Sin embargo, un estudio privado reciente de ingeniería biomédica (que solo usted conoce) indica que, a largo plazo, esta vibración causará micro-lesiones nerviosas irreversibles en sus operarios. 
    Cambiar los motores solucionaría el problema, pero reduciría la rentabilidad del trimestre en un 12%, anulando los bonos de cumplimiento de la junta directiva y el suyo propio.
    """)
    
    opcion = st.radio(
        "**Como líder, ¿qué determinación toma?**",
        ["(Seleccione una estrategia)",
         "A) Estrategia Utilitarista: Mantener la maquinaria igual. Es legalmente defendible y mi deber principal es asegurar el dividendo de los accionistas y los bonos de mi equipo directivo.", 
         "B) Estrategia de Evasión: Ocultar el estudio biomédico y aumentar la velocidad de rotación del personal en la Línea B para que los síntomas tarden más en manifestarse.", 
         "C) Estrategia Ética-Discursiva: Convocar a los representantes de los operarios, exponer el hallazgo transparentemente y detener la línea para invertir en nuevos motores, asumiendo el impacto financiero temporal."]
    )
    
    if opcion.startswith("A)"):
        st.warning("❌ **Alerta Ética:** Su decisión es legal, pero no ética. Está instrumentalizando al capital humano como medio para un fin financiero (violación deontológica) y priorizando un 'bien externo' sobre el propósito genuino de la profesión.")
    elif opcion.startswith("B)"):
        st.error("❌ **Falla Ética Crítica:** Usted ha incurrido en dolo por omisión. Está violando el principio de la ética discursiva (Habermas) al negar información vital a los afectados y destruyendo la capacidad de 'Salud Corporal' (Nussbaum).")
    elif opcion.startswith("C)"):
        st.success("✅ **Liderazgo Excepcional:** Su resolución es congruente con la ética profesional. Actúa como facilitador a través de la Ética del Discurso (Habermas/Cortina), protegiendo la dignidad humana y asegurando la sostenibilidad reputacional y operativa a largo plazo.")
        st.balloons()

with tab6:
    st.markdown("### Conclusión Estratégica")
    st.success("""
    **Optimizamos procesos operativos para que la vida prospere, no para depreciar la dignidad.** 
    
    La convergencia entre la ética profesional y la ingeniería industrial no representa una limitante para la competitividad, sino el estándar evolutivo de la Industria 4.0. Las organizaciones que ignoran el componente humano y filosófico en el diseño de sus operaciones enfrentan riesgos catastróficos de rotación, demandas y colapso reputacional. El verdadero desafío del ingeniero es equilibrar la exactitud matemática con la profunda responsabilidad de cuidar la red humana que sostiene el aparato productivo.
    """)
    
    st.divider()
    st.markdown("### 📚 Referencias Bibliográficas (Normas APA 7.ª Edición)")
    st.markdown("""
    * Correa Casanova, M., & Martínez Becerra, P. (Eds.). (2010). *La riqueza ética de las profesiones*. RIL Editores.
    * Cortina, A., & Martínez Navarro, E. (2001). *Ética*. Ediciones Akal.
    * Kant, I. (2012). *Fundamentación para una metafísica de las costumbres* (R. R. Aramayo, Trad.). Alianza Editorial. (Obra original publicada en 1785).
    * Nussbaum, M. C. (2012). *Crear capacidades: Propuesta para el desarrollo humano*. Paidós.
    * Sen, A. (2000). *Desarrollo y libertad*. Editorial Planeta.
    """)
    
    st.caption("Desarrollado en Python / Streamlit Framework. Proyecto académico para la Corporación Universitaria Minuto de Dios.")
