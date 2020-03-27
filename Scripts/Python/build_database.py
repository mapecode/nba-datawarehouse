from team_stats import *
from player_stats import *
import pandas as pd
import sqlite3 as sqlite
import os

players_df, teams_df = None, None
rookies_df, central_df = None, None

def load_data():
    global players_df, teams_df, rookies_df
    # Players DataFrame
    players_df = get_player_stats(2019).reset_index()
    players_df = players_df.rename(columns={'index': 'id'})

    # Teams Abbreviation DataFrame
    teams_abbreviation_df = get_entire_team_name()
    teams_abbreviation_df.at[23,'Key']= 'PHO'
    teams_abbreviation_df.at[1,'Key']= 'BOS'
    teams_abbreviation_df.at[2,'Key']= 'BRK'
    teams_abbreviation_df.at[3,'Key']= 'CHO'



    # Teams DataFrame
    teams_df = get_team_stats(2019).reset_index()
    teams_df = teams_df.rename(columns={'index': 'id'})
    teams_df.insert(1, "Key", teams_abbreviation_df['Key'], False)

    # Rookie DataFrame
    rookies_df = get_rookie_stats(2019).reset_index()
    rookies_df = rookies_df.rename(columns={'index': 'id'})


def clean_data():
    global players_df, teams_df, rookies_df
    # Remove columns that we don't use
    players_df = players_df.drop('eFG%', 1)
    teams_df = teams_df.drop(
        ['Div', 'MOV/A', 'ORtg/A', 'DRtg/A', 'NRtg/A'], 1)
    rookies_df = rookies_df.drop(
        ['Yrs', 'MP', 'PTS', 'TRB', 'AST'], 1)

    # Remove NaN rows
    players_df = players_df.dropna()
    teams_df = teams_df.dropna()
    rookies_df = rookies_df.dropna()

    # Remove players with invalid team
    for i, row in players_df.iterrows():
        if row['Tm'] == 'TOT':
            continue

        if row['Tm'] not in list(teams_df['Key']):
            players_df = players_df.drop(index=i)

    # Reboot index, because it need start with 0
    rookies_df = rookies_df.reset_index().drop('index', 1)



def build_central_df():
    global players_df, teams_df, rookies_df, central_df
    central_df = pd.DataFrame(
        columns=['id_player', 'id_team', 
        'Player', 'Team', 'Rookie'])

    # build id_player
    central_df['id_player'] = players_df['id']
    # build player names
    central_df['Player'] = players_df['Player']

    for i, row in central_df.iterrows():
        # build id team
        if players_df.loc[i]['Tm'] == 'TOT':
            # id for total statistics, be cause he 
            # played in more one team
            row['id_team'] = -1
        else:
            row['id_team'] = int(teams_df.loc[list(
                teams_df['Key']).index(
                    players_df.loc[i]['Tm'])]['id'])

        # build team name
        if row['id_team'] == -1:
            row['Team'] = 'Total'
        else:
            row['Team'] = teams_df.loc[list(
                teams_df['id']).index(row['id_team'])]['Team']

        # build is rookie
        if row['Player'] in list(rookies_df['Player']):
            row['Rookie'] = int(rookies_df.loc[list(
                rookies_df['Player']).index(row['Player'])]['id'])

        central_df.loc[i] = row
    
    # Remove team column, because team info will be in the central table
    players_df = players_df.drop('Tm', 1)

def build_database():
    global players_df, teams_df, rookies_df, central_df

    sql_data = 'nba_data.db'
    connection = sqlite.connect(sql_data)

    # load db creation script
    file = open('creation.sql', 'r')
    query = ''
    for line in file:
        query += line

    # db tables creation
    connection.cursor().executescript(query)

    # Load players_df in db
    players_df.to_sql('PLAYERS', connection, 
        if_exists='append', index=False)

    # Load teams_df in db
    teams_df.to_sql('TEAMS', connection, 
        if_exists='append', index=False)

    # Load rookies_df in db
    rookies_df.to_sql('ROOKIES', connection, 
        if_exists='append', index=False)

    # Load central_df in db
    central_df.to_sql('PLAYER_TEAM', connection, 
        if_exists='append', index=False)

    # Close the connection with the db
    connection.close()


if __name__ == '__main__':
    if os.path.isfile('nba_data.db'):
        print('The db file exists, remove to build newly')
    else:
        load_data()
        clean_data()
        build_central_df()
        build_database()
