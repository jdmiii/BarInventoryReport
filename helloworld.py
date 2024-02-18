from pathlib import Path
import re
from datetime import date

# Get the most recently modified xls file
downloadspath = str(Path.home() / "Downloads")
paths = [(p.stat().st_mtime, p) for p in Path(downloadspath).iterdir() if p.suffix == ".xls"]
paths = sorted(paths, key=lambda x: x[0], reverse=True)
last = str(paths[0][1])

# Verify filename to make sure we are using the correct xls file
test = re.search("InventoryActivity_Drakes_Danville", last)
if(test == None):
	print("Most recently downloaded excel file is not an inventory file")
	exit()

output = re.findall("\d{1,2}_\d{1,2}_\d{4}", last)
if(len(output) != 2):
	print("Most recently downloaded excel file is not an inventory file")
	exit()

# Make sure the date range for the inventory report is correct
dateinfo = output[0].split("_")
startdate = date(int(dateinfo[2]), int(dateinfo[0]), int(dateinfo[1]))
dateinfo = output[1].split("_")
enddate = date(int(dateinfo[2]), int(dateinfo[0]), int(dateinfo[1]))

if((enddate - startdate).days != 6):
	print("Please download an inventory report with a length of 1 week, starting on Monday and ending on Sunday")
	print("Length of time for current inventory report is incorrect")
	exit()

period1day1 = date(2024,1,1)

if((startdate - period1day1).days % 7 != 0):
	print("Please download an inventory report with a length of 1 week, starting on Monday and ending on Sunday")
	print("Current inventory report does not begin on a Monday")
	exit()

week = (startdate - period1day1).days / 7
period = int(week / 4 + 1)
week = int(week % 4 + 1)
periodweek = "P" + str(period) + "W" + str(week)

print(periodweek)



