# pip install pytube
# brew install pytube

from pytube import YouTube
from pytube.cli import on_progress


link= input("Enter youtube video link: ")#"https://www.youtube.com/watch?v=_j1CWOhnotg"
SAVE_PATH = "./"
try: 
    yt = YouTube(link, on_progress_callback=on_progress) 
except: 
    print("Connection Error or invalid link") 
    exit(0)

title = yt.title + ".mp4"
title = title.replace("/", "")
title = title.replace("\\", "")
title = title.replace("|", "")
print(title)
try:
    yt.streams.filter(file_extension = "mp4", progressive = True).first().download(filename = title, output_path = SAVE_PATH) 
    print('\n\nTask Completed!') 
except: 
    print("Some Error Occured!") 
    
