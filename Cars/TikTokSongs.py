from pytube import YouTube, Playlist
from concurrent.futures import ThreadPoolExecutor
import os
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f"{stream.title} is {percentage_of_completion}% downloaded.")


def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', '', filename)


def download_audio(youtube_link, output_path):
    try:
        yt = YouTube(youtube_link)
        yt.register_on_progress_callback(progress_callback)
        title = sanitize_filename(yt.title)
        output_filename = f"{title}.mp3"
        output_filepath = os.path.join(output_path, output_filename)
        
        if os.path.exists(output_filepath):
            print(f"File {output_filename} already exists, skipping download.")
            return
        
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(output_path=output_path, filename=output_filename)
        
    except Exception as e:
        print(f"Error while downloading {youtube_link}: {e}")


def main():
    playlist_url = 'https://www.youtube.com/playlist?list=PLHg022HMFzFDMNp9xBGy3sARnqxaPl3PG'
    output_path = 'output_folder/Music'

    playlist = Playlist(playlist_url)

    tasks = [(video_url, output_path) for video_url in playlist.video_urls]

    with ThreadPoolExecutor(max_workers=5) as executor:
        for youtube_link, output_path in tasks:
            executor.submit(download_audio, youtube_link, output_path)


if __name__ == "__main__":
    main()
