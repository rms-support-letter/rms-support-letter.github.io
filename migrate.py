"""Automate migration to new sign system
"""

import re
from urllib.request import urlopen
from string import ascii_letters


md_link_regex = re.compile(r'\[(?P<name>.*)\]\((?P<link>.+)\)')
username_regex = re.compile(r'https:\/\/(git(hub|lab)\.com|twitter\.com)\/(?P<username>.+\b)')


def parse_signed(text: str):
    for match in md_link_regex.findall(text):
        name, url = match[0], match[1]

        if url.startswith('https://github.com/rms-support-letter'):
            continue

        username_match = username_regex.match(url)
        if username_match is None:
            filename = ''.join([i for i in name if i in ascii_letters + ' '])
            filename = filename.replace(' ', '_')
            if not filename:
                print(f'failed to make filename for {name}')
                continue
        else:
            filename = username_match.group('username')
        with open(f'_data/signed/{filename}.yaml', 'w', encoding='utf-8') as file:
            file.write(
                f'name: {name}\nlink: {url}'
            )


def load_index():
    with urlopen('https://raw.githubusercontent.com/rms-support-letter/rms-support-letter.github.io/master/index.md') as f:
        return f.read().decode()


if __name__ == '__main__':
    parse_signed(load_index())
