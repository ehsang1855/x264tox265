#!/usr/bin/python
import re
import subprocess
import os
import ask_ok
dir_addr=input("pleas enter directory address :")
process=subprocess.check_output(["ls",dir_addr])
for line in process.splitlines():
    if re.search('(mp4)$|(mkv)$|(MTS)$', str(line)[2:-1]):
        p2 = subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=codec_name', '-of','default=noprint_wrappers=1:nokey=1', dir_addr + "/" + str(line)[2:-1]])
        if ask_ok.ask_ok('codec is ' + str(p2)[2:-3]+ ' Do you convert '+str(line)[2:-1]+' ?(y/n)'):
            os.system("ffmpeg -i "+dir_addr.replace(' ','\ ') + "/" + str(line)[2:-1]+" -c:v libx265 -c:a copy "+dir_addr.replace(' ','\ ') + "/"+str(line)[2:-5]+"_out.mp4")



