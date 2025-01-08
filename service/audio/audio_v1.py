from helper.utils.save_file import save_to_tmp, download_tmp_file


async def save_audio_file(file):
    tmp_file_path = await save_to_tmp(file)
    return tmp_file_path


async def download_audio_file(file_name):
    tmp_file_path = await download_tmp_file(file_name)
    return tmp_file_path
