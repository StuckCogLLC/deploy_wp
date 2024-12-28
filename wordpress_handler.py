#!/usr/bin/env python3
###########
# Wordpress Handler
###########

# imports
import subprocess
import os

#download wordpress
def download(vhostDirectory):
    print(download)
    os.chdir(vhostDirectory)
    try:
        subprocess.run(
            [
                'wp',
                'core',
                'download',
                '--allow-root'
            ],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

#create wp-config.php
def create_config(vhostDirectory,dbname,dbuser,dbpass):
    print(create_config)
    os.chdir(vhostDirectory)
    try:
        print("Create wp-config.php")
        subprocess.run(
            [
                'wp',
                'config',
                'create',
                '--dbname='+dbname,
                '--dbuser='+dbuser,
                '--dbpass='+dbpass,
                '--allow-root'
            ],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

#install wordpress
def install_wordpress(vhostDirectory,domainName,username,wppass):
    os.chdir(vhostDirectory)
    url = "--url="+domainName
    title = "--title="+domainName
    admin = "--admin_user="+username
    adminpass = "--admin_password="+wppass
    adminemail = "--admin_email=info@stuckcog.com"
    try:
        print("install wordpress")
        subprocess.run(
            [
                'wp',
                'core',
                'install',
                url,
                title,
                admin,
                adminpass,
                adminemail,
                '--allow-root'
            ]
        )
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

#run
def deploy_wordpress(vhostDirectory,dbname,dbuser,dbpass,domainName,username,wppass):
    download(vhostDirectory)
    create_config(vhostDirectory,dbname,dbuser,dbpass)
    install_wordpress(vhostDirectory,domainName,username,wppass)