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
    """count employees with invalid emails, 
        An email is considered invalid if:
        - It is missing the '@' symbol.
        - It contains more than one '@' symbol.
        - The local part (before '@') is empty.
        - The domain part (after '@') is empty.
        - The domain contains no dot ('.').
        Blank or whitespace-only emails are skipped (not counted as invalid).
    """

    count_invalid_email =0
    for line in employees:
        email=line["email"]
        if email is None:
            count_invalid_email+=1
            continue
        value_error_1=email.count('@')
        cleaned_email=len(email.strip())
        
        if cleaned_email==0:
            continue      
        elif '@' not in email:
             count_invalid_email+=1
        
        elif value_error_1>1 :
            count_invalid_email+=1
        
        else:
            email=email.strip()
            parts = email.split("@")
            username=parts[0]
            username_len=len(username)
            domain=parts[1]
            domain_len=len(domain)
            domain_value=parts[1].count(".")
            if username_len==0 or domain_len==0:
                count_invalid_email+=1    
            elif username!=username.strip():
                count_invalid_email+=1  
            elif username.startswith(".") or username.endswith('.'):
                count_invalid_email+=1  
            elif  domain.startswith(".") or domain.endswith('.'):
                count_invalid_email+=1  
            elif '..' in username:
                count_invalid_email+=1  
            elif '..' in domain:
                count_invalid_email+=1 
            elif domain!=domain.strip():
                count_invalid_email+=1   
            elif (" " in domain.strip()):
                count_invalid_email+=1 
            elif (" " in username.strip()):
                count_invalid_email+=1 
            elif domain_value<1:
                count_invalid_email+=1       
    return count_invalid_email

def find_invalid_age(employees):
    """Count employees with invalid ages"""
    count_invalid_age=0
    for line in employees:
        age=line["age"]
        # cleaned_age=len(age.strip())
        # if cleaned_age==0:
        
        if age is None:
                count_invalid_age += 1
                continue
        if isinstance(age, str) and age.strip()=="":
            count_invalid_age += 1
            continue
        try:
            int_age=int(age)
        except (ValueError, TypeError):
            count_invalid_age+=1
        else :
            if int_age < config.MIN_AGE or int_age > config.MAX_AGE:
                count_invalid_age += 1
        #  it is an alternative
        # if age.isnumeric():
        #     int_age=int(line["age"])
        #     if int_age < 18 or int_age > 65:
        #         count_invalid_age += 1
    return count_invalid_age

def find_invalid_salary(employees):
    count_invalid_salary=0
    for line in employees:
        salary_str=line["salary"]
        if salary_str is None:
                count_invalid_age += 1
                continue
        # cleaned_salary=len(salary_str.strip())
        # if cleaned_salary==0:
        if isinstance(salary_str,str) or salary_str.strip()=="":
            count_invalid_age += 1
            continue
        try:
            salary_int=int(salary_str)
        except (ValueError,TypeError):
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

  
