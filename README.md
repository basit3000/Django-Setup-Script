# Django Setup Script

The purpose of this script is to automate the creation of a Python virtual environment, set up a Django server, upgrade pip, and start the server.

## Prerequisites

- Ensure Python is installed locally. You can download it from [python.org](https://www.python.org/).

## Steps to Run the Script

1. **Open Command Prompt / Shell / PowerShell**

    Open your preferred command line interface.

2. **Clone this Project**

    Clone the repository to your local machine using the following command:

    ```sh
    git clone https://github.com/basit3000/Django-Setup-Script.git

3. **Navigate to the project directory**

    ```sh
    cd <project_directory>

4. **Run the script (for Windows)**

    - **For Windows:**

      ```sh
      python script.py
      ```

    - **For Linux:**

      ```sh
      python3 script_linux.py
      ```

## Running the Django Development Server

After running the setup script, follow these steps:

1. **Navigate to the Project Directory**

    ```sh
    cd <project_directory>
    ```

2. **Start the Django Development Server**

    - **For Windows:**

      ```sh
      python manage.py runserver
      ```

    - **For Linux:**

      ```sh
      python3 manage.py runserver
      ```

## Notes

- Ensure you have the necessary permissions to execute the scripts.
- If you encounter any issues, refer to the troubleshooting section in the documentation.

## Troubleshooting

### Common Issues

1. **Script Execution Errors**

    - **Issue**: `python: command not found` or `python3: command not found`
      - **Solution**: Ensure Python is installed and added to your system's PATH. You may need to install Python or adjust your PATH environment variable.

    - **Issue**: `Permission denied` when running the script
      - **Solution**: Check file permissions. You might need to adjust permissions or run the command with elevated privileges (e.g., using `sudo` on Linux).

2. **Virtual Environment Issues**

    - **Issue**: `venv/bin/python: No such file or directory`
      - **Solution**: Ensure the virtual environment was created successfully. Verify the path and try recreating the virtual environment with `python3 -m venv venv`.

    - **Issue**: `ModuleNotFoundError: No module named 'django'`
      - **Solution**: Make sure you have activated the virtual environment. If not, activate it with `source venv/bin/activate` on Linux or `venv\Scripts\activate` on Windows, and then reinstall Django using `pip install django`.

3. **Django Development Server Issues**

    - **Issue**: `django.db.utils.OperationalError: (psycopg2.OperationalError) connection to server at "localhost" (::1), port 5432 failed: FATAL:  password authentication failed for user "admin"`
      - **Solution**: Check your database settings in `settings.py`. Ensure that your PostgreSQL server is running and that the credentials are correct.

    - **Issue**: `Error: No module named 'manage'`
      - **Solution**: Ensure you are in the correct project directory where `manage.py` is located.

### Further Help

- Check the [Django documentation](https://docs.djangoproject.com/en/stable/) for more details on common issues and configuration tips.
