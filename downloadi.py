from google_images_search import GoogleImagesSearch
import os

def imgsear(keyword, imageNumber):
    api_key = os.getenv("API_KEY")
    search_engine_id = os.getenv("CX_ID")
    gis = GoogleImagesSearch(api_key, search_engine_id, validate_images=True)
    
    _search_params = {
        'q': keyword,
        'num': imageNumber,
    }
    
    current_directory = os.path.dirname(os.path.abspath(__file__)) 
    images_folder = os.path.join(current_directory, '../images')

    if not os.path.exists(images_folder):
        os.makedirs(images_folder)

    gis.search(search_params=_search_params, path_to_dir=images_folder)