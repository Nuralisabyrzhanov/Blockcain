import json
import os
import hashlib

bloks_dir = os.curdir + '/bloks/'

def get_files():
    files = os.listdir(bloks_dir)
    return sorted([int(i) for i in files])

def get_hash(filename):
    file = open(bloks_dir + filename , 'rb').read()
    return hashlib.md5(file).hexdigest()

def write_block(creditor, amout, borrower, prev_hash=''):
    files = get_files()
    last_file = files[-1]
    filename = str(last_file + 1)
    prev_hash = get_hash(str(last_file))
    data = {
            'creditor': creditor,
            'money': amout,
            'borrower':borrower,
            'hash': prev_hash
    }
    with open (bloks_dir + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def chek():
    files = get_files()
    result = []
    for file in files[1:]:
        f = open(bloks_dir + str(file))
        h = json.load(f)['hash']

        prev_hash = str(file - 1)
        actual_hash = get_hash(prev_hash)
        if h == actual_hash:
            res = 'ok'
        else:
            res = 'not'
        result.append(f'block {prev_hash} -- {res}')
    return result


if __name__=='__main__':
    # write_block('azamat',1590000,'riko')
    print(chek())