import subprocess
import argparse
import os.path
import office2john
import shlex
from colorama import init, Fore

# init colorama
init()

def invoke_hashcat(file, dictionary):
    exec_string = './hashcat-3.30/hashcat64.exe -w 3 -a 0 -m 9600 --status -o "{0}" "{1}" "{2}"'.format('result.txt', file, dictionary)

    args = shlex.split(exec_string)
    code = subprocess.call(args)
    print('Hashcat has finished, return code = {}'.format(code))

def create_hash_file(hash):
    hash_file = './hash.txt'
    with open(hash_file, 'w') as f:
        f.write(hash)
    return hash_file


def check_file(path):
    if not os.path.exists(path):
        print(Fore.LIGHTRED_EX + 'File not found!' + Fore.RESET)
        return False
    return True


def print_header():
    print(Fore.YELLOW + "this code is just to academic purposes")
    print("if you really want to recover your lost password")
    print("check:")
    print("     office2john.py - https://github.com/magnumripper/JohnTheRipper/blob/unstable-jumbo/run/office2john.py")
    print("     hashcat - https://hashcat.net/forum/thread-1291.html")


parser = argparse.ArgumentParser(description='Calculate hash of a file or string.', add_help=True)

parser.add_argument('-f', '--file', help='path for the file to crack', default=None)
parser.add_argument('-d', '--dictionary', help='path for the dictionary file', default=None)

args = parser.parse_args()

if args.file is None or args.dictionary is None:
    parser.print_help()
    exit()

is_valid = check_file(args.file)
is_valid &= check_file(args.dictionary)

if is_valid:
    print_header()
    hash = office2john.process_file(args.file)
    create_hash_file(hash)
    invoke_hashcat(args.file, args.dictionary)
else:
    parser.print_help()