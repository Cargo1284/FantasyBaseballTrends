# the example is to create  
# Pandas DataFrame by lists of dicts.  
import pandas as pd  
  
# assign values to lists.  
data = [{'A': 10, 'B': 20, 'C':30, 'x':143, 'y': 250, 'z': 324}, {'A': 24, 'B': 54, 'C':75, 'x':100, 'y': 200, 'z': 300}]  
  
# Creates DataFrame.  
df = pd.DataFrame(data)  
  
# Print the data  
print(df.mean(axis=0))  