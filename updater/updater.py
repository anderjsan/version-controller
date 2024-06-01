from flask import Flask, jsonify
from updater.commit_updater.commit_updater import CommitUpdater

class Updater:
    def __init__(self, app):
        self.app = app
        self.add_routes()

    def add_routes(self):
        @self.app.route('/')
        def index():
            return 'Hello World!'
    
        @self.app.route('/<string:project>/tag', methods=['POST'])
        def new_version(project):
            updater = CommitUpdater(project)
            return jsonify(updater.new_version())

        @self.app.route('/<string:project>/logs', methods=['GET'])
        def get_logs(project):
            updater = CommitUpdater(project)
            return jsonify(updater.get_log())

        @self.app.route('/<string:project>/logs/<string:tag>', methods=['GET'])
        def get_log_by_id(project, tag):
            updater = CommitUpdater(project)
            return jsonify(updater.get_log(tag))

        @self.app.route('/<string:project>/last', methods=['GET'])
        def get_last_tag(project):
            updater = CommitUpdater(project)
            return jsonify(updater.get_last_tag())

        @self.app.route('/<string:project>/logs/last', methods=['GET'])
        def get_last_log(project):
            updater = CommitUpdater(project)
            return jsonify(updater.get_last_log())
        
    def run(self, host='0.0.0.0', port=4005, debug=True):
        self.app.run(host=host, port=port, debug=debug)
