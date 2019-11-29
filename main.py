import os
import shutil
from os import getcwd, chdir, mkdir
import sys

ARG_AVAILABLE = ['-b', '-r', '-bnr', '-h', '--help']
ARG_DOCS = {'-b': 'Backup',
            '-bnr': 'Backup and remove folder from source location',
            '-r': 'Restore data',
            '-h,--help': 'Show a list of command'}


'''
Function save:
This function is used to backup the user files
source = Which folder to backup
destination = Where to backup
delete = If you want to remove the source folder and keep only the backup folder
'''


def save(source, destination, delete):

    if os.path.exists(source):

        crypt = input('Would you crypt your data ? [y/n]\n')
        # We check if we need to crypt data
        if crypt == 'y':
            print('This feature is not actually developed')
        else:
            print('Won\'t crypt')

        source_path = source.replace('\\', '/')
        destination_name = source_path.split('/')
        destination_path = destination.replace('\\', '/')
        destination_path = destination_path + \
            destination_name[len(destination_name) - 1]

        # We check if user want to delete source folder after backup
        if not delete:
            print('### STARTING... ')
            try:
                shutil.copytree(source_path, destination_path)
                shutil.copystat(source_path, destination_path)
                print('### FILES SAVED ###')
                autosave = input('Would you auto save ' +
                                 destination_name[len(destination_name) - 1] + ' [y/n]\n')
                if autosave == 'y':
                    try:
                        folder_path = os.path.dirname(
                            os.path.abspath(__file__))
                        file_path = folder_path + '/dirToSave.txt'
                        dir_file = open(file_path, 'w')
                        dir_file.write(source_path + ';')
                        dir_file.close()
                    except IOError:
                        print('Error')
                        # The error need to be described
            except (IOError, os.error) as why:
                print(why)
        else:
            try:
                print("### STARTING...")
                shutil.move(source_path, destination_path,
                            copy_function='copytree')
                print('### FILES SAVED ###')
            except (IOError, os.error) as why:
                print(why)
    else:
        print('Folder does not exist!')


'''
Function restore:
This function is used to restore user data
source = folder to restore
destination = where to restore
delete = if you want to delete or not the old backup file
'''


def restore(source, destination, delete):
    if os.path.exists(source):

        crypt = input('Would you crypt your data ? [y/n]\n')
        # We check if we need to crypt data
        if crypt == 'y':
            print('This feature is not actually developed')
        else:
            print('Won\'t crypt')

        source_path = source.replace('\\', '/')
        destination_name = source_path.split('/')
        destination_path = destination.replace('\\', '/')
        destination_path = destination_path + \
            destination_name[len(destination_name) - 1]

        # We check if user want to delete source folder after backup
        print('### STARTING... ')
        try:
            shutil.copytree(source_path, destination_path)
            shutil.copystat(source_path, destination_path)
            print('### FILES SAVED ###')
        except (IOError, os.error) as why:
            print(why)
    else:
        print('Folder does not exist!')


for arg in sys.argv:
    if len(sys.argv) <= 1:
        print("\n")
        print(
            'Correct use of the script is: [-COMMANDS] [source-path] [destination-path]')
        print('\n COMMANDS:')
        for element in ARG_DOCS:
            print("     " + element + " : " + ARG_DOCS[element])
        print('\n')
    else:
        if arg in ARG_AVAILABLE:
            if arg == '-b':
                save(sys.argv[2], sys.argv[3], 0)
            elif arg == '-bnr':
                save(sys.argv[2], sys.argv[3], 1)
            elif arg == '-r':
                restore(sys.argv[2], sys.argv[3], 0)
            elif arg == '-h' or '--help':
                print('Show help')
            break
        elif arg == sys.argv[0]:
            continue
        else:
            print('Invalid command\n Here are good commands:')
            for element in ARG_DOCS:
                print("     " + element + " : " + ARG_DOCS[element])
            print('\n')
            break
