import os
import shutil
from helper.constant.path import TMP_DIR


async def save_to_tmp(file):
    # Check if tmp dir exists
    os.makedirs(TMP_DIR, exist_ok=True)

    tmp_file_path = TMP_DIR / file.filename

    with open(tmp_file_path, "wb") as tmp_file:
        shutil.copyfileobj(file.file, tmp_file)

    relative_path = tmp_file_path.relative_to(TMP_DIR.parents[1])
    return relative_path
