import pandas as pd
df = pd.read_csv('skill_builder_data.csv', sep=',', encoding = "gbk")
print(df.head())

# with open('skill_builder_data.csv','r' ) as f:
#     lines = f.readlines()
#     a = 1

