#!/usr/bin/python3.4
import sys
import subprocess

#command = 'docker system df -v'
command = 'dir'

try:
       keyword = sys.argv[1]
       command += ' | grep -E \'usage|VOLUMN|CONTAINER|' + keyword + '\''
except:
       pass

subprocess.call(command, shell=True)

#print("Hello world")
