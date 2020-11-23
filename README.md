# Next Level Python LiveLessons
This is the code for **Next Level Python LiveLessons** by Arianne Dee

To get started with this course, please follow these instructions:
1. [Download the code](#1-download-the-code)
2. [Install Python 3.6+](#2-install-python-36-or-higher)
3. [Set up your IDE](#3-set-up-your-ide)

## Set up instructions
### 3. Download the code
If you're viewing this on GitHub already, stay on this page.
Otherwise, go to the GitHub repository: https://github.com/ariannedee/next-level-python-livelessons

#### If you know git:
Clone the repository.

#### If you don't know git:
1. Click the green "Code" button on the top-right of the page
2. Click "Download ZIP"
3. Unzip it
4. Move the **next-level-python-livelessons-main** folder to a convenient location

### 2. Install Python 3.6 or higher
Go to https://www.python.org/downloads/

Click the yellow button at the top to download the latest version of Python.

#### On Mac or Linux
Follow the prompts and install using the default settings.

#### On Windows
The default settings don't add Python to your PATH 
so your computer doesn't know where to look for it when Python runs 
(for some inexplicable reason).

##### If you're just installing Python now
Follow the instructions here: [Windows Python installer instructions](docs/WININSTALL.md)

##### If you've already installed Python with the default settings
Follow the instructions here: [Add Python to PATH variable in Windows](docs/WINSETPATH.md)

### 3. Set-up your IDE

#### 3.1 Choose an IDE
Throughout the course, I use the **PyCharm IDE** (*Community Edition*).
If you would like to use the same set-up, download it here:
https://www.jetbrains.com/pycharm/download/.
**Note** that one section goes through using PyCharm and using its keyboard shortcuts. 

Install, open, and use the default settings.


Another good option, if you're a more experienced developer,
is [**Visual Studio Code**](https://code.visualstudio.com/Download).

#### 3.2 Open up the code in your IDE
Open the top-level folder (*next-level-python-livelessons* or *next-level-python-livelessons-main*)
in your IDE of choice.

#### 3.3 Make sure it's configured to run the proper Python version
Try running `Lesson1/_3a_dictionary_examples.py` in your IDE.
If it fails to execute properly, you will need to make sure it is running with Python 3.6 (or higher).

##### PyCharm
On a Mac:
- Go to **PyCharm** > **Preferences**

On a PC:
- Go to **File** > **Settings**

Once in Settings:
1. Go to **Project: next-level-python-livelessons** > **Project Interpreter**
1. Look for your Python version in the Project Interpreter dropdown
1. If it's not there, click **gear icon** > **Add...**
1. In the new window, select **System Interpreter** on the left, and then look for the Python version in the dropdown
1. If it's not there, click the **...** button and navigate to your Python location
   - To find where Python is located, [look in these directories](docs/PATH_LOCATIONS.md)
   - You may have to search the internet for where Python gets installed by default on your operating system

##### VS Code
1. On the bottom left toolbar, select the Python version the terminal is using to run your file
1. In the pop-up, select the correct version, or enter the path for the desired Python version to run

## FAQs
### Can I use Python 2?
No, Python 2 is out of date and any project you're working on should be written in Python 3 by now.

### Can I use a different code editor besides PyCharm?
Yes, but it is only recommended if you are already know it and are comfortable navigating to different files and running commands in the command line. 
Make sure to install the most popular Python plugin(s) for syntax highlighting and code completions that are available for your IDE.

**Note** that part of the course is configuring PyCharm and using its shortcuts,
so that lesson will not help much if you are using a different IDE.

### Do you offer private Python help?
Yes, email **arianne.dee.studios at gmail.com** if you have any questions
or would like to set up some remote training.
