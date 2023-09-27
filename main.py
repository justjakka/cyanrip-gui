import subprocess
from cli_parser import drive_lookup, start_ripping


if __name__ == "__main__":
    pipe = drive_lookup()
    print(pipe.communicate()[0].decode("utf-8"))