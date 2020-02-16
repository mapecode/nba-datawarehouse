 /* Primera Vista */
CREATE VIEW NUM_PT(Id, Team, Conference, Players) AS 
    SELECT id_team, T.Team, Conf, count(*) AS PLAYERS 
    FROM PLAYER_TEAM PT, TEAMS T 
    WHERE PT.id_team = T.id AND T.Team not like("%Total%") 
    GROUP BY id_team, T.Team, T.Conf;

 /* Segunda vista */
 CREATE VIEW STAT_PT(Id, Key, Team, Conference, Players, Players_Perc, NoRookies, NoRookies_Perc, Rookies, Rookies_Perc) AS 
    SELECT NT.id AS Id, NT.Team AS Team, NT.Conference, NT.Players, ROUND(NT.Players/6.22, 2) AS "Players %",NT.Players - COUNT(*) AS "No Rookies", ROUND((NT.Players - COUNT(*))/6.22, 2) AS "No Rookies %",COUNT(*) AS Rookies,  ROUND(COUNT(*)/6.22, 2) AS "Rookies %" 
    FROM PLAYER_TEAM PT, NUM_PT NT 
    WHERE PT.id_team = NT.ID AND Rookie IN (SELECT ID FROM ROOKIES) 
    GROUP BY NT.ID, NT.Team, NT.Conference;