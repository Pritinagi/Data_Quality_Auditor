import pytest
from validators import find_missing_values, find_invalid_emails

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



# ======================-EMAIL-=========================

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
# ------Test - 8 ------------------------------
def test_endstwith_dots():
    sample_email_data=[
        
        {"email":"none.@email.com"},
        {"email":"none@email.com."},
    ]
    result = find_invalid_emails(sample_email_data)
    assert result ==    1