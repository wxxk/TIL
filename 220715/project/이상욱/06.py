import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    movies_info = []

    for movie in movies:
        genre_ids = movie['genre_ids']

        genre_names = []

        for genre in genres:
            if genre['id'] in genre_ids:
                genre_names.append(genre['name'])
    
        key_list = ['id', 'title', 'vote_average', 'overview']

        movie_info = {}

        for key in key_list:
            movie_info[key] = movie[key]
    
        movie_info['genre_names'] = genre_names

        movies_info.append(movie_info)
    return movies_info

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))