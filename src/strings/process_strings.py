DESKTOP_CONTENTS = '#!/usr/bin/env xdg-open\n#\n[Desktop Entry]\nName=Sublime Text 3\nGenericName=Text Editor\nComment=Sophisticated text editor for code, html and prose\nExec=$<HOME>/.local/share/sublime-text-2/sublime_text %F\nTerminal=false\nType=Application\nMimeType=text/plain;text/x-chdr;text/x-csrc;text/x-c++hdr;text/x-c++src;text/x-java;text/x-dsrc;text/x-pascal;text/x-perl;text/x-python;application/x-php;application/x-httpd-php3;application/x-httpd-php4;application/x-httpd-php5;application/xml;text/html;text/css;text/x-sql;text/x-diff;x-directory/normal;inode/directory;\nIcon=$<HOME>/.local/share/sublime-text-2/Icon/256x256/sublime_text.png\nCategories=TextEditor;Development;Utility;\nStartupNotify=true\nActions=Window;Document;\n#\nX-Desktop-File-Install-Version=0.21\n#\n[Desktop Action Window]\nName=New Window\nExec=$<HOME>/.local/share/sublime-text-2/sublime_text -n\nOnlyShowIn=Unity;\n#\n[Desktop Action Document]\nName=New File\nExec=$<HOME>/.local/share/sublime-text-2/sublime_text --command new_file\nOnlyShowIn=Unity;\n'
INSTALL_ICON = '$<HOME>/.local/share/sublime-text-2/Icon/256x256/sublime_text.png'
TMP_DIR = '/tmp/install_sublime_tmp'
PKG_DIR = 'Sublime Text 2'
INSTALL_SUBL_DIR = '$<HOME>/.local/share/sublime-text-2'
INSTALL_APPS_DIR = '$<HOME>/.local/share/applications'
MAJOR_VERSION = 2
BASHRC_FILE = '$<HOME>/.bashrc'
URL = 'http://szhu.me/subl'
BASHRC_CONTENTS = 'export PATH=~/".local/bin":"$PATH"'
TMP_DIRECTORY_INFO_FILE = 'README'
PKG_URL = 'http://c758482.r82.cf2.rackcdn.com/Sublime Text 2.0.2 x64.tar.bz2'
TMP_DIRECTORY_INFO_CONTENTS = "This directory is used by the Sublime Text installer. You can delete this when it's finished installing.\n"
PKG_NAME = 'Sublime Text 2.0.2 x64.tar.bz2'
MIME_TYPES = ['application/x-perl', 'application/x-shellscript', 'text/mathml', 'text/plain', 'text/x-c++', 'text/x-chdr', 'text/x-csrc', 'text/x-dtd', 'text/x-java', 'text/x-python', 'text/x-scheme', 'text/x-sql']
DESKTOP_FILE = '$<HOME>/.local/share/applications sublime-text-2.desktop'
DESKTOP_NAME = 'sublime-text-2.desktop'
INSTALL_EXE = '$<HOME>/.local/share/sublime-text-2/sublime_text'
