def querys_sql(id_user):

    query = f"""
SELECT gamertag FROM Jogadores
WHERE id={id_user}
UNION ALL
SELECT COUNT(id_user) FROM Placement
WHERE id_user={id_user}
UNION ALL
SELECT COUNT(id_user) FROM Placement
WHERE id_user={id_user} AND placement=1
UNION ALL
SELECT COUNT(id_user) FROM Placement
WHERE id_user={id_user} AND placement<=3 AND placement>1
UNION ALL
SELECT COUNT(id_user) FROM Placement
WHERE id_user={id_user} AND placement<=8 AND placement>3
UNION ALL
SELECT COUNT(id_set) AS Vitorias_Dark FROM (SELECT tab1.id_set, tab1.round, tab1.id_player1,tab1.Jogador_1, tab1.score1, tab2.id_player2, tab2.Jogador_2, tab2.score2 FROM (SELECT Partidas.id_set, round, id_player1, gamertag as Jogador_1, score1 FROM Partidas LEFT JOIN Jogadores ON Jogadores.id=Partidas.id_player1) AS tab1
LEFT JOIN
(SELECT Partidas.id_set, round, id_player2, gamertag as Jogador_2, score2 FROM Partidas LEFT JOIN Jogadores ON Jogadores.id=Partidas.id_player2) AS tab2 ON tab2.id_set=tab1.id_set) as tab3
WHERE id_player1={id_user} AND score1>score2 OR id_player2={id_user} AND score2>score1
UNION ALL
SELECT COUNT(id_set) AS Derrota_Dark FROM (SELECT tab1.id_set, tab1.round, tab1.id_player1,tab1.Jogador_1, tab1.score1, tab2.id_player2, tab2.Jogador_2, tab2.score2 FROM (SELECT Partidas.id_set, round, id_player1, gamertag as Jogador_1, score1 FROM Partidas LEFT JOIN Jogadores ON Jogadores.id=Partidas.id_player1) AS tab1
LEFT JOIN
(SELECT Partidas.id_set, round, id_player2, gamertag as Jogador_2, score2 FROM Partidas LEFT JOIN Jogadores ON Jogadores.id=Partidas.id_player2) AS tab2 ON tab2.id_set=tab1.id_set) as tab3
WHERE id_player1={id_user} AND score1<score2 OR id_player2={id_user} AND score2<score1
UNION ALL
SELECT COUNT(id_set) AS Derrota_Dark FROM (SELECT tab1.id_set, tab1.round, tab1.id_player1,tab1.Jogador_1, tab1.score1, tab2.id_player2, tab2.Jogador_2, tab2.score2 FROM (SELECT Partidas.id_set, round, id_player1, gamertag as Jogador_1, score1 FROM Partidas LEFT JOIN Jogadores ON Jogadores.id=Partidas.id_player1) AS tab1
LEFT JOIN
(SELECT Partidas.id_set, round, id_player2, gamertag as Jogador_2, score2 FROM Partidas LEFT JOIN Jogadores ON Jogadores.id=Partidas.id_player2) AS tab2 ON tab2.id_set=tab1.id_set) as tab3
WHERE id_player1={id_user} OR id_player2={id_user}
"""

    return query


