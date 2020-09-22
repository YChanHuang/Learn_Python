# import relevant libraries
import pandas as pd
import seaborn as sns
import numpy as np

# read historical nobel winner data
nobel = pd.read_csv('nobel_archive.csv')

# Let's have a look of the first 6 rows
nobel.head(6)
