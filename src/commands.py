from subprocess import Popen, CalledProcessError


CMD_ENV = '/usr/bin/env'


class Command(Popen):
    '''
    A subclass of subprocess.Popen that has some custom defaults, takes in a
    `wait` parameter, and remembers its arguments.
    '''

    def __init__(self, args, wait=True, **kwargs):
        self.args = args
        self.options = options = {
            'universal_newlines': True
        }
        self.options.update(kwargs)
        Popen.__init__(self, args, **options)
        if wait:
            self.wait()

    def __str__(self):
        ' '.join(
            (repr(arg) if "'" in arg else arg)
            for arg in self.args
        )


class CommandError(CalledProcessError):
    def __init__(self, command, message=None):
        self.command = command
        self.message = message

    def __str__(self):
        s = "Command %s exited with status code %s." % (
            ' '.join(self.args),
            self.command
        )
        if self.message:
            s += '\n' + self.message
        return s


def start_command(*args):
    '''
    Launches a command asynchronously.
    '''
    return Command(args, wait=False)


def try_command(*args):
    '''
    Launches a command synchronously and waits for it to exit.
    '''
    return Command(args)


def do_command(*args):
    '''
    Does try_command and requires it to exit with return code 0.
    '''
    command = Command(args)
    if command.returncode != 0:
        raise CommandError(command)
    return command


def pipe(*args):
    '''
    Does do_command and returns the output.
    '''
    from subprocess import PIPE
    command = Command(args, stdout=PIPE)
    if command.returncode != 0:
        raise CommandError(command)
    return command.stdout.read()
