import subprocess
import os

def run_command(command, **kwargs):
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True, **kwargs)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result

try:
    print("Upgrading pip...")
    run_command('python3 -m pip install -U pip')

    print("Creating virtual environment...")
    run_command('python3 -m venv venv')

    venv_python = os.path.join('venv', 'bin', 'python')

    print("Installing Django in virtual environment...")
    run_command('{} -m pip install django'.format(venv_python))

    project_name = input("Please enter the name of the project: ")

    print("Creating Django project...")
    run_command('{} -m django startproject {}'.format(venv_python, project_name))

    print("Running Django development server...")
    run_command('{} {}/manage.py runserver'.format(venv_python, project_name))

except subprocess.CalledProcessError as e:
    print(f"An error occurred while running a command: {e}")
    print(e.stderr)
