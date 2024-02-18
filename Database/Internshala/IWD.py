import requests, openpyxl
from bs4 import BeautifulSoup

excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = 'Internshala Web Development Job Search'
print(excel.sheetnames)
sheet.append(['Job Profile', 'Company', 'Location', 'Stipened'])
try:
    url = "https://internshala.com/internships/web-development-internship/"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')


    jobs = soup.find('div', class_="internship_list_container with_breadcrumbs").find_all('div', class_="internship_meta")

    for job in jobs:
        profile = job.find('h3', class_ ="heading_4_5 profile").a.text

        company = job.find('h4', class_="heading_6 company_name").get_text(strip=True)

        location = job.find('a', class_="location_link view_detail_button").get_text(strip=True)

        money = job.find('span', class_="stipend").text

        print(profile, company, location, money)
        sheet.append([profile, company, location, money])
     

except Exception as e:
    print(e)

excel.save('Database\Internshala\Data\IWD.xlsx')