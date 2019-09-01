import os


def get_random_seed():
    random_bytes = os.urandom(32)
    return random_bytes


