import requests_with_caching
import json
import sys
sys.setExecutionLimit(35000)
def get_movies_from_tastedive(str):
    base_url = "https://tastedive.com/api/similar"
    d = {}
    d["q"] = str
    d["type"] = "movies"
    d["limit"] = 5
    resp = requests_with_caching.get(base_url, params = d)
    req = resp.json()
    #print(req)
    print("-----------1---")
    return req

def extract_movie_titles(dicts):
    movie_lst = []
    for ele in dicts['Similar']['Results']:
        movie_lst.append(ele['Name'])
    print("-----------2---")
    return movie_lst

def get_related_titles(lst):
    rel_tit_lst = []
    for movie in lst:
        for name in extract_movie_titles(get_movies_from_tastedive(movie)):
            if name not in rel_tit_lst :
                rel_tit_lst.append(name)
    print("-----------3---")
    return rel_tit_lst

def get_movie_data(title):
    base_url = "http://www.omdbapi.com/"
    d = {}
    d['t'] = title
    d['r'] = 'json'
    resp2 = requests_with_caching.get(base_url, params = d )
    req2 = resp2.json()
    #print(req2['Ratings'])
    print("-----------4---")
    return(req2)

def get_movie_rating(OMDB_data):

    for rating in OMDB_data['Ratings']:
        if rating['Source'] == 'Rotten Tomatoes' :
            #print(rating['Value'])
            print("-----------5---")
            val = rating['Value'].replace("%", "")
            return int(val)
    return 0

def get_sorted_recommendations(tit_lst):
    print(tit_lst)
    print("-----------6---")
    sorted_lst = sorted(get_related_titles(tit_lst), reverse = True, key = lambda title: ( get_movie_rating(get_movie_data(title)), title))
    print(sorted_lst)
    return sorted_lst


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
