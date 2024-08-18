import os
import requests
import pprint
import time
from urllib.parse import quote


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

# From Google: Custom Search JSON API provides 100 search queries per day for free
def fetch_images(query, num_images, save_folder):
    # Simplify the query
    encoded_query = quote(query)

    search_url = f"https://www.googleapis.com/customsearch/v1?q={encoded_query}&cx={SEARCH_ENGINE_ID}&key={API_KEY}&searchType=image&num={min(num_images, 10)}"
    
    response = requests.get(search_url).json()
    
    if 'items' not in response:
        print(f"No items found for {query}")
        print(f"Search URL: {search_url}")
        pprint.pprint(f"Response: {response}")
        return
    
    for i, item in enumerate(response['items']):
        img_url = item['link']
        try:
            img_data = requests.get(img_url).content
            # Get the file extension
            file_extension = os.path.splitext(img_url)[1]  
            
            # If there is no file extension, default to .jpg
            if not file_extension:
                file_extension = '.jpg'  
                
            # Save the image to the specified folder
            with open(f'{save_folder}/{query.replace(" ", "_")}_{i+1}{file_extension}', 'wb') as img_file:
                img_file.write(img_data)
                
            # Print the name of the image that was downloaded
            print(f"Downloaded {query.replace(' ', '_')}_{i+1}{file_extension}")
            
        except Exception as e:
            print(f"Could not download {img_url}. Error: {e}")


dishes = [
    "Musakhan", "Mansaf", "Maqluba", "Mandi",
    "Mulukhiyyah", "Fasoulya", "Bamia",
    "Bamia", "Kofta", "Kebab Halabi",
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
        
    fetch_images(query, num_images_per_dish, save_folder)
