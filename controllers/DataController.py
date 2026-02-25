from .BaseController import BaseController

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1024 * 1024

    def validate_uploaded_file(self, file: UploadFile):
        
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            raise False
        
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            raise False

        return True