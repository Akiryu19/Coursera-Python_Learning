import requests_with_caching
import json

def get_movies_from_tastedive(string):
    baseurl = "http://tastedive.com/api/similar"
    params_diction = {}
    params_diction["q"] = string
    params_diction["type"] = "movies"
    params_diction["limit"] = 5
    tastedive_resp = requests_with_caching.get(baseurl, params = params_diction)
    #print(tastedive_resp)
    return tastedive_resp.json()



def extract_movie_titles(results):
    #results = get_movies_from_tastedive(string)
    #print(results)
    movies_lst = results["Similar"]["Results"]
    #print(movies_lst)
    movies_names_lst = []
    for movie in movies_lst:
        movie_name = movie["Name"]
        movies_names_lst.append(movie_name)
    return movies_names_lst


# def get_related_titles(list):
#     related_movie_titles = []
#     for i in range(len(list)):
#         related_movie_title = extract_movie_titles(list[i])
#         related_movie_titles.append(related_movie_title)
#     print(related_movie_titles)
#     titles = []
#     for related_movies_lst in related_movie_titles:
#         for movie in related_movies_lst:
#             titles.append(movie)
#     print(titles)

def get_related_titles(lst):
    related_movies_lsts = []
    for movie in lst:
        related_movies = extract_movie_titles(get_movies_from_tastedive(movie))
        for movie in related_movies:
            if movie not in related_movies_lsts:
                related_movies_lsts.append(movie)
    return related_movies_lsts

#print(get_related_titles(["Black Panther", "Captain Marvel"]))

def get_movie_data(title):
    baseurl = "http://www.omdbapi.com/"
    param = {}
    param["t"] = title
    param["r"] = "json"
    omdb_resq = requests_with_caching.get(baseurl, params=param)

    return json.loads(omdb_resq.text)





get_movie_data("Venom")
get_movie_data("Baby Mama")

def get_movie_rating(dic):
    ratings_ = dic["Ratings"]
    for rating in ratings_:
        if rating["Source"] == "Rotten Tomatoes":
            return int(rating["Value"][0:2])
        sources = []
        sources.append(rating["Source"])
    if "Rotten Tomatoes" not in sources:
        return 0

def get_sorted_recommendations(lst):
    movies = get_related_titles(lst) #['Captain Marvel', 'Avengers: Infinity War', 'Ant-Man And The Wasp', 'The Fate Of The Furious', 'Deadpool 2', 'Inhumans', 'Venom', 'American Assassin', 'Black Panther']
    movies_name_and_rating = {}
    for movie in movies:
        movie_data = get_movie_data(movie)
        movies_rating = get_movie_rating(movie_data)
        movies_name_and_rating[movie] = movies_rating
    return sorted(movies_name_and_rating.keys(),key = lambda rating:movies_name_and_rating[movie])



get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
