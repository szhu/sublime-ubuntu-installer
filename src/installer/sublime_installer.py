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






def flush(dev=None):
    from sys import stdout
    (dev or stdout).flush()

def user_yn(prompt):
    while True:
        response = raw_input(lang(prompt) + lang('yes_or_no')).lower()
        if 'y' in response and 'n' in response: continue
        elif 'y' in response: return True
        elif 'n' in response: return False

def main():


    if not is_ubuntu():
        print
        print_langblock('requires_ubuntu')
        print
        print_langblock('see_url')
        return 1

    print
    print_lang('banner')
    print
    print
    print_langblock('what_this_script_does')
    print
    print_langblock('see_url')
    print_langblock('confirm_continue')
    raw_input()

    print_lang('preparing')
    cmd('mkdir', '-p', s('tmp_dir'))
    chdir(s('tmp_dir'))

    cmd('mkdir', '-p', path('install_apps_dir'))
    writefile( s('tmp_directory_info_file') , s('tmp_directory_info') )

    cmd('rm', '-rf', s('pkg_name'), s('pkg_dir'))
    if exists(path('install_subl_dir')):
        print
        print_lang('uninstalling')
        cmd('rm', '-rf', path('install_subl_dir'), path('desktop_file'))
        print_langblock('uninstalled')
        print_langblock('confirm_continue')
        raw_input()

    print_lang('downloading')
    pkgfile = file(s('pkg_name'), 'w')
    cmd('curl', '-fsSL', s('pkg_url'), stdout=pkgfile)
    pkgfile.close()

    print_lang('installing')
    cmd('tar', '-xf', s('pkg_name'), '--bzip2')
    cmd('mv', s('pkg_dir'), path('install_subl_dir'))
    writefile( path('desktop_file') , user_multi('desktop_contents') )
    cmd('chmod', 'u+x', path('desktop_file'))
    print_langblock('installed')

    # print_lang('cleaning_up')
    chdir('..')
    cmd('rm', '-rf', path('tmp_dir'))
    # print_langblock('cleaned_up')

    if exists(path('bashrc_file')) and s('bashrc_contents') in readfile(path('bashrc_file')):
        print_langblock('cmd_already_installed')
    elif user_yn('cmd_install'):
        appendfile(path('bashrc_file'), '\n' + s('bashrc_contents'))
        print_langblock('cmd_caveats')


    isdefault = True
    for mimetype in s('mime_types'):
        if cmd_stdout('xdg-mime', 'query', 'default', mimetype).strip() != s('desktop_name'):
            isdefault = False
            break
    if isdefault:
        print_langblock('mime_already_installed')
    elif user_yn('mime_install'):
        for mimetype in s('mime_types'):
            cmd('xdg-mime', 'default', s('desktop_name'), mimetype)


    launcher_items = cmd_stdout('gsettings', 'get', 'com.canonical.Unity.Launcher', 'favorites')
    launcher_items = literal_eval(launcher_items)
    # print launcher_items
    subl_item = s('desktop_name')
    if subl_item not in launcher_items:
        launcher_items.append(subl_item)
    # print launcher_items
    cmd('gsettings', 'set', 'com.canonical.Unity.Launcher', 'favorites', repr(launcher_items))

    # if [ -n "$DISPLAY" ]; then
    #   print -e 'Opening Sublime Text...'
    #   $EXEC_FILE &

    print
    print_langblock('all_done')
    print_langblock('all_caveats')
    print_langblock('see_url_problem')
    print
    print_langblock('have_fun')
    print
    print
