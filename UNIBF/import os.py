import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def download_image(url, output_folder):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        file_path = os.path.join(output_folder, os.path.basename(url))
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"Image downloaded and saved: {file_path}")
    else:
        print(f"Failed to download image: {url}")


def process_website(url, output_folder):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch the website: {url}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Inclua aqui lógica para encontrar outras imagens se necessário
    img_tags = soup.find_all('img')

    for img_tag in img_tags:
        img_url = urljoin(url, img_tag['src'])
        download_image(img_url, output_folder)


if __name__ == "__main__":
    website_url = "https://www.unibf.com.br/"
    output_folder = "C:/Users/User/Desktop/UNIBF/img import"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    process_website(website_url, output_folder)
