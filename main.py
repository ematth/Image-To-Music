# type "pip install pillow" in terminal for PIL installation
from PIL import Image
import sys
import os

try:
    picture = Image.open(str(sys.argv[1]))
    pic = picture.load()
    width, height = picture.size
except all:
    print('no valid image given')
    quit(1)

factor = 25
try:
    factor = int(sys.argv[2])
except:
    pass


# reference dicts
note_dict = {
    0: 'C', 1: 'C#', 2: 'D', 3: 'Eb',
    4: 'E', 5: 'F', 6: 'F#', 7: 'G',
    8: 'Ab', 9: 'A', 10: 'Bb', 11: 'B'
}

octave_dict = {
    0: 'Major', 1: 'Minor', 2: 'Augmented', 3: 'diminished',
    4: '*Melody*', 5: '*Melody*', 6: '*Melody*', 7: '*Melody*',
    8: '*Melody*', 9: '*Melody*', 10: '*Melody*'
}

length_dict = {
    0: 'sixteenth', 1: 'eighth', 2: 'quarter',
    3: 'half', 4: 'whole'
}

# initialize list/file
note_list = list()
final_list = list()
file = open(str(sys.argv[1]) + '.txt', 'w')

# getting data from pixels
pixel_prev = (0, 0, 0)
pixel = (0, 0, 0)
for x in range(int(width / factor)):
    for y in range(int(height / factor)):
        pixel = pic[int(x * factor), int(y * factor)]
        if pixel[0] is not 0 and pixel[1] is not 0 and pixel[2] is not 0 \
                and pixel_prev[0] is not pixel[0] and pixel_prev[1] is not pixel[1] and pixel_prev[2] is not pixel[2]:
            note_list.append((pixel[0] % 12, pixel[1] % 11, pixel[2] % 4))
            pixel_prev = pixel
for note in note_list:
    final_list.append((note_dict[note[0]], octave_dict[note[1]], length_dict[note[2]]))
for note in final_list:
    file.write(str(note) + '\n')
    print(note)
file.close()

