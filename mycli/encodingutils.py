# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import binascii
import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY2:
    text_type = unicode
    binary_type = str
else:
    text_type = str
    binary_type = bytes


def unicode2utf8(arg):
    """Convert strings to UTF8-encoded bytes.

    Only in Python 2. In Python 3 the args are expected as unicode.

    """

    if PY2 and isinstance(arg, text_type):
        return arg.encode('utf-8')
    return arg


def utf8tounicode(arg):
    """Convert UTF8-encoded bytes to strings.

    Only in Python 2. In Python 3 the errors are returned as strings.

    """

    if PY2 and isinstance(arg, binary_type):
        return arg.decode('utf-8')
    return arg


def bytes_to_string(b):
    """Convert bytes to a string. Hexlify bytes that can't be decoded.

    >>> print(bytes_to_string(b"\\xff"))
    0xff
    >>> print(bytes_to_string('abc'))
    abc
    >>> print(bytes_to_string('✌'))
    ✌

    """
    if isinstance(b, binary_type):
        try:
            return b.decode('utf8')
        except UnicodeDecodeError:
            return '0x' + binascii.hexlify(b).decode('ascii')
    return b
