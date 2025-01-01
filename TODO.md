# To Do List

## .htaccess file
standard .htaccess file to copy into ~/public dir
code: 
```
      # BEGIN WordPress
      # The directives (lines) between "BEGIN WordPress" and "END WordPress" are
      # dynamically generated, and should only be modified via WordPress filters.
      # Any changes to the directives between these markers will be overwritten.
      <IfModule mod_rewrite.c>
              RewriteEngine On
              RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
              RewriteBase /
              RewriteRule ^index\.php$ - [L]
              RewriteCond %{REQUEST_FILENAME} !-f
              RewriteCond %{REQUEST_FILENAME} !-d
              RewriteRule . /index.php [L]
      </IfModule>
      <IfModule mod_authz_core.c>
        <FilesMatch "wp-config.php">
          Require all denied
        </FilesMatch>
      </IfModule>

      # END WordPress
```

## file permissions
Need to set file permissions on /var/www/<username>/<dns>/public directory. This will allow for WP to have automatic updates, install themes and plugins without the need for FTP creds. Ownership needs to be granted to the apache2 service account (www-data) and permission set to 0775.

commands:
chown -R www-data:www-data /var/www/<username>/<dns>/public
chmod -r 0775 /var/www/<username>/<dns>/public