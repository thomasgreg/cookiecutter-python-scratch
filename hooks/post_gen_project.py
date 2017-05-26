import os
import sh as sh

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

if __name__ == '__main__':
    pass
    # todo creating conda environment, in the same directory if specified
    # todo dockerfile, etc
