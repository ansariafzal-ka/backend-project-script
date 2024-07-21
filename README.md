# Backend Project Setup Automation

This Python script automates the setup of a backend project with a predefined structure. It initializes a Node.js project, creates necessary directories and files, installs dependencies, and updates the `package.json` file with a custom script.

## Features

- **Project Initialization**: Automatically creates a directory structure for a Node.js backend project.
- **Dependency Installation**: Installs essential Node.js packages and a development tool (`supervisor`).
- **Dynamic `package.json` Update**: Adds a custom `"dev"` script to `package.json`.

## Prerequisites

- **Python**: Ensure Python is installed on your machine. The script has been tested with Python 3.12.2
- **Node.js and npm**: Ensure Node.js and npm are installed and correctly configured. The script assumes npm is located at `C:\Program Files\nodejs\npm.cmd` on Windows.

## Getting Started

**Run the Script**:

    ```sh
    python script.py
    ```

    You will be prompted to enter the path of the directory where you want to set up the backend project.

## How It Works

1. **Directory and File Creation**: The script creates the following structure:
    ```
    /api
    ├── /src
    │   ├── /config
    │   ├── /routes
    │   ├── /models
    │   └── /controllers
    ├── server.js
    ├── .env
    └── .gitignore
    ```
   
2. **Project Initialization**: Runs `npm init -y` to generate a basic `package.json`.

3. **Dependency Installation**: Installs the `supervisor` package and essential dependencies (`express`, `mongoose`, `dotenv`, `cors`).

4. **`package.json` Update**: Adds a `"dev"` script to `package.json` for running the project with `supervisor`.

## Customizing npm Path

If npm is not located at `C:\Program Files\nodejs\npm.cmd`, you may need to update the path in the script.

*This project was created to simplify backend project setups.*
