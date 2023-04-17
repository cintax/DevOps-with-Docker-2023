#!/usr/bin/env python3

import os, sys, docker
from halo import Halo

print("NOTE: MAKE SURE YOU ADD YOUR DOCKER HUB CREDENTIALS")

if len(sys.argv) != 3:
    print(f'''
Run the script as `python3 script.py <github_repo> <dockerhub_repo>`
Ensure that both repositories are valid and public.
    ''')
    sys.exit()
else:
    print(f'''
The Github repository you are trying to clone is {sys.argv[1]}
The Docker Hub repository you are trying to push to is {sys.argv[2]}
    ''')
 
# PENDING: Add user input validator
    
sanitized_github_repo_name = sys.argv[1]
sanitized_dockerhub_repo_name = sys.argv[2]

github_repo_url = 'https://github.com/'+sanitized_github_repo_name

spinner = Halo(text='', spinner='dots')

spinner.text = 'Cloning'
with spinner:
    os.system("git clone -q {0}".format(github_repo_url))
    spinner.text = '✔ Cloned repository!' 
    spinner.stop_and_persist()
    
repo_name = sanitized_github_repo_name.split('/')[-1]

os.chdir("{0}/{1}".format(os.getcwd(),repo_name))

dockerfile = "{0}".format(os.getcwd())

tag = "{0}:latest".format(sanitized_dockerhub_repo_name)

client = docker.from_env() 
    
spinner.text = 'Logging into your Docker Hub'
with spinner:
    client.login(os.environ.get('DOCKER_USERNAME'), os.environ.get('DOCKER_PASSWORD'))
    spinner.text = '✔ Logged In!'
    spinner.stop_and_persist()

spinner.text='Building Docker image'
with spinner:
    image, build_logs = client.images.build(path=dockerfile, tag=tag)
    spinner.text= '✔ Built docker image!'
    spinner.stop_and_persist()

spinner.text='Push the Docker image to Docker Hub'
with spinner:
    client.images.push(repository=sanitized_dockerhub_repo_name, tag='latest')
    spinner.text = '✔ Pushed docker image to docker hub repository!'
    spinner.stop_and_persist()
