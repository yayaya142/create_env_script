# Virtual Environment Setup and Jupyter Notebook Launcher

This Python script automates the creation and activation of a virtual environment, installs required packages, and launches Jupyter Notebook within the virtual environment. 

## What the Script Does

1. **Checks for Existing Configuration**:
   - If `activate_env.json` is not found, it prompts the user to create a new virtual environment.
   - Saves the path to the `activate.bat` file in the `activate_env.json` file.

2. **Creates a New Virtual Environment**:
   - Uses `virtualenv` to create a new virtual environment.
   - Stores the activation path and initial run status in a JSON file.

3. **Activates the Virtual Environment**:
   - Opens a new command prompt and activates the virtual environment.
   - Installs packages from `requirements.txt` if running for the first time.
   - Launches Jupyter Notebook within the activated environment.

4. **Creates Necessary Directories**:
   - Ensures a `src` directory is created for your project files.

## How to Use

1. **Ensure Requirements**:
   - Make sure `virtualenv` is installed.
   - Place a `requirements.txt` file in the same directory as the script, listing the required packages.

2. **Run the Script**:
   - Execute the script using Python or double click the .py file:
     ```bash
     python your_script_name.py
     ```
     

3. **Follow Prompts**:
   - If prompted, enter the name for the new virtual environment.


