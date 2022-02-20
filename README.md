# File with magic methods

### The interface provides the following features for working with files:

- Reading from a file
- Writing to a file
- The addition of objects type File, the result of the addition is an object of the File class, while creating a new file and a file object in which the contents of the second file are added to the contents of the first file.
- Return the full path to the file as a string representation of an object of the File class
- Support the iteration protocol, and the iteration goes through the lines of the file

<br>

When creating an instance of the File class, the full path to the file on the file system is passed to the constructor. If a file with this path does not exist, it must be created
during initialization.

Example of work:

```python
>>> import os.path
>>> from solution import File
>>> path_to_file = 'some_filename'
>>> os.path.exists(path_to_file)
False
>>> file_obj = File(path_to_file)
>>> os.path.exists(path_to_file)
True
>>> print(file_obj)
some_filename
>>> file_obj.read()
''
>>> file_obj.write('some text')
9
>>> file_obj.read()
'some text'
>>> file_obj.write('other text')
10
>>> file_obj.read()
'other text'
>>> file_obj_1 = File(path_to_file + '_1')
>>> file_obj_2 = File(path_to_file + '_2')
>>> file_obj_1.write('line 1\n')
7
>>> file_obj_2.write('line 2\n')
7
>>> new_file_obj = file_obj_1 + file_obj_2
>>> isinstance(new_file_obj, File)
True
>>> print(new_file_obj)
C:\Users\Media\AppData\Local\Temp\71b9e7b695f64d85a7488f07f2bc051c
>>> for line in new_file_obj:
....    print(ascii(line))  
'line 1\n'
'line 2\n'
>>> new_path_to_file = str(new_file_obj)
>>> os.path.exists(new_path_to_file)
True
>>> file_obj_3 = File(new_path_to_file)
>>> print(file_obj_3)
C:\Users\Media\AppData\Local\Temp\71b9e7b695f64d85a7488f07f2bc051c
>>>
```
