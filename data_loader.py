import csv
from logger_config import logger
def load_csv():
    logger.info("Starting to load employee_data.csv")
    try:
        with open("employee_data.csv","r",  encoding="utf-8") as csv_file:
            csv_reader=csv.DictReader(csv_file)
            employees=[]

            for line in csv_reader:
                employees.append(line)
        logger.info("CSV loaded successfully | total records: %d", len(employees))
        return employees
    except FileNotFoundError:
        logger.error("employee_data.csv file not found")
        raise
    except Exception :
        logger.exception("Error while loading CSV file ")
        raise
        