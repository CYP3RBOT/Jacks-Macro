# Jacks-Macro
Mainly used for RainyLofi's GAR, but can be used anywhere

# Setup
*Assuming python & git are already installed*

- Part 1 | Cloning the repository (skip this part if you know what you're doing)
1. Open up any directory that you'd like the files to be stored (Downloads, Documents, etc).
2. Right click the folder/directory and press "Copy as path".
3. Press the windows key and type in "cmd", then hit enter. This opens up a command prompt.
4. First, type "cd" then paste the path. It should look something like this: `cd "C:\Users\(user)\(your_directory)"`
5. Use the left and right arrow key to remove the quotation marks. After it should look like this: `cd C:\Users\(user)\(your_directory)`
6. Then click enter.
7. Copy this next: `git clone https://github.com/CYP3RBOT/Jacks-Macro.git`, then hit enter. This clones the repository 
- Part 2 | Finishing setup and running the macro
1. Don't close out the cmd yet, first type `cd Jacks-Macro` and hit enter.
2. Then copy this command and hit enter: `python -m venv env`
3. Wait for that to finish creating, once completed, run the command: `env\Scripts\activate.bat`

Steps 2 & 3 create and active a virtual environment, where we'll install the necessary packages to continue.

4. Run this command and hit enter: `pip install requirements.txt`
5. Run this command to begin: `python source/main.py`

- Download python: https://www.python.org/downloads/
- Download git: https://git-scm.com/download/win (windows)
