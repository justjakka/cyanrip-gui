import subprocess


def drive_lookup():
    return subprocess.Popen(['cyanrip', '-f'], stdout=subprocess.PIPE)


def start_ripping(arglist):
    arglist.insert(0, 'cyanrip')
    return subprocess.Popen(arglist, stdout=subprocess.PIPE)
