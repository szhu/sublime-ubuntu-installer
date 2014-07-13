class JsonSerializable(dict):
    def __repr__(self):
        from json import dumps
        return dumps(self)


# Used for `level` parameter of ReasonedBoolean. Its truthiness indicates
# whether the reason should be presented with increased visibility to the user.
WARN = False
ERROR = True


class ReasonedBoolean(JsonSerializable):
    def __init__(self, boolean, level=WARN, message=None):
        JsonSerializable.__init__(self, {
            'boolean': boolean,
            'level': level,
            'message': message,
        })


class CheckResult(JsonSerializable):
    def __init__(self, installed, do_allowed, undo_allowed, message=None):
        JsonSerializable.__init__(self, {
            'installed': installed,
            'do_allowed': do_allowed,
            'undo_allowed': undo_allowed,
            'message': message
        })


class Package(object):
    def __init__(self, packages):
        self.name = self.__name__.lower()
        self.packages = packages
        self.undo_dependencies = []
        self._check_results = None
        self.init()

    def init(self):
        raise NotImplementedError('this is an abstract class bro')

    def supports_action(self, action):
        assert action in ('do', 'undo', 'check')
        return getattr(self, action, None) is not None

    def do_and_check(self):
        self.do()
        return self.check_and_cache()

    def undo_and_check(self):
        self.undo()
        return self.check_and_cache()

    def check_and_cache(self):
        self._check_results = self.check()
        return self._check_results

    def autoundo(self):
        if self.autoundo_action == 'undo':
            return self.undo_and_check()
        elif self.autoundo_action == 'do':
            return self.do_and_check()
        elif self.autoundo_action == 'check':
            return self.check_and_cache()
        else:
            raise ValueError()

    def lazy_check(self):
        if self._check_results is None:
            self.check_and_cache()
        return self._check_results

    def isok(self):
        assert type(self.dependencies) == list
        for dependency in self.dependencies:
            assert dependency in self.packages
        for dependency in self.dependencies:
            assert self.name in self.packages[dependency].undo_dependencies
        for dependency in self.undo_dependencies:
            assert self.name in self.packages[dependency].dependencies
        if self.autoundo_action:
            assert self.supports_action(self.autoundo_action)


def register_package_with_packages(packages):
    def register_package(package_class):
        package = package_class()
        packages[package.name] = package
        return package.name
    return register_package
