# Title

Basic script that calculates hashs of either file or text.

# Usage

```
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
```

# Examples

## calculate hash for text
```
C:\>python getHash.py -t "test123"
md5      cc03e747a6afbbcbf8be7668acfebee5
sha1     7288edd0fc3ffcbe93a0cf06e3568e28521687bc
sha256   ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae
sha512   daef4953b9783365cad6615223720506cc46c5167cd16ab500fa597aa08ff964eb24fb19687f34d7665f778fcb6c5358fc0a5b81e1662cf90f73a2671c53f991
sha3-256 3054762b0a8b31adfe79efb3bc7718624627cc99c7c8f39bfa591ce6854ac05d
sha3-512 61b976821ad4a7545054a2e45367e3af53522477d39b28fdca26b36fed95f8b1a2005e3188b682a74f9e772aa3cb7201fcb6d01ce6cb2cdf720690fd26d5bb1e
```
## compare hash of text
```
C:\>python getHash.py -t "test123" -c cc03e747a6afbbcbf8be7668acfebee5
OK md5      cc03e747a6afbbcbf8be7668acfebee5
XX sha1     7288edd0fc3ffcbe93a0cf06e3568e28521687bc
XX sha256   ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae
XX sha512   daef4953b9783365cad6615223720506cc46c5167cd16ab500fa597aa08ff964eb24fb19687f34d7665f778fcb6c5358fc0a5b81e1662cf90f73a2671c53f991
XX sha3-256 3054762b0a8b31adfe79efb3bc7718624627cc99c7c8f39bfa591ce6854ac05d
XX sha3-512 61b976821ad4a7545054a2e45367e3af53522477d39b28fdca26b36fed95f8b1a2005e3188b682a74f9e772aa3cb7201fcb6d01ce6cb2cdf720690fd26d5bb1e
```
