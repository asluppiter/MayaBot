import json
import random

def randomMsg():

    with open('kdn/data.json', encoding="utf8") as json_file:
      data = json.load(json_file)
      msg= data["messages"]

    boto = False
    while boto == False:
      equisDe = random.randint(1, len(msg)) #Gets a random number between 1 and the lenght of the json file adn we use it to browse the json
      #print(msg[equisDe])
      imagen = False
      noesBot=msg[equisDe]["author"]["isBot"] #Check if the msg author is a bot
      mensaje = msg[equisDe]["content"]
      if not mensaje: #When theres no text only img
        imagen = True
        mensaje = msg[equisDe]["attachments"][0]["url"]

      autor = msg[equisDe]["author"]["name"]
      pica = msg[equisDe]["author"]["avatarUrl"]
      fecha = msg[equisDe]["timestamp"]
      fecha = fecha[0:10]
      if not fecha:
        fecha = "NULL / IMAGEN"
      myDict = {
        "pfp" : pica,
        "autor" : autor,
        "mensaje" : mensaje,
        "fecha": fecha,
        "imagen": imagen
      }
      if noesBot == False:
        boto = True
        return myDict
      else:
        boto = False
