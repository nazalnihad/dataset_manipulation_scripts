import json
import requests
from bs4 import BeautifulSoup
import os

def get_img_search_url(file_path):
    search_url = 'https://yandex.com/images/search'
    files = {'upfile': ('blob', open(file_path, 'rb'), 'image/jpeg')}
    params = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
    response = requests.post(search_url, params=params, files=files)
    
    if response.status_code != 200:
        raise Exception('Failed to upload image to Yandex.')
    
    query_string = json.loads(response.content)['blocks'][0]['params']['url']
    img_search_url = search_url + '?' + query_string + '&cbir_page=similar'
    
    return img_search_url

def download_similar_images(img_search_url):
    response = requests.get(img_search_url)
    
    if response.status_code != 200:
        raise Exception('Failed to retrieve search results.')
    
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tags = soup.find_all('img', class_='serp-item__thumb')

    if not img_tags:
        raise Exception('No similar images found.')

    # Ensure the directory exists
    if not os.path.exists('downloaded_images'):
        os.makedirs('downloaded_images')

    # Download the first 20 similar images
    for i, img in enumerate(img_tags[:20]):
        img_url = 'https:' + img['src']
        img_data = requests.get(img_url).content
        with open(f'downloaded_images/similar_image_{i+1}.jpg', 'wb') as f:
            f.write(img_data)
        print(f'Downloaded similar_image_{i+1}.jpg')

if __name__ == '__main__':
    file_path = "D:\\projects\\iist\\backup_data\\final_data\\predictions\\data\\val\\images\\568c75b6-6cb2-4c65-b74c-eacc132dc07a.jpg"
    img_search_url = get_img_search_url(file_path)
    download_similar_images(img_search_url)
