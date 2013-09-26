#!/usr/bin/env bash

#S=install_sublime.sh;curl -Lk goo.gl/9fzkCo>$S;chmod u+x $S;./$S

README_MSG="This directory is used by the Sublime install script. You can delete this when it's finished installing."
WORK_DIR='install_sublime_tmp'
SUBL_TAR_URL='http://c758482.r82.cf2.rackcdn.com/Sublime%20Text%202.0.2%20x64.tar.bz2'
SUBL_TAR_NAME='Sublime Text 2.0.2 x64.tar.bz2'
SUBL_DIR='Sublime Text 2'

INSTALL_DIR=~/'.local/share/sublime-text-2'
APPS_DIR=~/'.local/share/applications'

PROMPT_INSTALL_BASHRC="Set the 'subl' command to open/open files with with Sublime Text?\nIt works just like the emacs, vim, and gedit commands! [y/n] "
BASHRC_NONEED_MSG="entry already in ~/.bashrc."
BASHRC='alias subl=~/".local/share/sublime-text-2/sublime_text"'
BASHRC_INSTALL_MSG="'subl' will work with terminals opened from now on.\nTo make the subl command work right here right now, do: source ~/.bashrc"

PROMPT_INSTALL_MIMEAPPS="Set Sublime Text as the default editor when you double-click on a text file?\nOtherwise, right-click a file and select Open With > Sublime Text 2. [y/n] "

ICON_MSG='An app icon has been installed to the Unity Dash (the "start menu" apps list).\nYou can drag this to the Unity Launcher (dock/taskbar).'
PROMPT_SHOW_ICON="Press [enter] to show this icon."
DESKTOP_FILENAME="sublime-text-2.desktop"
DESKTOP_FILE="$APPS_DIR/$DESKTOP_FILENAME"
DESKTOP=$( cat <<EOF
#!/usr/bin/env xdg-open

[Desktop Entry]
Name=Sublime Text 2
GenericName=Text Editor
Comment=Sophisticated text editor for code, html and prose
Exec=~/.local/share/sublime-text-2/sublime_text %F
Terminal=false
Type=Application
MimeType=text/plain;text/x-chdr;text/x-csrc;text/x-c++hdr;text/x-c++src;text/x-java;text/x-dsrc;text/x-pascal;text/x-perl;text/x-python;application/x-php;application/x-httpd-php3;application/x-httpd-php4;application/x-httpd-php5;application/xml;text/html;text/css;text/x-sql;text/x-diff;x-directory/normal;inode/directory;
Icon=~/.local/share/sublime-text-2/Icon/256x256/sublime_text.png
Categories=TextEditor;Development;Utility;
StartupNotify=true
Actions=Window;Document;

X-Desktop-File-Install-Version=0.21

[Desktop Action Window]
Name=New Window
Exec=~/.local/share/sublime-text-2/sublime_text -n
OnlyShowIn=Unity;

[Desktop Action Document]
Name=New File
Exec=/usr/bin/subl --command new_file
OnlyShowIn=Unity;
EOF
)


lsb_release 2> /dev/null
if [[ $? -ne 0 ]]; then
	echo -e "This installer must be run from an Ubuntu machine. Please seat yourself at an Ubuntu machine (i.e., the hiveN.cs.berkeley.edu machines in 330 Soda) or ssh into one before installing. If you're sshing, try:\n ssh `whoami`@hive10.cs.berkeley.edu"
	exit 1
fi

echo
echo -e "This script will install Sublime Text 2 into your user directory\nat $INSTALL_DIR.\nSublime will be added to the Ubuntu Dash (apps button on the top-left)\nand optionally can be run with the 'subl' command.\nSee interestinglythere.com/berkeley/sublime/ for more details.\nPress [enter] to continue, [ctrl-C] to exit."
read

set -e
# set -x

echo -e 'Preparing to install Sublime Text 2...'
mkdir -p "$WORK_DIR"
cd "$WORK_DIR"
mkdir -p "$APPS_DIR"
echo -e "$README_MSG">"README"

echo -en 'Removing possible old installations... '
rm -rf "$SUBL_TAR_NAME" "$SUBL_DIR" "$DESKTOP_FILE"
if [ -e "$INSTALL_DIR" ]; then
	rm -rf "$INSTALL_DIR"
	echo -e
	echo -en "Sublime Text 2 uninstalled.\nPress [ctrl-C] to stop here, [enter] to install."
	read
else
	echo -e 'no old installation exists.'
fi

echo -e 'Downloading Sublime Text 2...'
curl -L "$SUBL_TAR_URL" > "$SUBL_TAR_NAME"
echo -e 'Decompressing...'
tar -xf "$SUBL_TAR_NAME" --bzip2
echo -e 'Moving files into place...'
cp -r "$SUBL_DIR" "$INSTALL_DIR"
echo -e 'Installing launcher shortcut icon...'
echo -e "$DESKTOP" | sed "s,~,$HOME,g" > "$DESKTOP_FILE"
chmod u+x "$DESKTOP_FILE"


echo -en "Installing 'subl' command... "
IS_BASHRC_INSTALLED=
if [ -e ~/.bashrc ]; then
	if [ -n "`grep "$BASHRC" ~/.bashrc`" ]; then
		IS_BASHRC_INSTALLED=true
		echo -e "$BASHRC_NONEED_MSG"
	fi
fi
if [ -z $IS_BASHRC_INSTALLED ]; then
	echo -e; echo -e
	loop=true
	while "$loop"; do
		echo -en "$PROMPT_INSTALL_BASHRC"
		read input
		if [ -n "`echo -e "$input" | grep -i [yn]`" ]; then
			loop=false
		fi
	done
	if [ "$input" = "y" ]; then
		echo >> ~/.bashrc
		echo "$BASHRC" >> ~/.bashrc
		echo -e "$BASHRC_INSTALL_MSG"
	fi
fi

echo -e
loop=true
while "$loop"; do
	echo -en "$PROMPT_INSTALL_MIMEAPPS"
	read input
	if [ -n "`echo -e "$input" | grep -i [yn]`" ]; then
		loop=false
	fi
echo -en ""
done
if [ "$input" = "y" ]; then
	xdg-mime default "$DESKTOP_FILENAME" application/x-perl
	xdg-mime default "$DESKTOP_FILENAME" text/plain
	xdg-mime default "$DESKTOP_FILENAME" text/x-chdr
	xdg-mime default "$DESKTOP_FILENAME" text/x-csrc
	xdg-mime default "$DESKTOP_FILENAME" text/x-dtd
	xdg-mime default "$DESKTOP_FILENAME" text/x-java
	xdg-mime default "$DESKTOP_FILENAME" text/mathml
	xdg-mime default "$DESKTOP_FILENAME" text/x-python
	xdg-mime default "$DESKTOP_FILENAME" text/x-sql
fi

echo -e 'Sublime Text 2 installed!'

echo -e 'Cleaning up...'
cd ..
rm -rf "$WORK_DIR"

if [ -z disabled"$DISPLAY" ]; then
	if [ -n "`which nautilus`" ]; then	
		echo -e
		echo -e "$ICON_MSG"
		echo -en "$PROMPT_SHOW_ICON"
		read
		nautilus "$DESKTOP_FILE"
	fi
else
	echo -e
	echo -e "$ICON_MSG"
	echo -e
fi

echo -e "All done. You can run this installer again ($0)\nto reinstall or uninstall.\nBye!"
read
