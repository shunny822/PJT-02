import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()

def credits(title):
    pass
    # 여기에 코드를 작성합니다.
    url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    parameters = {
        'api_key': os.getenv('API_KEY'),
        'query': title,
        'language': 'ko-KR'
    }

    find_movie = requests.get(url+path, params = parameters).json()

    try:
        movie_id = find_movie['results'][0]['id']
        path2 = f'/movie/{movie_id}/credits'
        parameters2 = {
            'api_key': 'ea580b7bcbaaee64e8a93320f9f81aa2',
            'language': 'ko-KR'
        }

        credits_data = requests.get(url+path2, params = parameters2).json()
        cast_data = credits_data['cast']
        crew_data = credits_data['crew']
        cast_name = []
        crew_name = []
        cast_directing = {}

        for c in cast_data:
            if c['cast_id'] < 10:
                cast_name.append(c['name'])
        for c in crew_data:
            if c['department'] == 'Directing':
                crew_name.append(c['name'])
        
        cast_directing['cast'] = cast_name
        cast_directing['crew'] = crew_name

        return cast_directing
    except:
        None



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
