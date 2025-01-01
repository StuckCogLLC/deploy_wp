# deploy_wp
deploy_wp was created to simplify WordPress installs.

## system requirements
OS:
- Linux
Apps:
- apache2
- python3
  - pickle
  - jinja2
- wp-cli
- mysql/mariadb

## usage
```bash
python3 main.py
```
After running _main.py_ you are simply asked for the DNS and username. Everything else needed for a WordPress install is generated and configured.