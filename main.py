import requests
from bs4 import BeautifulSoup

def run_app():
    currentsession = requests.session()

    url = 'http://vixcentral.com/'
    page = currentsession.get(url=url)

    if(page.status_code != 200):
        return "Status Code: " + page.status_code
    
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find_all('script', type='text/javascript')

    print (len(data))

if __name__ == "__main__":
    run_app()