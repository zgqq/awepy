import os
import subprocess

exclude_suffix = set(['build','node_modules','target'])
rootdir = "/home/zgq/Dropbox"

for folder, subs, files in os.walk(rootdir):
    for subdir in subs:
        if subdir in exclude_suffix:
            dir_path = os.path.join(folder, subdir)
            print('Excluding ' + dir_path)
            subprocess.run(['dropbox-cli', 'exclude', 'add', dir_path])
