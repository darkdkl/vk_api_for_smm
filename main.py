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
    posts = []
    for post in info_posts:
        posts.append(post[1])
    date_posts = []
    for day in info_posts:
        date_posts.append(day[0])

    data = [plotly.graph_objs.Bar(
            x=date_posts,
            y=posts
            )]

    return plotly.plotly.plot(data, filename=name, auto_open=False)


def main(search_string, interval):
    info_posts = []

    for day in range(0, interval):
        start_data = datetime.today()-timedelta(days=day)

        number_of_posts = search_posts(search_string, int(
            start_data.timestamp()), int((start_data+timedelta(days=1)).timestamp()))

        date_and_posts = start_data.date().isoformat(), number_of_posts
        info_posts.append(date_and_posts)
        time.sleep(3)

    return build_plot(info_posts, search_string)


if __name__ == "__main__":
    print(main(settings.SEARCH_NAME, settings.SEARCH_INTERVAL))
