import requests
from bs4 import BeautifulSoup as bs

# This is a basic web scraper. You will input the gitHub username in the terminal, then it requests the html content
# of that user's profile page. From the html content, we are able to determine the user's profile image,
# and we will then return the user's image url in the terminal.

github_user = input('Input Github User: ')
url = 'https://github.com/' + github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img', {'alt' : 'Avatar'})['src']
print(profile_image)
