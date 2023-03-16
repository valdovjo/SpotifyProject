import time
import zmq
import requests
import random
import json

url_endpoint = "https://api.spotify.com/v1/recommendations?"

#filters
limit=1
market="US"
seed_genres=[
    "acoustic",
    "afrobeat",
    "alt-rock",
    "alternative",
    "ambient",
    "anime",
    "black-metal",
    "bluegrass",
    "blues",
    "bossanova",
    "brazil",
    "breakbeat",
    "british",
    "cantopop",
    "chicago-house",
    "children",
    "chill",
    "classical",
    "club",
    "comedy",
    "country",
    "dance",
    "dancehall",
    "death-metal",
    "deep-house",
    "detroit-techno",
    "disco",
    "disney",
    "drum-and-bass",
    "dub",
    "dubstep",
    "edm",
    "electro",
    "electronic",
    "emo",
    "folk",
    "forro",
    "french",
    "funk",
    "garage",
    "german",
    "gospel",
    "goth",
    "grindcore",
    "groove",
    "grunge",
    "guitar",
    "happy",
    "hard-rock",
    "hardcore",
    "hardstyle",
    "heavy-metal",
    "hip-hop",
    "holidays",
    "honky-tonk",
    "house",
    "idm",
    "indian",
    "indie",
    "indie-pop",
    "industrial",
    "iranian",
    "j-dance",
    "j-idol",
    "j-pop",
    "j-rock",
    "jazz",
    "k-pop",
    "kids",
    "latin",
    "latino",
    "malay",
    "mandopop",
    "metal",
    "metal-misc",
    "metalcore",
    "minimal-techno",
    "movies",
    "mpb",
    "new-age",
    "new-release",
    "opera",
    "pagode",
    "party",
    "philippines-opm",
    "piano",
    "pop",
    "pop-film",
    "post-dubstep",
    "power-pop",
    "progressive-house",
    "psych-rock",
    "punk",
    "punk-rock",
    "r-n-b",
    "rainy-day",
    "reggae",
    "reggaeton",
    "road-trip",
    "rock",
    "rock-n-roll",
    "rockabilly",
    "romance",
    "sad",
    "salsa",
    "samba",
    "sertanejo",
    "show-tunes",
    "singer-songwriter",
    "ska",
    "sleep",
    "songwriter",
    "soul",
    "soundtracks",
    "spanish",
    "study",
    "summer",
    "swedish",
    "synth-pop",
    "tango",
    "techno",
    "trance",
    "trip-hop",
    "turkish",
    "work-out",
    "world-music"
  ]


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    mes = message.decode("utf-8")
    print(f"Received request: {str(mes)}")

    #  Do some 'work'
    time.sleep(1)
    
    rand_seed_genres = seed_genres[random.randint(0,len(seed_genres)-1)]
    target_danceability = random.randint(0,100)/100
    seed_tracks = "0c6xIDDpzE81m2q797ordA"
    seed_artists = "4NHQUGzhtTLFvgF5SZesLK"

    query = f'{url_endpoint}limit={limit}&market={market}&seed_genres={rand_seed_genres}&seed_tracks={seed_tracks}&seed_artists{seed_artists}&target_danceability={target_danceability}'

    response = requests.get(query, 
            #    headers={"Content-Type":"application/json", 
                        #"Authorization":"Bearer BQDBX5a8KHDVn8O9uV_7_WDVTxpJGko1Ev1Qt4v6KHLw3DJoPBOK0taXi52gA78VYsjhiDB9pzUCojDWFLqXWas_0tVmmFzKtyC6t-JWoIIT1GegnsoWGzZIu_C_Pbpy0TNLqj5CRP4yE1nMCS-77zow9PzvGqKbDuonW3rJMJWLiyk"})
                headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer BQCjfecmpzOVBo_ALaiq5xEaQr3BiTWTN0Z9uy48HRKlgS62nW89BFbTkXpWN0n0R_q80Ej2ml00bw5qCnmwHYNj6GeST2TYjRfx1peA79Zpo06n2uTGVa8VQ7a8w42ff-UaD_pVfHyvAOH_ywdwDzIVUc7FI9ufDX_ODtBUQYuatHds3w"})
    json_response = response.json()
    # print(json.dumps(json_response, indent=1, sort_keys=True))
    # if json_response['error']:
    #     raise Exception("refresh OAuth token")
    print(json_response)
    uris = ''
    for i in json_response['tracks']:
        new = f"\"{i['name']}\" by {i['artists'][0]['name']}\n"
        uris += new
    #  Send reply back to client
    socket.send_string(uris)