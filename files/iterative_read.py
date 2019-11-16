import sys
from io import StringIO


def read_file_iteratively(file: StringIO, chunk_bytes: int = 1024):
    with open(file, 'rb') as f:
        def l_func(): return f.read(chunk_bytes)
        for chunk in iter(l_func):
            print(chunk)


if __name__ == "__main__":
    try:
        file = sys.argv[1]
    except IndexError as e:
        print(f"Error: {e}\n ==> Please provide a path to a file as argument.")
        sys.exit(1)
    read_file_iteratively(file)
