import requests as link
from requests.structures import CaseInsensitiveDict
import json
import sqlite3
from time import sleep
from datetime import datetime


def pagina_txt(p, id__):
    query = """query{event(id: """ + str(id__) + """){ 
      standings(query:{
        perPage:150
        page:""" + str(p) + """
      }){
        nodes{
          placement
          entrant{
            participants{
             player{
                gamerTag
              }
              user{
                id
                slug
                location{
                  country
                }
              }
            }
          }   
            }
          }
        }
      }"""

    return query


def busca():
    db = sqlite3.connect("twitchbotdb.db")

    link_para_api = 'https://api.smash.gg/gql/alpha'
    chave = ""
    protocolo = CaseInsensitiveDict()
    protocolo["Accept"] = "application/json"
    protocolo["Authorization"] = chave

    id_events = db.execute(
        f"SELECT id FROM Eventos WHERE busca_jogador != 'REGISTRADO' AND "
        f"ultima_busca_jogador != '{datetime.now().strftime('%d/%m/%Y')}'"
        f" ORDER BY startAt ASC").fetchall()
    print(id_events, len(id_events), sep="\n")
    if len(id_events) >= 1:
        for tupla_event in id_events:

            pagina = 1
            id_event = tupla_event[0]

            while True:
                sleep(0.8)
                print(f"Pagina: {pagina} EVENTO: {id_event}")

                try:
                    pedido = link.post(link_para_api, headers=protocolo, json={"query": pagina_txt(pagina, id_event)}).text

                except Exception as _:
                    print(f"ERRO LINK\n{_}")
                    db.close()
                    return _

                t = json.loads(pedido)
                print(t)
                if int(t["extensions"]["queryComplexity"]) < 10 or \
                        t["data"]["event"]["standings"]["nodes"][0]["placement"] > 1:
                    if len(db.execute(
                            f"SELECT placement FROM Placement WHERE id_event={id_event} AND placement= 1").fetchall()) > 0:
                        db.execute(f"UPDATE Eventos SET busca_jogador = 'REGISTRADO' WHERE id={id_event}")

                    db.execute(
                        f"UPDATE Eventos SET ultima_busca_jogador = '{datetime.now().strftime('%d/%m/%Y')}' "
                        f"WHERE id={id_event}")
                    db.commit()
                    break

                for x in t["data"]["event"]["standings"]["nodes"]:

                    try:
                        placement = x["placement"]

                        for player in x["entrant"]["participants"]:
                            pais = "None" if player["user"]["location"] is None else player["user"]["location"]["country"]
                            dados = [player['user']["id"], player["player"]["gamerTag"], pais, player['user']["slug"],
                                     placement]

                            dados[1] = str(dados[1]).replace("'", "''")

                            validador = db.execute(
                                f"SELECT *FROM 'Jogadores' WHERE id={dados[0]} AND link='{dados[3]}'").fetchall()
                            validador2 = db.execute(
                                f"SELECT *FROM Placement WHERE id_event={id_event} AND id_user={dados[0]}").fetchall()

                            if not validador:
                                db.execute(f"""INSERT INTO 'Jogadores' ('id','gamertag','country', 'link') VALUES 
                                                ({dados[0]}, '{dados[1]}', '{dados[2]}', '{dados[3]}')""")
                            if not validador2:
                                db.execute(f"""INSERT INTO 'Placement' ('id_event','id_user','placement') VALUES 
                                                ({id_event}, {dados[0]}, {dados[4]})""")
                    except Exception as Erro:
                        print("--" * 50, Erro, id_event, player, sep="\n")

                pagina += 1
    else:
        print("lista vazia")
        return False


if __name__ == '__main__':

    while True:

        try:
            register = busca()
            if not register:
                break

        except Exception as er:
            print(f"Fora\n{er}")
            sleep(5)
            pass
