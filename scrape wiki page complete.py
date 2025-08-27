import pandas as pd
import requests
from bs4 import BeautifulSoup
import nltk
import wikipedia as wk
from tqdm import tqdm

# Import table of country | url
links_dataframe = pd.read_csv("/Users/katlosiyandamohutsiwa/Downloads/country wikiurl.csv",sep="\t")
links_dataframe["url"] = links_dataframe["url"].apply(lambda x: x.replace("'",""))

# Load country list
links_dataframe = pd.read_csv("/Users/katlosiyandamohutsiwa/Downloads/country wikiurl.csv", sep="\t")
links_dataframe["url"] = links_dataframe["url"].apply(lambda x: x.replace("'", ""))

# Set language
wikipedia.set_lang("en")

# Initialize list to collect data
results = []

# Loop and fetch Wikipedia content
for country in tqdm(links_dataframe['country']):
    try:
        content = wikipedia.page(country, auto_suggest=False).content
        results.append({'country': country, 'text': content})
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation error for {country}: {e.options}")
        results.append({'country': country, 'text': None})
    except wikipedia.exceptions.PageError:
        print(f"Page not found for {country}")
        results.append({'country': country, 'text': None})
    except Exception as e:
        print(f"Error fetching {country}: {e}")
        results.append({'country': country, 'text': None})

# Save to DataFrame
wiki_df = pd.DataFrame(results)
wiki_df.to_csv("wikipedia_country_texts.csv", index=False)
