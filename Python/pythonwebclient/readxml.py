from bs4 import BeautifulSoup as bs

# reading the data from xml

with open('samplexml.xml', 'r') as f:
    data = f.read()

bs_data = bs(data,'xml')

# find data with name tag

bs_name = bs_data.find_all('name')
print(bs_name)

# find tag with value

bs_waffle = bs_data.find('food').find('name')
print(bs_waffle)