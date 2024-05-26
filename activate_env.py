import os
import json
import subprocess


#region new environment
def create_json_file(parm):
    """
    Creates a JSON file with the given file name and data.
    Args:
    data (dict): The data to be written to the JSON file.
    """
    FILE_NAME = 'activate_env.json'
    try:
        with open(FILE_NAME, 'w') as json_file:
            json.dump(parm, json_file, indent=4)
        print(f"File {FILE_NAME} created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file {FILE_NAME}: {e}")


def create_new_env(env_name):
    # Create a new virtual environment
    subprocess.run(['cmd', '/c', f'virtualenv {env_name}_env'])
    print(f"Virtual environment {env_name} created successfully.\n\n\n")


def get_env_path(env_name):
    """
    Checks if there is a folder with the given env_name and looks for the activate.bat file.

    Args:
    env_name (str): The name of the virtual environment.

    Returns:
    str: The path to the activate.bat file if found, otherwise an empty string.
    """
    env_dir = f"{env_name}_env"
    activate_bat_path = os.path.join(env_dir, 'Scripts', 'activate.bat')

    if os.path.isdir(env_dir) and os.path.isfile(activate_bat_path):
        return activate_bat_path
    else:
        return None


def first_initialize():
    """
    check if environment is already initialized
    if not create a new one
    """
    if not os.path.exists('activate_env.json'):
        activate_env = {}
        env_name = ""
        while (env_name == ""):
            env_name = input("Enter the name of the new virtual environment: ")
            if (env_name == ""):
                print("Please enter a valid name.")

        create_new_env(env_name)
        env_path = get_env_path(env_name)
        if env_path:
            activate_env['env_path'] = env_path
            activate_env['first_run'] = True
            create_json_file(activate_env)
            return True
        else:
            print(f"An error occurred while creating the virtual environment {env_name}.")
            return False
            
    # if the file exists, read the file and return the env_path
    if os.path.exists('activate_env.json'):
        return True
    return False
#endregion new environment


#region activate environment
def activate_env():
    """
    Open cmd and activate the virtual environment
    """
    with open('activate_env.json', 'r') as f:
        activate_env = json.load(f)
    env_path = activate_env['env_path']
    print("Activating virtual environment...")
    try:
        # Open a new cmd process and activate the virtual environment
        process = subprocess.Popen(['cmd.exe'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        
        # Activate the virtual environment
        process.stdin.write(f'call "{env_path}"\n')

        if activate_env.get('first_run'):
            if (not os.path.exists('requirements.txt')):
                print("requirements.txt file not found.\nUnable to run jupyter notebook.")
                input ("Press any key to exit...")
                return
            # Install requirements if first_run is true
            print("Please wait while the requirements are being installed...\nIt may take a few minutes. you cannot see the progress so please be patient.")
            process.stdin.write('pip install -r requirements.txt\n')
            activate_env['first_run'] = False
            with open('activate_env.json', 'w') as f:
                json.dump(activate_env, f, indent=4)
            


        # Run Jupyter Notebook
        process.stdin.write('jupyter notebook\n')
        print("Jupyter Notebook is running in the virtual environment.")
        # Close the input to ensure the commands are executed
        process.stdin.close()

        # Wait for the process to complete
        stdout, stderr = process.communicate()

        # Print output and errors if any
        print(stdout)
        if stderr:
            print(stderr)
    except Exception as e:
        print(e)
        print("Make sure you have a requirements.txt file in the same directory.")

#endregion activate environment



def create_code_folder():
    """
    Create a folder named 'code' if it does not exist.
    """
    if not os.path.exists('code'):
        os.makedirs('code')
        print("Folder 'code' created successfully.")



if __name__ == '__main__':
    is_valid = first_initialize()
    if not is_valid:
        print("An error occurred while initializing the environment.")
        exit(1)
        
    # open cmd and activate the virtual environment
    create_code_folder()
    
    # activate the virtual environment
    activate_env()
