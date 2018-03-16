#!/usr/bin/python3
import re
import subprocess
import os
import ask_ok

while True:
    dir_add = input("pleas enter directory address :")
    if os.path.isdir(dir_add):
        break
    else:
        print('no such directory!!Tray again')

process = str(subprocess.check_output(["ls", dir_add]))
dir_list = process[2:-3].split('\\n')
for line in dir_list:
    if re.search('(mp4)$|(mkv)$|(MTS)$', line):

        codec_check_command = ['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
         'stream=codec_name', '-of', 'default=noprint_wrappers=1:nokey=1', dir_add +"/" + line]
        codec_check = subprocess.check_output(codec_check_command)

        if ask_ok.ask_ok('codec is ' + str(codec_check)[2:-3] + ' Do you convert '+line+' ?(y/n)'):

            command = "ffmpeg -i "+dir_add+"/"+line+" -f matroska -c:v libx265 -acodec libvorbis "+dir_add+"/"+line+"_x265.mkv"
            os.system(command)
