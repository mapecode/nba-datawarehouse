from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# URL page we will scraping (see image above)
url = "https://en.wikipedia.org/wiki/Wikipedia:WikiProject_National_Basketball_Association/National_Basketball_Association_team_abbreviations"
# this is the HTML from the given URL
html = urlopen(url)
soup = BeautifulSoup(html, features="html.parser")

# avoid the first header row
rows = soup.findAll('tr')[1:]

team_names = [[td.getText().replace('\n','') for td in rows[i].findAll('td')]
            for i in range(len(rows))]


# Create DataFrame
team_names_df = pd.DataFrame(team_names, columns = ['Abreviation','Name'])

# Save stats in csv file
team_names_df.to_csv('team_names.csv')