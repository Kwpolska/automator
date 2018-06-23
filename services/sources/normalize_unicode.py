#!/usr/bin/env python2
import sys
import unicodedata
print unicodedata.normalize('NFC', sys.stdin.read().decode('utf-8')).encode('utf-8')