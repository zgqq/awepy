import os
import subprocess

rootdir = "/home/zgq/Dropbox"

for folder, subs, files in os.walk(rootdir):
    print ('root ' + folder)
    for subdir in subs:
        dir_path = os.path.join(folder, subdir)
        print('sub ' + dir_path)
