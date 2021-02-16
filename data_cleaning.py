#
# Created on Wed Feb 03 2021 by Amit Sambrekar
#
#
from typing import Any, Union

import pandas as pd
from pandas import DataFrame, Series
from pandas.io.parsers import TextFileReader

df = pd.read_csv('glassdoor_jobs.csv')
# print(df)

#Salary parsing
#Company Name text only
#State Field
#Age of company
#Parsing of Job description

df = df[df['Salary Estimate'] != '-1']
print(df)