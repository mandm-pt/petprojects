import hashlib
import argparse
import os.path
from colorama import init, Fore
# init colorama
init()
supported_hashes = ['md5', 'sha1', 'sha256', 'sha512', 'sha3-256', 'sha3-512']


def calculate_hash(input, hash_types=supported_hashes, compare_hash=None):

    hash_types = supported_hashes if hash_types is None else [hash_types]

    for hash_type in hash_types:
        if hash_type == 'md5':
            hash_obj = hashlib.md5()
        elif hash_type == 'sha1':
            hash_obj = hashlib.sha1()
        elif hash_type == 'sha256':
            hash_obj = hashlib.sha256()
        elif hash_type == 'sha512':
            hash_obj = hashlib.sha512()
        elif hash_type == 'sha3-256':
            hash_obj = hashlib.sha3_256()
        elif hash_type == 'sha3-512':
            hash_obj = hashlib.sha3_512()

        hash_obj.update(input)
        current_hash = hash_obj.hexdigest()
        print((Fore.LIGHTMAGENTA_EX + '{}\t' + Fore.WHITE + '{}').format(hash_type, current_hash))

        if compare_hash is not None:
            if compare_hash == current_hash:
                print(Fore.LIGHTGREEN_EX + 'Hash match!')
            else:
                print(Fore.LIGHTRED_EX + 'Hash do not match!')


parser = argparse.ArgumentParser(description='Calculate hash of a file or string.', add_help=True)

group = parser.add_mutually_exclusive_group()
group.add_argument('-f', '--file', help='the input file to calculate the hash', default=None)
group.add_argument('-t', '--text', help='the input text to calculate the hash', default=None)
parser.add_argument('-ht', '--hash-type', help='the type of the hash to be calculated', choices=supported_hashes,
                    default=None)
parser.add_argument('-c', '--compare', help='the hash to compare with', default=None)

args = parser.parse_args()

data = None
if args.file is not None:
    if os.path.exists(args.file):
        with open(args.file, "rb") as binary_file:
            data = binary_file.read()
    else:
        print(Fore.LIGHTRED_EX + 'File not found!' + Fore.RESET)
elif args.text is not None:
    data = str.encode(args.text)

if data is not None:
    calculate_hash(data, hash_types=args.hash_type, compare_hash=args.compare)
else:
    parser.print_help()
