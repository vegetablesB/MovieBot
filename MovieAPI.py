import http.client
IP="imdb8.p.rapidapi.com"
headers = {
    'x-rapidapi-key': "c7cbaf6610mshf6019caa1f2eb77p1a31a2jsnc9bcc59861d5",
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }
def Respond(message):
    conn = http.client.HTTPSConnection(IP)
    RequestUrl = "/title/auto-complete?q="+message
    conn.request("GET", RequestUrl, headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def RespondGenres(message):

    conn = http.client.HTTPSConnection(IP)
    RequestUrl = "/title/get-genres?tconst=" + message
    conn.request("GET", RequestUrl, headers=headers)
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def RespondPoster(message):
    conn = http.client.HTTPSConnection(IP)
    RequestUrl = "/title/get-images?tconst=" + message + "&limit=3"
    conn.request("GET", RequestUrl, headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def RespondPopular(message):
    conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")
    RequestUrl = "/title/get-popular-movies-by-genre?genre=%2Fchart%2Fpopular%2Fgenre%2F" + message
    conn.request("GET", RequestUrl, headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

