from updater.commit_updater.commit_updater import CommitUpdater

c = CommitUpdater("version-controller")
new_version = c.new_version()
print()
print(new_version)
print()
print(c.get_log())
print()
print(c.get_log('0.1.13'))
print()
print(c.get_last_tag())
print()
print(c.get_last_log())
print()