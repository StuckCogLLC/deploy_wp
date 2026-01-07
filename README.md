# deploy_wp

**deploy_wp** is a lightweight Python automation tool designed to simplify the deployment of WordPress instances on Linux servers running Apache. It automates the creation of system users, database credentials, Apache Virtual Hosts, and the WordPress core installation using `wp-cli`.

## Features

* **Automated Configuration**: Generates Apache Virtual Host files using Jinja2 templates.
* **Database Management**: Automatically creates MySQL/MariaDB databases and users.
* **User Isolation**: Sets up specific system users and handles file permissions for security.
* **Streamlined Input**: Requires only a DNS (Domain) and Username to execute; passwords and configs are generated automatically.

## Prerequisites

Ensure your server is running a Linux environment with the following dependencies installed:

* **Web Server**: Apache2
* **Database**: MySQL or MariaDB
* **WordPress CLI**: `wp-cli`
* **Python 3**:
    * `jinja2`
    * `pickle`

### Installing Python Dependencies
If you have Python 3 installed but lack the required libraries, you can install them via pip:

```bash
pip3 install jinja2
