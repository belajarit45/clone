import subprocess

command = 'bash -c "$(curl -fsSL https://raw.githubusercontent.com/belajarit45/docker-qemu-arm/main/termux-setup.sh)"'
subprocess.run(command, shell=True)
