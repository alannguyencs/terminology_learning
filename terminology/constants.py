from pathlib import Path
import os

CWF = Path(__file__)

PROJECT_PATH = str(CWF.parent.parent) + '/'
DATA_PATH = PROJECT_PATH + 'data/'
INPUT_PATH = DATA_PATH + 'input.xlsx'
QUESTION_PATH = DATA_PATH + 'question.xlsx'
RESULT_PATH = DATA_PATH + 'result.xlsx'
DATABASE_PATH = DATA_PATH + 'database.json'