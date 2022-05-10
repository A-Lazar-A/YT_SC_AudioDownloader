import click
from art import text2art
from pytube import YouTube

@click.command()
@click.argument('url')
@click.option('--path', default='', help='Path to the download folder')
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
    else:
        print('Invalid URL')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    downloader()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
