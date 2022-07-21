from gc import get_referents
import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.
    genre_ids = movie['genre_ids']
    name = []

    for genre in genres: 
        if genre['id'] in genre_ids: 
            name.append(genre['name'])

    list = ['id', 'title', 'vote_average', 'overview']
    dict = {}

    for key in list:
        dict[key] = movie[key]

    dict['name'] = name
    
    return dict
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))