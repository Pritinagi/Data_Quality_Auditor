import pytest
from validators import find_missing_values, find_invalid_emails, find_invalid_age, find_invalid_salary ,find_invalid_joining_date, find_duplicate_values

# =================-Missing-Values-====================
# ------Fixture-reusable test data  -----------
@pytest.fixture
def sample_employee():
    return [{"name":"alice","age":None, "email":""},
            {"name":"success", "age":"24", "email":"success@gmail.com"},
            # {"name":"rine","age":45,"email": "  "},
            {"name":"successful", "age":"24", "email":"successful@gmail.com"}]


# ------Test - 1 ------------------------------
def test_single_empty_value(sample_employee):
    """"
    when exactly one row has an empty string for the  target column, the function  should return 1 .
    """
    result= find_missing_values(sample_employee,"email")
    assert result==1

# ------Test - 2 ------------------------------

def test_multiple_empty_value():
    """
    when more than one row has an empty string for th target column, the function coutns all of them
    """
    data =  [ {"col":""}, 
            {"col":"   "}, 
            {"col":"Success"},
            {"col": ""}
    ]
    result = find_missing_values(data,"col")
    assert result==3

# ------Test - 3 ------------------------------

def test_empty_employee_list():
    result=find_missing_values([],"any_column")
    # any_column is a dummy name can be anything 
    assert result==0

# ------Test - 4 ------------------------------
def test_missing_column_key():
    data= [
        {"name":"growth","email":"growth@gmail.com"},
        {"name":"uowards"}
    ]
    with pytest.raises(KeyError):
        result=find_missing_values(data,"email")
    # assert result==1

# ------Test - 5 ------------------------------
def test_non_existing_column(sample_employee):
    with pytest.raises(KeyError):
        result=find_missing_values(sample_employee,"phone_number")


# ------Test - 6 ------------------------------
def  test_no_missing_values():
    data= [
        {"name":"growth","email":"growth@gmail.com"},
        {"name":"success", "email":"success@gmail.com"}
    ]
    result=find_missing_values(data,"email")
    assert result==0



# ======================-EMAIL-======================

# ------Test - 1 ------------------------------
def test_missing_at_symbol():
    sample_email_data= [
            {"email":"invallid.com"},
            {"email":"invallid.at.com"}
        ]
    result=find_invalid_emails(sample_email_data)
    assert result==2

# ------Test - 2 ------------------------------
def test_missing_dot_symbol():
    sample_email_data=[
        {"email":"valid@gmail.com"},
        {"email":"invalid@gmailcom"},
        {"email":"invalid@gmail@dot@com"},
    ]

    result=find_invalid_emails(sample_email_data)
    assert result==2

# ------Test - 3 ------------------------------
def test_empty_username():
    sample_email_data=[
        {"email":"valid@gmail.com"},
        {"email":"@gmail.com"},
        {"email":"None@gmail.com"},
        {"email":"N @gmail.com"},
        {"email":" @gmail.com"}
    ]
    result=find_invalid_emails(sample_email_data)
    assert result==3

# ------Test - 4 ------------------------------
def test_empty_domain():
    sample_email_data=[
        {"email":"valid@gmail.com"},
        {"email":"invalid@"},
        {"email":"Nonevalid@gmail.com"},
        {"email":"invaid@ m"},
        {"email":"invalid@gmail.c om "}
    ]
    result=find_invalid_emails(sample_email_data)
    assert result==3

# ------Test - 5 ------------------------------
def test_email_with_empty_username():
    sample_email_data=[
        {"email":""},
        {"email":None},
        {"email":" None"},
        {"email":"valid@email.com"},
    ]
    result = find_invalid_emails(sample_email_data)
    assert result == 2

# ------Test - 6 ------------------------------
def test_none_email():
    sample_email_data=[
        
        {"email":None},
        {"email":"none@email.com"},
    ]
    result = find_invalid_emails(sample_email_data)
    assert result == 1

# ------Test - 7 ------------------------------
def test_double_dots():
    sample_email_data=[
        
        {"email":"none@email..com"},
        {"email":"none..@email.com"},
    ]
    result = find_invalid_emails(sample_email_data)
    assert result == 2

# ------Test - 8 ------------------------------
def test_starstwith_dots():
    sample_email_data=[
        
        {"email":"none@email.com"},
        {"email":"none@email.com"},
    ]
    result = find_invalid_emails(sample_email_data)
    assert result == 0
# ------Test - 9 ------------------------------
def test_endstwith_dots():
    sample_email_data=[
        
        {"email":"none@email.com"},
        {"email":"none@email.com."},
    ]
    result = find_invalid_emails(sample_email_data)
    assert result ==    1

# ------Test - 10 ------------------------------
def test_happy_email():
    sample_email_data=[
        
        {"email":"valid@email.com"},
        {"email":"valid2@email.com"},
    ]
    result = find_invalid_emails(sample_email_data)
    assert result ==    0


# ======================-AGE-======================

# ------Test - 1 ------------------------------
def test_invalid_max_age():
    sample_age=[
        {"age":120},
        {"age":35},
        {"age":60},
        {"age":150}
    ]

    result=find_invalid_age(sample_age)
    assert result==2

