from moviepy.editor import VideoFileClip
from tqdm import tqdm
import os

def convert_to_mp3(mp4_file, mp3_file):
    video = VideoFileClip(mp4_file)
    audio = video.audio
    audio.write_audiofile(mp3_file)
    audio.close()
    video.close()

def convert_folder_to_mp3(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    mp4_files = [f for f in os.listdir(folder_path) if f.endswith(".mp4")]
    total_files = len(mp4_files)

    progress_bar = tqdm(total=total_files, unit='file(s)')

    for file_name in mp4_files:
        mp4_file = os.path.join(folder_path, file_name)
        mp3_file = os.path.join(output_folder, file_name.replace(".mp4", ".mp3"))
        convert_to_mp3(mp4_file, mp3_file)
        progress_bar.update(1)

    progress_bar.close()

folder_path = 'INPUT FOLDER PATH'
output_folder = 'OUTPUT FOLDER PATH'

convert_folder_to_mp3(folder_path, output_folder)
