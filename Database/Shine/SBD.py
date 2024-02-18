import requests, openpyxl
from bs4 import BeautifulSoup

excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = 'Shine Web Development Job Search'
print(excel.sheetnames)
sheet.append(['Job Profile', 'Company', 'Location', 'Experience'])

try:

    url = "https://www.shine.com/job-search/backend-developer-jobs?q=backend%20developer"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')


    jobs = soup.find('div', class_="parentClass position-relative").find_all('div', class_="false")

    for job in jobs:
        profile = job.find('h2').text

        company = job.find('div', class_="jobCard_jobCard_cName__mYnow").get_text(strip=True)

        location = job.find('div', class_="jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2").get_text(strip=True)

        experience = job.find('div', class_="jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t").text

        print(profile, company, location, experience)
        sheet.append([profile, company, location, experience])
        
except Exception as e:
    print(e)

excel.save('Database\Shine\Data\SBD.xlsx')
    
