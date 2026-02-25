from .BaseController import BaseController
from helpers.config import Settings
import os

class ProjectController(BaseController):
    def __init__(self): # حذفنا app_settings لأن BaseController يستدعيها تلقائياً
        super().__init__()
        
    def get_project_path(self, project_id: str):
        # تصحيح اسم المتغير من files_dir إلى file_dir
        project_dir = os.path.join(
            self.file_dir, 
            project_id
        )

        if not os.path.exists(project_dir):
            os.makedirs(project_dir)

        return project_dir