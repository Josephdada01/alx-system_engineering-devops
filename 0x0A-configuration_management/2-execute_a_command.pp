# killing a proccess
exec { 'kill_killmenow_process':
  command     => 'pkill killmenow',
  refreshonly => true,
  onlyif      => 'pgrep -x killmenow',
  logoutput   => true,
  provider    => 'shell',
}

