import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()

def recommendation(title):
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
    movie_id = find_movie['results'][0]['id'] if find_movie['results'] else None

    try:
        path2 = f'/movie/{movie_id}/recommendations'
        parameters2 = {
            'api_key': 'ea580b7bcbaaee64e8a93320f9f81aa2',
            'language': 'ko-KR'
        }
        recom = requests.get(url+path2, params = parameters2).json()
        recom_movies = []
        for movie in recom['results']:
            recom_movies.append(movie['title'])
        return recom_movies

    except:
        return None

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
