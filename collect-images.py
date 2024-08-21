import os
import requests
import pprint
import time
from urllib.parse import quote
from google_images_search import GoogleImagesSearch


from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('GOOGLE_API_KEY')
SEARCH_ENGINE_ID = os.getenv('SEARCH_ENGINE_ID')

# Parameters
QUERY = "Palestinian Maqluba dish"
NUM_IMAGES = 10
SAVE_FOLDER = "images/maqluba"


# Create the directory if it doesn't exist
if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)
    
gis = GoogleImagesSearch(API_KEY, SEARCH_ENGINE_ID)

def fetch_images(query, num_images, save_folder):
    
    _search_params = {
        'q': query,
        'num': num_images,
        'fileType': 'jpg',
        'num': num_images,
    }
    
    gis.search(search_params=_search_params, path_to_dir=save_folder)


dishes = [
    "Musakhan", "Mansaf", "Maqluba", "Mandi",
    "Mulukhiyyah", "Fasoulya", "Bamia",
    "Kofta", "Kebab Halabi",
    "Shawarma", "Sumaghiyyeh", "Kibbeh",
    "Falafel", "Hummus", "Malfuf",
    "Waraq al-'anib", "Baba Ghanoush", "Galayt bandora",
    "Fattoush", "tabbouleh", "Taboon",
    "Manakish", "Sambusak", "Zayt w Zatar",
    "Knafeh", "Baklawa", "Halawa",
    "Ma'moul", "Qatayef", "Muhallebi",
]

num_images_per_dish = 50
for dish in dishes:
    print("-----------------")
    print(f"Fetching images for {dish}")
    query = f"Palestinian {dish} dish"
    save_folder = f"images/{dish}"
    
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
        
    try: 
        fetch_images(query, num_images_per_dish, save_folder)
    except:
        continue
