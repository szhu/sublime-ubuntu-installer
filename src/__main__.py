
# from os import getcwd
from os.path import join, dirname
from sys import path
YAML_PATH = join(dirname(__file__), 'PyYAML-3.11.zip/PyYAML-3.11/lib')
print YAML_PATH
path.append(YAML_PATH)
import yaml
print yaml

from installer import *

if __name__ == '__main__':
    from sys import exit
    try:
        exit(main() or 0)
    except CmdError, exc:
        print exc
        exit(1)
    except (KeyboardInterrupt, EOFError):
        print
        exit(-1)
