import requests
import os
from dotenv import load_dotenv

load_dotenv()

def popular_count():
    pass
    # 여기에 코드를 작성합니다.
    url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    parameters = {
        'api_key': os.getenv('API_KEY'),
        'language': 'ko-KR'
    }

    popular_movies = requests.get(url+path, params = parameters).json()
    return len(popular_movies['results'])


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
