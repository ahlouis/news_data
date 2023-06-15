import pandas as pd
from newsapi import NewsApiClient

class NewsData:
    def __init__(self):
        self.newsapi = NewsApiClient(api_key='')
    
    def fetch_news(self, country):
        everything = self.newsapi.get_everything(q=country)
        top_headlines = self.newsapi.get_top_headlines(q=country)
        return everything, top_headlines
    
    def collect_data(self):
        countries = [
            "China", "Canada", "Germany", "Malaysia", "Mexico",
            "Netherlands", "Philippines", "Switzerland", "Taiwan", "United States",
            "Austria", "Belgium", "Bosnia and Herzegovina", "Brazil", "Bulgaria",
            "Croatia", "Czech Republic", "East Timor", "France", "India",
            "Ireland", "Israel", "Italy", "Liechtenstein", "Monaco",
            "Norway", "Poland", "Portugal", "Romania", "Russia",
            "Serbia", "Slovakia", "Slovenia", "South Africa", "South Korea",
            "Spain", "Sweden", "Turkey", "United Kingdom", "Hungary",
            "Argentina", "Belarus", "Morocco", "Thailand", "North Macedonia",
            "Australia", "New Zealand", "Queensland", "Hong Kong"
        ]
        
        everything_data = []
        top_headlines_data = []
        
        for country in countries:
            everything, top_headlines = self.fetch_news(country)
            
            everything_df = pd.DataFrame(everything['articles'])
            top_headlines_df = pd.DataFrame(top_headlines['articles'])
            
            everything_df['Country'] = country
            top_headlines_df['Country'] = country
            
            everything_data.append(everything_df)
            top_headlines_data.append(top_headlines_df)
        
        everything_data_combined = pd.concat(everything_data, ignore_index=True)
        top_headlines_data_combined = pd.concat(top_headlines_data, ignore_index=True)
        
        everything_data_combined.drop_duplicates(subset='title', keep='first', inplace=True)
        top_headlines_data_combined.drop_duplicates(subset='title', keep='first', inplace=True)
        
        everything_data_combined.to_csv('new_news_master.csv', index=False)
        top_headlines_data_combined.to_csv('top_news_master.csv', index=False)

news_data = NewsData()
news_data.collect_data()
