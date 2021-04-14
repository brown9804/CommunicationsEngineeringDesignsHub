## AUDIO SPLIT IN PIECES BY SIZE 
## 24 MB MAIL LIMIT 

# bit rate: 270427 bits per second
# ranges
# 1. 128 -- 16 bytes --- of data
# 2. 192 kbps MP3, then, contains 192 kilobits -- 24 bytes -- of data
# 3. 320 kbps --- 32 bytes -- of data
#Get piece size by following method 
#There are more than one of course
#for  duration_in_sec (X) -->  mp3_file_size (Y)
#So   whats duration in sec  (K) --> for file size of 10Mb
#  K = X * 24Mb / Y
import os
import sys

from pydub import AudioSegment
from pydub.utils import make_pieces
import math

mp3_audio = AudioSegment.from_file("Class_3.mp3", "mp3")
#Count channels
channel_count = mp3_audio.channels
#Get audio thats os goint to split width
sample_width = mp3_audio.sample_width
#Length of audio in sec
duration_in_sec = len(mp3_audio) / 1000
sample_rate = mp3_audio.frame_rate

bit_rate =24
mp3_file_size = (sample_rate * bit_rate * channel_count * duration_in_sec) / 8

# 24Mb OR 24, 000, 000 bytes
file_split_size = 24000000
total_pieces =  mp3_file_size

# TO SECONDS 
piece_length_in_sec = math.ceil((duration_in_sec * 24000000 ) /mp3_file_size)
piece_length_ms = piece_length_in_sec * 1000
pieces = make_pieces(mp3_audio, piece_length_ms)

print ("mp3_file_size = ", mp3_file_size)
print ("Sample Width : "), sample_width
print ("Channel Count : "), channel_count
print ("Duration in seconds: "), duration_in_sec
print ("Frame Rate: "), sample_rate

# Export all of the individual pieces as mp3 files
for i, piece in enumerate(pieces):
    piece_name = "Class_3_PART-".format(i)
    print("------- / -------")
    print ("Exporting ..."), piece_name
    piece.export(piece_name, format: "mp3")
