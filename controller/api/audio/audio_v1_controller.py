from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse
from service.audio import save_audio_file, download_audio_file

audio_router = APIRouter(prefix="/audio/user", tags=["Audio API"])


@audio_router.post("/{user_id}/phrase/{phrase_id}")
async def upload_audio_v1(user_id: int, phrase_id: int, file: UploadFile):
    file_path = await save_audio_file(file)
    return {"message": f"File saved at {file_path}"}


@audio_router.get("/{user_id}/phrase/{phrase_id}/{audio_format}")
async def download_audio_v1(user_id: int, phrase_id: int, audio_format: str):
    audio_file_path = await download_audio_file(f"{user_id}.{audio_format}")

    if audio_file_path is None:
        return {"Message": "File doesn't exists"}

    return FileResponse(
        audio_file_path, media_type="audio/mpeg", filename=f"{user_id}.{audio_format}"
    )
