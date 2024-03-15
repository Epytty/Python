'''Найти суммарный размер всех файлов, находящихся в вашей папке,
воспользовавшись функциями os.path.getsize() и os.listdir().'''

import os

folder_path = 'C:/Users/Admin/OneDrive'

total_size = 0

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        total_size += os.path.getsize(file_path)

print(f'Суммарный размер всех файлов в папке {folder_path}: {total_size} байт')