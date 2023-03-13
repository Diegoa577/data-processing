# Data processing

This is a solution of the data-processing that consist with a input data generate a report using python.

## Description

### Input data

The input data is data from different sites that have the following columns:

a.	Page Views 
b.	Unique Visitors 
c.	Total Time Spent 
d.	Visits 
e.	Average Time Spent on Site

Each column have data of integer data type
Input shows 100 sites
The data have a start date and end day

### Output data

The output data is a report that we generate with the input data that have the information of two sites in a period of 31 days, have the following columns:

a.	Day of Month 
b.	Date 
c.	Site ID
d.	Page Views 
e.	Unique Visitors 
f.	Total Time Spent 
g.	Visits 
h.	Average Time Spent on Site

## Installation steps:

For this solution we need the following python libraries:

- Pandas
- Pytest

We install the above libraries with the following commands:

```
pip install pandas
```

```
pip install pytest
```

## Run the project

The project solution is in two files one is jupyter file this is a more illustrative solution without functions and the other file is .py file that is the same code that the jupyter file but the different is the code is separate with functions, to run the project we just need to open the file with our preferred IDE and run the code, we obtaint at the end a excel file with the solution.

## Run the test

We build some unit test with pytest, the tests are for the .py file, the jupyter file is just illustrative. to run the test just open the terminal and write pytest

## Limitations

The solution just work for the input data template, we can add new columns or sites only if we keep the structure.






