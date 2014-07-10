from singleton import singleton


@singleton
class strings(object):
    tmp_dir = 'install_sublime_tmp'
    tmp_directory_info = "This directory is used by the Sublime install script. You can delete this when it's finished installing."
    tmp_directory_info_file = "README"

    pkg_url = 'http://c758482.r82.cf2.rackcdn.com/sublime_text_3_build_3059_x64.tar.bz2'
    pkg_name = 'sublime_text_3_build_3059_x64.tar.bz2'
    pkg_dir = 'sublime_text_3'

    install_subl_dir = '~/.local/share/sublime-text-3'
    install_apps_dir = '~/.local/share/applications'
    install_exe = '~/.local/share/sublime-text-3/sublime_text'

    bashrc_file = '~/.bashrc'
    bashrc_contents = 'alias subl=~/".local/share/sublime-text-3/sublime_text"'

    mime_types = [
        "application/x-shellscript",
        "application/x-perl",
        "text/plain",
        "text/x-c++",
        "text/x-chdr",
        "text/x-csrc",
        "text/x-dtd",
        "text/x-java",
        "text/mathml",
        "text/x-python",
        "text/x-sql",
        "text/x-scheme"
    ]

    desktop_name = "sublime-text-3.desktop"
    desktop_file = join(install_apps_dir, desktop_name)
    desktop_contents = '''
#!/usr/bin/env xdg-open

[Desktop Entry]
Name=Sublime Text 3
GenericName=Text Editor
Comment=Sophisticated text editor for code, html and prose
Exec=~/.local/share/sublime-text-3/sublime_text %F
Terminal=false
Type=Application
MimeType=text/plain;text/x-chdr;text/x-csrc;text/x-c++hdr;text/x-c++src;text/x-java;text/x-dsrc;text/x-pascal;text/x-perl;text/x-python;application/x-php;application/x-httpd-php3;application/x-httpd-php4;application/x-httpd-php5;application/xml;text/html;text/css;text/x-sql;text/x-diff;x-directory/normal;inode/directory;
Icon=~/.local/share/sublime-text-3/Icon/128x128/sublime-text.png
Categories=TextEditor;Development;Utility;
StartupNotify=true
Actions=Window;Document;

X-Desktop-File-Install-Version=0.21

[Desktop Action Window]
Name=New Window
Exec=~/.local/share/sublime-text-3/sublime_text -n
OnlyShowIn=Unity;

[Desktop Action Document]
Name=New File
Exec=/usr/bin/subl --command new_file
OnlyShowIn=Unity;
'''

    confirm_continue = "Press <s>[enter]</s> to continue, <s>[ctrl-C]</s> to exit."
    yes_or_no = "  <s>[y/n]</s> "
    see_url = "See <u>http://szhu.me/subl</u> for more details."

    banner = "<s>                  SO I HEARD YOU WANT TO INSTALL SUBLIME TEXT                  </s>"
    requires_ubuntu = "This installer must be run from an Ubuntu machine. Please seat yourself at one (e.g., the 2nd floor Soda machines or the hiveN.cs.berkeley.edu machines in 330) or ssh into one before running this script. If you're sshing, try:\n\n    ssh <u>username</u>@hive10.cs.berkeley.edu"

    what_this_script_does = 'This script will download <u>Sublime Text 3 build 3059</u> and install it into your user directory at ' + install_subl_dir + '\n\nSublime will be added to the Ubuntu Unity Dash (apps button/"start menu" on the top-left) and optionally can be run with the <u>subl</u> command.\n'

    uninstalling = "Uninstalling ..."
    uninstalled = "old version of Sublime Text uninstalled."

    preparing = "Preparing ... "
    downloading = "Downloading ... "
    installing = "Installing ... "
    installed = "Installed."
    cleaning_up = "Cleaning up... "
    cleaned_up = "done."

    cmd_install = "Set the <u>subl</u> command to open/open files with with Sublime Text?\nIt works just like the emacs, vim, and gedit commands!"
    cmd_already_installed = "The <u>subl</u> command is already aliased in " + bashrc_file + "."
    cmd_caveats = "<u>subl</u> will work with terminals opened from now on.\nTo make the subl command work right here right now, do: \n\n    source ~/.bashrc\n"

    mime_install = "Set Sublime Text as the <u>default editor</u> when you double-click a text file?\nOtherwise, right-click a file and select Open With > Sublime Text 2."
    mime_already_installed = "Sublime is already set as the default text editor."

    icon_installed = 'An app icon has been installed to the Unity Dash (the "start menu" apps list).\nYou can drag this to the Unity Launcher (dock/taskbar).'
    confirm_show_icon = "Press <s>[enter]</s> to show this icon."
    icon_caveats = 'Once it opens, please right-click the icon and select "Lock to Launcher". You can also find the icon in the Unity Dash (the "start menu" apps list). Sublime Text not working for some reason? Try logging out and back in.'

    #

    all_done = "All done. You can run this installer again to reinstall or uninstall."
    all_caveats = "Does Sublime's icon look blurry? Log out and log back in."
    see_url_problem = "Something else not working? See <u>http://szhu.me/subl</u> for more details."
    have_fun = "<u>Have fun with Sublime!</u>"
