import streamlit as st
import pandas as pd
import time

# Configuración inicial de la página (Debe ser el primer comando de Streamlit)
st.set_page_config(
    page_title="Optimizando con Dignidad | Ética Profesional",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    /* Estilos para textos justificados y citas */
    .justified-text { text-align: justify; font-size: 1.15rem; line-height: 1.7; color: #334155; }
    .quote-box { background-color: #f8fafc; border-left: 6px solid #0284c7; padding: 20px; font-style: italic; margin-bottom: 25px; border-radius: 0 8px 8px 0; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    .highlight { color: #0284c7; font-weight: 700; }
    
    /* Estilo para disimular los radio buttons y que parezcan un menú */
    div.row-widget.stRadio > div { background-color: #f1f5f9; padding: 15px; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    # Logo de UNIMINUTO (Cargado desde una URL pública)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Uniminuto_logo.svg/1200px-Uniminuto_logo.svg.png", width=160)
    
    st.markdown("### 📚 Información Académica")
    st.markdown("**Materia:** Ética Profesional")
    st.markdown("**NRC:** 10-84364")
    st.markdown("**Docente:** LUIS ALEXANDER APONTE ROJAS")
    st.markdown("**Estudiante(s):** [ESCRIBE TU NOMBRE COMPLETO AQUÍ]") 
    
    st.divider()
    
    st.markdown("### 🧭 Navegación del Blog")
    # Este menú interactivo controla qué parte del código se ejecuta y se muestra
    seccion = st.radio(
        "Selecciona un capítulo:",
        ("1. Inicio y Contexto", 
         "2. El 'Bien Interno'", 
         "3. Más allá de Taylor (Kant)", 
         "4. Enfoque de Capacidades", 
         "5. Ética Discursiva",
         "6. 🎮 Dilema Interactivo",
         "7. Conclusión y Referencias")
    )
    
    st.divider()
    st.caption("© 2026 - Proyecto Final de Ética Profesional. Desplegado en Python/Streamlit.")

if seccion == "1. Inicio y Contexto":
    st.title("⚙️ Optimizando con Dignidad")
    st.subheader("La Revolución Ética de la Ingeniería Industrial en la Era de las Capacidades")
    st.info("**Audiencia Objetivo:** Alta Dirección de Operaciones y Estudiantes Universitarios de Ingeniería.")
    
    st.divider()
    
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown("### Introducción: El algoritmo incompleto de la productividad")
        st.markdown("""
        <div class="justified-text">
        Durante décadas, la ingeniería industrial ha sido definida como la ciencia de la optimización. Tradicionalmente, se nos enseña a medir el éxito mediante indicadores estrictos de rendimiento y reducción de costos. Sin embargo, cuando reducimos la organización a una mera máquina de maximizar beneficios, el sistema queda incompleto.
        <br><br>
        Como señalan <strong>Adela Cortina y Emilio Martínez</strong>, la actividad profesional no puede desvincularse de su dimensión moral sin perder su legitimidad social. Si tratamos a las personas como meros insumos, caemos en la instrumentalización. En este espacio interactivo exploraremos un nuevo paradigma: <span class="highlight">la optimización centrada en la dignidad humana</span>.
        </div>
        """, unsafe_allow_html=True)
    with col2:
        # Imagen representativa (Stock libre de uso)
        st.image("https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="La Industria 4.0 exige una Ética Profesional 4.0")

elif seccion == "2. El 'Bien Interno'":
    st.title("1. El 'Bien Interno' de la Ingeniería Industrial")
    st.markdown("""
    <div class="justified-text">
    Para comprender la ética de nuestra profesión, debemos recuperar la distinción aristotélica explicada por Adela Cortina entre <em>bienes internos</em> y <em>bienes externos</em>. 
    El error de muchas empresas contemporáneas es sacrificar el sentido de su profesión por acumular métricas financieras.
    </div><br>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.success("### 🛡️ Bienes Internos")
        st.write("**La meta social que da sentido y legitimidad a la profesión.**")
        st.write("✅ Crear sistemas de trabajo seguros y ergonómicos.")
        st.write("✅ Armonizar la viabilidad técnica con el bienestar social.")
        st.write("✅ Innovar para facilitar la vida humana, no para precarizarla.")
    with c2:
        st.warning("### 💰 Bienes Externos")
        st.write("**Lo que se obtiene como añadidura (medios, no fines).**")
        st.write("⚠️ Dinero y utilidad neta de la planta.")
        st.write("⚠️ Estatus, poder en el mercado y prestigio empresarial.")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="quote-box">
    "Cuando un director de operaciones sacrifica la salud física de sus operarios para aumentar un margen de ganancia a corto plazo, está corrompiendo la profesión. La verdadera excelencia radica en diseñar procesos donde la eficiencia sea el vehículo para la dignificación."
    </div>
    """, unsafe_allow_html=True)

elif seccion == "3. Más allá de Taylor (Kant)":
    st.title("2. Más allá de Taylor: El Trabajador como Fin en Sí Mismo")
    st.markdown("""
    <div class="justified-text">
    El taylorismo clásico y la administración científica del siglo XX trataron de convertir al obrero en una simple extensión mecánica de la máquina. La <strong>ética deontológica de Immanuel Kant</strong> dinamita esta perspectiva al recordarnos que <em>"las cosas tienen precio, pero las personas tienen dignidad"</em>.
    <br><br>
    En la ingeniería industrial moderna, este imperativo categórico nos exige evolucionar en tres frentes fundamentales:
    </div><br>
    """, unsafe_allow_html=True)
    
    # Uso de Tabs interactivos de Streamlit para organizar información profesional
    tab1, tab2, tab3 = st.tabs(["🧍 Ergonomía Proactiva", "🧠 Sistemas Sociotécnicos", "🤖 Automatización Ética"])
    with tab1:
        st.subheader("Ergonomía Proactiva")
        st.write("Consiste en no diseñar puestos de trabajo que destruyan la salud física del operario a mediano o largo plazo. La visión antiética asume que el trabajador es 'desechable' y que simplemente 'se puede contratar a otro'. Un ingeniero ético previene el daño desde la concepción del plano.")
    with tab2:
        st.subheader("Sistemas Sociotécnicos")
        st.write("Es el diseño de líneas de montaje que permitan al trabajador mantener un control cognitivo sobre su tarea. Evita la alienación extrema, la hiper-especialización monótona y promueve el aprendizaje y el desarrollo integral humano dentro de la fábrica.")
    with tab3:
        st.subheader("Automatización Ética")
        st.write("La Inteligencia Artificial y la robótica no deben verse únicamente como vías rápidas para el despido masivo o la reducción de nómina, sino como herramientas para liberar al ser humano de tareas peligrosas, sucias y monótonas (Las 3 D's de la robótica: *Dull, Dirty, Dangerous*).")

elif seccion == "4. Enfoque de Capacidades":
    st.title("3. Del indicador OEE a las 'Capacidades'")
    st.markdown("En su obra *Crear capacidades*, **Martha Nussbaum** critica a los economistas que miden el progreso de una nación solo a través del PIB. Nosotros proponemos llevar esa crítica a la industria y sustituir métricas puramente utilitarias por el **Índice de Capacidades Industriales (ICI)**.")
    
    # Uso de Métricas interactivas visuales
    col_metric1, col_metric2, col_metric3 = st.columns(3)
    col_metric1.metric("Enfoque Tradicional", "Max. Rentabilidad", "- Salud Humana")
    col_metric2.metric("Nuevo Paradigma Ético", "Desarrollo Humano", "+ Sostenibilidad a Largo Plazo")
    col_metric3.metric("Indicador Propuesto", "Índice de Capacidades (ICI)", "10 Variables de Nussbaum")

    st.markdown("### Tabla de Aplicación de las Capacidades Centrales en la Industria")
    data = {
        "Capacidad de Nussbaum": [
            "1. Vida y Salud Corporal", 
            "2. Sentidos, Imaginación y Pensamiento", 
            "3. Razón Práctica", 
            "4. Afiliación"
        ],
        "Aplicación Directa en Dirección Industrial": [
            "Espacios libres de riesgos químicos/mecánicos; ergonomía preventiva integral.", 
            "Capacitación continua; fomento de la filosofía Kaizen (que el obrero proponga mejoras).", 
            "Autonomía y empoderamiento en la toma de decisiones del puesto (Empowerment).",
            "Fomento del trabajo en equipo, diálogo sindical libre y cero tolerancia al acoso."
        ]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, hide_index=True, use_container_width=True)

elif seccion == "5. Ética Discursiva":
    st.title("4. Ética Discursiva en Decisiones Estratégicas")
    st.markdown("""
    <div class="justified-text">
    ¿Qué ocurre cuando una empresa se enfrenta a una gran reestructuración tecnológica? 
    Ante recortes, traslados o despidos por automatización, la <strong>Ética del Discurso de Jürgen Habermas</strong> establece que una decisión solo es válida si cuenta con el consenso de los afectados, tras un diálogo celebrado en condiciones de simetría (sin coacción corporativa).
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 **El Rol Estratégico del Ingeniero:** El ingeniero ético no impone normas o rediseños desde su escritorio; actúa como un facilitador. Crea mesas de diálogo con operarios, sindicatos y comunidades, logrando equilibrar la *ética de la convicción* (nuestro deseo de ser eficientes) con la *ética de la responsabilidad* (asumir el impacto social de nuestras decisiones).")

elif seccion == "6. 🎮 Dilema Interactivo":
    st.title("Simulador: Resolución de un Dilema Ético")
    st.write("Pon a prueba tu criterio ético frente a una situación real de ingeniería y dirección de operaciones. Elije tu respuesta para ver la retroalimentación del sistema.")
    
    st.markdown("### El Caso de la 'Línea de Ensamblaje B'")
    st.warning("**Contexto:** Eres el Director de Operaciones. Acabas de descubrir que la maquinaria de la Línea B genera un nivel de vibración que, aunque está *justo en el límite legal permitido*, sabes por estudios recientes que está causando estrés crónico y micro-lesiones en tus operarios a largo plazo. Cambiar los motores protegería a tu equipo, pero reduciría la rentabilidad del trimestre en un 12%, afectando los bonos de fin de año de toda la gerencia (incluido el tuyo).")
    
    # Widget interactivo de decisión
    opcion = st.radio(
        "¿Qué decisión tomas basándote en la Ética Profesional?",
        ["(Selecciona una opción para continuar)",
         "A) Mantener la maquinaria igual. Es 100% legal y mi deber principal como gerente es maximizar la rentabilidad de la empresa a corto plazo.", 
         "B) Ocultar los estudios recientes y rotar al personal rápidamente de estación para que no se note el desgaste físico, evadiendo responsabilidades.", 
         "C) Detener/modificar la línea e invertir en los motores. La salud humana tiene dignidad, no precio. Se reajustarán las metas de rentabilidad."]
    )
    
    if opcion.startswith("A)"):
        st.error("❌ **Incoherente con la Ética Profesional.** Estás utilizando a las personas como un mero medio para un fin económico (violación del imperativo categórico de Kant) y estás priorizando un bien externo (dinero/bono) sobre el bien interno de tu profesión.")
    elif opcion.startswith("B)"):
        st.error("❌ **Falta Ética Grave.** Además de instrumentalizar al trabajador, estás incurriendo en dolo y violando la transparencia y la ética discursiva al negarles información vital sobre su propia salud.")
    elif opcion.startswith("C)"):
        st.success("✅ **¡Decisión Ética Correcta!** Actúas protegiendo el 'Bien Interno' de la profesión y fomentas la capacidad de 'Salud Corporal' (Martha Nussbaum). Como profesional, asumes tu responsabilidad social, incluso por encima de beneficios personales a corto plazo.")
        st.balloons() # Animación visual de celebración

elif seccion == "7. Conclusión y Referencias":
    st.title("Conclusión General")
    st.success("""
    **Optimizamos procesos para que la vida florezca, no para que la dignidad se deprecie.** 
    
    Integrar la ética profesional en el entorno industrial moderno no es un acto de caridad corporativa, es la única estrategia viable para la sostenibilidad, la innovación genuina y la obtención de la *licencia social* para operar. Para nosotros como estudiantes y futuros líderes, el reto es diseñar sistemas donde la tecnología y la eficiencia potencien la libertad humana en lugar de coartarla.
    """)
    
    st.divider()
    st.subheader("📚 Referencias Bibliográficas (Normas APA 7)")
    st.markdown("""
    * Cortina, A., & Martínez Navarro, E. (2001). *Ética*. Ediciones Akal.
    * Correa Casanova, M., & Martínez Becerra, P. (Eds.). (2010). *La riqueza ética de las profesiones*. RIL Editores.
    * Nussbaum, M. C. (2012). *Crear capacidades: Propuesta para el desarrollo humano*. Paidós.
    * Sen, A. (2000). *Desarrollo y libertad*. Editorial Planeta.
    * Kant, I. (2012). *Fundamentación para una metafísica de las costumbres* (R. R. Aramayo, Trad.). Alianza Editorial. (Obra original publicada en 1785).
    """)
