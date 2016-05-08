# delete a row
## drop
df.drop(label)  
df.drop(label, inplace=True)  
df.drop(df.index[:3], inplace=True)  
df.drop(df.index[[1,3]])  
http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.drop.html
## query
df.query('index > 2')   

# Indexing and Selecting Data
http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-callable  
## query  
df.query('index > 2')  
