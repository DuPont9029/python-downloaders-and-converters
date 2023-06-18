from pytube import YouTube, Playlist
import logging

logging.basicConfig(filename='download.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def scarica_da_youtube(url_playlist, posizione_download, percorso_download):
    playlist = Playlist(url_playlist)
    playlist._video_regex = r"\"url\":\"(/watch\?v=[\w-]*)"
    video_urls = playlist.video_urls

    if len(video_urls) > 0:
        for index, video_url in enumerate(video_urls, start=1):
            if index >= posizione_download:
                yt = YouTube(video_url)
                videos = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
                if videos:
                    video = videos.first()
                    video.download(percorso_download)
                    logging.info(f"Download completed for the video: {yt.title} ({video_url}) - Index: {index}")
                else:
                    logging.warning(f"No video available for the URL: {video_url}")
    else:
        logging.warning("The playlist contains no videos available.")

url_playlist = "PLAYLIST URL"
posizione_download = 518  # video index
percorso_download = "DOWNLOAD PATH"  # download path
scarica_da_youtube(url_playlist, posizione_download, percorso_download)
