import os
import time
import zipfile

def backup_to_zip(folder_path):
    target_dir = 'E:\Programs\IntelliJIDEA\Projects\pr_4_ipo'
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    today = time.strftime('%Y%m%d')
    now = time.strftime('%H%M%S')
    target = os.path.join(target_dir, today + '_' + now + '.zip')
    with zipfile.ZipFile(target, 'w') as zip_file:
        for foldername, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                zip_file.write(file_path, os.path.relpath(file_path, folder_path), compress_type=zipfile.ZIP_DEFLATED)

    print(f'Архив {target} создан успешно.')

backup_to_zip('E:\Programs\IntelliJIDEA\Projects\pr_4_ipo')