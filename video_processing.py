import os
from openai import OpenAI
from moviepy.editor import *
import moviepy.editor as mp

def extract_audio(video):
    # pasa video mp4 a formato wav
    video_clip = mp.VideoFileClip(video)
    audio_clip = video_clip.audio
    audio_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../temp/audio.wav"))
    audio_clip.write_audiofile(audio_path)
    print("Audio extraído con éxito")
    return audio_path

def transcribe_audio(audio_file_path):
    client = OpenAI(api_key="Aqui la API KEY")

    audio_file = open(audio_file_path, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    transcription_text = transcription.text

    # Guarda transcripción en un archivo de texto
    output_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../temp/transcription.txt"))
    with open(output_file_path, "w") as output_file:
        output_file.write(transcription_text)

    return output_file_path

def create_signs(text):
    # TODO: Implementar la generación de gestos de lenguaje de signos a partir del texto    
    # Placeholder para devolver un archivo de video de muestra
    video_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../test_files/test_signs.webm"))
    return video_path

def create_video(original_video_path, signs_video_path):
    # Carga el video original
    ''' Debugging
    original_video = VideoFileClip(original_video_path)

    # Carga el video de lenguaje de signos
    signs_video = VideoFileClip(signs_video_path)

    # Ajusta el tamaño del video de lenguaje de signos
    resized_signs_video = signs_video.resize(height=original_video.h // 4)

    # Posiciona el video de lenguaje de signos en la esquina inferior derecha
    x_pos = original_video.w - resized_signs_video.w - 10
    y_pos = original_video.h - resized_signs_video.h - 10

    # Ajusta la duración del video de salida
    overlay_duration = original_video.duration

    # Superpone el video de lenguaje de signos al video original
    overlay_video = CompositeVideoClip([original_video, resized_signs_video.set_position((x_pos, y_pos))])

    # Output video
    output_video = overlay_video.set_duration(overlay_duration)

    '''

    # Escribe el video de salida
    output_video_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../test_files/output_video.mp4"))
    #output_video.write_videofile(output_video_path, codec='libx264')

    return output_video_path
