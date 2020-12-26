import pandas
import xlsxwriter
data={
    "userName":["Ram","Sai","Sri"],
    "password":["1234","2345","6754"]
    }
dataFrame=pandas.DataFrame(data)
print(dataFrame)
fileWriter=pandas.ExcelWriter("ExcelFile1.xlsx",engine='xlsxwriter')
dataFrame.to_excel(fileWriter,sheet_name="Sheet1")
fileWriter.save()

file_open=pandas.read_excel("ExcelFile1.xlsx")
print(file_open["userName"])
print(file_open["password"])
print(file_open["userName"][0])
print(file_open["password"][0])
print(file_open["userName"][1])
print(file_open.sort_values("userName"))
print(file_open.sort_values("userName",ascending=False))
