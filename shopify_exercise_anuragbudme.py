import pandas as pd
googlesheetid= "16i38oonuX1y1g7C_UAmiK9GkY7cS-64DfiDMNiR41LM"
sheetname="Sheet1"

url="https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}".format(googlesheetid,sheetname)
orders_dataframe=pd.read_csv(url)

order_amount_description=orders_dataframe[['order_amount']].describe()
print(order_amount_description)

order_amount_median=orders_dataframe['order_amount'].median()

print("Median value of the order amount",order_amount_median)