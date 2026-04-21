from service.event_loop import run
from utils.create_dir import create_dir
from utils.constants import *

def main():
    create_dir(BACKUPS_DIR)
    run()

if __name__ == "__main__":
    main()