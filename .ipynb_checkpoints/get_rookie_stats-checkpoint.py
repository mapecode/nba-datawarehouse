from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# NBA season we will be analyzing
year = 2019
# URL page we will scraping (see image above)
url = "https://www.basketball-reference.com/leagues/NBA_2019_rookies-season-stats.html".format(year)
# this is the HTML from the given URL
html = urlopen(url)
soup = BeautifulSoup(html,features="html.parser")

# use findALL() to get the column headers
soup.findAll('tr', limit=2)
# use getText()to extract the text we need into a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')] # the first row is not the header
# exclude the first column as we will not need the ranking order from Basketball Reference for the analysis
headers = headers[1:]

# avoid the first header row
rows = soup.findAll('tr')[1:]

rookie_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]

rookie_stats_df = pd.DataFrame(rookie_stats, columns = headers)

# Save stats in csv file
rookie_stats_df.to_csv('rookie_stats.csv')