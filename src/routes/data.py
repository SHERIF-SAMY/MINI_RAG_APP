from fastapi import APIRouter, Depends, UploadFile, status
# from models import ResponseSignal
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController
from models import ResponseEnums 
import aiofiles
import os

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1","data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id : str, file : UploadFile,
                      app_settings : Settings = Depends(get_settings)):
    
    data_controller = DataController(app_settings)
    # 1. التحقق من الملف
    is_valid = data_controller.validate_uploaded_file(file)
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": ResponseEnums.FILE_TYPE_NOT_SUPPORTED.value}
        )

    # 2. الحصول على مسار المشروع (قبل الـ return)
    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path, file_id = data_controller.generate_unique_filepath(
        orig_file_name=file.filename,
        project_id=project_id
    )

    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:

        logger.error(f"Error while uploading file: {e}")

        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": ResponseEnums.FILE_TYPE_NOT_SUPPORTED.value
            }
        )
        

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": ResponseEnums.FILE_UPLOAD_SUCCESS.value,
            "project_id": project_id,
            "file_id": file_id,
            "file_name": file.filename,
            "file_size": file.size,
            "file_content_type": file.content_type,
            "path": project_dir_path # أضفناه للتأكد من نجاح العملية
        }
    )