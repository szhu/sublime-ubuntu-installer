from os.path import expanduser
HOME = expanduser("~")

BASHRC_CONTENTS = 'export PATH=~/".local/bin":"$PATH"'.replace('$<HOME>', HOME)
BASHRC_FILE = '$<HOME>/.bashrc'.replace('$<HOME>', HOME)
DESKTOP_CONTENTS = '#!/usr/bin/env xdg-open\n#\n[Desktop Entry]\nName=Sublime Text 3\nGenericName=Text Editor\nComment=Sophisticated text editor for code, html and prose\nExec=$<HOME>/.local/share/sublime-text-3/sublime_text %F\nTerminal=false\nType=Application\nMimeType=text/plain;text/x-chdr;text/x-csrc;text/x-c++hdr;text/x-c++src;text/x-java;text/x-dsrc;text/x-pascal;text/x-perl;text/x-python;application/x-php;application/x-httpd-php3;application/x-httpd-php4;application/x-httpd-php5;application/xml;text/html;text/css;text/x-sql;text/x-diff;x-directory/normal;inode/directory;\nIcon=$<HOME>/.local/share/sublime-text-3/Icon/128x128/sublime-text.png\nCategories=TextEditor;Development;Utility;\nStartupNotify=true\nActions=Window;Document;\n#\nX-Desktop-File-Install-Version=0.21\n#\n[Desktop Action Window]\nName=New Window\nExec=$<HOME>/.local/share/sublime-text-3/sublime_text -n\nOnlyShowIn=Unity;\n#\n[Desktop Action Document]\nName=New File\nExec=$<HOME>/.local/share/sublime-text-3/sublime_text --command new_file\nOnlyShowIn=Unity;\n'.replace('$<HOME>', HOME)
DESKTOP_FILE = '$<HOME>/.local/share/applications sublime-text-3.desktop'.replace('$<HOME>', HOME)
DESKTOP_NAME = 'sublime-text-3.desktop'.replace('$<HOME>', HOME)
INSTALL_APPS_DIR = '$<HOME>/.local/share/applications'.replace('$<HOME>', HOME)
INSTALL_EXE = '$<HOME>/.local/share/sublime-text-3/sublime_text'.replace('$<HOME>', HOME)
INSTALL_EXE_REL = 'share/sublime-text-3/sublime_text'.replace('$<HOME>', HOME)
INSTALL_ICON = '$<HOME>/.local/share/sublime-text-3/Icon/128x128/sublime-text.png'.replace('$<HOME>', HOME)
INSTALL_SUBL_DIR = '$<HOME>/.local/share/sublime-text-3'.replace('$<HOME>', HOME)
INSTALL_SUBL_DIR_REL = 'share/sublime-text-3'.replace('$<HOME>', HOME)
MAJOR_VERSION = 3
MIME_TYPES = ['application/x-perl', 'application/x-shellscript', 'text/mathml', 'text/plain', 'text/x-c++', 'text/x-chdr', 'text/x-csrc', 'text/x-dtd', 'text/x-java', 'text/x-python', 'text/x-scheme', 'text/x-sql']
PKG_DIR = 'sublime_text_3'.replace('$<HOME>', HOME)
PKG_NAME = 'sublime_text_3_build_3059_x64.tar.bz2'.replace('$<HOME>', HOME)
PKG_URL = 'http://c758482.r82.cf2.rackcdn.com/sublime_text_3_build_3059_x64.tar.bz2'.replace('$<HOME>', HOME)
SYMLINK_DIR = '$<HOME>/.local/bin'.replace('$<HOME>', HOME)
SYMLINK_FILE = '$<HOME>/.local/bin/subl'.replace('$<HOME>', HOME)
SYMLINK_TARGET = '../share/sublime-text-3/sublime_text'.replace('$<HOME>', HOME)
TMP_DIR = '/tmp/install_sublime_tmp'.replace('$<HOME>', HOME)
TMP_DIRECTORY_INFO_CONTENTS = "This directory is used by the Sublime Text installer. You can delete this when it's finished installing.\n".replace('$<HOME>', HOME)
TMP_DIRECTORY_INFO_FILE = 'README'.replace('$<HOME>', HOME)
URL = 'http://szhu.me/subl'.replace('$<HOME>', HOME)
