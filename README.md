# Python Learning Tool - README

## Overview
The **Python Learning Tool** is an interactive application designed to help users learn Python with structured topics, quizzes, challenges, and a progress tracking system.

## Features
- **User Authentication**: Sign-up and login system with stored user data.
- **Topic Navigation**: Previous & Next buttons for smooth topic browsing.
- **Resizable Frames**: Adjusts frame size dynamically based on content.
- **Dark Theme**: A modern dark UI for better readability.
- **Progress Tracking**: Monitors quiz scores, challenges, and stored code.
- **Interactive Learning**: Includes quizzes and coding challenges.

---

## Installation Guide
To install and use the Python Learning Tool, follow these steps:

### **Prerequisites**
- Ensure **Python** is installed on your system.
- Install necessary dependencies using:
  ```sh
  pip install -r requirements.txt
  ```

### **Running the Application**
Run the tool using:
```sh
python main.py
```

---

## Creating an Installer with Inno Setup
To distribute your application as a **Windows executable**, you can use **Inno Setup**.

### **Steps to Create an Installer**
1. **Download & Install Inno Setup**
   - Get it from [here](https://jrsoftware.org/isinfo.php)
   
2. **Convert Python Script to EXE**
   - Use `pyinstaller` to create an executable:
     ```sh
     pyinstaller --onefile --windowed main.py
     ```
   - The EXE file will be in the `dist` folder.

3. **Create an Inno Setup Script (setup.iss)**
   - Example script:
     ```iss
     [Setup]
     AppName=Python Learning Tool
     AppVersion=1.0
     DefaultDirName={pf}\PythonLearningTool
     OutputDir=.
     OutputBaseFilename=PythonLearningToolSetup
     SetupIconFile=icon.ico

     [Files]
     Source: "dist\main.exe"; DestDir: "{app}"
     Source: "README.txt"; DestDir: "{app}"

     [Icons]
     Name: "{group}\Python Learning Tool"; Filename: "{app}\main.exe"

     [Run]
     Filename: "{app}\main.exe"; Description: "Launch Python Learning Tool"; Flags: nowait postinstall skipifsilent
     ```

4. **Compile the Script**
   - Open **Inno Setup Compiler**, load `setup.iss`, and click **Compile**.

5. **Distribute the Installer**
   - The generated `.exe` installer can be shared for easy installation.
## Installation

1. **Download the Setup**

   [![Download Setup](https://img.shields.io/badge/Download-Setup-green?style=for-the-badge)](<https://drive.google.com/drive/folders/1X3yxgefiwNRVvWl7N40KWzQGncEl1xdw?usp=sharing>)

2. **Extract and Run**
   - Extract the downloaded file.
   - Run `setup.exe` (Windows) or `python main.py` (for manual execution).

## License
This project is licensed under the MIT License.



