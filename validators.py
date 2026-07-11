from datetime import datetime
import config
# def find_missing_first_name(employees):
#     count=0
#     for line in employees:
#         first_name=line["first_name"]
#         cleaned_first_name=len(first_name.strip())
#         if cleaned_first_name==0:
#             count+=1
#     return count

def find_missing_values(employees, column_name):
    
    count_missing_row=0
    for line in employees:
        column_value=line[column_name]
        cleaned_column_value=len(column_value.strip())
        if cleaned_column_value==0:
            count_missing_row+=1
    return count_missing_row

def find_invalid_emails(employees):
    count_invalid_email =0
    for line in employees:
        email=line["email"]
        value_error_1=email.count('@')
        cleaned_email=len(email.strip())
        if cleaned_email==0:
            continue      
        elif '@' not in email:
             count_invalid_email+=1
        elif value_error_1>1 :
            count_invalid_email+=1
        else:
            parts = email.split("@")
            part_1=len(parts[0])
            part_2=len(parts[1])
            part_2_value=parts[1].count(".")
            if part_1==0 or part_2==0:
                count_invalid_email+=1    
            elif part_2_value<1:
                count_invalid_email+=1       
    return count_invalid_email

def find_invalid_age(employees):
    count_invalid_age=0
    for line in employees:
        age=line["age"]
        # cleaned_age=len(age.strip())
        # if cleaned_age==0:
        if not age:
            continue
        try:
            int_age=int(age)
        except ValueError:
            count_invalid_age+=1
        else :
            if int_age < config.MIN_AGE or int_age > config.MAX_AGE:
                count_invalid_age += 1

        # it is an alternative
        # if age.isnumeric():
        #     int_age=int(line["age"])
        #     if int_age < 18 or int_age > 65:
        #         count_invalid_age += 1
    return count_invalid_age

def find_invalid_salary(employees):
    count_invalid_salary=0
    for line in employees:
        salary_str=line["salary"]
        cleaned_salary=len(salary_str.strip())
        if cleaned_salary==0:
            continue
        try:
            salary_int=int(salary_str)
        except ValueError:
            count_invalid_salary+=1
        else:
            if salary_int < config.MIN_SALARY or salary_int > config.MAX_SALARY:
                count_invalid_salary+=1

    return count_invalid_salary


# helpful with date and time
def find_invalid_joining_date(employees):
    count_invalid_dates=0
    
    for line in employees:
        
        joining_dates=line["joining_date"]
        cleaned_date=len(joining_dates.strip())
        if cleaned_date==0:
            continue
        try:
            datetime.strptime(joining_dates, config.JOINING_DATE_FORMAT)
        except ValueError:
            count_invalid_dates+=1
    return count_invalid_dates

# def find_duplicate_values(employees, column_name):
#     seen=set()
#     duplicate=set()
#     count_duplicate_entry=0
#     count_seen={}
#     for line in employees:
        
#         column_value=line[column_name]
#         cleaned_column_value=column_value.strip()
#         if not cleaned_column_value:
#             continue
#         elif cleaned_column_value in seen:
#             duplicate.add(cleaned_column_value)
#             count_duplicate_entry+=1
#             count_seen[cleaned_column_value]=count_seen.get(cleaned_column_value,0)+1
#         else:
#             seen.add(cleaned_column_value)
#     return count_duplicate_entry,count_seen




# a new fnction for find_duplicate_values 
def find_duplicate_values(employees,  column_name):
    occurrence={}
    duplicate={}
    for line in employees:
        column_value=line[ column_name]
        cleaned_column_data= column_value.strip()
        if not cleaned_column_data:
            continue
        else:
            occurrence[cleaned_column_data]=occurrence.get(cleaned_column_data,0)+1
    for value, count in occurrence.items():
                if count>1:
                    duplicate[value]=count
    return duplicate

  
