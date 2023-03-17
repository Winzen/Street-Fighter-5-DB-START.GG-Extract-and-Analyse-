import sqlite3
from querry_sql import head_a_head_number_set, banana, hxh_fast, partidas_event, hxh_fast_pog

db = sqlite3.connect("twitchbotdb.db")


def head_x_head():
    dados = db.execute(head_a_head_number_set(244727, 722478)).fetchall()
    txt = ''
    txt += f"{dados[0][0]:<15} x {dados[1][0]:>18}||" \
           f"Numero de partidas jogadas: {dados[2][0]}||" \
           f"Vitorias: {dados[3][0]:<13} Vitorias: {dados[2][0] - dados[3][0]}|" \
           f"% de Vitorias: {(dados[3][0] / dados[2][0]) * 100:.2f}{'%':>5}" \
           f" de Vitorias: {((dados[2][0] - dados[3][0]) / dados[2][0]) * 100:.2f}%|"
    txt += f"Em Finais|" \
           f"Sets Em Finais: {dados[4][0]}|"\
           f"Vitorias: {dados[5][0]:<13} Vitorias: {dados[4][0] - dados[5][0]}|"\
           f"% de Vitorias: {(dados[5][0] / dados[4][0]) * 100:.2f}{'%':>5}"\
           f" de Vitorias: {((dados[4][0] - dados[5][0]) / dados[4][0]) * 100:.2f}%|"
    txt += f"Em RESET FINALS|"\
           f"Sets Em RESET: {dados[6][0]}|"\
           f"Vitorias: {dados[7][0]:<13} Vitorias: {dados[6][0] - dados[7][0]}|"\
           f"% de Vitorias: {(dados[7][0] / dados[6][0]) * 100:.2f}{'%':>5}"\
           f" de Vitorias: {((dados[6][0] - dados[7][0]) / dados[6][0]) * 100:.2f}%|"

    return txt


def head_x_head2(p1_id=244727, p2_id=722478):

    db = sqlite3.connect(r"twitchbotdb.db")
    db.execute(banana())
    dados = db.execute(hxh_fast(p1_id, p2_id)).fetchall()
    #dados = db.execute(head_a_head_number_set(p1_id, p2_id)).fetchall()
    txt = ''
    try:
        if dados[2][0] > 0:

            txt = f"Em todo o histórico do Start, {dados[0][0]} e {dados[1][0]} se enfrentaram {dados[2][0]} vezes. " \
                  f"Das partidas enfrentadas {dados[0][0]} ganhou {dados[3][0]} vezes, " \
                  f"{(dados[3][0] / dados[2][0]) * 100:.2f}% das partidas e " \
                  f"{dados[1][0]} ganhou {dados[2][0] - dados[3][0]} vezes, " \
                  f"{((dados[2][0] - dados[3][0]) / dados[2][0]) * 100:.2f}% das partidas ||"
        else:
            txt = f"Dados Incompletos dessa partida Ou Eles nuncam se enfrentaram"

        if dados[4][0] > 0:
            txt += f"Em Finais se enfrentam {dados[4][0]} vezes. " \
                   f"Com {dados[0][0]} ganhando {dados[5][0]} vezes, " \
                      f"sendo {(dados[5][0] / dados[4][0]) * 100:.2f}% das partidas e " \
                      f"{dados[1][0]} ganhou {dados[4][0] - dados[5][0]}, " \
                      f"{((dados[4][0] - dados[5][0]) / dados[4][0]) * 100:.2f}% das partidas || "

        if dados[6][0] > 0:
            txt += f"Em RESET FINALS se enfrentam {dados[6][0]} vezes. " \
                  f"Com {dados[0][0]} ganhando {dados[7][0]} vezes, " \
                  f"sendo {(dados[7][0] / dados[6][0]) * 100:.2f}% das partidas e " \
                  f"{dados[1][0]} ganhou {dados[6][0] - dados[7][0]}, " \
                  f"{((dados[6][0] - dados[7][0]) / dados[6][0]) * 100:.2f}% das partidas || "

    except:
        txt = f"Dados Incompletos dessa partida Ou Eles nuncam se enfrentaram"

    db.close()
    return txt


def head_x_head_pog_fast(p1_id=244727, p2_id=722478):

    db = sqlite3.connect(r"twitchbotdb.db")
    db.execute(partidas_event())
    dados = db.execute(hxh_fast_pog(p1_id, p2_id)).fetchall()
    #dados = db.execute(head_a_head_number_set(p1_id, p2_id)).fetchall()
    txt = ''
    try:
        if dados[2][0] > 0:

            txt = f"Nos confrontos do Pogchamp, {dados[0][0]} e {dados[1][0]} se enfrentaram {dados[2][0]} vezes. " \
                  f"Das partidas enfrentadas {dados[0][0]} ganhou {dados[3][0]} vezes, " \
                  f"{(dados[3][0] / dados[2][0]) * 100:.2f}% das partidas e " \
                  f"{dados[1][0]} ganhou {dados[2][0] - dados[3][0]} vezes, " \
                  f"{((dados[2][0] - dados[3][0]) / dados[2][0]) * 100:.2f}% de partidas ||"
        else:
            txt = f"Dados Incompletos dessa partida Ou Eles nuncam se enfrentaram"

        if dados[4][0] > 0:
            txt += f"Em Finais se enfrentam {dados[4][0]} vezes. " \
                   f"Com {dados[0][0]} ganhando {dados[5][0]} vezes, " \
                      f"sendo {(dados[5][0] / dados[4][0]) * 100:.2f}% das partidas e " \
                      f"{dados[1][0]} ganhou {dados[4][0] - dados[5][0]}, " \
                      f"{((dados[4][0] - dados[5][0]) / dados[4][0]) * 100:.2f}% das partidas || "

        if dados[6][0] > 0:
            txt += f"Em RESET FINALS se enfrentam {dados[6][0]} vezes. " \
                  f"Com {dados[0][0]} ganhando {dados[7][0]} vezes, " \
                  f"sendo {(dados[7][0] / dados[6][0]) * 100:.2f}% das partidas e " \
                  f"{dados[1][0]} ganhou {dados[6][0] - dados[7][0]}, " \
                  f"{((dados[6][0] - dados[7][0]) / dados[6][0]) * 100:.2f}% das partidas || "

    except:
        txt = f"Dados Incompletos dessa partida Ou Eles nuncam se enfrentaram"

    db.close()
    return txt


if __name__ == '__main__':
    print(head_x_head2(244727, 1163020))