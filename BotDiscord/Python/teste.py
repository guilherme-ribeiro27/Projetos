import pandas as pd
msg = '@guigs#8031 27/06/2002    '
msg[::-10]
print(msg[-10::])
print(msg.split())

datas_df = pd.read_excel("Pasta de trabalho.xlsx")

print(datas_df)