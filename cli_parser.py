import subprocess


def drive_lookup():
    return subprocess.Popen(['cyanrip', '-f'], stdout=subprocess.PIPE)


def start_ripping(arglist):
    arglist.insert('cyanrip', 0)
    return subprocess.Popen(arglist, stdout=subprocess.PIPE)
