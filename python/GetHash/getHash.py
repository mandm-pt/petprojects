import hashlib
import sha3
import argparse


def calculate_hash(input, hash_types=['sha1', 'sha256', 'sha512', 'sha3']):
    for hash_type in hash_types:
        if hash_type == 'sha1':
            hash_obj = hashlib.sha1()
        elif hash_type == 'sha256':
            hash_obj = hashlib.sha256()
        elif hash_type == 'sha512':
            hash_obj = hashlib.sha512()
        elif hash_type == 'sha384':
            hash_obj = hashlib.sha384()
        elif hash_type == 'sha3':
            hash_obj = sha3.keccak_512()

        hash_obj.update(input)
        print('{} \t {}'.format(hash_type, hash_obj.hexdigest()))


parser = argparse.ArgumentParser(description='Calculate hash of a file or string.', add_help=True)

group = parser.add_argument_group('input_group')
group.add_argument('-f', '--file', help='the input file to calculate the hash')
group.add_argument('-t', '--text', help='the input text to calculate the hash')
parser.add_argument('-ht', '--hash-type', help='the type of the hash to be calculated')

args = parser.parse_args()

if args.file is not None:
    with open(args.file, "rb") as binary_file:
        data = binary_file.read()
elif args.text is not None:
    data = str.encode(args.text)

if data is not None:
    calculate_hash(data)
else:
    parser.print_help()
