from bs4 import BeautifulSoup
import requests
import time

def re_scrape():

    html_text = requests.get("https://www.zillow.com/homes/for_sale/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-72.93833590551758%2C%22east%22%3A-72.73749209448242%2C%22south%22%3A42.903244710168536%2C%22north%22%3A43.00902914738091%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22pmf%22%3A%7B%22value%22%3Atrue%7D%2C%22pf%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D", headers= {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}).text
    soup = BeautifulSoup(html_text, 'lxml')
    listings = soup.find_all('article', class_ = 'list-card list-card-additional-attribution list-card_not-saved')

    for index, listing in enumerate(listings):
        address = listing.find('address', class_ = 'list-card-addr').text
        price = listing.find('div', class_ = 'list-card-price').text
        beds = listing.find('ul', class_ = 'list-card-details').text
        other_deets = listing.find('div', class_ = 'list-card-variable-text list-card-img-overlay').text
        with open(f"listings/{address}.txt", "w") as f:
            f.write(f'Address: {address} \n')
            f.write(f'Price: {price} \n')
            f.write(f'Details: {beds} \n')
            f.write(f'More Context: {other_deets} \n')
        print(f'File saved: {(address, index)}')


if __name__ == '__main__':
    while True:
        re_scrape()
        time_wait = 10
        time.sleep(time_wait * 60)