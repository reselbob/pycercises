import os
import subprocess
import sys

os.system("date")
print("\n")
subprocess.call("pwd")

print("\n")
subprocess.call("ls")

print(sys.copyright)

print("\n")

print(sys.executable)

print("\n")


cmdping = "ping -c2 www.google.com"
p = subprocess.Popen(cmdping, shell=True, stderr=subprocess.PIPE)
while True:
    out = p.stderr.read(1)
    if out == '' and p.poll() != None:
        break
    if out != '':
        sys.stdout.write(out)
        sys.stdout.flush()