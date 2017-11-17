#!/usr/bin/python
import subprocess
## command to run - tcp only ##
cmd = "mpc current"
 
## run it ##
p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
 
## But do not wait till netstat finish, start displaying output immediately ##
if True:
    out = p.stderr.read(1)
    
#print p
