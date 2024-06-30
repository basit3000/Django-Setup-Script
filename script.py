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
    run_command('python -m pip install -U pip')

    print("Creating virtual environment...")
    run_command('python -m venv venv')
    venv_python = os.path.join('venv', 'Scripts', 'Activate' ,'python.exe')

    print("Installing Django in virtual environment...")
    run_command('{} -m pip install django'.format(venv_python))

    project_name = input("Please enter the name of the project. \n")

    print("Creating Django project...")
    run_command('{} -m django startproject {}'.format(venv_python, project_name))

    print("Running Django development server...")
    subprocess.run('{} {}/manage.py runserver'.format(venv_python, project_name), shell=True, check=True)

except subprocess.CalledProcessError as e:
    print(f"An error occurred while running a command: {e}")
    print(e.stderr)
