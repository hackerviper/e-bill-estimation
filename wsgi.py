import sys
import os

# IMPORTANT: Replace YOUR_USERNAME with your PythonAnywhere username when deploying
username = 'hackerviper'
project_name = 'mysite'

# Configure paths
project_home = f'/home/{username}/{project_name}'
virtualenv_path = os.path.join(project_home, 'venv')
python_version = '3.11'

# Add virtualenv site packages to path
venv_site_packages = os.path.join(virtualenv_path, 'lib', f'python{python_version}', 'site-packages')

# Add paths to Python path
paths = [project_home, venv_site_packages]
for path in paths:
    if path not in sys.path:
        sys.path.insert(0, path)

# Set environment variables
os.environ['FLASK_ENV'] = 'production'
os.environ.setdefault('PYTHONHASHSEED', '0')

# Import Flask application
try:
    from app import app as application  # This is the correct import statement
except Exception as e:
    print(f"Error importing application: {e}")

# Error handling
if __name__ == '__main__':
    try:
        application.run()
    except Exception as e:
        print(f"An error occurred: {e}")