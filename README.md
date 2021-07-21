# levels-fyi-scraper
Basic web scraper to grab levels.fyi data and put it into a csv

# To use:

## 1.) Edit the URL to be the levels.fyi search page with your desired filters applied

    default: https://www.levels.fyi/comp.html?track=Software%20Engineer
    example with 0yoe: https://www.levels.fyi/comp.html?track=Software%20Engineer&yoestart=0&yoeend=0
    
## 2.) Edit numpages to be the correct number of pages to scrape
(if you enter a number larger, then the code will successfully write all the data but jsut error out at the end)
    
## 3.) Edit the sleepTime to be how long the pages take to load for you

