from pathlib import Path

# Yeh file (config.py) jahan hai, uska parent = project root
BASE_DIR = Path(__file__).resolve().parent

#========Files============

CSV_FILE=BASE_DIR/ "data" / "employee_data.csv"
LOG_FILE=BASE_DIR/ "logs" /"app.log"
REPORT_FILE=BASE_DIR/"reports"/"quality_report.txt"

#========AGE============

MIN_AGE=18
MAX_AGE=65

#========SALARY's============

MIN_SALARY=1
MAX_SALARY=500000

#========DATE============
from datetime import datetime
JOINING_DATE_FORMAT = "%m/%d/%Y"
MIN_JOINING_DATE=datetime.strptime(
    "1/7/2021", JOINING_DATE_FORMAT
)
MAX_JOINING_DATE=datetime.now()