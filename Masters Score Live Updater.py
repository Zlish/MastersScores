#!/usr/bin/env python
# coding: utf-8

# In[45]:


from bs4 import BeautifulSoup
import requests
import csv




URL = 'https://www.espn.com/golf/leaderboard'
page=requests.get(URL)
soup=BeautifulSoup(page.text, 'html.parser')



file= open('Masters_Snakedraft.csv', 'w')
writer = csv.writer(file)
writer.writerow(['Place', 'Name', 'Score'])


for table in soup.find_all('tbody'):
    leaderboard = soup.find_all('tr', class_ = 'Table__TR Table__even')
    
print("how many golfers do you want live scores for? --> type \"All\" for full leaderboard")
num_golfers=input()

if num_golfers=='All':
    for player in soup.find_all('tbody'):
        rows = player.find_all('tr')
        print('\n')
    
    
        for row in rows:
            POS = row.find('td', class_='tl Table__TD').text.strip() 
            Name = row.find_all('td', class_='tl Table__TD')[1].text
            Score = row.find_all('td', class_='Table__TD')[2].text
            print(POS,'\t', end=''),  print(Name, '\t', end=''), print(Score)
            
else:
    answer=''
    TotalScore=0
    num_golfers=int(num_golfers)
    
    #print("Please enter the player you want updated scores for: ")


    while num_golfers>0 :
        print("Please enter the player you want updated scores for: ")
        wanted_player=input()
        num_golfers=num_golfers-1
    
        for player in soup.find_all('tbody'):
            rows = player.find_all('tr')
            print('\n')
    
    
            for row in rows:
                POS = row.find('td', class_='tl Table__TD').text.strip() 
                Name = row.find_all('td', class_='tl Table__TD')[1].text
                Score = row.find_all('td', class_='Table__TD')[2].text
                
                if Name == wanted_player:
                    print(POS,'\t', end=''),  print(Name, '\t', end=''), print(Score) 
                    writer.writerow([POS, Name, Score])
                    if Score=='E':
                        Score=0
                    else:
                        Score=int(Score)
                        
                    TotalScore+=Score
                 
    print('\n The total score of your golfers is: ' , TotalScore)
    #print(TotalScore)


        
      
           
            
file.close()


    
   


# 

# In[ ]:




