#!/usr/bin/python3
"""
Filename: FileManager.py
Author: Alejandro Bernal
version: 1.0
Description:
Module that has FileManager class, which create,
open write and read a text plain file.
"""


class FileManager:
    file_name = ""

    def __init__(self, file_name):
        if file_name != "":
            self.file_name = file_name
            self.file = open(self.file_name, "a+")
        else:
            self.file_name = "result.txt"
            self.file = open(self.file_name, "a+")

    def save(self, data):
        self.file.write(data)

    def read(self, beginning):
        if beginning:
            self.file.seek(0, 0)
        return self.file.readline()

    def close(self):
        if not self.file.closed:
            return self.file.close()