def head_a_head_number_set(id_user1, id_user2):

    query = f"""
SELECT gamertag FROM Jogadores
WHERE id={id_user1}
UNION ALL
SELECT gamertag FROM Jogadores
WHERE id={id_user2}
UNION ALL
SELECT COUNT(id_set) FROM (SELECT tab1.id_set, tab1.round, tab1.id_player1,tab1.Jogador_1, tab1.score1, tab2.id_player2, tab2.Jogador_2, tab2.score2 FROM (SELECT Partidas.id_set, round, id_player1, gamertag as Jogador_1, score1 FROM Partidas LEFT JOIN Jogadores ON Jogadores.id=Partidas.id_player1) AS tab1
LEFT JOIN
(SELECT Partidas.id_set, round, id_player2, gamertag as Jogador_2, score2 FROM Partidas LEFT JOIN Jogadores ON Jogadores.id=Partidas.id_player2) AS tab2 ON tab2.id_set=tab1.id_set) as tab3
WHERE id_player1={id_user2} AND id_player2={id_user1} OR id_player2={id_user2} AND id_player1={id_user1}
UNION ALL
SELECT COUNT(id_set) FROM (SELECT tab1.id_set, tab1.round, tab1.id_player1,tab1.Jogador_1, tab1.score1, tab2.id_player2, tab2.Jogador_2, tab2.score2 FROM (SELECT Partidas.id_set, round, id_player1, gamertag as Jogador_1, score1 FROM Partidas LEFT JOIN Jogadores ON Jogadores.id=Partidas.id_player1) AS tab1
LEFT JOIN
(SELECT Partidas.id_set, round, id_player2, gamertag as Jogador_2, score2 FROM Partidas LEFT JOIN Jogadores ON Jogadores.id=Partidas.id_player2) AS tab2 ON tab2.id_set=tab1.id_set) as tab3
WHERE id_player1={id_user1} AND id_player2={id_user2} AND score1>score2 OR id_player2={id_user1} AND id_player1={id_user2} AND score2>score1
UNION ALL
SELECT COUNT(id_set) FROM (SELECT tab1.id_set, tab1.round, tab1.id_player1,tab1.Jogador_1, tab1.score1, tab2.id_player2, tab2.Jogador_2, tab2.score2 FROM (SELECT Partidas.id_set, round, id_player1, gamertag as Jogador_1, score1 FROM Partidas LEFT JOIN Jogadores ON Jogadores.id=Partidas.id_player1) AS tab1
LEFT JOIN
(SELECT Partidas.id_set, round, id_player2, gamertag as Jogador_2, score2 FROM Partidas LEFT JOIN Jogadores ON Jogadores.id=Partidas.id_player2) AS tab2 ON tab2.id_set=tab1.id_set) as tab3
WHERE id_player1={id_user2} AND id_player2={id_user1} AND round='Grand Final' OR id_player2={id_user2} AND id_player1={id_user1} AND round='Grand Final'
UNION ALL
SELECT COUNT(id_set) FROM (SELECT tab1.id_set, tab1.round, tab1.id_player1,tab1.Jogador_1, tab1.score1, tab2.id_player2, tab2.Jogador_2, tab2.score2 FROM (SELECT Partidas.id_set, round, id_player1, gamertag as Jogador_1, score1 FROM Partidas LEFT JOIN Jogadores ON Jogadores.id=Partidas.id_player1) AS tab1
LEFT JOIN
(SELECT Partidas.id_set, round, id_player2, gamertag as Jogador_2, score2 FROM Partidas LEFT JOIN Jogadores ON Jogadores.id=Partidas.id_player2) AS tab2 ON tab2.id_set=tab1.id_set) as tab3
WHERE id_player1={id_user1} AND id_player2={id_user2} AND round='Grand Final' AND score1>score2 OR id_player2={id_user1} AND id_player1={id_user2} AND round='Grand Final' AND score2>score1
UNION ALL
SELECT COUNT(id_set) FROM (SELECT tab1.id_set, tab1.round, tab1.id_player1,tab1.Jogador_1, tab1.score1, tab2.id_player2, tab2.Jogador_2, tab2.score2 FROM (SELECT Partidas.id_set, round, id_player1, gamertag as Jogador_1, score1 FROM Partidas LEFT JOIN Jogadores ON Jogadores.id=Partidas.id_player1) AS tab1
LEFT JOIN
(SELECT Partidas.id_set, round, id_player2, gamertag as Jogador_2, score2 FROM Partidas LEFT JOIN Jogadores ON Jogadores.id=Partidas.id_player2) AS tab2 ON tab2.id_set=tab1.id_set) as tab3
WHERE id_player1={id_user2} AND id_player2={id_user1} AND round='Grand Final Reset' OR id_player2={id_user2} AND id_player1={id_user1} AND round='Grand Final Reset'
UNION ALL
SELECT COUNT(id_set) FROM (SELECT tab1.id_set, tab1.round, tab1.id_player1,tab1.Jogador_1, tab1.score1, tab2.id_player2, tab2.Jogador_2, tab2.score2 FROM (SELECT Partidas.id_set, round, id_player1, gamertag as Jogador_1, score1 FROM Partidas LEFT JOIN Jogadores ON Jogadores.id=Partidas.id_player1) AS tab1
LEFT JOIN
(SELECT Partidas.id_set, round, id_player2, gamertag as Jogador_2, score2 FROM Partidas LEFT JOIN Jogadores ON Jogadores.id=Partidas.id_player2) AS tab2 ON tab2.id_set=tab1.id_set) as tab3
WHERE id_player1={id_user1} AND id_player2={id_user2} AND round='Grand Final Reset' AND score1>score2 OR id_player2={id_user1} AND id_player1={id_user2} AND round='Grand Final Reset' AND score2>score1"""

    return query


def ranking_brazil():

    query = """
SELECT gamertag, COUNT(*) AS Vezes from placement
LEFT JOIN
Jogadores ON id_user=id
WHERE placement=1 AND  country='Brazil'
GROUP By gamertag	
ORDER BY Vezes DESC"""

    return query


def ranking_brazil_pogchamp():

    query = """
SELECT gamertag, COUNT(*) AS VEZES FROM (SELECT * FROM Placement
LEFT JOIN
Eventos
On Eventos.id=Placement.id_event
LEFT JOIN
Jogadores
ON Placement.id_user=Jogadores.id) AS t1
WHERE slug like '%pog%' and placement=1
GROUP By gamertag	
ORDER BY Vezes DESC"""

    return query


def hxh_fast(id_user1, id_user2):

    query = f"""
SELECT gamertag FROM Jogadores
WHERE id={id_user1}
UNION ALL
SELECT gamertag FROM Jogadores
WHERE id={id_user2}
UNION ALL
SELECT count(id_set) from banana
WHERE id_player1={id_user2} AND id_player2={id_user1} OR id_player2={id_user2} AND id_player1={id_user1}
UNION ALL
SELECT count(id_set) from banana
WHERE id_player1={id_user1} AND id_player2={id_user2} AND score1>score2 OR id_player2={id_user1} AND id_player1={id_user2} AND score2>score1
UNION ALL
SELECT count(id_set) from banana
WHERE id_player1={id_user2} AND id_player2={id_user1} AND round='Grand Final' OR id_player2={id_user2} AND id_player1={id_user1} AND round='Grand Final'
UNION ALL
SELECT count(id_set) from banana
WHERE id_player1={id_user1} AND id_player2={id_user2} AND round='Grand Final' AND score1>score2 OR id_player2={id_user1} AND id_player1={id_user2} AND round='Grand Final' AND score2>score1
UNION ALL
SELECT count(id_set) from banana
WHERE id_player1={id_user2} AND id_player2={id_user1} AND round='Grand Final Reset' OR id_player2={id_user2} AND id_player1={id_user1} AND round='Grand Final Reset'
UNION ALL
SELECT count(id_set) from banana
WHERE id_player1={id_user1} AND id_player2={id_user2} AND round='Grand Final Reset' AND score1>score2 OR id_player2={id_user1} AND id_player1={id_user2} AND round='Grand Final Reset' AND score2>score1"""
    return query


def banana():

    query = """
CREATE TEMP TABLE banana as SELECT * FROM(SELECT * FROM (SELECT tab1.id_set, tab1.round, tab1.id_player1,tab1.Jogador_1, tab1.score1, tab2.id_player2, tab2.Jogador_2, tab2.score2 FROM (SELECT Partidas.id_set, round, id_player1, gamertag as Jogador_1, score1 FROM Partidas LEFT JOIN Jogadores ON Jogadores.id=Partidas.id_player1) AS tab1
LEFT JOIN
(SELECT Partidas.id_set, round, id_player2, gamertag as Jogador_2, score2 FROM Partidas LEFT JOIN Jogadores ON Jogadores.id=Partidas.id_player2) AS tab2 ON tab2.id_set=tab1.id_set) as tab3)
"""
    return query


def fast_user_info(id_p1):

    query = f"""
SELECT gamertag FROM Jogadores
WHERE id={id_p1}
UNION ALL
SELECT COUNT(id_user) FROM Placement
WHERE id_user={id_p1}
UNION ALL
SELECT COUNT(id_user) FROM Placement
WHERE id_user={id_p1} AND placement=1
UNION ALL
SELECT COUNT(id_user) FROM Placement
WHERE id_user={id_p1} AND placement<=3 AND placement>1
UNION ALL
SELECT COUNT(id_user) FROM Placement
WHERE id_user={id_p1} AND placement<=8 AND placement>3
UNION ALL
SELECT COUNT(id_set) from banana
WHERE id_player1={id_p1} AND score1>score2 OR id_player2={id_p1} AND score2>score1
UNION ALL
SELECT COUNT(id_set) from banana
WHERE id_player1={id_p1} AND score1<score2 OR id_player2={id_p1} AND score2<score1
UNION ALL
SELECT COUNT(id_set) from banana
WHERE id_player1={id_p1} OR id_player2={id_p1}
    """
    return query


def partidas_event():
    query = """
CREATE TEMP TABLE partidas_event as SELECT * FROM (SELECT *  FROM Partidas
LEFT JOIN
Eventos
ON  Eventos.id=Partidas.id_event)"""
    return query


