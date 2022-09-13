from datetime import datetime as dt
import os

import wx
from dotenv import load_dotenv
import psycopg2 as pc

from library_management_system.main import LibManageSys

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
HOST = os.getenv("HOST")
DATABASE = os.getenv("DATABASE")
PORT = os.getenv("PORT")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

app = LibManageSys(redirect=False)
