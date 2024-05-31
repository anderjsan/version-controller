from flask import Flask, jsonify
from updater.commit_updater import CommitUpdater

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/<string:project>/tag', methods=['POST'])
def new_version(project):
    updater = CommitUpdater(project)
    return jsonify(updater.new_version())

@app.route('/<string:project>/logs', methods=['GET'])
def get_logs(project):
    updater = CommitUpdater(project)
    return jsonify(updater.get_log())

@app.route('/<string:project>/logs/<string:tag>', methods=['GET'])
def get_log_by_id(project, tag):
    updater = CommitUpdater(project)
    return jsonify(updater.get_log(tag))

@app.route('/<string:project>/last', methods=['GET'])
def get_last_tag(project):
    updater = CommitUpdater(project)
    return jsonify(updater.get_last_tag())

@app.route('/<string:project>/logs/last', methods=['GET'])
def get_last_log(project):
    updater = CommitUpdater(project)
    return jsonify(updater.get_last_log())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4005, debug=True)