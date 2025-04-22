import sys
import os

# Add your project directory to the sys.path
project_home = '/home/hackerviper/electricity_fuzzy_project'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variables
os.environ['FLASK_ENV'] = 'production'

from app import app as application  # noqa