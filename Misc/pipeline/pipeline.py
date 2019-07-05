# pipeline.py


import requests as req
from bs4 import BeautifulSoup
import re



SEARCH_URL_TEMPLATE = "https://www.switchup.org/rankings/"
	
q = ['best-coding-bootcamps', 'best-online-bootcamps', 
 'best-data-science-bootcamps', 'best-web-design-bootcamps', 
 'best-cyber-security-bootcamps']




# scraping

def scraping(label, class_, url):
    
    res = req.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    scrap = soup.find_all(label, class_=class_)[0:20]
    
    return scrap



# ranking

def ranking():
    lst = []
    for i in range(len(q)):
        rank=scraping('span', 'ranking-item__rating--count', SEARCH_URL_TEMPLATE + q[i])
        for j in range(len(rank)):
            lst.append(j+1)
        
    return lst



# rating

def rating():
    lst = []
    for i in range(len(q)):
        rate = scraping('span', 'ranking-item__rating--value', SEARCH_URL_TEMPLATE + q[i])
        for j in range(len(rate)):
            lst.append(float(re.findall('\d.\d+',str(rate[j]))[0]))
    
    return lst




# reviews

def reviews():
    lst = []
    for i in range(len(q)):
        rev=scraping('span', 'ranking-item__rating--count', SEARCH_URL_TEMPLATE + q[i])
        for j in range(len(rev)):
            lst.append(re.sub(',', '', (re.findall('[0-9,]+',str(rev[j]))[0])))
    
    return lst   




# $$$$

def cost():
    lst = []
    for i in range(len(q)):
        c=scraping('div', 'ranking-item__price', SEARCH_URL_TEMPLATE + q[i])
        for j in range(len(c)):
            lst.append(len(re.findall('filled', str(c[j]))))
            
    return lst
    
    
    
# summary

def summary():
    lst = []
    for i in range(len(q)):
        summ=scraping('div', 'ranking-item__desc', SEARCH_URL_TEMPLATE + q[i])
        for j in range(len(summ)):
            lst.append(re.sub('\n', '', str(summ[j].text)).lstrip().rstrip())
    
    return lst  
    
    
    
# build function(s)

def return_results():
    rank = ranking()
    rate = rating()
    rev = reviews()
    c = cost()
    s = summary()
    result=[{'ranking':rank[i], 'rating':rate[i], 
             'reviews':rev[i], 'cost':c[i], 'summary':s[i]} for i in range(len(s))]
    
    return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



