#importing required modules..

import requests # give me the access to the website
import csv #
from bs4 import BeautifulSoup #parsing html code & take the infos that I want


date=input("enter a date like this MM/DD/YYYY : ")
page = requests.get(f'https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}')

def main(page):
    source = page.content
    soup = BeautifulSoup(source , 'lxml') #the whole page code..
    matchDetails = []
    tournment = soup.find_all('div',{'class' : 'matchCard'}) #specify what I need to take from it..
    def tournment_details(tournment):
        title = tournment.contents[1].find('h2').text.strip()
        all_matches=tournment.contents[3].find_all('li')
        n_of_matches=len(all_matches)
        for i in range(n_of_matches):
            team_1= all_matches[i].find('div',{'class':'teamA'}).text.strip()
            team_2= all_matches[i].find('div',{'class':'teamB'}).text.strip()
            result= all_matches[i].find('div',{'class':'MResult'}).find_all('span',{'class':'score'})
            score = f'{result[0].text.strip()}-{result[1].text.strip()}'
            match_time = all_matches[i].find('div',{'class':'MResult'}).find('span',{'class':'time'}).text.strip()
            matchDetails.append({'tournment':title, '1st team':team_1,'2nd team':team_2,'time':match_time,'score':score})

    for i in range(len(tournment)):
        tournment_details(tournment[i])

    keys= matchDetails[0].keys()
    with open('/home/mohammed/Desktop/aaaa.csv','w') as output_file:
        dict_Writer = csv.DictWriter(output_file,keys)
        dict_Writer.writeheader()
        dict_Writer.writerows(matchDetails)
        print('file created')


main(page)