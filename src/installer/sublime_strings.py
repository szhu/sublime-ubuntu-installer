from os.path import expanduser
HOME = expanduser("~")

def BASHRC_CONTENTS():
    if _version == 2:
        return 'export PATH=~/".local/bin":"$PATH"'.replace('$<HOME>', HOME)
    elif _version == 3:
        return 'export PATH=~/".local/bin":"$PATH"'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def BASHRC_FILE():
    if _version == 2:
        return '$<HOME>/.bashrc'.replace('$<HOME>', HOME)
    elif _version == 3:
        return '$<HOME>/.bashrc'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def DESKTOP_CONTENTS():
    if _version == 2:
        return '#!/usr/bin/env xdg-open\n#\n[Desktop Entry]\nName=Sublime Text 2\nGenericName=Text Editor\nComment=Sophisticated text editor for code, html and prose\nExec=$<HOME>/.local/share/sublime-text-2/sublime_text %F\nTerminal=false\nType=Application\nMimeType=text/plain;text/x-chdr;text/x-csrc;text/x-c++hdr;text/x-c++src;text/x-java;text/x-dsrc;text/x-pascal;text/x-perl;text/x-python;application/x-php;application/x-httpd-php3;application/x-httpd-php4;application/x-httpd-php5;application/xml;text/html;text/css;text/x-sql;text/x-diff;x-directory/normal;inode/directory;\nIcon=$<HOME>/.local/share/sublime-text-2/Icon/256x256/sublime_text.png\nCategories=TextEditor;Development;Utility;\nStartupNotify=true\nActions=Window;Document;\n#\nX-Desktop-File-Install-Version=0.21\n#\n[Desktop Action Window]\nName=New Window\nExec=$<HOME>/.local/share/sublime-text-2/sublime_text -n\nOnlyShowIn=Unity;\n#\n[Desktop Action Document]\nName=New File\nExec=$<HOME>/.local/share/sublime-text-2/sublime_text --command new_file\nOnlyShowIn=Unity;\n'.replace('$<HOME>', HOME)
    elif _version == 3:
        return '#!/usr/bin/env xdg-open\n#\n[Desktop Entry]\nName=Sublime Text 3\nGenericName=Text Editor\nComment=Sophisticated text editor for code, html and prose\nExec=$<HOME>/.local/share/sublime-text-3/sublime_text %F\nTerminal=false\nType=Application\nMimeType=text/plain;text/x-chdr;text/x-csrc;text/x-c++hdr;text/x-c++src;text/x-java;text/x-dsrc;text/x-pascal;text/x-perl;text/x-python;application/x-php;application/x-httpd-php3;application/x-httpd-php4;application/x-httpd-php5;application/xml;text/html;text/css;text/x-sql;text/x-diff;x-directory/normal;inode/directory;\nIcon=$<HOME>/.local/share/sublime-text-3/Icon/128x128/sublime-text.png\nCategories=TextEditor;Development;Utility;\nStartupNotify=true\nActions=Window;Document;\n#\nX-Desktop-File-Install-Version=0.21\n#\n[Desktop Action Window]\nName=New Window\nExec=$<HOME>/.local/share/sublime-text-3/sublime_text -n\nOnlyShowIn=Unity;\n#\n[Desktop Action Document]\nName=New File\nExec=$<HOME>/.local/share/sublime-text-3/sublime_text --command new_file\nOnlyShowIn=Unity;\n'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def DESKTOP_FILE():
    if _version == 2:
        return '$<HOME>/.local/share/applications sublime-text-2.desktop'.replace('$<HOME>', HOME)
    elif _version == 3:
        return '$<HOME>/.local/share/applications sublime-text-3.desktop'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def DESKTOP_NAME():
    if _version == 2:
        return 'sublime-text-2.desktop'.replace('$<HOME>', HOME)
    elif _version == 3:
        return 'sublime-text-3.desktop'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def INSTALL_APPS_DIR():
    if _version == 2:
        return '$<HOME>/.local/share/applications'.replace('$<HOME>', HOME)
    elif _version == 3:
        return '$<HOME>/.local/share/applications'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def INSTALL_EXE():
    if _version == 2:
        return '$<HOME>/.local/share/sublime-text-2/sublime_text'.replace('$<HOME>', HOME)
    elif _version == 3:
        return '$<HOME>/.local/share/sublime-text-3/sublime_text'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def INSTALL_EXE_REL():
    if _version == 2:
        return 'share/sublime-text-2/sublime_text'.replace('$<HOME>', HOME)
    elif _version == 3:
        return 'share/sublime-text-3/sublime_text'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def INSTALL_ICON():
    if _version == 2:
        return '$<HOME>/.local/share/sublime-text-2/Icon/256x256/sublime_text.png'.replace('$<HOME>', HOME)
    elif _version == 3:
        return '$<HOME>/.local/share/sublime-text-3/Icon/128x128/sublime-text.png'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def INSTALL_SUBL_DIR():
    if _version == 2:
        return '$<HOME>/.local/share/sublime-text-2'.replace('$<HOME>', HOME)
    elif _version == 3:
        return '$<HOME>/.local/share/sublime-text-3'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def INSTALL_SUBL_DIR_REL():
    if _version == 2:
        return 'share/sublime-text-2'.replace('$<HOME>', HOME)
    elif _version == 3:
        return 'share/sublime-text-3'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def MAJOR_VERSION():
    if _version == 2:
        return 2.replace('$<HOME>', HOME)
    elif _version == 3:
        return 3.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def MIME_TYPES():
    if _version == 2:
        return ['application/x-perl', 'application/x-shellscript', 'text/mathml', 'text/plain', 'text/x-c++', 'text/x-chdr', 'text/x-csrc', 'text/x-dtd', 'text/x-java', 'text/x-python', 'text/x-scheme', 'text/x-sql'].replace('$<HOME>', HOME)
    elif _version == 3:
        return ['application/x-perl', 'application/x-shellscript', 'text/mathml', 'text/plain', 'text/x-c++', 'text/x-chdr', 'text/x-csrc', 'text/x-dtd', 'text/x-java', 'text/x-python', 'text/x-scheme', 'text/x-sql'].replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def PKG_DIR():
    if _version == 2:
        return 'Sublime Text 2'.replace('$<HOME>', HOME)
    elif _version == 3:
        return 'sublime_text_3'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def PKG_NAME():
    if _version == 2:
        return 'Sublime Text 2.0.2 x64.tar.bz2'.replace('$<HOME>', HOME)
    elif _version == 3:
        return 'sublime_text_3_build_3059_x64.tar.bz2'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def PKG_URL():
    if _version == 2:
        return 'http://c758482.r82.cf2.rackcdn.com/Sublime Text 2.0.2 x64.tar.bz2'.replace('$<HOME>', HOME)
    elif _version == 3:
        return 'http://c758482.r82.cf2.rackcdn.com/sublime_text_3_build_3059_x64.tar.bz2'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def REASON_CORE_ALREADY_INSTALLED():
    if _version == 2:
        return 'Sublime Text 2 appears to already be installed to $<HOME>/.local/share/sublime-text-2. Installing will overwrite the previous version.\n'.replace('$<HOME>', HOME)
    elif _version == 3:
        return 'Sublime Text 3 appears to already be installed to $<HOME>/.local/share/sublime-text-3. Installing will overwrite the previous version.\n'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def REASON_CORE_NOT_INSTALLED():
    if _version == 2:
        return "Sublime Text 2 is not installed to $<HOME>/.local/share/sublime-text-2 (or at all), and so can't be removed by this installer.\n".replace('$<HOME>', HOME)
    elif _version == 3:
        return "Sublime Text 3 is not installed to $<HOME>/.local/share/sublime-text-3 (or at all), and so can't be removed by this installer.\n".replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def REASON_REQUIRES_UBUNTU():
    if _version == 2:
        return 'This installer can only be run on an Ubuntu machine.\n'.replace('$<HOME>', HOME)
    elif _version == 3:
        return 'This installer can only be run on an Ubuntu machine.\n'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def SYMLINK_DIR():
    if _version == 2:
        return '$<HOME>/.local/bin'.replace('$<HOME>', HOME)
    elif _version == 3:
        return '$<HOME>/.local/bin'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def SYMLINK_FILE():
    if _version == 2:
        return '$<HOME>/.local/bin/subl'.replace('$<HOME>', HOME)
    elif _version == 3:
        return '$<HOME>/.local/bin/subl'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def SYMLINK_TARGET():
    if _version == 2:
        return '../share/sublime-text-2/sublime_text'.replace('$<HOME>', HOME)
    elif _version == 3:
        return '../share/sublime-text-3/sublime_text'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def TMP_DIR():
    if _version == 2:
        return '/tmp/install_sublime_tmp'.replace('$<HOME>', HOME)
    elif _version == 3:
        return '/tmp/install_sublime_tmp'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def TMP_DIRECTORY_INFO_CONTENTS():
    if _version == 2:
        return "This directory is used by the Sublime Text installer. You can delete this when it's finished installing.\n".replace('$<HOME>', HOME)
    elif _version == 3:
        return "This directory is used by the Sublime Text installer. You can delete this when it's finished installing.\n".replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def TMP_DIRECTORY_INFO_FILE():
    if _version == 2:
        return 'README'.replace('$<HOME>', HOME)
    elif _version == 3:
        return 'README'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
def URL():
    if _version == 2:
        return 'http://szhu.me/subl'.replace('$<HOME>', HOME)
    elif _version == 3:
        return 'http://szhu.me/subl'.replace('$<HOME>', HOME)
    else:
        raise ValueError('unknown version %r' % _version)
