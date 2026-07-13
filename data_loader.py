import csv
import config
from logger_config import logger

def load_csv():
    logger.info("Starting to load %s" , config.CSV_FILE)
    try:
        with open(config.CSV_FILE,"r",  encoding="utf-8") as csv_file:
            csv_reader=csv.DictReader(csv_file)
            employees=[]

            for line in csv_reader:
                employees.append(line)
        logger.info("CSV loaded successfully | total records: %d", len(employees))
        return employees
    except FileNotFoundError:
        logger.error("%s file not found",config.CSV_FILE)
        print("Error : File Not Found")
        raise
    except Exception :
        logger.exception("Error while loading CSV file ")
        print(f"Error Loading Data {Exception}")
        raise
        