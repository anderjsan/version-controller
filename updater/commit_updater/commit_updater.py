from .git_utils import GitUtils
from .version_manager import VersionManager
from .file_manager import FileManager
import datetime

class CommitUpdater():
    def __init__(self, project):
        self._commit_keywords = {
            "[RELEASE]": 0,
            "[FEATURE]": 1,
            "[INIT]": 1,
            "[FIX]": 2
        }
        self._project = project
        self._version_manager = VersionManager(self._commit_keywords)
        self._file_manager = FileManager(project)
        self._last_tag = [0,0,0]
        self._commit_message = ""
    
    def _set_version_terms(self):
        try:
            git = GitUtils()
            git.clone_repository(self._project)

            self._commit_message = git.get_last_commit_message()
            self._version_manager.set_version_terms(self._commit_message)
            
        except Exception as e:
            print(f"Erro ao clonar repositório: {e}")
            raise
        
    def _log_version(self, new_version):
        commit_logs = self._file_manager.read_commit_logs()
        
        if self._version_manager.keyword == "[FIX]":
            commit_log = {
            "tag": new_version,
            "git_message": self._commit_message,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
            for commit in reversed(commit_logs):
                if commit["tag"].split(".")[:2] == new_version.split(".")[:2]:
                    commit["fixes"].append(commit_log)
                    break
        else:
            commit_log = {
                    "tag": new_version,
                    "git_message": self._commit_message,
                    "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "fixes": []
                }
            commit_logs.append(commit_log)
        self._file_manager.write_commit_logs(commit_logs)
    
    def _filter_logs_by_tag(self, commit_logs, tag):
        log_return = []
        if tag.split(".")[-1] == "0":
            log_return = [commit for commit in commit_logs if commit["tag"] == tag]
        else:
            base_tag = ".".join(tag.split(".")[:2]) + ".0"
            for commit in commit_logs:
                if commit["tag"] == base_tag:
                    fixes = [fix for fix in commit.get("fixes", []) if fix["tag"] == tag]
                    if fixes:
                        commit_copy = {"fixes": fixes, "git_message": commit["git_message"], "tag": commit["tag"]}
                        log_return.append(commit_copy)
        return log_return
    
    def new_version(self):
        self._set_version_terms()
        last_version = self._file_manager.read_last_version().split(".")
        new_version = self._version_manager.calculate_new_version(last_version)
        new_version_str = ".".join(new_version)
        self._file_manager.write_new_version(new_version_str)
        self._log_version(new_version_str)
        return new_version_str

    def get_last_tag(self):
        return self._file_manager.read_last_version()

    def get_log(self, tag=None):
        try:
            commit_logs = self._file_manager.read_commit_logs()
            if not tag:
                return commit_logs
            return self._filter_logs_by_tag(commit_logs, tag)
        except Exception as e:
            print(f"Erro em get_log: {e}")
            raise

    def get_last_log(self):
        last_tag = self.get_last_tag()
        return self.get_log(last_tag)