from bs4 import BeautifulSoup
import requests

# Web Scraping Part
response = requests.get("http://www.sahiwal.comsats.edu.pk/ProgramOverviewOfSE.aspx")
content = response.text

soup = BeautifulSoup(content, 'html.parser')
data = soup.find_all('p')

for i in data:
    print(i.get_text())

# Admission Logic Part
req_inter_marks = 600
req_nts_marks = 50

marks = int(input("Enter intermediate marks: "))
entry_test = int(input("Enter NTS marks: "))

if marks >= req_inter_marks and entry_test > req_nts_marks:
    print("You are eligible for Admission")
else:
    print("You are not eligible for Admission")