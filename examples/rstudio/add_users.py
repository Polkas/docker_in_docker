import subprocess

# Read user-pw-list.txt and add users
with open('/etc/rstudio/user-pw-list.txt', 'r') as file:
    for line in file:
        user, passw = line.strip().split(':')
        subprocess.run(['useradd', '-m', user])
        subprocess.run(['chpasswd'], input=f'{user}:{passw}'.encode())
