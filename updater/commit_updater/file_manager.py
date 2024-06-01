import os
import json

class FileManager():
    def __init__(self, project):
        self.project = project
        self.project_dir = f".version/{project}"
        self.version_path = os.path.join(self.project_dir, ".version")
        self.log_path = os.path.join(self.project_dir, ".version_log")
        self._create_directories()
    
    def _create_directories(self):
        os.makedirs(self.project_dir, exist_ok=True)
    
    def read_last_version(self, project):
        try:
            with open(self.version_path, "r") as f:
                if not f.read():
                    return "0.0.0"
                f.seek(0)
                return f.readline().strip()
        except FileNotFoundError:
            with open(self.version_path, "w") as f:
                f.write("0.0.0")
            return "0.0.0"
        except Exception as e:
            print(f"Error in read_last_version: {e}")
        
    def write_new_version(self, new_version):
        try:
            with open(self.version_path, "w") as f:
                f.write(new_version)
            self.version = new_version
        except Exception as e:
            print(f"Error in write_new_version: {e}")
    
    def read_commit_logs(self):
        try:
            with open(self.log_path, "r", encoding='utf-8') as json_file:
                if not json_file.read(1):
                    return []
                json_file.seek(0)
                return json.load(json_file)
        except FileNotFoundError:
            with open(self.log_path, "w") as f:
                json.dump([], f)
            return []
        except Exception as e:
            print(f"Error in read_commit_logs: {e}")
    
    def write_commit_logs(self, logs):
        try:
            for log in logs:
                if "fixes" in log:
                    log["fixes"] = sorted(log["fixes"], key=lambda x: x["date"], reverse=True)
                    
            sorted_logs = sorted(logs, key=lambda x: x["date"], reverse=True)

            with open(self.log_path, "w") as json_file:
                json.dump(sorted_logs, json_file, indent=4)
        except Exception as e:
            print(f"Error in write_commit_logs: {e}")
            print()

            with open(self.log_path, "w") as json_file:
                json.dump(sorted_logs, json_file, indent=4)
        except Exception as e:
            print(f"Error in write_commit_logs: {e}")
            print