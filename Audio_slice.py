# pip install pydub
# Also make sure ffmpeg is installed
# For ubuntu use "sudo apt install ffmpeg"
# For windows go to "https://www.ffmpeg.org/download.html" link download ffmpeg and update your environment path with ffmpeg/bin

from pydub import AudioSegment
from pydub.utils import make_chunks

audio_file_name = "Make some noise! DJI FPV Drone vs Mavic Air 2, 2 ProZoom & Mini - Noise & speed comparison"

newAudio = AudioSegment.from_file(audio_file_name + ".mp4", "mp4")

chunk_length_ms = 10 * 1000 # pydub calculates in millisec (10 sec)

chunks = make_chunks(newAudio, chunk_length_ms)

for i, chunk in enumerate(chunks):
    chunk_name = "{0}{1}.wav".format(audio_file_name, i)
    print("exporting", chunk_name)
    chunk.export(chunk_name, format="wav")


