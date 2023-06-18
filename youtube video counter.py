from pytube import Playlist

def print_playlist_videos(playlist_url):
    playlist = Playlist(playlist_url)
    playlist._video_regex = r"\"url\":\"(/watch\?v=[\w-]*)"
    video_urls = playlist.video_urls

    if len(video_urls) > 0:
        for index, video_url in enumerate(video_urls, start=1):
            print(f"Video {index}: {video_url}")
    else:
        print("The playlist contains no videos available.")

playlist_url = "YOUR PUBLIC PLAYLIST URL"
print_playlist_videos(playlist_url)
