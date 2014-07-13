#!/usr/bin/env python
# -*- coding: utf-8 -*-

INDENT = '   '
from sys import stderr


def main(args):
    if len(args) == 1:
        args.append(None)
    assert len(args) == 2
    infile, outfile = args

    print >> stderr, 'read yaml...'
    data = load_data_from_yaml(infile)

    strings = {}

    for version in (2, 3):
        print >> stderr, 'merge strings for %s...' % version
        strings[version] = merge_strings(data, version)

        print >> stderr, 'variable-substitute strings for %s...' % version
        sub_strings(strings[version])

    print >> stderr, 'transform strings...'
    assignments = strings_to_assignments(strings, data['line_template'])

    print >> stderr, 'write strings...'
    outcontents = data['file_prefix'] + '\n'
    outcontents += ''.join(assignments)
    if outfile:
        writefile(outfile, outcontents)
    else:
        from sys import stdout
        stdout.write(outcontents)


def load_data_from_yaml(path):
    from yaml import load
    return load(file(path))


def writefile(path, contents):
    with file(path, 'w') as f:
        return f.write(contents)


def merge_strings(data, version):
    common = data['common']
    versioned = data[version]

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
                val0 = val0.replace(targeted_search_pattern, str(val1))
                if key1 in keys_to_check:
                    print >> stderr, INDENT + INDENT * len(seen_keys) + '└─ ' + key1
                    process_key(key1, new_seen_keys)
            strings[key0] = val0

        keys_to_check.remove(key0)

    while keys_to_check:
        key = keys_to_check[0]
        print >> stderr, INDENT + key
        process_key(key, [])


def strings_to_assignments(strings, line_template):
    assert set(strings[2].keys()) == set(strings[3].keys())
    keys = strings[2].keys()
    keys.sort()
    return [
        line_template % (
            key.upper(),
            strings[2][key],
            strings[3][key],
        )
        for key in keys
    ]


if __name__ == '__main__':
    try:
        from sys import argv
        exit(main(argv[1:]))
    except (KeyboardInterrupt, EOFError), e:
        print >> stderr, e
        exit(1)
