#!/bin/bash

export PROJECT=$JOB_NAME
curl -X POST http://version-control:4005/$PROJECT/tag
export TAG=$(cat /var/jenkins_home/.version/$PROJECT/.version)
echo "Project: $PROJECT; Version: $TAG"