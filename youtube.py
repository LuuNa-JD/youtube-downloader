import youtube_downloader

urls = input("Entrez les urls des vidéos à télécharger (séparées par des espaces): ").split(" ")



for url in urls:
    youtube_downloader.download_video(url)
