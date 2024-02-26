from pytube import YouTube
import ffmpeg
import os


def on_progress(stream, chunk, bytes_remaining):
    print("progression du telechargement: ", round((1-bytes_remaining/stream.filesize)*100, 3), "%")

def download_video(url):
    yt = YouTube(url)
    yt.register_on_progress_callback(on_progress)


    print("Titre de la video ;", yt.title)
    print("Nombre de vue :", yt.views)

    print("")

    streams = yt.streams.filter(progressive=False, file_extension='mp4', type="video").order_by("resolution").desc()
    video_stream = streams[0]

    streams = yt.streams.filter(progressive=False, file_extension='mp4', type="audio").order_by("abr").desc()
    audio_stream = streams[0]

    # télécharger la vidéo
    print(f"Téléchargement ¸{yt.title}...")
    video_stream.download("video")
    audio_stream.download("audio")
    print("Télécharment terminé !!")

    audio_filename = os.path.join("audio", video_stream.default_filename)
    video_filename = os.path.join("video", video_stream.default_filename)
    output_filename = video_stream.default_filename

    print("Combinaison de l'audio et de la vidéo...")
    ffmpeg.output(ffmpeg.input(audio_filename), ffmpeg.input(video_filename), output_filename, vcodec="copy", acodec="copy", loglevel="quiet").run(overwrite_output=True)
    print("Combinaison terminée !!")

    os.remove(audio_filename)
    os.remove(video_filename)
    os.rmdir("audio")
    os.rmdir("video")
    print("Fichiers temporaires supprimés !!")

    print("Téléchargement terminé !!")
    print("Fichier sauvegardé sous le nom: ", output_filename)
    print("")
    print("")
    print("")