# ------Test - 2 ------------------------------
def test_invalid_min_age():
    sample_age=[
        {"age":23},
        {"age":5},
        {"age":6},
        {"age":56}
    ]

    result=find_invalid_age(sample_age)
    assert result==2

# ------Test - 3 ------------------------------
def test_negative_age():
        sample_age=[
                {"age":-20},
                {"age":-5},
                {"age":60},
                {"age":-120}
            ]

        result=find_invalid_age(sample_age)
        assert result==3

# ------Test - 4 ------------------------------
def test_non_integer_age():
        sample_age=[
                {"age":"one"},
                {"age":28},
                {"age":60},
                {"age":25}
            ]
        result=find_invalid_age(sample_age)
        assert result==1

# ------Test - 5 ------------------------------
def test_whitespace_age():
        sample_age=[
                {"age":" "},
                {"age": "  "},
                {"age":60},
                {"age":25}
            ]
        result=find_invalid_age(sample_age)
        assert result==2
    
# ------Test - 6 ------------------------------
def test_None_age():
    sample_age=[
            {"age":23},
            {"age":None},
            {"age":60},
            {"age":None}
        ]
    result=find_invalid_age(sample_age)
    assert result==2

# ------Test - 7 ------------------------------
def test_missing_column_age():
    data= [
        {"name":"growth","age":54},
        {"name":"uowards"}
    ]
    with pytest.raises(KeyError):
        result=find_invalid_age(data)
    # assert result==1

# ------Test - 8 ------------------------------
def test_happy_age():
    sample_age=[
            {"age":23},
            {"age":35},
            {"age":60},
            {"age":25}
        ]
    result=find_invalid_age(sample_age)
    assert result==0


# ======================-Salary-======================

# ------Test - 1 ------------------------------

def test_none_salary():
    data=[
        {"salary":70000},
        {"salary":87834},
        {"salary":None},
        {"salary":70000},
        {"salary":70000}

    ]
    result=find_invalid_salary(data)
    assert result==1

# ------Test - 2 ------------------------------

def test_min_salary():
    data=[
        {"salary":70000},
        {"salary":87834},
        {"salary":1000},
        {"salary":0},
        {"salary":5000}

    ]
    result=find_invalid_salary(data)
    assert result==1

# ------Test - 3 ------------------------------

def test_max_salary():
    data=[
        {"salary":500001},
        {"salary":87834},
        {"salary":50000},
        {"salary":70000},
        {"salary":70000}

    ]
    result=find_invalid_salary(data)
    assert result==1

# ------Test - 4 ------------------------------

def test_empty_salary():
    data=[
        {"salary":50000},
        {"salary":87834},
        {"salary":""},
        {"salary":70000},
        {"salary":70000}

    ]
    result=find_invalid_salary(data)
    assert result==1

# ------Test - 5 ------------------------------

def test_whitespace_salary():
    data=[
        {"salary":50000},
        {"salary":87834},
        {"salary":" "},
        {"salary":70000},
        {"salary":70000}

    ]
    result=find_invalid_salary(data)
    assert result==1


# ------Test - 6 ------------------------------

def test_missing_salary_column():
    data=[
        {"salary":50000},
        {"salary":87834},
        {},
        {"salary":70000},
        {"salary":70000}

    ]
    with pytest.raises(KeyError):
        result=find_invalid_salary(data)

# ------Test - 7 ------------------------------

def test_negative_salary():
    data=[
        {"salary":50000},
        {"salary":87834},
        {"salary":-87834},
        {"salary":70000},
        {"salary":70000}

    ]
    result=find_invalid_salary(data)
    assert result==1

# ------Test - 8 ------------------------------

def test_non_integer_salary():
    data=[
        {"salary":50000},
        {"salary":87834},
        {"salary":"eight hundred"},
        {"salary":70000},
        {"salary":70000}

    ]
    result=find_invalid_salary(data)
    assert result==1

# ------Test - 9 ------------------------------

def test_happy_salary():
    salary=[
         {"salary":50000},
         {"salary":70000},
         {"salary":70000}
        ]
    result=find_invalid_salary(salary)
    assert result==0


# ======================-Joining date-======================

# ------Test - 1 ------------------------------
def test_empty_date():
    dates=[
        {"joining_date":"11/6/2023"},
        {"joining_date":"11/6/2023"},
        {"joining_date":""},
        {"joining_date":"11/6/2023"},

    ]
    result=find_invalid_joining_date(dates)
    assert result==1

# ------Test - 2 ------------------------------

def test_whitespace_date():
    dates=[
        {"joining_date":"11/6/2023"},
        {"joining_date":"11/6/2023"},
        {"joining_date":"    "},
        {"joining_date":"11/6/2023"},

    ]
    result=find_invalid_joining_date(dates)
    assert result==1

# ------Test - 3 ------------------------------
def test_garbage_date():
    dates=[
        {"joining_date":"11/6/2023"},
        {"joining_date":"11/6/2023"},
        {"joining_date":"abcd"},
        {"joining_date":"11/6/2023"},

    ]
    result=find_invalid_joining_date(dates)
    assert result==1

