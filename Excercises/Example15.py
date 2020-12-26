import pandas
data={
    "userName":["Ram","Sai","Sri"],
    "password":["1234","2345","6754"]
    }
data_frame=pandas.DataFrame(data)
print(data_frame)
data_frame.to_csv("FileNumber1.csv",index=False)

