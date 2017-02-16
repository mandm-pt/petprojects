# Title

Basic script that calculates hashs of either file or text.

# Usage

  usage: getHash.py [-h] [-f FILE | -t TEXT]
                    [-ht {md5,sha1,sha256,sha512,sha3-256,sha3-512}]
                    [-c COMPARE]

  Calculate hash of a file or string.

  optional arguments:
    -h, --help            show this help message and exit
    -f FILE, --file FILE  the input file to calculate the hash
    -t TEXT, --text TEXT  the input text to calculate the hash
    -ht {md5,sha1,sha256,sha512,sha3-256,sha3-512}, --hash-type {md5,sha1,sha256,sha512,sha3-256,sha3-512}
                          the type of the hash to be calculated
    -c COMPARE, --compare COMPARE
                          the hash to compare with