def fast_user_info_without_banana(id_p1):

    query = f"""
SELECT gamertag FROM Jogadores
WHERE id={id_p1}
UNION ALL
SELECT COUNT(id_user) FROM Placement
WHERE id_user={id_p1}
UNION ALL
SELECT COUNT(id_user) FROM Placement
WHERE id_user={id_p1} AND placement=1
UNION ALL
SELECT COUNT(id_user) FROM Placement
WHERE id_user={id_p1} AND placement<=3 AND placement>1
UNION ALL
SELECT COUNT(id_user) FROM Placement
WHERE id_user={id_p1} AND placement<=8 AND placement>3
UNION ALL
SELECT COUNT(id_set) from Partidas
WHERE id_player1={id_p1} AND score1>score2 OR id_player2={id_p1} AND score2>score1
UNION ALL
SELECT COUNT(id_set) from Partidas
WHERE id_player1={id_p1} AND score1<score2 OR id_player2={id_p1} AND score2<score1
UNION ALL
SELECT COUNT(id_set) from Partidas
WHERE id_player1={id_p1} OR id_player2={id_p1}
    """
    return query


def hxh_fast_pog(id_user1, id_user2):

    query = f"""
SELECT gamertag FROM Jogadores
WHERE id={id_user1}
UNION ALL
SELECT gamertag FROM Jogadores
WHERE id={id_user2}
UNION ALL
SELECT count(id_set) from partidas_event
WHERE id_player1={id_user2} AND id_player2={id_user1} and slug like '%pog%' OR id_player2={id_user2} AND id_player1={id_user1} and slug like '%pog%'
UNION ALL
SELECT count(id_set) from partidas_event
WHERE id_player1={id_user1} AND id_player2={id_user2} AND score1>score2 and slug like '%pog%' OR id_player2={id_user1} AND id_player1={id_user2} AND score2>score1 and slug like '%pog%'
UNION ALL
SELECT count(id_set) from partidas_event
WHERE id_player1={id_user2} AND id_player2={id_user1} AND round='Grand Final' and slug like '%pog%' OR id_player2={id_user2} AND id_player1={id_user1} AND round='Grand Final' and slug like '%pog%'
UNION ALL
SELECT count(id_set) from partidas_event
WHERE id_player1={id_user1} AND id_player2={id_user2} AND round='Grand Final' AND score1>score2 and slug like '%pog%' OR id_player2={id_user1} AND id_player1={id_user2} AND round='Grand Final' AND score2>score1 and slug like '%pog%'
UNION ALL
SELECT count(id_set) from partidas_event
WHERE id_player1={id_user2} AND id_player2={id_user1} AND round='Grand Final Reset' and slug like '%pog%' OR id_player2={id_user2} AND id_player1={id_user1} AND round='Grand Final Reset' and slug like '%pog%'
UNION ALL
SELECT count(id_set) from partidas_event
WHERE id_player1={id_user1} AND id_player2={id_user2} AND round='Grand Final Reset' AND score1>score2 and slug like '%pog%' OR id_player2={id_user1} AND id_player1={id_user2} AND round='Grand Final Reset' AND score2>score1 and slug like '%pog%'
    """
    return query


def hxh_fast_without_banana(id_user1, id_user2):

    query = f"""
SELECT gamertag FROM Jogadores
WHERE id={id_user1}
UNION ALL
SELECT gamertag FROM Jogadores
WHERE id={id_user2}
UNION ALL
SELECT count(id_set) from Partidas
WHERE id_player1={id_user2} AND id_player2={id_user1} OR id_player2={id_user2} AND id_player1={id_user1}
UNION ALL
SELECT count(id_set) from Partidas
WHERE id_player1={id_user1} AND id_player2={id_user2} AND score1>score2 OR id_player2={id_user1} AND id_player1={id_user2} AND score2>score1
UNION ALL
SELECT count(id_set) from Partidas
WHERE id_player1={id_user2} AND id_player2={id_user1} AND round='Grand Final' OR id_player2={id_user2} AND id_player1={id_user1} AND round='Grand Final'
UNION ALL
SELECT count(id_set) from Partidas
WHERE id_player1={id_user1} AND id_player2={id_user2} AND round='Grand Final' AND score1>score2 OR id_player2={id_user1} AND id_player1={id_user2} AND round='Grand Final' AND score2>score1
UNION ALL
SELECT count(id_set) from Partidas
WHERE id_player1={id_user2} AND id_player2={id_user1} AND round='Grand Final Reset' OR id_player2={id_user2} AND id_player1={id_user1} AND round='Grand Final Reset'
UNION ALL
SELECT count(id_set) from Partidas
WHERE id_player1={id_user1} AND id_player2={id_user2} AND round='Grand Final Reset' AND score1>score2 OR id_player2={id_user1} AND id_player1={id_user2} AND round='Grand Final Reset' AND score2>score1"""
    return query