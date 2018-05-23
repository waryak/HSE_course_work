#!/usr/bin/env bash
sudo docker build -t registry.gitlab.com/wnm.development/my-awesome-project/nginx -f Dockerfile.nginx .
sudo docker push registry.gitlab.com/wnm.development/my-awesome-project/nginx
