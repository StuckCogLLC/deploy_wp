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

## wp-config.php file
create template for wp-config.php file

## mariadb
setup database for Wordpress.
- create database
- create database user
- setup wordpress tables
