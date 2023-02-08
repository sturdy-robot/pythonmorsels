import re
from io import StringIO
from typing import Union, TextIO
import sys


def entries_by_date(file_data: Union[StringIO, TextIO]):
    lines = file_data.read()
    pattern = re.compile(r"\d{4}-\d{2}-\d{2}\n")
    dates = re.findall(pattern, lines)
    body = re.split(pattern, lines)
    entries = []
    for date in dates:
        for b in body:
            if b:
                original_b = b
                b = b.replace('&nbsp;', ' ')
                b = b.replace('&quot;', '"')
                b = b.replace('&amp;', '&')
                entries.append((date.strip(), b.strip()))
                body.remove(original_b)
                break
    return entries


def main(filename):
    with open(filename, 'r') as fp:
        entries = entries_by_date(fp)
        for entry in entries:
            file, contents = entry
            file = file + '.txt'
            with open(file, 'w') as fw:
                fw.write(contents)


if __name__ == '__main__':
    main(sys.argv[1])
