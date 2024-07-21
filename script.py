import os
import subprocess
import json
from halo import Halo
import time

def create_backend_setup(user_directory_path):
    api_directory = os.path.join(user_directory_path, "api")
    
    directories = [
        os.path.join(api_directory, "src"),
        os.path.join(api_directory, "src", "config"),
        os.path.join(api_directory, "src", "routes"),
        os.path.join(api_directory, "src", "models"),
        os.path.join(api_directory, "src", "controllers")
    ]
    
    files = [
        os.path.join(api_directory, "server.js"),
        os.path.join(api_directory, ".env"),
        os.path.join(api_directory, ".gitignore")
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        
    for file in files:
        with open(file, 'w') as f:
            f.write("")
        
    spinner = Halo(text='Initializing project...', spinner='dots')
    spinner.start()
    try:
        # Note: You may need to update the path to the npm executable to match the location on your machine.
        subprocess.run([r'C:\Program Files\nodejs\npm.cmd', 'init', '-y'], cwd=api_directory, check=True, text=True, capture_output=True)
        spinner.succeed('Project initialized successfully!')
    except subprocess.CalledProcessError as e:
        spinner.fail(f"An error occurred while running 'npm init -y': {e}")
        return
    
    spinner.text = 'Installing dev dependency supervisor...'
    spinner.start()
    try:
        # Note: You may need to update the path to the npm executable to match the location on your machine.
        subprocess.run([r'C:\Program Files\nodejs\npm.cmd', 'install', '--save-dev', 'supervisor'], cwd=api_directory, check=True, text=True, capture_output=True)
        spinner.succeed('Supervisor installed successfully!')
    except subprocess.CalledProcessError as e:
        spinner.fail(f"An error occurred while installing supervisor: {e}")
        return

    spinner.text = 'Installing packages...'
    spinner.start()
    packages = ["express", "mongoose", "dotenv", "cors"]
    for package in packages:
        try:
            # Note: You may need to update the path to the npm executable to match the location on your machine.
            subprocess.run([r'C:\Program Files\nodejs\npm.cmd', 'install', package], cwd=api_directory, check=True, text=True, capture_output=True)
            spinner.text = f'{package} Installation done...'
            time.sleep(1)
        except subprocess.CalledProcessError as e:
            spinner.fail(f"An error occurred while installing {package}: {e}")
            return
    
    package_json_path = os.path.join(api_directory, 'package.json')
    try:
        with open(package_json_path, 'r') as f:
            package_data = json.load(f)

        package_data['scripts']['dev'] = 'supervisor server.js'
        package_data['scripts'].pop('test', None)

        with open(package_json_path, 'w') as f:
            json.dump(package_data, f, indent=2)

        spinner.succeed('package.json updated successfully!')
    except Exception as e:
        spinner.fail(f"An error occurred while updating package.json: {e}")
    
    spinner.succeed(f"Backend setup has been created in: {api_directory}")

base_directory = input("Enter the path of the directory : ")
create_backend_setup(base_directory)
