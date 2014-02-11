#!/usr/bin/env python

from subprocess import Popen
from os.path import exists, join #, split
from os import chdir
from ast import literal_eval

class Cmd(Popen):

	def __init__(self, *args, **kwargs):
		if len(args) == 0:
			raise TypeError('requires at least 1 argument (0 given)')
		self.args = args
		self.return_stdout = kwargs.get('return_stdout')
		self.return_stderr = kwargs.get('return_stderr')
		self.return_self = kwargs.get('return_self')
		self.custom_stdout = kwargs.get('stdout')

	def run(self):
		from subprocess import PIPE
		rout = self.return_stdout
		rerr = self.return_stderr
		Popen.__init__(self,
			self.args,
			stdout=self.custom_stdout or (PIPE if rout else None),
			stderr=PIPE if rerr else None,
			universal_newlines=True
		)
		self.wait()
		if self.returncode != 0: raise CmdError(self)
		if self.return_self: return self
		elif rout and rerr: return self.stdout.read(), self.stderr.read()
		elif rout: return self.stdout.read()
		elif rerr: return self.stderr.read()

class CmdError(Exception):
	def __init__(self, cmd):
		self.cmd = cmd
		self.args = cmd.args
		self.returncode = cmd.returncode

	def __str__(self):
		return "The command %s exited with return code %d" % (' '.join(self.args), self.returncode)

def cmd(*args, **kwargs):
	return Cmd(*args, **kwargs).run()

def cmd_stdout(*args):
	stdout = cmd(*args, return_stdout=True)
	# print args, '->', stdout
	return stdout


class Strings(object):
	tmp_dir = 'install_sublime_tmp'
	tmp_directory_info = "This directory is used by the Sublime install script. You can delete this when it's finished installing."
	tmp_directory_info_file = "README"

	pkg_url = 'http://c758482.r82.cf2.rackcdn.com/Sublime%20Text%202.0.2%20x64.tar.bz2'
	pkg_name = 'Sublime Text 2.0.2 x64.tar.bz2'
	pkg_dir = 'Sublime Text 2'

	install_subl_dir = '~/.local/share/sublime-text-2'
	install_apps_dir = '~/.local/share/applications'
	install_exe = '~/.local/share/sublime-text-2/sublime_text'

	bashrc_file = '~/.bashrc'
	bashrc_contents = 'alias subl=~/".local/share/sublime-text-2/sublime_text"'

	mime_types = ["application/x-shellscript",
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
				"text/x-scheme"]

	desktop_name = "sublime-text-2.desktop"
	desktop_file = join(install_apps_dir, desktop_name)
	desktop_contents = '''
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
'''

	confirm_continue = "Press <s>[enter]</s> to continue, <s>[ctrl-C]</s> to exit."
	yes_or_no = "  <s>[y/n]</s> "
	see_url = "See <u>http://szhu.me/subl</u> for more details."

	banner = "<s>                  SO I HEARD YOU WANT TO INSTALL SUBLIME TEXT                  </s>"
	requires_ubuntu = "This installer must be run from an Ubuntu machine. Please seat yourself at one (e.g., the 2nd floor Soda machines or the hiveN.cs.berkeley.edu machines in 330) or ssh into one before running this script. If you're sshing, try:\n\n    ssh <u>username</u>@hive10.cs.berkeley.edu"

	what_this_script_does = 'This script will download <u>Sublime Text 2.0.2</u> and install it into your user directory at ' + install_subl_dir + '\n\nSublime will be added to the Ubuntu Unity Dash (apps button/"start menu" on the top-left) and optionally can be run with the <u>subl</u> command.\n'

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


	all_done = "All done. You can run this installer again to reinstall or uninstall."
	all_caveats = "Does Sublime's icon look blurry? Log out and log back in."
	see_url_problem = "Something else not working? See <u>http://szhu.me/subl</u> for more details."
	have_fun = "<u>Have fun with Sublime!</u>"

strings = Strings()

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

def readfile(path):
	f = open(path, 'r')
	try: contents = f.read()
	except IOError: f.close(); raise
	f.close()
	return contents

def writefile(path, contents):
	f = open(path, 'w')
	try: f.write(contents)
	except IOError: f.close(); raise
	f.close()

def appendfile(path, contents):
	f = open(path, 'a')
	try: f.write(contents)
	except IOError: f.close(); raise
	f.close()

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

	try: cmd('/usr/bin/env', 'lsb_release', return_stderr=1, return_self=1)
	except CmdError:
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
	# 	print -e 'Opening Sublime Text...'
	# 	$EXEC_FILE &

	print
	print_langblock('all_done')
	print_langblock('all_caveats')
	print_langblock('see_url_problem')
	print
	print_langblock('have_fun')
	print
	print

if __name__ == '__main__':
	from sys import exit
	try:
		exit(main() or 0)
	except CmdError, exc:
		print exc
		exit(1)
	except (KeyboardInterrupt, EOFError):
		print
		exit(-1)
