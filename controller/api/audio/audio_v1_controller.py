from fastapi import APIRouter, File, UploadFile
from service.audio import save_audio_file

audio_router = APIRouter(prefix="/audio/user", tags=["Audio API"])


@audio_router.post("/{user_id}/phrase/{phrase_id}")
async def test_v1(user_id: int, phrase_id: int, file: UploadFile):
    file_path = await save_audio_file(file)
    return {"message": f"File saved at {file_path}"}
