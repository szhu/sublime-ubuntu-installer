from __future__ import with_statement


def readfile(path):
    with open(path, 'r') as f:
        return f.read()


def writefile(path, contents):
    with open(path, 'w') as f:
        return f.write(contents)


def appendfile(path, contents):
    with open(path, 'a') as f:
        return f.write(contents)


def flush(dev=None):
    from sys import stdout
    (dev or stdout).flush()
