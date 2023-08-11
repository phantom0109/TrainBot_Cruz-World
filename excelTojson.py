import pandas
import json
import re
import datetime

Title_line_num = 4
begin_line_num = 6
End_line_unm = 50
Add_lines = 14
Days_monthly = 28

excel_data_df = pandas.read_excel('Few_Attendances.xlsx', sheet_name='Sheet1')
array_dt = excel_data_df.values
total_data = {}
for i in range(int((End_line_unm-begin_line_num)/Add_lines)):
    index_vl = 0
    Start_line_num = begin_line_num + (Add_lines + 1) * i 
    total_data["Employee" + str(i+1)] = {}   
    for j in range(int(Days_monthly)):
           if len(array_dt[index_vl + Start_line_num+1-2][4].split()) <= 3:
                array_dt[index_vl + Start_line_num+1-2][4] += str(" .")
           total_data["Employee" + str(i+1)][str(j+1)] = {
		"PAYCODE": array_dt[index_vl + Start_line_num+1-2][4].split()[0],
		"CARD NO.": array_dt[index_vl + Start_line_num+1-2][4].split()[1],
		"NAME": array_dt[index_vl + Start_line_num+1-2][4].split()[2] + " " + array_dt[index_vl + Start_line_num+1-2][4].split()[3],
		"Present ": array_dt[index_vl + Start_line_num+1-2][10],
		"Holiday ": array_dt[index_vl + Start_line_num+1-2][13],
		"W. Off": array_dt[index_vl + Start_line_num+1-2][16],
		"Absent": array_dt[index_vl + Start_line_num+1-2][19],
		"Leave": array_dt[index_vl + Start_line_num+1-2][22],
		"Hour Work": array_dt[index_vl + Start_line_num+1-2][25],
		"OT ": array_dt[index_vl + Start_line_num+1-2][28],
		"Designation NA": array_dt[index_vl + Start_line_num+2-2][10],
		"IN1": array_dt[index_vl + Start_line_num+3-2][j+1].replace("\u00a0", ""),
		"Out1": array_dt[index_vl + Start_line_num+4-2][j+1].replace("\u00a0", ""),
		"IN2": array_dt[index_vl + Start_line_num+5-2][j+1].replace("\u00a0", ""),
		"Out2": array_dt[index_vl + Start_line_num+6-2][j+1].replace("\u00a0", ""),
		"H Work": str(array_dt[Start_line_num+7-2][j+1]).replace("\u00a0", ""),
		"OT": array_dt[index_vl + Start_line_num+12-2][j+1].replace("\u00a0", ""),
		"Status": array_dt[index_vl + Start_line_num+13-2][j+1].replace("\u00a0", ""),
		"Shift": array_dt[index_vl + Start_line_num+14-2][j+1].replace("\u00a0", "")
		}
                      
print(json.dumps(total_data, indent=4))
now = datetime.datetime.now()
date_time = now.strftime("%m%d%Y_%H%M%S")
with open(str(date_time) + ".json", "w") as outfile:
    json.dump(total_data, outfile, indent=4)

