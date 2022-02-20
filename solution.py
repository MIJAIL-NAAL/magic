# VERSION IV. File with magical methods

import os
import tempfile


class File:
    def __init__(self, file_name):
        self.file_name = file_name

        if not os.path.exists(self.file_name):
            open(self.file_name, 'w').close()


    def read(self):
        with open(self.file_name, "r") as f:
            return f.read()


    def write(self, text):
        with open(self.file_name, "w") as f:
            return f.write(text)


    def __str__(self):
        return self.file_name


    def __add__(self, other):
        if isinstance(self, File) and isinstance(other, File):
            obj_2 = other.read()
            obj_1 = self.read() + obj_2

            new_file = tempfile.mkstemp()
            new_obj = File(new_file[1])

            with open(new_file[1], 'w') as f:
                f.write(obj_1)

            return new_obj

        else:
            pass


    def __getitem__(self, index):
        with open(self.file_name, 'r') as f:
            lines = f.readlines()
            return lines[index]


