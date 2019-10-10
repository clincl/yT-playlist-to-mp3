import csv
import youtube_dl
#REQUIRED INFO
#CSV FILE
CSV_FILE = 'youtube_links.csv'
#FILE OUTPUT SETTINGS
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '/songs/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
        }],
}
#Download from csv
def download(ydl_opts):
    with open(CSV_FILE, 'r', encoding = 'utf8') as f:
        r = csv.reader(f)
        for row in r:
            print(row[0])
            print(row[1])
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(['https://www.youtube.com/watch?v=' + row[1]])
        f.close()

#Main
def main():
    download(ydl_opts) #download files
main()