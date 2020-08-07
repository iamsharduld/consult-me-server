import pandas as pd

# Stomach symptoms
STOMACH_GOOGLE_SHEET_ID = '1dPTIcVN9ux6mX5y8Xql_kvHZXm45mF9UXbdznytyoto'
STOMACH_WORKSHEET_NAME = 'Code-J'
STOMACH_SHEET_URL = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
	STOMACH_GOOGLE_SHEET_ID,
	STOMACH_WORKSHEET_NAME
)


# All diseases symptoms
ALL_DISEASES_GOOGLE_SHEET_ID = '14iF_6zUWb48JOruoUnNopwjK0ztllmgEBDNEhSh026Q'
ALL_DISEASES_WORKSHEET_NAME = 'X'
ALL_DISEASES_SHEET_URL = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
	ALL_DISEASES_GOOGLE_SHEET_ID,
	ALL_DISEASES_WORKSHEET_NAME
)

stomach_data = pd.read_csv(STOMACH_SHEET_URL)
stomach_data_cols = stomach_data.columns
stomach_data_cols = stomach_data_cols[2:]
X = stomach_data[stomach_data.columns]
y = stomach_data['0Symptoms list']

all_disease_data = pd.read_csv(ALL_DISEASES_SHEET_URL)
all_disease_data_cols = all_disease_data.columns
print(all_disease_data.head())
print(all_disease_data_cols)