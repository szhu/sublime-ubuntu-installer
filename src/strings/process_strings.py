#!/usr/bin/env python


MAJOR_VERSION = 2


def main(args):
    assert len(args) == 2
    infile, outfile = args
    data = load_data_from_yaml(infile)
    strings = merge_strings(data)
    sub_strings(strings)
    assignments = strings_to_assignments(strings)
    assignments.sort()
    writefile(outfile, ''.join(assignments))


def load_data_from_yaml(path):
    from yaml import load
    return load(file(path))


def writefile(path, contents):
    with file(path, 'w') as f:
        return f.write(contents)


def merge_strings(data):
    common = data['common']
    versioned = data[MAJOR_VERSION]

    # Insure no duplicates
    assert not [key for key in versioned if key in common]
    # Insure all lowercase keys
    assert all(key.islower() for key in versioned)
    assert all(key.islower() for key in common)

    strings = common.copy()
    strings.update(versioned)
    return strings


def sub_strings(strings):
    from re import compile, search
    general_search_pattern = compile(r'\$\((\w+?)\)')
    keys_to_check = strings.keys()

    def process_key(key0, seen_keys):
        if key0 in seen_keys:
            raise ValueError('Circular reference for key %r' % key0)
        val0 = strings[key0]
        if isinstance(val0, str):
            new_seen_keys = seen_keys + [key0]

            while True:
                m = search(general_search_pattern, val0)
                if not m:
                    break
                key1 = m.group(1)
                val1 = strings[key1]
                targeted_search_pattern = '$(%s)' % key1
                val0 = val0.replace(targeted_search_pattern, val1)
                if key1 in keys_to_check:
                    print key1
                    process_key(key1, new_seen_keys)
            strings[key0] = val0

        keys_to_check.remove(key0)

    while keys_to_check:
        key = keys_to_check[0]
        print key
        process_key(key, [])


def strings_to_assignments(strings):
    return ['%s = %r\n' % (key.upper(), strings[key]) for key in strings.keys()]


# DESKTOP_CONTENTS = '#!/usr/bin/env xdg-open\n#\n[Desktop Entry]\nName=Sublime Text 3\nGenericName=Text Editor\nComment=Sophisticated text editor for code, html and prose\nExec=$<HOME>/.local/share/sublime-text-2/sublime_text %F\nTerminal=false\nType=Application\nMimeType=text/plain;text/x-chdr;text/x-csrc;text/x-c++hdr;text/x-c++src;text/x-java;text/x-dsrc;text/x-pascal;text/x-perl;text/x-python;application/x-php;application/x-httpd-php3;application/x-httpd-php4;application/x-httpd-php5;application/xml;text/html;text/css;text/x-sql;text/x-diff;x-directory/normal;inode/directory;\nIcon=$<HOME>/.local/share/sublime-text-2/Icon/256x256/sublime_text.png\nCategories=TextEditor;Development;Utility;\nStartupNotify=true\nActions=Window;Document;\n#\nX-Desktop-File-Install-Version=0.21\n#\n[Desktop Action Window]\nName=New Window\nExec=$<HOME>/.local/share/sublime-text-2/sublime_text -n\nOnlyShowIn=Unity;\n#\n[Desktop Action Document]\nName=New File\nExec=$<HOME>/.local/share/sublime-text-2/sublime_text --command new_file\nOnlyShowIn=Unity;\n'
# INSTALL_ICON = '$<HOME>/.local/share/sublime-text-2/Icon/256x256/sublime_text.png'
# TMP_DIR = '/tmp/install_sublime_tmp'
# PKG_DIR = 'Sublime Text 2'
# INSTALL_SUBL_DIR = '$<HOME>/.local/share/sublime-text-2'
# INSTALL_APPS_DIR = '$<HOME>/.local/share/applications'
# MAJOR_VERSION = 2
# BASHRC_FILE = '$<HOME>/.bashrc'
# URL = 'http://szhu.me/subl'
# BASHRC_CONTENTS = 'export PATH=~/".local/bin":"$PATH"'
# TMP_DIRECTORY_INFO_FILE = 'README'
# PKG_URL = 'http://c758482.r82.cf2.rackcdn.com/Sublime Text 2.0.2 x64.tar.bz2'
# TMP_DIRECTORY_INFO_CONTENTS = "This directory is used by the Sublime Text installer. You can delete this when it's finished installing.\n"
# PKG_NAME = 'Sublime Text 2.0.2 x64.tar.bz2'
# MIME_TYPES = ['application/x-perl', 'application/x-shellscript', 'text/mathml', 'text/plain', 'text/x-c++', 'text/x-chdr', 'text/x-csrc', 'text/x-dtd', 'text/x-java', 'text/x-python', 'text/x-scheme', 'text/x-sql']
# DESKTOP_FILE = '$<HOME>/.local/share/applications sublime-text-2.desktop'
# DESKTOP_NAME = 'sublime-text-2.desktop'
# INSTALL_EXE = '$<HOME>/.local/share/sublime-text-2/sublime_text'


if __name__ == '__main__':
    try:
        from sys import argv
        exit(main(argv[1:]))
    except (KeyboardInterrupt, EOFError), e:
        from sys import stderr
        print >> stderr, e
        exit(1)
