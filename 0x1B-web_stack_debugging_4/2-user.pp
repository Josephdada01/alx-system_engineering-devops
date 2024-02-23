# 1-user_limit.pp

# Define the user 'holberton'
user { 'holberton':
  ensure => present,
  managehome => true,
}

# Set a password for the 'holberton' user (replace 'password' with the actual password)
# Note: It's not recommended to put the password directly in the manifest file. Use hiera or another external source for storing sensitive data.
user { 'holberton':
  password => '$6$/mlPlnzfiC4ZhzAp$eSQ.bwOqQw/UCnngeE5ZA5YvGlJvjOfzXdle/uJKvhcwCx4hBMFkaZ0l1MgRc972XYI4YH7poBLf3BIlqzOHQ1',
}

# Allow the 'holberton' user to login
file { '/etc/ssh/sshd_config':
  ensure => present,
  content => template('module_name/sshd_config.erb'), # You'll need to create this template file
  notify => Service['sshd'],
}

# Define the SSH service
service { 'sshd':
  ensure => running,
  enable => true,
}
