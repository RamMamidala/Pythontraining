import pandas
file_open=pandas.read_csv("FileNumber1.csv")
print(file_open["userName"])
print(file_open["password"])
print(file_open["userName"][0])
print(file_open["password"][0])
print(file_open["userName"][1])
print(file_open.sort_values("userName"))
print(file_open.sort_values("userName",ascending=False))
