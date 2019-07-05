import os

from os.path import join, dirname

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("SECRET_KEY")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")



'''
Esto dentro del .env

SECRET_KEY=96923651thhqfqkegfj
DATABASE_PASSWORD=543673giewn48t93yhf103hjfr
ABC_KEY=1234xyz
DEF_KEY=2349875
DEBUG=True
'''
