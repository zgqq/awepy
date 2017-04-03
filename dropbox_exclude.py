import os
import subprocess

exclude_suffix = set(['build','node_modules','target','cache'])
rootdir = "/home/zgq/Dropbox"

def exclude_dir(folder):
    """exclude dir

    :folder: TODO
    :returns: TODO

    """
    for f in os.listdir(folder):
        dir_path = os.path.join(folder,f)
        if os.path.isdir(dir_path):
            suffix = dir_path[dir_path.rfind('/') + 1:]
            if suffix in exclude_suffix:
                print('excluding ' + dir_path)
                subprocess.run(['dropbox-cli', 'exclude', 'add', dir_path])
            else:
                exclude_dir(dir_path)


exclude_dir(rootdir)
