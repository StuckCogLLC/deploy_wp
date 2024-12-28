#!/usr/bin/env python3

# imports
from ast import Num
from jinja2 import Environment, FileSystemLoader
import os.path
import getpass
import random,string

# local imports
from wordpress_handler import deploy_wordpress
from apache_conf import apache2_conf_creation, enable_site
from setup_user import build_user
from setup_db import create_wpdbuser


#vars
##get inputs
domainName = input('FQDN: ')
###domainName = 'example.com'
username = input('Username: ')
###username = 'example'
ldbpass = getpass.getpass(prompt='Local DB pass: ')
# vars
vhostDirectory = os.path.join('/var/www', username, domainName, 'public')

##ascii to vars
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
alpha = lower+upper+num
beta = lower+num
##random vars
ran1 = random.sample(alpha,10)
ran2 = random.sample(alpha,10)
ran3 = random.sample(alpha,10)
ran4 = random.sample(beta,10)
ran5 = random.sample(beta,10)
##random vars to strings
dbpass = ''.join(ran1)
wppass = ''.join(ran2)
userpass = ''.join(ran3)
dbname = ''.join(ran3)
dbuser = ''.join(ran5)

## Create user first
build_user(username, userpass)
## create vhost env
apache2_conf_creation(domainName, vhostDirectory)
## database creation
create_wpdbuser(dbuser,dbpass,dbname,ldbpass)
## handles wordpress
deploy_wordpress(vhostDirectory,dbname,dbuser,dbpass,domainName,username,wppass)
## enable site
enable_site(domainName)

print(f"WordPress either was or was not setup with the following \nuserpass: {userpass}\nwppass: {wppass}")