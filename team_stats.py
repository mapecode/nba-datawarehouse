from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


def get_team_stats(year):
    # URL page we will scraping (see image above)
    url = "https://www.basketball-reference.com/ \
    leagues/NBA_{}_ratings.html".format(year)
    # this is the HTML from the given URL
    html = urlopen(url)
    soup = BeautifulSoup(html, features="html.parser")

    # use findALL() to get the column headers
    soup.findAll('tr', limit=2)
    # use getText()to extract the text we need into a list
    headers = [th.getText() for th in 
        soup.findAll('tr', limit=2)[1].findAll('th')]  
    # the first row is not the header
    # exclude the first column as we will not need the ranking 
    # order from Basketball Reference for the analysis
    headers = headers[1:]

    # avoid the first header row
    rows = soup.findAll('tr')[1:]

    team_stats = [[td.getText() for td in rows[i].findAll('td')]
                  for i in range(len(rows))]

    team_df = pd.DataFrame(team_stats, columns=headers)

    return team_df.sort_values('Team')


def get_entire_team_name():
    # URL page we will scraping (see image above)
    url = "https://en.wikipedia.org/wiki/ \
    Wikipedia:WikiProject_National_Basketball_Association/ \
    National_Basketball_Association_team_abbreviations "
    # this is the HTML from the given URL
    html = urlopen(url)
    soup = BeautifulSoup(html, features="html.parser")

    # avoid the first header row
    rows = soup.findAll('tr')[1:]

    team_names = [[td.getText().replace('\n', '') for 
        td in rows[i].findAll('td')]
        for i in range(len(rows))]

    team_names_df = pd.DataFrame(team_names, 
        columns=['Key', 'Name'])
    return team_names_df.sort_values('Name')
