import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from urllib.request import urlopen
from bs4 import BeautifulSoup

# start our query
# def startQuery():
url = "https://www.indeed.com/jobs?rq=1&q=software+developer&l=California&ts=1577149148422&from=searchOnSerp&rsIdx=0&mobtk=1dsqmkjebq45n800&fromage=last&mobRdr=1"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
type(soup)
title = soup.title
print(title)

# scrape links to job postings
# def scrapePage():
links = soup.find_all("a", {"target": "_blank"})#_blank
if links == []: print("Empty") 
else: 
    
    urls = []
    i = 0
    print("Not empty")
    for link in links:
        if link.get("href") is not None:
            urls.append(link.get("href"))
            print(link.get("href"))
            i = i+1
            
print(i)

# scrape postings array
# def scrapeAllPostings
postings = []
print("starting")
for url in urls:
    if ".com" not in url:
        url = "https://indeed.com/" + url
        #print("url")
    if "reviews" in url: 
        continue
    #print("here")
    html = urlopen(url)
    new_soup = BeautifulSoup(html, 'lxml')
    type(new_soup)
    site_title = new_soup.title
    print(site_title)
    titles = new_soup.findAll("h3")
    for t in titles:
        if t.get("class") == "icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title":
            title = t.text
            print(title + " here")
    
    posting = [site_title]    

# scrape postings array
# def scrapeAllPostings
postings = []
print("starting")
if urls[0] is not None:
    url = urls[0]
    if ".com" not in url:
        url = "https://indeed.com/" + url
        #print("url")
    print("here")
    html = urlopen(url)
    new_soup = BeautifulSoup(html, 'lxml')
    type(new_soup)
    site_title = new_soup.title
    print(site_title)
    titles = new_soup.findAll("h3")
    print("h3 titles")
    print(titles)
    
    # job title
    for t in titles:
        print(t['class'])
        if t['class'] == ['icl-u-xs-mb--xs', 'icl-u-xs-mt--none', 'jobsearch-JobInfoHeader-title']:
            job_title = t.text
            print(job_title)
        
    print(job_description)
    posting = [site_title]  


