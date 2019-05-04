import requests
import time
from datetime import datetime, timedelta
import plotly
import settings


def search_posts(search_string, start='', end=''):

    params = {'q': search_string,

              'start_time': start,
              'end_time': end,

              'access_token': settings.VK_TOKEN,
              'v': '5.95',
              }

    response = requests.get(
        'https://api.vk.com/method/newsfeed.search', params=params)

    return response.json()['response']['total_count']


def build_plot(info_posts, name):
    
    plotly.tools.set_credentials_file(
        username=settings.PLOTLY_USERNAME, api_key=settings.PLOTLY_TOKEN)
    posts = [post[1] for post in info_posts]
    
    date_posts = [day[0] for day in info_posts]
   
    data = [plotly.graph_objs.Bar(
            x=date_posts,
            y=posts
            )]

    return plotly.plotly.plot(data, filename=name, auto_open=False)


def main():

    info_posts = []
    today=datetime.today()
    for day in range(settings.SEARCH_INTERVAL):
        start_date = today-timedelta(days=day)

        number_of_posts = search_posts(settings.SEARCH_NAME, int(
            start_date.timestamp()), int((start_date+timedelta(days=1)).timestamp()))

        date_and_posts = start_date.date().isoformat(), number_of_posts
        info_posts.append(date_and_posts)
        time.sleep(3)

    return build_plot(info_posts, settings.SEARCH_NAME)


if __name__ == "__main__":
    print(main())
