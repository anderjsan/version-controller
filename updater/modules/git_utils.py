import subprocess as sp
import tempfile
import os
from dotenv import load_dotenv
import shutil
import atexit

class GitUtils:
    def __init__(self, project=None):
        #
        load_dotenv()
        self.temp_dir = tempfile.mkdtemp()
        #
        self.project = project
        #
        self.repo_path = os.getenv("GIT_URL", "").replace("PROJECT", project) if project else os.getenv("GIT_URL", "")
        self.temp_path = f"{self.temp_dir}/{project}" if project else self.temp_dir

    def clone_repo(self):
        try:
            sp.run(["git", "clone", self.repo_path, self.temp_path])
        except Exception as e:
            print(f"Error cloning repository: {e}")
    
    def open_explorer(self):
        try:
            os.startfile(self.temp_dir)
        except Exception as e:
            print(f"Error opening file explorer: {e}")
    
    def get_git_messages(self):
        try:
            git_messages = sp.run(["git", "log", "--pretty=format:%s"], capture_output=True, text=True, encoding='utf-8', cwd=self.temp_path).stdout.splitlines()
            return git_messages
        except Exception as e:
            print(f"Error getting git messages: {e}")
            return []
    
    def get_git_last_message(self):
        try:
            last_message = sp.run(["git", "log", "-1", "--pretty=%B"], capture_output=True, text=True, encoding='utf-8', cwd=self.temp_path).stdout.strip()
            return last_message
        except Exception as e:
            print(f"Error getting last git message: {e}")
            return ""

    def clean_temp(self):
        try:
            atexit.register(lambda: shutil.rmtree(self.temp_dir, ignore_errors=True))
        except Exception as e:
            print(f"Error cleaning temporary directory: {e}")
    
    def run(self):
        print("")
        print("GitUtils module is running.")
        print("")
        print(f"Repository Path: {self.repo_path}")
        print("...")
        print(f"Temporary Path: {self.temp_path}")
        print("")
        print(f"Cloning repository: {self.temp_dir}")
        print("")
        self.clone_repo()
        print("...")
        print("Getting git messages:")
        print("...")
        for msg in self.get_git_messages():
            print(f"{msg}")
        print("...")
        print("Getting last git messages:")
        print("...")
        print(f"{self.get_git_last_message()}")



if __name__ == "__main__":

    project = "labdata"
    git_utils = GitUtils(project)
    git_utils.run()
    print("...")
    print("...")
    print("Done.")
    print("")