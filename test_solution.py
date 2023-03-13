import solution
import pandas as pd
import pytest

@pytest.mark.parametrize("path_file,expected", [("Analytics Template for Exercise.cvs", "File does not exist"), ("test_file.csv", "File is not a .xlsx format")])
def test_wrong_read_data(path_file, expected):
    result = solution.read_data(path_file)
    assert result == expected
    

def test_get_column_and_date_range():
    data = {"2021-01-01 00:00:00":["2021-01-03 00:00:00",0], 'Unnamed: 1':[0,1]}
    df = pd.DataFrame(data)
    total_date, _ = solution.get_column_and_date_range(df)
    assert total_date == ['2021/01/01', '2021/01/02', '2021/01/03']
    
def test_wrong_get_column_and_date_range():
    data = {"2021-01-01 00:00:00":["1",0], 'Unnamed: 1':[0,1]}
    df = pd.DataFrame(data)
    result = solution.get_column_and_date_range(df)
    assert result  == "Can't find a date"
    
@pytest.mark.parametrize(
    "data,expected", 
    [
        ({"2021-01-01 00:00:00":["1",0,5,1], 'Unnamed: 1':[0,1,5,1]}, "Site ID does not exist"), 
        ({"2021-01-01 00:00:00":["1",0,5,1,4,2,None], 'Site ID':[0,1,5,1,4,2, 5]}, [5, 1, 4, 2])])   
def test_data_clean(data, expected):
    df = pd.DataFrame(data)
    result = solution.data_clean(df)
    assert result  == expected


    
