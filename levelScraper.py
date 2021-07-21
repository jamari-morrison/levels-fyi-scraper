import selenium
from selenium import webdriver
import time


def yoinkData(filepath, url, numpages, sleepTime):
    #change this URL to change the filters
    browser.get(url)

    time.sleep(sleepTime+2)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    f = open(filepath, 'w')
    header = "Company,State,City,Date Added,Level Name,Tag,Years At Company,Total Years of Experience,Total Compensation,Base,Stock,Bonus\n"
    f.write(header)



    for i in range(1, numpages):
        for j in range(1, 11):
            company=''
            try:
                company = browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[4]/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr["+str(j)+"]/td[2]/span[2]/a").text
            except selenium.common.exceptions.NoSuchElementException:
                company = browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[4]/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr["+str(j)+"]/td[2]/span[2]").text

            location = ''
            try:
                location = browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[4]/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr["+str(j)+"]/td[2]/span[4]").text.split("|")[0]
            except selenium.common.exceptions.NoSuchElementException:
                location=" "

            date = ''
            try:
                date = browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[4]/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr["+str(j)+"]/td[2]/span[4]").text.split("|")[1]
            except selenium.common.exceptions.NoSuchElementException:
                date=" "

            lvlname = ''
            try:
                lvlname = browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[4]/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr["+str(j)+"]/td[3]/span[1]").text
            except selenium.common.exceptions.NoSuchElementException:
                lvlname = " "

            try:
                tag = browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[4]/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr["+str(j)+"]/td[3]/span[2]/a").text
            except selenium.common.exceptions.NoSuchElementException:
                tag = browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[4]/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[6]/td[3]/span[2]").text

            yrsAtCompany = ''
            try:
                yrsAtCompany = browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[4]/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr["+str(j)+"]/td[4]/span").text.split("/")[0]
            except selenium.common.exceptions.NoSuchElementException:
                yrsAtCompany = " "

            totalYOE = ''
            try:
                totalYOE = browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[4]/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr["+str(j)+"]/td[4]/span").text.split("/")[1]
            except selenium.common.exceptions.NoSuchElementException:
                totalYOE = " "

            totalComp = ''
            try:
                totalComp = browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[4]/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr["+str(j)+"]/td[5]/div/div/span[1]").text
            except selenium.common.exceptions.NoSuchElementException:
                totalComp=" "

            base = ''
            try:
                base = browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[4]/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr["+str(j)+"]/td[5]/div/div/span[2]").text.split("|")[0]
            except selenium.common.exceptions.NoSuchElementException:
                base=" "

            stocks = ''
            try:
                stocks = browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[4]/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr["+str(j)+"]/td[5]/div/div/span[2]").text.split("|")[1]
            except selenium.common.exceptions.NoSuchElementException:
                stocks = " "

            bonus = ''
            try:
                bonus = browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[4]/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr["+str(j)+"]/td[5]/div/div/span[2]").text.split("|")[2]
            except selenium.common.exceptions.NoSuchElementException:
                bonus = " "

            dataEntry = company + "," + location + "," + date + "," + lvlname + "," + tag + "," + yrsAtCompany + "," + totalYOE + "," + totalComp + ","+base+","+stocks+","+bonus+ "\n"
            f.write(dataEntry)

        browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div[4]/div/div[1]/div[1]/div[3]/div[2]/ul/li[9]/a').click()
        time.sleep(sleepTime)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)


    f.close()

#to use:
#1.) Edit the filepath to point to a csv
#2.) Edit the URL to be the levels.fyi search page with your desired filters applied
    #default: https://www.levels.fyi/comp.html?track=Software%20Engineer
    #example with 0yoe: https://www.levels.fyi/comp.html?track=Software%20Engineer&yoestart=0&yoeend=0
#3.) Edit numpages to be the correct number of pages to scrape
    #(if you enter a number larger, then the code will successfully write all the data but jsut error out at the end)
#4.) Edit the sleepTime to be how long pages take to load for you


chromedriverPath = './chromedriver.exe'
filepath = "./levels.csv"
url = 'https://www.levels.fyi/comp.html?track=Software%20Engineer&yoestart=0&yoeend=0'
numpages = 500
browser = webdriver.Chrome(chromedriverPath)
sleepTime = 2
yoinkData(filepath, url, numpages, sleepTime)
