import subprocess as sp
import tempfile
import shutil
import atexit

class GitUtils:
    def __init__(self):
        self.repo_path = ""
        self.temp_path = ""
        

    def clone_repository(self, project):
        try:
            temp_dir = tempfile.mkdtemp()
            self.repo_path = f"https://github.com/anderjsan/{project}.git"
            self.temp_path = f"{temp_dir}/{project}"
            
            sp.run(["git", "clone", self.repo_path, self.temp_path], stderr=sp.DEVNULL, stdout=sp.DEVNULL)
            
        except Exception as e:
            print(f"Erro ao clonar repositório: {e}")
            raise
        finally:
            atexit.register(lambda: shutil.rmtree(temp_dir, ignore_errors=True))
    
    def get_last_commit_message(self):
        try:
            commit_message = sp.run(["git", "log", "-1", "--pretty=%B"], capture_output=True, text=True, encoding='utf-8', cwd=self.temp_path).stdout.strip()
            return commit_message
        except Exception as e:
            print(f"Erro ao obter a mensagem do último commit: {e}")
            raise
