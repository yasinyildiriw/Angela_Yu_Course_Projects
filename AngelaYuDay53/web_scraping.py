from bs4 import BeautifulSoup
import requests

ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"

class WebScraping:
    def __init__(self):
        self.response = requests.get(ZILLOW_CLONE_URL)
        self.data = self.response.text
        self.soup = BeautifulSoup(self.data, "html.parser")

    def get_address_list(self):
        '''
        Fetch the addresses from zillow.com return as a list
        :return:
        '''
        addresses = self.soup.find_all(name="address")
        address_list = [address.text for address in addresses]
        clean_address_list = [adres.strip() for adres in address_list]
        return clean_address_list

    def get_rent_price(self):
        '''
        Fetch the rental prices from zillow.com return as a list
        :return:
        '''
        prices = self.soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
        price_list = [price.text for price in prices]
        clean_price_list = [prc[:6] for prc in price_list]
        return clean_price_list
    def get_links(self):
        '''
        Fetch the links from zillow.com return as a list
        :return:
        '''
        links = self.soup.find_all(name="a", attrs={"data-test": "property-card-link"})
        link_list = [link["href"] for link in links if link.has_attr("href")]
        unique_list = []
        for item in link_list:
            if item not in unique_list:
                unique_list.append(item)
        return unique_list