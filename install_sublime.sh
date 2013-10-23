#!/usr/bin/env bash

#S=install_sublime.sh;curl -Lk goo.gl/9fzkCo>$S;chmod u+x $S;./$S

smso=`tput smso`
rmso=`tput rmso`
smul=`tput smul`
rmul=`tput rmul`

README_MSG="This directory is used by the Sublime install script. You can delete this when it's finished installing."
WORK_DIR='install_sublime_tmp'
SUBL_TAR_URL='http://c758482.r82.cf2.rackcdn.com/Sublime%20Text%202.0.2%20x64.tar.bz2'
SUBL_TAR_NAME='Sublime Text 2.0.2 x64.tar.bz2'
SUBL_DIR='Sublime Text 2'

INSTALL_DIR_RELATIVE='.local/share/sublime-text-2'
INSTALL_DIR=~/"$INSTALL_DIR_RELATIVE"
APPS_DIR=~/'.local/share/applications'
EXEC_FILE=~/'.local/share/sublime-text-2/sublime_text'

PROMPT_CONTINUE="Press ${smso}[enter]${rmso} to continue, ${smso}[ctrl-C]${rmso} to exit."
PROMPT_YN="  ${smso}[y/n]${rmso} "
LINK_MSG="See ${smul}http://interestinglythere.com/berkeley/sublime${rmul} for more details.\n"

PROMPT_INSTALL_BASHRC="Set the ${smul}subl${rmul} command to open/open files with with Sublime Text?\nIt works just like the emacs, vim, and gedit commands!${PROMPT_YN}"
BASHRC_NONEED_MSG="no need; entry already in ~/.bashrc."
BASHRC='alias subl=~/".local/share/sublime-text-2/sublime_text"'
BASHRC_INSTALL_MSG="${smul}subl${rmul} will work with terminals opened from now on.\nTo make the subl command work right here right now, do: \n\n    source ~/.bashrc\n"

PROMPT_INSTALL_MIMEAPPS="Set Sublime Text as the ${smul}default editor${rmul} when you double-click a text file?\nOtherwise, right-click a file and select Open With > Sublime Text 2.${PROMPT_YN}"
MIME_TYPES="application/x-shellscript application/x-perl text/plain text/x-c++ text/x-chdr text/x-csrc text/x-dtd text/x-java text/mathml text/x-python text/x-sql text/x-scheme"

ICON_MSG='An app icon has been installed to the Unity Dash (the "start menu" apps list).\nYou can drag this to the Unity Launcher (dock/taskbar).'
PROMPT_SHOW_ICON="Press ${smso}[enter]${rmso} to show this icon."
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
	echo
	echo -e "This installer must be run from an Ubuntu machine. Please seat yourself at one\n(e.g., the 2nd floor Soda machines or the hiveN.cs.berkeley.edu machines in\n330) or ssh into one before running this script. If you're sshing, try:\n\n    ssh ${smul}username${rmul}@hive10.cs.berkeley.edu"
	echo
	echo -e "$LINK_MSG"
	exit 1
fi

echo
echo -e "${smso}                  SO I HEARD YOU WANT TO INSTALL SUBLIME TEXT                  ${rmso}"
echo
echo -e "This script will download ${smul}Sublime Text 2.0.2${rmul} and install it into your user\ndirectory at ~/${INSTALL_DIR_RELATIVE}.\n\nSublime will be added to the Ubuntu Unity Dash (apps button/\"start menu\" on\nthe top-left) and optionally can be run with the ${smul}subl${rmul} command.\n\n$LINK_MSG\n$PROMPT_CONTINUE"
read

set -e
# set -x

echo -e "Preparing to install Sublime Text 2..."
mkdir -p "$WORK_DIR"
cd "$WORK_DIR"
mkdir -p "$APPS_DIR"
echo -e "$README_MSG">"README"

echo -en 'Removing possible old installations... '
rm -rf "$SUBL_TAR_NAME" "$SUBL_DIR" "$DESKTOP_FILE"
if [ -e "$INSTALL_DIR" ]; then
	rm -rf "$INSTALL_DIR"
	echo -e "old version of Sublime Text uninstalled.\n$PROMPT_CONTINUE"
	read
else
	echo -e "no old installation exists."
fi

echo -e "Downloading Sublime Text 2..."
curl -L "$SUBL_TAR_URL" > "$SUBL_TAR_NAME"
echo -e "Downloaded."
echo -en "Decompressing... "
tar -xf "$SUBL_TAR_NAME" --bzip2
echo -e "done."
echo -en "Moving files into place... "
echo -e "done."
cp -r "$SUBL_DIR" "$INSTALL_DIR"
echo -en "Installing launcher shortcut icon... "
echo -e "$DESKTOP" | sed "s,~,$HOME,g" > "$DESKTOP_FILE"
chmod u+x "$DESKTOP_FILE"
echo -e "done."

echo -en "Installing ${smul}subl${rmul} command... "
IS_BASHRC_INSTALLED=''
if [ -e ~/.bashrc ]; then
	if [ -n "`grep "$BASHRC" ~/.bashrc`" ]; then
		IS_BASHRC_INSTALLED=true
		echo -e "$BASHRC_NONEED_MSG"
	fi
fi
if [ -z $IS_BASHRC_INSTALLED ]; then
	echo; echo
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

echo -en "Checking mimetype defaults... "
IS_DEFAULT_MIMEAPP=''
for MIME_TYPE in $MIME_TYPES
do
	if [ "`xdg-mime query default "$MIME_TYPE"`" != "$DESKTOP_FILENAME" ]; then
		IS_DEFAULT_MIMEAPP=false
	fi
done
if [ -z $IS_DEFAULT_MIMEAPP ]; then
	echo -e 'already default app.'
else
	echo; echo
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
		for MIME_TYPE in $MIME_TYPES
		do
			xdg-mime default "$DESKTOP_FILENAME" "$MIME_TYPE"
		done
	fi
fi

echo
echo -e "Sublime Text 2 ${smul}installed${rmul}!"

echo -en "Cleaning up... "
cd ..
rm -rf "$WORK_DIR"
echo -e "done."

if [ -n "$DISPLAY" ]; then
	echo -e 'Opening Sublime Text...'
	$EXEC_FILE &
	echo
	echo -e 'Once it opens, please right-click the icon and select "Lock to Launcher".'
	echo -e 'You can also find the icon in the Unity Dash (the "start menu" apps list).'
	echo -e 'Sublime Text not working for some reason? Try logging out and back in.'
	echo
else
	echo
	echo -e "$ICON_MSG"
	echo
fi

echo -e "All done. You can run this installer again ($0) to reinstall\nor uninstall. ${smul}Have fun with Sublime!${rmul}"
read