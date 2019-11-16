import sys


def rows(f, chunksize=1024, sep='|'):
    """
    Read a file where the row separator is '|' lazily.
    """
    incomplete_row = None
    while True:
        chunk = f.read(chunksize)
        if not chunk:  # End of file
            if incomplete_row is not None:
                yield incomplete_row
                break
        # Split the chunk as long as possible
        while True:
            i = chunk.find(sep)
            if i == -1:
                break
            # If there is an incomplete row waiting to be yielded,
            # prepend it and set it back to None
            if incomplete_row is not None:
                yield incomplete_row + chunk[:i]
                incomplete_row = None
            else:
                yield chunk[:i]
            chunk = chunk[i+1:]
        # If the chunk contained no separator, it needs to be appended to
        # the current incomplete row.
        if incomplete_row is not None:
            incomplete_row += chunk
        else:
            incomplete_row = chunk


def main(file):
    with open(file) as f:
        for row in rows(f):
            print(row)


if __name__ == "__main__":
    try:
        file = sys.argv[1]
    except IndexError as e:
        print(f"Error: {e}\n ==> Please provide a path to a file as argument.")
        sys.exit(1)
    main(file)
