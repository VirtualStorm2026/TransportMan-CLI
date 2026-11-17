# BUILDING YOUR OWN EXECUTABLES

Welcome to this quick guide where you can build your own executables. This comes handy if you make any mods that you want to share or compile for your platform.

## By now, we only provide instructions for Windows building. We will provide building steps for macOS and Linux soon.

# Dependencies
To compile the game, you will need:
- Python 3 in its latest version
- Pyinstaller

# Getting the source code

# Standard way

To get the source code, ensure you have installed Git, it's up-to-date and it's inside PATH. You can download it from [here](www.git-scm.com).

Now follow these steps:

1. Open a terminal and type `git clone https://github.com/VirtualStorm2026/TransportMan-CLI.git`.
2. Proceed with the compiling steps below.

If you want to update the source code, go inside the source code folder you just cloned and use `git pull`.

# Beginners

If you don't know how to use Git, or you will download the source code once, follow these steps:

1. Go to the project's main page
2. Click on the green `Code` button and select `Download ZIP`.
3. Extract the content in a folder, and proceed with the compiling steps below.

If you want to update the source code, redownload the source code following the steps above.
This is not recommended for long-term use. We recommend instead using the standard method.

# Compiling the code
## Windows

Follow these steps to compile:
1. Go inside the folder of the cloned repository.
2. Open a command prompt window and create your virtual environment using `python -m venv .venv`.
3. Initialize the virtual environment using `.venv\Scripts\activate.bat`.
4. Install `pyinstaller` using `pip install -U pyinstaller`.
5. Now compile the project for your platform using `pyinstaller --onefile manager.py`.
5. Wait until the process finishes and then you'll be done. The result will be in the newly created `dist` folder.

## Linux

Follow these steps to compile:
1. Go inside the folder of the cloned repository.
2. Open a terminal inside that folder and create your virtual environment using `python3 -m venv .venv`.
3. Initialize your virtual environment using `source .venv/bin/activate`.
4. Install `pyinstaller` using `pip install -U pyinstaller`.
4. Now compile the project for your platform using `pyinstaller --onefile --terminal manager.py`.
5. Wait until the process finishes and then you'll be done. The result will be in the newly created `dist` folder.

# macOS users
Unfortunately, for Mac users, we cannot provide a detailed guide for the moment for distinct reasons.

# Troubleshooting
This is a basic troubleshooting guide which covers some common errors that could happen.

## pyinstaller: command not found
This means you haven't installed Pyinstaller yet. Do so by running `pip install -U pyinstaller` inside your virtual environment.

## pip: command not found
This means you haven't either installed Python or your installation is broken. Download a fresh copy from here: www.python.org and update `pip` running `python -m pip install --upgrade pip` if you are on Windows or `python3 -m pip install --upgrade pip` if you are on macOS/Linux.

## externally-managed-environment
This problem mostly happens in Linux and macOS systems when trying to install dependencies via pip. This occurs because you have not created and/or initialized your virtual environment. Follow the steps above to create and initialize your virtual environment.