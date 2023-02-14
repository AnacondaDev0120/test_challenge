import sys
import requests
from datetime import datetime
from bs4 import BeautifulSoup


def fetch_and_save(url):
    try:
        # Fetch the web page
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Get metadata
        num_links = len(soup.find_all('a'))
        num_images = len(soup.find_all('img'))
        current_time = datetime.now()

        # Save the web page
        file_name = url.split('/')[-1] + '.html'
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(response.text)

        # Save metadata to a separate file
        meta_file_name = url.split('/')[-1] + '_meta.txt'
        with open(meta_file_name, 'w', encoding='utf-8') as f:
            f.write(f'Last fetch time: {current_time}\n')
            f.write(f'Number of links: {num_links}\n')
            f.write(f'Number of images: {num_images}\n')

        print(f'Successfully fetched and saved {url} with metadata.')
    except requests.exceptions.RequestException as e:
        print(f'Error fetching {url}: {e}')


if __name__ == '__main__':
    urls = sys.argv[1:]
    for url in urls:
        fetch_and_save(url)