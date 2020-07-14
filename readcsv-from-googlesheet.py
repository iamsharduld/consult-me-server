import pandas

# https://learndataanalysis.org/import-google-sheets-to-pandas-dataframe-without-using-google-sheets-api/

googleSheetId = '1dPTIcVN9ux6mX5y8Xql_kvHZXm45mF9UXbdznytyoto'
worksheetName = 'Code-J'
URL = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
	googleSheetId,
	worksheetName
)

data = pandas.read_csv(URL)
print(data.head())
cols = data.columns
cols = cols[2:]
X = data[data.columns]
y = data['0Symptomslist']
# print(data.columns)