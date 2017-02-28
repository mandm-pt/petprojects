# Title

Basic script that extracts the hash of a word file and lunches a dictionary attack using hashcat.
This isn't nothing more than just a wrapper on top of office2john script and hashcat.

# How to run the code

Just make sure you have python 2.7.13 installed (I haven't tested with other versions).
Make sure you have the colorama package.
You can install colorama via pip (Python Packaging Index)

```
pip install colorama
```

Moreover, make sure you download Hashcat and put the folder beside the script:
```
|-crackdocx.py
|-office2john.py
|-hashcat-3.30
	|-hashcat32.exe
	|-hashcat64.exe
	|-...
```

## Note

This code is just to academic purposes
I've changed 1 or 2 lines of code, of the original office2john script in order to get the value back.
if you really want to recover your lost password
check:
- office2john.py - https://github.com/magnumripper/JohnTheRipper/blob/unstable-jumbo/run/office2john.py
- hashcat - https://hashcat.net/forum/thread-1291.html


# Usage

```
usage: crackdocx.py [-h] [-f FILE] [-d DICTIONARY]

Calculate hash of a file or string.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  path for the file to crack
  -d DICTIONARY, --dictionary DICTIONARY
                        path for the dictionary file
```

# Example

```
C:\>python crackdocx.py -f "C:\my.docx" -d "C:\dictionary.dict"
```
