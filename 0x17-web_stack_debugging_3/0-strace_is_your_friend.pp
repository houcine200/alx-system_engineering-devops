# Fix 500 Internal Server Error returned by the Apache server.
exec {'replace':
  command  => 'bin/sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
}
