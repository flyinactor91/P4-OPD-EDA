lines = []
newlines = []
with open('opddata.csv' , 'r') as fin: lines = fin.readlines()
#Split datetime into columns
for line in lines:
  line = line.split(',')
  newline = line[0].strip('"')
  for item in ['-',' ',':']: newline = newline.replace(item , ',')
  newline = line[0] + ',' + newline + ',' + ','.join(line[1:])
  newlines.append(newline)
#Add header line
header = 'datetime,year,month,day,hour,minute,second,lat,lon,reason,agency\n'
with open('opddatasplit2.csv' , 'w') as fout:
  fout.write(header + ''.join(newlines))
