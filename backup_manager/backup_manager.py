import sys
from utils.create_dir import create_dir
from utils.constants import *
from manager.command import run




def main():
    create_dir(LOGS_DIR)
    run(sys.argv[1:])

if __name__ == "__main__":
    main()

