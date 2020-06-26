#!/bin/python3

import os, sys
# take a text file and count requests from each host
file_path = 'test.txt'

# get column of hosts and make it into something you can iterate over
def open_file():
  """
  open file and append to list of list
  """
  with open(file_path, 'r') as f:
    text_as_lol = []
    for line in f:
      line_as_list = line.strip().split()
      text_as_lol.append(line_as_list)
  return text_as_lol

def list_host(): 
  """
  returns a list of all hosts
  """
  t = open_file()
  all_hosts = []
  for i in range(len(t)):
    all_hosts.append(t[i][0])
  return all_hosts

def count_and_print_host_count():
  """
  Count all hosts and print to screen
  """
  hosts = list_host()
  wd = {}
  for host in hosts:
    wd[host] = hosts.count(host)
  print('\n{:^8}{:^8}'.format('Host','Count'))

  for h in wd:
    print('{:^8}{:^8d}'.format(h,wd[h]))

def redirect_stdout():
  """
  redirects logs to records_hosts_access_log_00.txt
  """
  sys.stdout = open("records_hosts_access_log_00.txt", "w")
  count_and_print_host_count()
  sys.stdout.close()

redirect_stdout()

