#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import re
import time
import requests

movie   = 'clouds_2020'
name    = 'ziyi_he'
pageNum = 1

url     = 'https://www.rottentomatoes.com/m/clouds_2020/reviews/'

with open('data/ziyi_he_clouds_2020.txt','w') as fw:
    
    for p in range(1,pageNum+1): 
        
        print ('Getting page',p)
        
        html=None        
        
        if p==1: 
            pageLink=url 
        else:
            pageLink=url+'?page='+str(p)+'&sort='
            
        for i in range(1): 
            try:
                response = requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content

                break 
           
            except:
                print ('failed attempt #',i)
                time.sleep(2)

        if not html:
            print('could not get page #', p)
            continue 
            
     
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml')
        
        reviews=soup.findAll('div', {'class':re.compile('review_table_row')})
        
        print ('Parsing page',p)
        
        
        for review in reviews:
            
            critic,rating,source,text,date='NA','NA','NA','NA','NA'
            
            criticAdams=review.find('a',{'href':re.compile('/critic/')})
            if criticAdams: 
                critic=criticAdams.text.strip()
            
            ratingAdams=review.find('a',{'href':re.compile('/rating/')})
            if ratingAdams: 
                rating=ratingAdams.text.strip()
                
            sourceAdams=review.find('a',{'href':re.compile('/source/')})
            if sourceAdams: 
                source=sourceAdams.text.strip()
                
            textAdams=review.find('a',{'href':re.compile('/text/')})
            if textAdams: 
                text=textAdams.text.strip()
                
            dateAdams=review.find('a',{'href':re.compile('/date/')})
            if dateAdams: 
                date=dateAdams.text.strip()
                
            
                
          
            fw.write(critic+'\t'+rating+'\t'+source+'\t'+text+'\t'+date+'\n')

print ('Done!')
        
 

