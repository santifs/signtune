import streamlit as st
from st_paywall import add_auth
from streamlit_option_menu import option_menu
from src.video_processing import extract_audio, transcribe_audio, create_signs, create_video
from email.mime.multipart import MIMEMultipart
from email.mime.text import *
import smtplib
import time

# define functions to process the uploaded video, extract the audio and transcribe it
def process_video(video):
    # proceso general que va llamando a las demas funciones
    print("Procesando video...")
    audio = extract_audio(video)
    st.success("Audio extraído con éxito")
    text = transcribe_audio(audio)
    st.success("Audio transcrito con éxito")
    signs = create_signs(text)
    st.success("Texto traducido con éxito")
    complete_video = create_video(video, signs)
    st.success("Vídeo creado con éxito")
    return complete_video

def download_video(video):
    # descarga video a local
    print("Descargando video...")
    pass

# FRONT
st.set_page_config(page_title="SignTune", page_icon="📚", layout="wide", initial_sidebar_state="expanded")
st.image("assets/logo.png",width=750)
st.markdown("<h2 style='text-align: center;font-family: Verdana;  color: black;'>Comunicación sin barreras</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;font-family: Verdana;  color: black;'>Bienvenido a la plataforma de comunicación inclusiva</h3>", unsafe_allow_html=True)

st.subheader("")

# NAVIGATION MENU
selected = option_menu(
    menu_title=None,
    options=["Inicio", "Traductor", "Sobre nosotros","Ayuda"],
    icons=["🏠", "🌐", "📚", "❓"],
    orientation="horizontal",
)

izq , med , der = st.columns(3)

if selected == "Inicio":
    st.write("Somos una plataforma que busca facilitar la comunicación entre personas con discapacidad auditiva y personas que no la tienen. Para ello, ofrecemos un traductor de signos que permite convertir el lenguaje de signos en texto y viceversa. Además, ofrecemos la posibilidad de traducir vídeos de lenguaje de signos a lenguaje hablado y viceversa.")    
    st.write("Nuestro principal foco esta enfocado hacia personas sordas que quieran nutrirse de conocimientos y experiencias de otras personas, sin importar su condición auditiva.")

creditos = 10
num_telefor ="+34"+"678123456"
nombre = "Juan"

logged_in = False
with st.sidebar:
    while (add_auth()==False):
        st.image("assets/chrome-logo.png")
        st.write("###")
        st.warning("Para poder usar la plataforma, necesitas iniciar sesión y estar suscrito a algún plan")
        add_auth(required=True)
        logged_in = True
        
        st.image("assets/chrome-logo.png")
        st.write("###")
        st.warning("Para poder usar la plataforma, necesitas iniciar sesión y estar suscrito a algún plan")
        add_auth(required=True)
        logged_in = True
        
    st.success("¡Bienvenido!")
    st.markdown("<p1 style= 'margin-left: 65px; font-family: Verdana;'>Mi Cuenta</p1>", unsafe_allow_html=True)
    st.image("assets/rafa.jpeg")
    st.markdown("<p1 style= ' text-align: center;'>Nombre: <br>{}</br></p1>".format(nombre), unsafe_allow_html=True)
    st.markdown("<p1 style= '  text-align: center;'>Num de telefono: {}</p1>".format(num_telefor), unsafe_allow_html=True)

    st.markdown("<p1 style= '  text-align: center;'>Creditos restantes: {}</p1>".format(creditos), unsafe_allow_html=True)

if selected == "Traductor":
    st.header("Traductor de signos")
    uploaded_video = st.file_uploader("Sube un vídeo...", type="mp4")

    if uploaded_video is not None:
        st.video(uploaded_video)
        translate_video = st.button(label="Traducir vídeo")

        if translate_video:
            video_path = "temp/uploaded_video.mp4"
            with open(video_path, "wb") as f:
                f.write(uploaded_video.read())
            translated_video = process_video(video_path)
            st.video(translated_video)

            st.download_button("Descargar vídeo", data=translated_video, file_name="translated_video.mp4")

if selected == "Sobre nosotros":
    st.markdown("<h1 style='text-align: center; color: black;font-family: Verdana;'>Sobre nosotros</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;font-family: Verdana;'>¿Quién está detrás de SignTune? </h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: black; font-size:25px;'>Estos son las personas que han hecho posible este proyecto: </h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: black; font-size:25px;'> </h3>", unsafe_allow_html=True) # Header vacio para dar espacio

    left_co, left_co2,cent_co,cent_co2,last_co,last_co2 = st.columns(6)
    izq , med , der = st.columns(3)
    with left_co2:
        st.image("assets/santi.jpeg")
        st.markdown("<h3 style='text-align: center;  color: black;'>Santiago</h3>", unsafe_allow_html=True)

        st.image("assets/dina.jpeg")
        st.markdown("<h3 style='text-align: center;  color: black;'>Dina</h3>", unsafe_allow_html=True)

        st.image("assets/antonio.jpeg")
        st.markdown("<h3 style='text-align: center; color: black;'>Antonio</h3>", unsafe_allow_html=True)
        
    with last_co:
        st.image("assets/maria.jpeg")
        st.markdown("<h3 style='text-align: center; ; color: black;'>María</h3>", unsafe_allow_html=True)

        st.image("assets/rafa.jpeg")
        st.markdown("<h3 style='text-align: center; color: black;'>Rafael</h3>", unsafe_allow_html=True)

        st.image("assets/javi.jpeg")
        st.markdown("<h3 style='text-align: center; color: black;'>Javier</h3>", unsafe_allow_html=True)

    with med:
        st.markdown("<h1 style='text-align: center; color: black; font-size:25px;'> </h1>", unsafe_allow_html=True) # Header vacio para dar espacio
        st.image("assets/equipo.jpg" ,width=400)

def formulario():
    if submit:
        st.success("Formulario enviado con éxito!\nRevisaremos el problema y lo corregiremos lo antes posible")

        # Crear el mensaje
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = 'rdelarosaregana@gmail.com'
        msg['Subject'] = incidencia_seleccionada
        msg.attach(MIMEText(message, 'plain'))

        # Enviar el mensaje
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        server.login(email, 'qfvq mcql vuad wuxk')
        text = msg.as_string()
        server.sendmail(email, 'rdelarosaregana@gmail.com', text)
        server.quit()
        
if selected == "Ayuda":
    st.markdown("<h1 style='text-align: center;  color: black;'>Formulario de contacto</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;  color: black;'>Para cualquier duda o problema rellene el siguiente formulario</h3>", unsafe_allow_html=True)

    with st.form(key='my_form'):
        name = st.text_input("Nombre")
        email = st.text_input("Email")
        incidencias = ['Problema con el traductor', 'Problema con la suscripción','Problema con los créditos' ,'Otro']
        incidencia_seleccionada = st.selectbox("Incidencia", incidencias)
        message = st.text_area("Detalles")
        submit = st.form_submit_button("Enviar")
        formulario()