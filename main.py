# main.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import pandas as pd
import pickle

def configure_driver(driver_path):
    service = Service(driver_path)
    return webdriver.Chrome(service=service)

def scrape_job_data(driver, start_page, end_page):
    urls = []
    df = pd.DataFrame(columns=['Title', 'Description', 'Skills', 'Company', 'Experience', 'Location', 'URL'])
    for i in range(start_page, end_page):
        url_new = f'https://www.naukri.com/fresher-jobs-{i}'
        driver.get(url_new)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        with open(f"temp{i}.pickle", "wb") as f:
            pickle.dump(soup, f)
            print(f"{i}th page done")

        file = open(f"temp{i}.pickle", "rb")
        soup = pickle.load(file)
        results = soup.find(class_='list')
        job_elems = results.find_all('article', class_='jobTuple')

        for job_elem in job_elems:
            # Title
            title = job_elem.find('a', class_='title ellipsis').text
            # print("Title:", title)
            # print(' ')

            # Job Description
            description = job_elem.find('div', class_='ellipsis job-description').text
            if description is None:
                    description = job_elem.find('div', class_='clearboth description').text
            # print(description)
            # print(' ')

            # Company
            company = job_elem.find('a', class_='subTitle ellipsis fleft').text
            if company is None:
                    company = job_elem.find('p', class_='cpName').text
            # print("Company:", company)
            # print(' ')

            # Experience
            experience = job_elem.find('span', class_='slide-meta-exp')
            if experience is None:
                experience = job_elem.find('span', class_='slide-meta-exp pull-left') 
                if experience is None:
                        experience = job_elem.find('div', class_='exp')
                if experience is not None:
                    experience = experience.text.strip()
                else:
                    experience = ""
            # print("Experience:", experience)
            # print(' ')

            # Salary
            salary = job_elem.find('li', class_='fleft br2 placeHolderLi salary').text
            # print("Salary:", salary)
            # print(' ')

            # Location
            location = job_elem.find('li', class_='fleft br2 placeHolderLi location').text
            # print("Location:", location)
            # print(' ')

            # URL
            article_url = job_elem.find('a', class_='title ellipsis').get('href')
            driver.get(article_url)
            
            # Wait for the page to fully load (add necessary wait time)
            time.sleep(1)
            
            # Get the page source
            page_source = driver.page_source
            
            # Create a BeautifulSoup object
            soup = BeautifulSoup(page_source, 'html.parser')
            
            # Perform part 2 of your code
            key_skills_div = soup.find('div', class_='key-skill')
            if key_skills_div:
                skills = key_skills_div.find_all('a', class_='chip clickable')
                skill_list = [skill.text.strip() for skill in skills]
            else:
                skill_list = []
            # Go back to the previous page
            # response = requests.get(url)
            # soup = BeautifulSoup(response.content, 'html.parser')
            skill_list = ",".join(skill_list)
            print(skill_list)

            df = df.append({
                'URL': article_url, 'Title': title, 'Company': company, 'Description': description,
                'Experience': experience, 'Salary': salary, 'Location': location, 'Skills': skill_list
            }, ignore_index=True)
        file.close()

    return df

def main():
    chrome_driver_path = "data/chromedriver.exe"
    start_page = 1
    end_page = 70

    driver = configure_driver(chrome_driver_path)
    df = scrape_job_data(driver, start_page, end_page)
    driver.quit()

    df.to_csv("data/scraped_data.csv", index=False)
    print("Scraping completed and data saved to 'data/scraped_data.csv'.")

if __name__ == "__main__":
    main()
