from logger_config import logger
import config



from validators import find_missing_values, find_duplicate_values
def generate_report(employees,
                    total_rows,
                    total_columns,
                    total_invalid_emails,
                    total_invalid_age,
                    total_invalid_salary,
                    total_invalid_joining_date):
        logger.info("Generating Report.....")
        try:
            with open(config.REPORT_FILE,"w",encoding="utf-8") as file:
                file.write("="*40 + "\n")
                file.write("DATA QUALITY REPORT\n")
                file.write("="*40 + "\n\n")

                file.write("Dataset Summary\n")
                file.write("-"*40 + "\n")
                file.write(f"Total Rows : {total_rows} \n")
                file.write(f"Total Columns : {total_columns} \n\n")
                file.write("Validation Results\n")
                file.write("-"*40 + "\n")

                file.write(f"Total Invalid Emails :{total_invalid_emails} \n")
                file.write(f"Total Invalid Age    : {total_invalid_age} \n")
                file.write(f"Total Invalid Salary : {total_invalid_salary} \n")
                file.write(f"Total Invalid Joining date : {total_invalid_joining_date} \n")
                mising_columns=[ "first_name",
                                "last_name",
                                "email",
                                "gender",
                                "joining_date",
                                "department"]
                file.write(f"Missing Values ---> \n")
                file.write("-"*40 + "\n")
                for missing_column in mising_columns:
                    missing_count=find_missing_values(employees,missing_column)
                    file.write( f"{missing_column:<20} : {missing_count}\n")
                file.write("-"*40 + "\n")

                duplicate_columns=[ "first_name",
                                "last_name",
                                "email",
                                "joining_date",
                                "department"]
                
                file.write(f"Duplicate Values ---> \n")
                file.write("-"*40 + "\n")

                for duplicate_column in duplicate_columns:
                    duplicate=find_duplicate_values(employees,duplicate_column)
                    duplicate_items_found=len(duplicate)
                    file.write(f"\nColumn : {duplicate_column}\n")
                    file.write(f"Duplicate items : {duplicate_items_found}\n")
                    file.write("Duplicate items and their occurrences:\n")    
                    # file.write(f"duplicate values {count:>3}\n")
                    if duplicate:
                            for value, count in duplicate.items():
                                file.write(f"{value:<20} : {count}\n")
                    else:
                        file.write("No duplicates found\n")
                file.write("-"*40 + "\n")
                logger.info("Report Generation successfully")
        except Exception as e:
             logger.exception("Failed to generate report.")
             print(f"Failed to generate report {e}.")
             raise
                
    