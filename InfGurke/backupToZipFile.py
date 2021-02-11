#macht das file nicht wirklich kleiner --- kompremiert es nicht????
import shelve, pyinputplus as pyip, os, shutil
from zipfile import ZipFile

path = pyip.inputFilepath('Filepath? ')
pathShelf = shelve.open((str(path) + 'Shelf'))
pathShelf['path'] = path
print(pathShelf['path'])

if 'version' not in list(pathShelf.keys()):
    pathShelf['version'] = 0
else:
    pathShelf['version'] += 1

name = path.split('\\')[-1] + '_BackupVersion_' + str(pathShelf['version'])
docname = name
name = ''.join(path.split('\\')[:-1]) +'\\' + name + '.zip'
print('working')
with ZipFile(name, 'w') as zipObj:
    # Iterate over all the files in directory
    for folderName, subfolders, filenames in os.walk(pathShelf['path']):
        for filename in filenames:
            print(filename)
            # create complete filepath of file in directory
            filePath = os.path.join(folderName, filename)
            # Add file to zip
            zipObj.write(filePath)

print(docname)
print('Done')
pathShelf.close()
