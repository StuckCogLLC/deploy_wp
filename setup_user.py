#!/usr/bin/env python3

# imports
import crypt
import subprocess

def build_user(username, password):
    # input
    
    homedir = "/var/www/" + username
    cryptpass = crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))

    # add user
    subprocess.run(["/usr/sbin/useradd", "-d", homedir, "-m", "-s", "/bin/bash", \
        "-G", "sshusers", "-p", cryptpass, username])