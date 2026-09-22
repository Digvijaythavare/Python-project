import pandas as pd

print("Program Started")

Rawdata = "hello.txt"

show_data = pd.read_csv(Rawdata)

print(show_data)

print("Program Ended")