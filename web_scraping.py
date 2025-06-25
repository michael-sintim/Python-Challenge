import requests
from bs4 import BeautifulSoup
import csv
import time
import random

class WebScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        }

    def fetch_page(self, url):
        try:
            time.sleep(random.uniform(1, 3))
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def scrape_books(self, num_pages=5):
        all_books = []
        for page_num in range(1, num_pages + 1):
            page_url = f"{self.base_url}/catalogue/page-{page_num}.html"
            soup = self.fetch_page(page_url)
            if not soup:
                print(f"Skipping page {page_num}")
                continue
            book_containers = soup.find_all('article', class_='product_pod')
            for book in book_containers:
                title = book.h3.a['title']
                price = book.find('p', class_='price_color').text
                availability = book.find('p', class_='instock availability').text.strip()
                star_rating = book.find('p', class_='star-rating')['class'][1]
                book_info = {
                    'title': title,
                    'price': price,
                    'availability': availability,
                    'star_rating': star_rating
                }
                all_books.append(book_info)
            print(f"Scraped page {page_num}")
        return all_books

    def save_to_csv(self, books, filename='books.csv'):
        if not books:
            print("No books to save.")
            return
        keys = books[0].keys()
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                dict_writer = csv.DictWriter(csvfile, fieldnames=keys)
                dict_writer.writeheader()
                dict_writer.writerows(books)
            print(f"Successfully saved {len(books)} books to {filename}")
        except IOError as e:
            print(f"Error saving to CSV: {e}")

def main():
    base_url = "http://books.toscrape.com"
    scraper = WebScraper(base_url)
    books = scraper.scrape_books(num_pages=3)
    scraper.save_to_csv(books)

if __name__ == "__main__":
    main()