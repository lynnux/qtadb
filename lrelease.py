#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

lang_files = ("qtadb_ar", "qtadb_cs", "qtadb_de", "qtadb_el", "qtadb_en", "qtadb_es", "qtadb_hu", "qtadb_it", "qtadb_ja", "qtadb_nl", "qtadb_pl", "qtadb_pt", "qtadb_ru", "qtadb_sr", "qtadb_sv", "qtadb_zh")

def main():
    os.environ['PATH'] = os.environ['PATH'] + ';' + r"D:\Qt\Qt5.6.0\5.6\msvc2013\bin"
    for l in lang_files:
        os.system("lrelease languages\\"+ l +".ts")
    raw_input("...")

if __name__ == "__main__":
    try:
        main()
    except:
        import traceback
        traceback.print_exc()
        raw_input()
