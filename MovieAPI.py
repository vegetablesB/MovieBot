import http.client
import json
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
    data_bites = res.read()
    data_str = data_bites.decode("utf-8")
    data_dict = json.loads(data_str)
    data_list = data_dict["d"]
    return data_list

def RespondGenres(message):

    conn = http.client.HTTPSConnection(IP)
    RequestUrl = "/title/get-genres?tconst=" + message
    conn.request("GET", RequestUrl, headers=headers)
    res = conn.getresponse()
    data_bites = res.read()
    data_str=data_bites.decode("utf-8")
    data_dict = json.loads(data_str)
    # data_list = data_dict["d"]
    return data_dict

def RespondPoster(message):
    conn = http.client.HTTPSConnection(IP)
    RequestUrl = "/title/get-images?tconst=" + message + "&limit=3"
    conn.request("GET", RequestUrl, headers=headers)
    res = conn.getresponse()
    data_bites = res.read()
    data_str = data_bites.decode("utf-8")
    data_dict = json.loads(data_str)
    data_list = data_dict["images"]
    return data_list

def RespondPopular(message):
    conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")
    RequestUrl = "/title/get-popular-movies-by-genre?genre=%2Fchart%2Fpopular%2Fgenre%2F" + message
    conn.request("GET", RequestUrl, headers=headers)
    res = conn.getresponse()
    data_bites = res.read()
    data_str = data_bites.decode("utf-8")
    data_dict = json.loads(data_str)
    # data_list = data_dict["d"]
    return data_dict




