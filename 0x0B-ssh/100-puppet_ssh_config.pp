#Your SSH client configuration must be configured to use the private key ~/.ssh/school
#Your SSH client configuration must be configured to refuse to authenticate using a password

file { "/etc/ssh/ssh_config":
  ensure  => file,
  content => "IdentityFile ~/.ssh/school\nPasswordAuthentication no\n",
  mode    => '0600'
}