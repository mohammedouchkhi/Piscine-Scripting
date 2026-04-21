import os


def create_dir(dir):
    os.makedirs(dir, exist_ok=True)
