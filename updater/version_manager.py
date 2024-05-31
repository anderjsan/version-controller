class VersionManager():
    def __init__(self, commit_keywords):
        self.commit_keywords = commit_keywords
        self.version_terms = [0,0,0]
        self.keyword = ""

    def set_version_terms(self, commit_message):
        try:
            for keyword, index in self.commit_keywords.items():
                if keyword in commit_message:
                    self.keyword = keyword
                    self.version_terms[index] += 1
                    break
        except Exception as e:
            print(f"Error in update_version_terms: {e}")
            raise
    
    def calculate_new_version(self, last_version):
        try:
            new_version = last_version[:]
            if self.version_terms[0] > 0:
                new_version[0] = str(int(new_version[0]) + self.version_terms[0])
                new_version[1] = '0'
                new_version[2] = '0'
            elif self.version_terms[1] > 0:
                new_version[1] = str(int(new_version[1]) + self.version_terms[1])
                new_version[2] = '0'
            elif self.version_terms[2] > 0:
                new_version[2] = str(int(new_version[2]) + self.version_terms[2])
            return new_version

        except Exception as e:
            print(f"Error in calculate_new_version: {e}")