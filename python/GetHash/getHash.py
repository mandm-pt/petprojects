import hashlib
import argparse

supported_hashes = ['md5', 'sha1', 'sha256', 'sha512', 'sha384']


def calculate_hash(input, hash_types=supported_hashes, compare_hash=None):
    for hash_type in hash_types:
        if hash_type == 'md5':
            hash_obj = hashlib.md5()
        elif hash_type == 'sha1':
            hash_obj = hashlib.sha1()
        elif hash_type == 'sha256':
            hash_obj = hashlib.sha256()
        elif hash_type == 'sha512':
            hash_obj = hashlib.sha512()
        elif hash_type == 'sha384':
            hash_obj = hashlib.sha384()

        hash_obj.update(input)
        current_hash = hash_obj.hexdigest()
        print('{} \t {}'.format(hash_type, current_hash))

        if compare_hash is not None:
            if compare_hash == current_hash:
                print('\x1b[6;30;42m' + 'Hash match!' + '\x1b[0m')
            else:
                print('\x1b[6;30;42m' + 'Hash do not match!' + '\x1b[0m')

parser = argparse.ArgumentParser(description='Calculate hash of a file or string.', add_help=True)

parser.add_argument('-f', '--file', help='the input file to calculate the hash')
parser.add_argument('-t', '--text', help='the input text to calculate the hash')
parser.add_argument('-ht', '--hash-type', help='the type of the hash to be calculated', choices=supported_hashes)
parser.add_argument('-c', '--compare', help='the hash to compare with')

args = parser.parse_args()

if args.file is not None:
    with open(args.file, "rb") as binary_file:
        data = binary_file.read()
elif args.text is not None:
    data = str.encode(args.text)
else:
    data = None

if data is not None:
    calculate_hash(data, compare_hash=args.compare)
else:
    parser.print_help()
