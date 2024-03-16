# SignTune

SignTune es una plataforma de comunicación inclusiva que permite traducir el contenido de un video a lenguaje de señas.

## Funciones

### `extract_audio(video)`

Extrae el audio de un archivo de video.

**Parámetros:**

- `video` (str): La ruta al archivo de video.

**Devuelve:**

- La ruta al archivo de audio extraído.

### `transcribe_audio(audio_file_path)`

Transcribe un archivo de audio utilizando la API de OpenAI.

**Parámetros:**

- `audio_file_path` (str): La ruta al archivo de audio.

**Devuelve:**

- La ruta al archivo de texto de transcripción.

### `create_signs(text)`

Crea un video de lenguaje de señas a partir de un texto de entrada. Esta función aún no está implementada.

**Parámetros:**

- `text` (str): El texto para crear un video de lenguaje de señas.

**Devuelve:**

- La ruta al video de lenguaje de señas.

### `create_video(original_video_path, signs_video_path)`

Superpone un video de lenguaje de señas en un video original.

**Parámetros:**

- `original_video_path` (str): La ruta al video original.
- `signs_video_path` (str): La ruta al video de lenguaje de señas.

**Devuelve:**

- La ruta al video de salida.

### `process_video(video)`

Proceso general que va llamando a las demás funciones para procesar el video, extraer el audio, transcribirlo, crear el video de lenguaje de señas y superponerlo en el video original.

**Parámetros:**

- `video` (str): La ruta al archivo de video.

**Devuelve:**

- La ruta al video final.

### `download_video(video)`

Descarga el video a local. Esta función aún no está implementada.

**Parámetros:**

- `video` (str): La ruta al archivo de video.

## Uso

Para usar la plataforma, necesitas iniciar sesión y estar suscrito a algún plan. Una vez que estés autenticado, puedes subir un video en formato MP4. Luego, puedes presionar el botón "Traducir vídeo" para procesar el video. Una vez que el video se haya procesado, puedes ver el video final en la plataforma y descargarlo a tu dispositivo local.