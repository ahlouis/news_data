import pandas as pd
import subprocess

class NewsData:
    def __init__(self):
        self.data = None

    def set_working_directory(self, directory):
        pass

    def load_libraries(self):
        subprocess.call('pip install remotes ggplot2 dplyr plyr newsapi', shell=True)
        subprocess.call('pip install git+https://github.com/news-r/newsapi', shell=True)

        import newsapi
        newsapi.newsapi_key("f10e794ff2cb4a6085ba5c32b3dc36bc")

        self.data = pd.DataFrame(columns=['Country'])

    def fetch_news(self, country):
        from newsapi import newsapi

        dat = newsapi.every_news(country)
        data = newsapi.top_headlines(country)

        dat['Country'] = country
        data['Country'] = country

        self.data = pd.concat([self.data, dat])

    def save_data(self, filename):
        self.data.to_csv(filename, index=False)


if __name__ == "__main__":
    news_data = NewsData()

    news_data.load_libraries()

    countries = [
        "China", "Canada", "Germany", "Malaysia", "Mexico",
        "Netherlands", "Philipines", "Switzerland", "Taiwan", "United States",
        "Austria", "Belgium", "Bosnia and Herzegovina", "Brazil", "Bulgaria",
        "Croatia", "Czech Republic", "East Timor", "France", "India",
        "Ireland", "Israel", "Italy", "Liechtenstein", "Monaco",
        "Norway", "Poland", "Portugal", "Romania", "Russian Federation",
        "Serbia", "Slovakia", "Slovenia", "South Africa", "South Korea",
        "Spain", "Sweden", "Turkey", "United Kingdom", "Hungary",
        "Argentina", "Belarus", "Morocco", "Thailand", "North Macedonia",
        "Australia", "New Zealand", "Queensland", "Hong Kong"
    ]

    for country in countries:
        news_data.fetch_news(country)

    news_data.save_data("new_news_master.csv")
