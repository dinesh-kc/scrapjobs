from bs4 import BeautifulSoup as bs
import requests
import csv

url = 'https://kathmandujobs.com/jobs/category/others'
r = requests.get(url)
soup = bs(r.content,'lxml')
job_divs = soup.find_all('div',attrs = {
                                'class':'single-post d-flex row no-gutters job_list'
                })

csv_file = open('job_dataset.csv','a')

csvwriter = csv.writer(csv_file)
# csvwriter.writerow(['image','title','location','category','job_type'])

for job_div in job_divs:
    image  = job_div.find('img')['src']
    title = job_div.find('h4').text
    # description =

    listing_div = job_div.find('div',attrs={'class':'job-listing-footer'})
    ul = listing_div.find_all('li')

    location  = ul[0].text
    category = 'others'
    # qualification =
    #
    # experience_year =
    # salary =
    job_type = ul[1].text
    # deadline =
    # skills =
    csvwriter.writerow([image,title,location,category,job_type])

print('done')

csv_file.close()
