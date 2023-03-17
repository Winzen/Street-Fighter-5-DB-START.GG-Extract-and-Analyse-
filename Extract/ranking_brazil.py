import sqlite3
from querry_sql import ranking_brazil_pogchamp, ranking_brazil


def rank_brazil_pog():
    db = sqlite3.connect("twitchbotdb.db")
    dados = db.execute(ranking_brazil_pogchamp()).fetchall()
    txt = 'Ranking Pogchamp - '
    for x, placement in enumerate(dados[:12]):
        txt += f"{x + 1}º {placement[0]}, {placement[1]}x campeão | "

    return txt


def rank_brazil_all():
    db = sqlite3.connect("twitchbotdb.db")
    dados = db.execute(ranking_brazil()).fetchall()
    txt = 'Ranking Geral Start gg - '
    for x, placement in enumerate(dados[:12]):
        txt += f"{x + 1}º {placement[0]}, {placement[1]}x campeão | "

    return txt

if __name__ == '__main__':
    print(rank_brazil_pog())