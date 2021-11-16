import re

dates = '17 lutego 2022, 17.02.2022, 17 lut 2022'
pattern = "\d{1,2}.\d{1,2}.\d{4}"

correctDate = re.findall(pattern, dates)

strEnd = 'Correct Date is: {}'.format(correctDate)

print(strEnd)