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
