import sqlite3
from querry_sql import querys_sql, fast_user_info, banana

db = sqlite3.connect("twitchbotdb.db")


def info_user():
    txt = ''
    dados = db.execute(querys_sql(1163020)).fetchall()
    txt += f"{dados[0][0]}||" \
           f"{'Nº Torneios:':<12} {dados[1][0]:<8} {'%':^5}||" \
           f"{'Nº Campeão:':<12} {dados[2][0]:<8} {dados[2][0] / dados[1][0] * 100:.2f}%||" \
           f"{'Nº 2º e 3º:':<12} {dados[3][0]:<8} {dados[3][0] / dados[1][0] * 100:.2f}%||" \
           f"{'Nº 4º a 8º:':<12} {dados[4][0]:<8} {dados[4][0] / dados[1][0] * 100:.2f}%||" \
           f"{'Nº Sets:':<12} {dados[7][0]:<8} {'%':^5}||" \
           f"{'Vitorias:':<12} {dados[5][0]:<8} {dados[5][0] / dados[7][0] * 100:.2f}%||" \
           f"{'Derrotas:':<12} {dados[6][0]:<8} {dados[6][0] / dados[7][0] * 100:.2f}%||"

    return txt


def info_user2(id_=1163020):

    db = sqlite3.connect(r"twitchbotdb.db")

    db.execute(banana())
    dados = db.execute(fast_user_info(id_)).fetchall()

    #dados = db.execute(querys_sql(id_)).fetchall()
    try:
        txt = f"{dados[0][0]} competiu em {dados[1][0]} torneios na plataforma Start, " \
              f"foi campeão em {dados[2][0]} deles, " \
              f"{dados[2][0] / dados[1][0] * 100:.2f}% dos torneios. " \
              f"Ficou em 2º ou 3º {dados[3][0]} vezes, {dados[3][0] / dados[1][0] * 100:.2f}% dos torneios. " \
              f"Ficou de 4º a 8º {dados[4][0]} vezes, {dados[4][0] / dados[1][0] * 100:.2f}% dos torneios. || " \
              f"{dados[0][0]} tem um total de {dados[7][0]} partidas disputadas, " \
              f"venceu {dados[5][0]} vezes {dados[5][0] / dados[7][0] * 100:.2f}% das partidas"
    except:
        txt = f"Dados Incompletos desse Jogador"

    db.close()
    return txt