# ------Test - 4 ------------------------------

def test_non_date_values():
    dates=[
        {"joining_date":"11/6/2023"},
        {"joining_date":"11/6/2023"},
        {"joining_date":1234},
        {"joining_date":"11/6/2023"},

    ]
    result=find_invalid_joining_date(dates)
    assert result==1

# ------Test - 5 ------------------------------

def test_boolean_date():
    dates=[
        {"joining_date":"11/6/2023"},
        {"joining_date":True},
        {"joining_date":True},
        {"joining_date":"11/6/2023"},

    ]
    result=find_invalid_joining_date(dates)
    assert result==2

# ------Test - 6 ------------------------------

def test_missing_date_column():
    dates=[
        {"joining_date":"11/6/2023"},
        {"joining_date":"11/6/2023"},
        {"joining_date":"11/6/2023"},
        {"age":46},

    ]
    with pytest.raises(KeyError):
        result=find_invalid_joining_date(dates)
    
# ------Test - 7 ------------------------------

def test_none_date():
    dates=[
        {"joining_date":"11/6/2023"},
        {"joining_date":"11/6/2023"},
        {"joining_date":None},
        

    ]
    result=find_invalid_joining_date(dates)
    assert result==1
    

# ------Test - 8 ------------------------------

def test_date_format():
    dates=[
        {"joining_date":"11/9/2023"},
        {"joining_date":"11/feb/2023"},
        {"joining_date":"3/1/2023"},
        

    ]
    result=find_invalid_joining_date(dates)
    assert result==1
    

# ------Test - 9  ------------------------------

def test_invalid_date():
    """date format is /m/d/yyyy"""
    dates=[
        {"joining_date":"11/9/2023"},
        {"joining_date":"2025/7/23"},
        {"joining_date":"23/13/2026"},
        

    ]
    result=find_invalid_joining_date(dates)
    assert result==2
    

# ------Test - 10  ------------------------------

def test_invalid_date_with_time():
    """date format is /m/d/yyyy"""
    dates=[
        {"joining_date":"11/9/2023:23:34"},
        {"joining_date":"2025/7/23 :2:53:4"},
        {"joining_date":"2/13/2026"},
        

    ]
    result=find_invalid_joining_date(dates)
    assert result==2
    

# ------Test - 11 ------------------------------

def test_future_date():
    dates=[
        {"joining_date":"11/9/2027"},
        {"joining_date":"11/7/2028"},
        {"joining_date":"11/6/2029"},
        

    ]
    result=find_invalid_joining_date(dates)
    assert result==3
    

# ------Test - 12 ------------------------------

def test_happy_date():
    dates=[
        {"joining_date":"11/9/2023"},
        {"joining_date":"11/7/2023"},
        {"joining_date":"11/6/2023"},
        

    ]
    result=find_invalid_joining_date(dates)
    assert result==0
    


# ======================-Duplicate's-======================

# ------Test - 1 ------------------------------
def test_string_duplicates():
    data=[
        {"name":"growth","age":54},
        {"name":"uowards","age":54},
        {"name":"growth","age":54},
        {"name":"uowards","age":54},
        {"name":"growth","age":55},
        {"name":"upwards","age":58}
    ]
    result=find_duplicate_values(data,"name")
    assert result=={'growth': 3, 'uowards': 2}
 
    
# ------Test - 2 ------------------------------
def test_int_duplicates():
    data=[
        {"name":"growth","age":54},
        {"name":"uowards","age":54},
        {"name":"growth","age":54},
        {"name":"uowards","age":54},
        {"name":"growth","age":55},
        {"name":"upwards","age":58}
    ]

    result=find_duplicate_values(data,"age")
    assert result=={'54': 4}

# ------Test - 3 ------------------------------
def test_missing_duplicates_with_missing_key():
    data=[
        {"name":"growth","age":54},
        {"name":"uowards","age":54},
        {"name":"growth","age":54},
        {"name":"uowards","age":54},
        {"name":"growth"},
        {"name":"upwards"}
    ]

    result=find_duplicate_values(data,"age")
    assert result=={'54': 4}
    
# ------Test - 4 ------------------------------
def test_none_duplicates():
    data=[
        {"name":"growth","age":24},
        {"name":"success","age":None},
        {"name":"upwards","age":None}
    ]
    # none is skipped so if multiple none is also there it will give us nothing

    result=find_duplicate_values(data,"age")
    assert result=={}
    
  
# ------Test - 5 ------------------------------
def test_multiple_key_duplicates():
    data=[{"name":"growth","age":54,"age":54,"age":54}]
    result=find_duplicate_values(data,"age")
    assert result=={}

    # assert result=={'age': 3}

"""You're treating the dict literal as if it preserves duplicate keys. It does not. A Python dict is a key-value mapping where each key maps to exactly one value. Writing the same key multiple times is not an error, but it's also not meaningful — only the last assignment survives.

This is different from:

A list — can have duplicate elements
A CSV row — can have duplicate column headers
A database table — can have duplicate column names (though it shouldn't)"""
    
    
