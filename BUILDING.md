# Building your executable

Welcome to this simple guide where you can build your own executables. This comes handy if you make any mods that you want to share or compile for your platform.

## By now, we only provide instructions for Windows building. We will provide building steps for macOS and Linux soon.

# Dependencies
To compile the game, you will need:
- Python 3 in its latest version
- Pyinstaller (Install using pip install -U pyinstaller)

# Getting the source code

# Standard way

To get the source code, ensure you have installed Git, it's up-to-date and it's inside PATH. You can download it from here: www.git-scm.com

Now follow these steps:

1. Open a terminal and type `git clone https://github.com/VirtualStorm2026/TransportMan-CLI.git`.
2. Proceed with the compiling steps below.

If you want to update the source code, go inside the source code folder you just cloned and use `git pull`.

# Beginners

To get the source code quickly, follow these steps:

1. Go to the project's main page
2. Click on the green `Code` button and select `Download ZIP`.
3. Extract the content in a folder, and proceed with the compiling steps below.

If you want to update the source code, redownload the source code following the steps above.

# Compiling the code
## Windows

Follow these steps to compile:
1. Go inside the folder of the source code.
2. Open a terminal and type `pyinstaller manager.py`.
(Optional): Add `--icon=path\to\icon.ico` to the command if you want to have a custom icon.
3. Wait until the process finishes.
4. You will have your compiled file inside the newly created `dist` folder.

# macOS and Linux users
Unfortunately, for Mac users, we cannot provide a detailed guide in how to compile the game. This is because we don't have a Mac to test with, and we can't be sure how much the process changes.
For Linux users, we'll update this guide soon to cover Linux as we find out how to compile the game on it.

# Troubleshooting
This is a basic troubleshooting guide which covers some common errors that could happen.

## pyinstaller: command not found
This means you haven't installed Pyinstaller yet. Do so by running `pip install -U pyinstaller`.

## pip: command not found
This means you haven't either installed Python or your installation is broken. Download a fresh copy from here: www.python.org and update `pip` running `python -m pip install --upgrade pip` if you are on Windows or `python3 -m pip install --upgrade pip` if you are on macOS/Linux.