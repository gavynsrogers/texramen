#!/usr/bin/env python3
import random
import os
import re
import shlex

# Universal constant referenced further on, this is a list of every character
# considered "valid"
valid_chars = list('1234567890abcdefghijklmnopqrstuvwxyz' +
                   'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

print('''\

            Welcome To:

 (     '           *             )
 )\ )    (      (  `         ( /(
(()/(    )\     )\))(   (    )\())
 /(_))((((_)(  ((_)()\  )\  ((_) |
(_))   )\ _ )\ (_()((_)((_)  _((_)
| _ \  (_)_\(_)|  \/  || __|| \| |
|   /   / _ \  | |\/| || _| | .` |
|_|_\  /_/ \_\ |_|  |_||___||_|\_|

        RAndoM ENcryption\n\n''')

print('DISCLAIMER: RAMEN IS NOT TRUE CRYPTOGRAPHY.\n \
It is human proof, not computer proof.')

# Generate a string of x random characters


def rand_str(x):
    randstr = ''.join(random.choice(valid_chars) for n in range(x))
    return randstr

# GIGANTIC CAUTION SIGN BECAUSE OF THE NATURE OF THE PROGRAM


def caution():
    print('''
*=================================================================*
|/  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  / |
|  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  |
| /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /|
|/  /  /  /  /  /  /  /  C A U T I O N ! ! !  /  /  /  /  /  /  / |
|  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  |
| /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /|
|/  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  / |
*=================================================================*''')
    return True

# Determine if user wishes to encrypt or decrypt their text file
print('Would you like to encrypt or decrypt a text file? (e/d)')
e_or_d = ''
while True:
    e_or_d = input(': ')
    if e_or_d.lower() in 'ed':
        break
print('The path to your file can be relative to the RAMEN directory.')
# Proceed with encryption
if e_or_d == 'e':
    print('Please note that any formatting will not be kept in this version.')
    file_loc = ''
    # The code is much nicer if the output files don't have a file extension.
    while True:
        print('What is the location of the textfile that you wish to encrypt? \
\nIts file extension must be empty, though you may add one later if you wish.')
        file_loc = input(': ')
        does_file_exist = os.path.isfile(file_loc)
        if '.' not in file_loc and does_file_exist is True:
            break
        else:
            print('Please reenter, the file location you gave does not exist.')
    os.system('touch {0}_temp && touch {0}_meta'.format(shlex.quote(file_loc)))
    temp = ''
    with open(file_loc, 'r') as f:
        temp = f.read().replace('\n', '')
    temp_list = re.findall(r"[\w']+|[.,!?;:]", temp)
    # Open file_loc_temp and file_loc_meta
    with open(file_loc + '_temp', 'a') as f, \
            open(file_loc + '_meta', 'a') as f2:
        for idx, word in enumerate(temp_list):
            word_list = list(word)
            # Adds a random string in between every character in file.
            # This makes the output text indecipherable without the meta file.
            for char in word_list:
                rand_str_loop = rand_str(random.randint(5, 20))
                f.write('{}{}'.format(char, rand_str_loop))
                f2.write('{}\n'.format(rand_str_loop))
            f.write('r4M#')
    os.system('rm {0} && mv {0}_temp {0}'.format(file_loc))
    print('\nEncryption complete at {}'.format(file_loc) +
          '\n\nThank you for using RAMEN.\n')
    caution()
    print('If you lose your _meta file, you will NOT be able to recover\n \
your data! I, the creator, am not responsible for this.\n')
    print('Also, please do not change the formatting of either file. I \
cannot\n guarantee the decryption process will work if you do.')

# Proceed with decryption
else:
    caution()
    print('IT IS RECOMMENDED YOU BACK UP YOUR FILES BEFORE DOING THIS!!!\n \
IN THE EVENT THERE IS AN ERROR, YOUR DATA WILL BECOME UNREADABLE.\n \
PROCEED WITH CAUTION.')
    # Learn the location of the file to be decrypted
    file_loc = ''
    while True:
        print('What is the location of the text file that you wish to \
decrypt? \n(This software isn\'t magic. It requires the RAMEN meta file.)')
        file_loc = input(': ')
        does_file_exist = os.path.isfile(file_loc)
        if does_file_exist is True:
            break
        else:
            print('Please reenter, the file location you gave does not exist.')
    # Learn the location of the meta file
    meta_loc = ''
    is_meta_same_format = input('Is the meta file location the same as the \
first one & \"_meta\"? (y/n) :')
    if is_meta_same_format in 'Yy':
        meta_loc = file_loc + '_meta'
    else:
        while True:
            print('What is the location of the meta file?\n \
(It should simply be \"folder/file_meta\")')
            meta_loc = input(': ')
            does_file_exist = os.path.isfile(meta_loc)
            if does_file_exist is True \
               and meta_loc.endswith('_meta'):
                break
            else:
                print('Please re-enter, the file location you gave does not \
exist or is not a _meta file.\n \
If you do not have the _meta file, your data is lost.')
    os.system('touch {}_temp'.format(file_loc))
    data = ''
    meta = ''
    # Read the file and meta file in the user-given location.
    with open(file_loc, 'r') as f, \
            open(file_loc + '_temp', 'a') as f_t, \
            open(meta_loc, 'r') as m:
        data = f.read().split('r4M#')
        meta = m.read().splitlines()
        # This works by comparing the values in the meta file with how the
        # data starts. If the data starts with a value in the meta file, it
        # erases that random string and then writes the next letter to the
        # output file.
        for idx, word in enumerate(data):
            try:
                if idx == 0:
                    f_t.write(list(word)[0])
                else:
                    f_t.write(' {}'.format(list(word)[0]))
            except:
                pass
            word = word[1:]
            try:
                for line in meta:
                    if word.startswith(line):
                        word = word[len(line):]
                        f_t.write(list(word)[0])
                        word = word[1:]
            except IndexError:
                pass
    os.system('rm {0} && rm {1} && mv {0}_temp {0}'.format(
        shlex.quote(file_loc), shlex.quote(meta_loc)))

    print('Your file: {} has been decrypted and the original meta file has \
been removed.\n'.format(file_loc) +
          'Thanks for using RAMEN.')
