#!/usr/bin/env python

from sublime_strings import BASHRC_CONTENTS
from sublime_strings import BASHRC_FILE
from sublime_strings import DESKTOP_CONTENTS
from sublime_strings import DESKTOP_FILE
from sublime_strings import DESKTOP_NAME
from sublime_strings import INSTALL_APPS_DIR
from sublime_strings import INSTALL_EXE
from sublime_strings import INSTALL_ICON
from sublime_strings import INSTALL_SUBL_DIR
from sublime_strings import MAJOR_VERSION
from sublime_strings import MIME_TYPES
from sublime_strings import PKG_DIR
from sublime_strings import PKG_NAME
from sublime_strings import PKG_URL
from sublime_strings import TMP_DIR
from sublime_strings import TMP_DIRECTORY_INFO_CONTENTS
from sublime_strings import TMP_DIRECTORY_INFO_FILE
from sublime_strings import URL
from sublime_strings import REASON_REQUIRES_UBUNTU
from sublime_strings import REASON_CORE_ALREADY_INSTALLED
from sublime_strings import REASON_CORE_NOT_INSTALLED


from command import do_command, pipe


def print_langblock(s):
    print s


def print_lang(s):
    print s


from installer import CheckResponse, ReasonedBoolean, Package, register_package_with_packages, WARN, ERROR

packages = {}
register_package = register_package_with_packages(packages)


@register_package
class Download(Package):
    def init(self):
        self.dependencies = []
        self.autoundo_action = None


@register_package
class Core(Package):
    def init(self):
        self.dependencies = [Download]
        self.autoundo_action = 'undo'

    def check(self):
        from utils_ubuntu import is_ubuntu
        from os.path import isdir

        if isdir(INSTALL_SUBL_DIR):
            do_allowed = ReasonedBoolean(True, ERROR, REASON_CORE_ALREADY_INSTALLED)
            undo_allowed = ReasonedBoolean(True)
        else:
            do_allowed = ReasonedBoolean(True)
            undo_allowed = ReasonedBoolean(False, WARN, REASON_CORE_NOT_INSTALLED)

        if not is_ubuntu():
            do_allowed = ReasonedBoolean(False, ERROR, REASON_REQUIRES_UBUNTU)

        self.cache_check_result(do_allowed, undo_allowed)

    def do(self):
        pkgfile = file(PKG_NAME, 'w')
        do_command('curl', '-fsSL', PKG_URL, stdout=pkgfile)
        pkgfile.close()

        print_lang('installing')
        do_command('tar', '-xf', PKG_NAME, '--bzip2')
        do_command('mv', PKG_DIR, INSTALL_SUBL_DIR)
        writefile( DESKTOP_FILE , DESKTOP_CONTENTS )
        do_command('chmod', 'u+x', DESKTOP_FILE)
        print_langblock('installed')


    def undo(self):
        do_command('rm', '-rf', INSTALL_SUBL_DIR, DESKTOP_FILE)
        print_langblock('uninstalled')



@register_package
class Launcher(Package):
    def init(self):
        self.dependencies = [Core]
        self.autoundo_action = 'check'


@register_package
class Mime(Package):
    def init(self):
        self.dependencies = [Core]
        self.autoundo_action = None


@register_package
class Open(Package):
    def init(self):
        self.dependencies = [Core]
        self.autoundo_action = None


@register_package
class Bashrc(Package):
    def init(self):
        self.dependencies = [Core, Bin]
        self.autoundo_action = None


@register_package
class Bin(Package):
    def init(self):
        self.dependencies = [Core]
        self.autoundo_action = None


#


@register_package('all', CHECK_ALLOWED)
def check_compatibility():
    from utils_ubuntu import is_ubuntu

    if not is_ubuntu():
        print
        print_langblock('requires_ubuntu')
        print
        print_langblock('see_url')
        return 1


@register_package('tmp', INSTALL)
def prepare_tmp():
    print_lang('preparing')
    do_command('mkdir', '-p', TMP_DIR)


def prepare_dest():
    from utils_io import writefile

    do_command('mkdir', '-p', INSTALL_APPS_DIR)
    writefile(TMP_DIRECTORY_INFO_FILE, TMP_DIRECTORY_INFO_CONTENTS)
    do_command('rm', '-rf', PKG_NAME, PKG_DIR)


@register_package('core', CHECK_INSTALLED)
def check_existing_install():
    from os.path import exists
    exists(INSTALL_SUBL_DIR)




    # print_lang('cleaning_up')
    chdir('..')
    do_command('rm', '-rf', TMP_DIR)
    # print_langblock('cleaned_up')

    if exists(BASHRC_FILE) and BASHRC_CONTENTS in readfile(BASHRC_FILE):
        print_langblock('cmd_already_installed')
    elif user_yn('cmd_install'):
        appendfile(BASHRC_FILE, '\n' + BASHRC_CONTENTS)
        print_langblock('cmd_caveats')


def check_in_launcher():
    from utils_ubuntu import app_is_in_launcher

    return app_is_in_launcher(DESKTOP_NAME)


def add_to_launcher():

    isdefault = True
    for mimetype in MIME_TYPES:
        if pipe('xdg-mime', 'query', 'default', mimetype).strip() != DESKTOP_NAME:
            isdefault = False
            break
    if isdefault:
        print_langblock('mime_already_installed')
    elif user_yn('mime_install'):
        for mimetype in MIME_TYPES:
            do_command('xdg-mime', 'default', DESKTOP_NAME, mimetype)


    launcher_items = pipe('gsettings', 'get', 'com.canonical.Unity.Launcher', 'favorites')
    launcher_items = literal_eval(launcher_items)
    # print launcher_items
    subl_item = DESKTOP_NAME
    if subl_item not in launcher_items:
        launcher_items.append(subl_item)
    # print launcher_items
    do_command('gsettings', 'set', 'com.canonical.Unity.Launcher', 'favorites', repr(launcher_items))

    # if [ -n "$DISPLAY" ]; then
    #   print -e 'Opening Sublime Text...'
    #   $EXEC_FILE &


for package in packages.values():
    package.isok()
