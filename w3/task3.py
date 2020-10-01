import shutil
import os


shutil.unpack_archive('main.zip', './', 'zip')
dirs_list = []
for root, subfolders, files in os.walk('./main'):
    for filename in files:
        if filename.endswith('.py'):
            dirs_list.append(root)

with open('answer_task3.txt', 'w') as ouf:
    answer = '\n'.join(sorted(dirs_list))
    ouf.write(answer)

