from helper.utils.save_file import save_to_tmp


async def save_audio_file(file):
    tmp_file_path = await save_to_tmp(file)
    return tmp_file_path
