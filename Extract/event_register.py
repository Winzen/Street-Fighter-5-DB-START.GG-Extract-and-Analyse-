import requests as link
from requests.structures import CaseInsensitiveDict
import json
import sqlite3


def pagina_txt(p):
    query = """query TournamentsByCountry{
          tournaments(query: {
            perPage: 150
            page: """ + str(p) + """
            filter: {
                videogameIds: 33990
        }
      }) {
        nodes {     
          events(filter:{
            videogameId: 33990
          }){
            id
            slug
            name
            isOnline
            startAt
            tournament{
              countryCode
              owner{
                id
              }
            }
          }
          } 
        }
      }"""

    return query


db = sqlite3.connect("twitchbotdb.db")

link_para_API = 'https://api.smash.gg/gql/alpha'
chave = ""
protocolo = CaseInsensitiveDict()
protocolo["Accept"] = "application/json"
protocolo["Authorization"] = chave

query_valid = True

while query_valid:

    pagina = int(open("pagina.txt", "r").read())

    pedido = link.post(link_para_API, headers=protocolo, json={"query": pagina_txt(pagina)}).text
    t = json.loads(pedido)

    for x in t["data"]["tournaments"]["nodes"]:

        try:

            for y in x["events"]:
                #y = x["events"][0]
                dados = [y["id"], y["slug"], y["name"], y["isOnline"], y["startAt"],
                         y["tournament"]["countryCode"], y["tournament"]["owner"]["id"]]

                dados[2] = str(dados[2]).replace("'", "''")

                duplicado = db.execute(f"""SELECT *FROM Eventos WHERE id={dados[0]} AND slug='{dados[1]}'""").fetchall()

                if not duplicado:
                    db.execute(f"""INSERT INTO 'Eventos' ('id','slug','name', 'isOnline', 'startAt', 'countryCode', 
                    'owner_id', 'busca_jogador', 'busca_partidas', 'ultima_busca_jogador', 'ultima_busca_partidas') VALUES 
                    ({dados[0]}, '{dados[1]}', '{dados[2]}', {dados[3]}
                    , {dados[4]}, '{dados[5]}', {dados[6]}, 
                    'NÃO REGISTRADO', 'NÃO REGISTRADO', 'NÃO REGISTRADO', 'NÃO REGISTRADO')""")

        except Exception as error:
            print(f"ERRO : {error}\n", x)

    print(t)

    with open("pagina.txt", "w") as txt:
        print(f"Pagina: {pagina}")
        pagina += 1
        txt.write(f"{pagina}")

    if t["extensions"]["queryComplexity"] < 10:
        query_valid = False

    db.commit()
