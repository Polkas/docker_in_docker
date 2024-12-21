import subprocess

# Read user-pw-list.txt and add users
with open('/etc/rstudio/user-pw-list.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        user, passw = line.split(':')
        subprocess.run(['useradd', '-m', user])
        subprocess.run(['chpasswd'], input=f'{user}:{passw}'.encode())
