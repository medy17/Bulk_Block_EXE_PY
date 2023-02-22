import os
import subprocess

print('Note: This program needs admin privileges to run properly\n\n')
directory = input('Enter the directory to scan for executable files: ')

while True:
    scan_subfolders = input('Scan subfolders too? (y/n): ').lower()
    if scan_subfolders == 'y':
        scan_subfolders = True
        break
    elif scan_subfolders == 'n':
        scan_subfolders = False
        break
    else:
        print('Invalid input. Please enter "y" or "n".')

os.chdir(directory)

exe_files = []
if scan_subfolders:
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.exe'):
                exe_files.append(os.path.join(root, file))
else:
    for file in os.listdir('.'):
        if file.endswith('.exe'):
            exe_files.append(file)

for exe_file in exe_files:
    rule_name = f'Blocked: {exe_file}'
    command = f'netsh advfirewall firewall add rule name="{rule_name}" dir=out program="{exe_file}" action=block'
    subprocess.run(command, shell=True)
    command = f'netsh advfirewall firewall add rule name="{rule_name}" dir=in program="{exe_file}" action=block'
    subprocess.run(command, shell=True)

input('Press Enter to exit...')
