#!/usr/bin/env python3


###########################################
# This file creates the needed apache conf 
# file. The template directory contains a 
# jinja2 template file called apache.njk. 
# Changes made to the template file will be 
# reflected the next time this file is ran 
# against the domain in question.
############################################

# imports
from pickle import TRUE
from jinja2 import Environment, FileSystemLoader
import os.path
import subprocess

## create apache2 conf file for the domain
## and place in /etc/apache2/sites-available
## folder.

def apache2_conf_creation(domainName, vhostDirectory):
    """Create Apache2 configuration file for new domain
    
    Uses jinja2 templating to create a configuration file for
    apache2. This file called apache_conf.py and is located in the
    folder ~/templates.  
    """
    # construct apache conf file and path
    conffile = os.path.join("/etc/apache2/sites-available/", domainName + ".conf")
    # bool if the path exist
    boolconffile = os.path.exists(conffile)
    # create or replace apache conf
    if boolconffile:
        aconf = open(conffile, "w")
        print(domainName + ".conf existed and was overwritten.")
    else:
        aconf = open(conffile, "x")
        print(domainName + ".conf was created a new.")

    # load the template
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('apache.njk')
    # pass vars into template
    output = template.render(domainName=domainName, vhostDirectory=vhostDirectory)

    # write apache conf
    aconf.write(output)

    # close file
    aconf.close()

    # create hosting dir
    os.makedirs(vhostDirectory, exist_ok=True)

def enable_site(domainName):
    """Enable the newly created site
    
    Uses the a2ensite to enable the new created domain. This also
    reloads the apache configuration which will bring up the new
    site.
    """
    # enable the domain
    try:
        print(f"Enabling site")
        subprocess.run(
            [
                '/usr/sbin/a2ensite',
                domainName
            ],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    # reload apache
    try:
        print(f"Reloading Apache")
        subprocess.run(
            [
                '/bin/systemctl',
                'reload',
                'apache2'
            ],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")