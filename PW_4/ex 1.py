from bs4 import BeautifulSoup

# HTML code
with open('Cheetah - Wikipedia.html','r', encoding ='utf-8') as file:
    html_code = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html_code, 'html.parser')

# Extract addresses
addresses = soup.find_all('address')
for address in addresses:
    print('Address:', address.get_text())

# Extract quotes
quotes = soup.find_all('q')
for quote in quotes:
    print('Quote:', quote.get_text())

# Extract text written in bold
bold_text = soup.find_all('b')
for text in bold_text:
    print('Bold Text:', text.get_text())

# Extract links
links = soup.find_all('a')
for link in links:
    print('Link:', link['href'])

# Extract tables
tables = soup.find_all('table')
for table in tables:
    print('Table:', table)