import sys
from io import StringIO


def read_file_in_chunks(file: StringIO, block_size: int = 1024):
    chunk = file.read(block_size)
    while chunk:
        yield chunk
        chunk = file.read(block_size)


if __name__ == "__main__":
    try:
        file = sys.argv[1]
    except IndexError as e:
        print(f"Error: {e}\n ==> Please provide a path to a file as argument.")
        sys.exit(1)
    with open(file) as f:
        for chunk in read_file_in_chunks(f):
            print(chunk)
