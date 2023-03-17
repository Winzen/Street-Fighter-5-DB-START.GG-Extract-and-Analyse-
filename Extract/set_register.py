import requests as link
from requests.structures import CaseInsensitiveDict
import json
import sqlite3
from time import sleep
from datetime import datetime


def query(id_, pag_):
    query_ = """query{event(id:"""f"""{id_}""""""){
   sets(perPage:40, page:"""f"""{pag_}""""""){
    nodes{
      id
      fullRoundText
      slots{
        standing{
          entrant{
            participants{
              user{
                id
              }
            }
          }
          stats{
            score{
              value
            }
          }
        }
      }}}}}"""
    return query_


def sets():

    db = sqlite3.connect("twitchbotdb.db")

    link_para_api = 'https://api.smash.gg/gql/alpha'
    chave = ""
    protocolo = CaseInsensitiveDict()
    protocolo["Accept"] = "application/json"
    protocolo["Authorization"] = chave

    ids_events = db.execute(f"SELECT id FROM Eventos "
                            f"WHERE busca_jogador='REGISTRADO' "
                            f"AND busca_partidas!='REGISTRADO' "
                            f"AND ultima_busca_partidas!='{datetime.now().strftime('%d/%m/%Y')}'").fetchall()

    if len(ids_events) > 0:

        for id_event_ in ids_events:
            id_event = id_event_[0]
            pagina = 1

            while True:
                sleep(0.8)
                print(f"Pagina: {pagina} EVENTO: {id_event}")
                try:
                    pedido = link.post(link_para_api, headers=protocolo, json={"query": query(id_event, pagina)}).text
                    t = json.loads(pedido)

                except Exception as error:
                    print(f"FALHA NA CONEXÃO.\n{error}")
                    db.close()
                    return error

                if int(t["extensions"]["queryComplexity"]) < 10:

                    db.execute(f"UPDATE Eventos SET busca_partidas = 'REGISTRADO' WHERE id={id_event}")

                    db.execute(
                        f"UPDATE Eventos SET ultima_busca_partidas = '{datetime.now().strftime('%d/%m/%Y')}' "
                        f"WHERE id={id_event}")
                    db.commit()
                    break

                for x in t["data"]["event"]["sets"]["nodes"]:
                    print(x)
                    try:
                        set_id_set_round = x["id"], x["fullRoundText"]
                        if len(x["slots"][0]["standing"]["entrant"]["participants"]) < 2:
                            players_stats = [x["slots"][0]["standing"]["entrant"]["participants"][0]["user"]["id"],
                                             x["slots"][0]["standing"]["stats"]["score"]["value"],
                                             x["slots"][1]["standing"]["entrant"]["participants"][0]["user"]["id"],
                                             x["slots"][1]["standing"]["stats"]["score"]["value"]]

                            validador = db.execute(
                                f"SELECT *FROM 'Partidas' WHERE id_set={set_id_set_round[0]}"
                                f" AND id_event='{id_event}'").fetchall()

                            if not validador:
                                db.execute(
                                    f"INSERT INTO 'Partidas' "
                                    f"('id_set','id_event','round', 'id_player1', 'score1', 'id_player2', 'score2') "
                                    f"VALUES ({set_id_set_round[0]},{id_event},'{set_id_set_round[1]}',{players_stats[0]}"
                                    f", {players_stats[1]}, {players_stats[2]}, {players_stats[3]})")

                            print(x["slots"][0]["standing"], x["slots"][1]["standing"], players_stats, set_id_set_round,
                                  sep="\n")
                    except Exception as erro2:
                        print(
                            f"{'-' * 50}\nErro Registro.\n{x}\n{erro2} ID EVENT: {id_event}"
                            f"\n{x['slots'][0]['standing']['entrant']['participants']}")

                pagina += 1
    else:

        print("LISTA VAZIA")
        return False


if __name__ == '__main__':
    while True:
        try:
            register = sets()
            if not register:
                break

        except Exception as er:
            print(f"Fora\n{er}")
            sleep(5)
            pass

