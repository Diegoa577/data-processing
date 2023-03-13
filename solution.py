import pandas

# Read input data
def read_data(path_file):
    try:
        df = pandas.read_excel(path_file)
    except FileNotFoundError:
        return "File does not exist"
    except ValueError:
        return "File is not a .xlsx format"
    return df

# Get date range
def get_column_and_date_range(df):
    try:
        start_date = df.columns[0]
        end_date = df.iloc[0][0]
        total_date = pandas.date_range(start_date,end_date,freq='d')
        total_date = list(total_date.strftime('%Y/%m/%d'))
    except ValueError:
        return "Can't find a date"
    
    # Rename columns
    df.columns = df.iloc[0]
    df.rename(columns={end_date: df.iloc[1][0]}, inplace=True)
    # Get columns name
    name_columns = df.columns.unique()
    
    
    return total_date, name_columns

def data_clean(df):
    # Drop unnecessary rows
    df = df.dropna(axis=0)
    df = df.drop([df.index[0], df.index[1]])
    # Get sites list
    try:
        site_list = df["Site ID"].tolist()
        df = df.drop(columns=['Site ID'], axis=1)
    except KeyError:
        return "Site ID does not exist"

    # Reset index
    df = df.reset_index(drop=True)
    
    return site_list
    

# Create new data
def create_new_data(df):
    total_date, name_columns = get_column_and_date_range(df)
    site_list = data_clean(df)
    number_site = len(site_list)
    number_date = len(total_date)
    day_month = [i for i in range(1,number_date+1)]
    data_values = {}
    data_values["Day of Month"] = day_month*number_site
    data_values["Date"] = total_date*number_site
    for i in range(number_site):
        start_data = 0
        end_data = number_date
        for column in name_columns:
            if column in data_values:
                if column == "Site ID":
                    data_values[column]+=[site_list[i]]*number_date
                    continue
                data_values[column]+=df.loc[i].values.tolist()[start_data:end_data]
            else:
                if column == "Site ID":
                    data_values[column] =[site_list[i]]*number_date
                    continue
                data_values[column]= df.loc[i].values.tolist()[start_data:end_data]
            start_data = end_data
            end_data = end_data + number_date
     # Create new dataframe with the new data       
    new_df = pandas.DataFrame(data_values).set_index('Day of Month')
    return new_df


path_file = "Analytics Template for Exercise.xlsx"
df = read_data(path_file)

new_df = create_new_data (df)
# Filter data 
sites_name =['site 1','site 2']
result = new_df[new_df["Site ID"].isin(sites_name) ]

# Create xlsx file
with pandas.ExcelWriter('output_31_days_report.xlsx') as writer:
    result.to_excel(writer, sheet_name="output_31_days_report")