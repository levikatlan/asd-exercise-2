import pathlib


def file_sizes():
    """Returns all the files mapped to their sizes in the current directory"""

    return {path.name: path.stat().st_size for path in filter(pathlib.Path, pathlib.Path('.').iterdir())}


if __name__ == '__main__':
    print(file_sizes())
