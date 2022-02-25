import json
import os
import hashlib

bloks_dir = os.curdir + '/bloks/'
def get_files():
    files = os.listdir(bloks_dir)
    list_files = sorted([int(i) for i in files])
    last_file = list_files[-1]
    filename = str(last_file + 1)
    print(type(filename), filename)


def get_hash():
    file = open('bloks/1', 'rb').read
    return    hashlib.md5(file).hexdigest()

def write_block(creditor, amout, borrower, prev_hash=''):
    files= get_hash()
    data = {
            'creditor': creditor,
            'money': amout,
            'borrower':borrower,
            'hash': file

}


with open ('bloks/1', 'w') as file:
    json.dump(file, indent=4, ensure_ascii=False)


if __name__=='__main__':

    write_block('Nur',159,'Argen')