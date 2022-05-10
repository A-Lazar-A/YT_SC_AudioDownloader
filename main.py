import os
import click
from art import text2art
from pytube import YouTube
import subprocess
import json
import requests


@click.command()
@click.argument('url')
@click.option('--path', default='.', help='Path to the download folder')
def downloader(url, path):
    print(text2art('YT SC Downloader'))
    if 'youtube.com' in url:
        try:
            file = YouTube(url)
            streams = file.streams
            audio_best = streams.get_audio_only()
            audio_best.download(output_path=path)

        except Exception as e:
            print(e)
    elif 'soundcloud.com' in url:
        try:
            subprocess.call(['youtube-dl', '--write-info-json', '-o', f'tmp/%(title)s.%(ext)s', '--skip-download', url])
            json_file = [pos_json for pos_json in os.listdir('tmp') if pos_json.endswith('.json')]

            with open(f'tmp/{json_file[0]}', 'r') as fl:
                data = json.load(fl)
            download_url = data['url']
            full_title = data['fulltitle']
            os.remove(f'tmp/{json_file[0]}')

            with open(f'{path}/{full_title}.mp3', 'wb') as fl:
                fl.write(requests.get(download_url, stream=True).content)

        except Exception as e:
            print(e)
    else:
        print('Invalid URL')


if __name__ == '__main__':
    downloader()
