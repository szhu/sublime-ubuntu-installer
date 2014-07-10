#!/usr/bin/env python

from subprocess import Popen
from os.path import exists, join  #, split
from os import chdir
from ast import literal_eval

from strings import strings

def s(key):
    if hasattr(strings, key): return getattr(strings, key)
    else: raise AttributeError('string not found: %r' % key)

ss=cmd_stdout('tput', 'smso')
rs=cmd_stdout('tput', 'rmso')
su=cmd_stdout('tput', 'smul')
ru=cmd_stdout('tput', 'rmul')
def lang(key):
    val = s(key)
    val = val.replace('<u>', su)
    val = val.replace('</u>', ru)
    val = val.replace('<s>', ss)
    val = val.replace('</s>', rs)
    return val

def print_lang(key):
    print lang(key),
    flush()

def print_langblock(key):
    from textwrap import fill
    val = lang(key)
    print fill(val, width=80)
    # print val
    flush()

def path(key):
    from os.path import expanduser
    return expanduser(s(key))

def user_multi(key):
    from os.path import expanduser
    return s(key).replace('~', expanduser('~'))


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
