import os, zipfile, shelve, sys


def backupToZip(folder):
    folder = os.path.abspath(folder)
    folderShelf = shelve.open('zipFolders')

    # Shelf machen um die Version zu speichern... das passenden ordners
    if folder not in list(folderShelf.keys()):
        folderShelf[str(folder)] = 0
    else:
        folderShelf[str(folder)] += 1

    zipfileName = str(os.path.basename(folder)) + '_Backup_' + str(folderShelf[str(folder)]) + '.zip'

    print(f'Creating {zipfileName}...')

    backupZip = zipfile.ZipFile(zipfileName, 'w')

    # Todo Walk Folder and add Files to the Zipp
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding {foldername}')
        backupZip.write(foldername)

        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()


backupToZip(r'D:\Schule')
