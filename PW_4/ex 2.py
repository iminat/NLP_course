from bs4 import BeautifulSoup

# Read HTML content from file
with open('Cheetah - Wikipedia.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Count the number of images
images = soup.find_all('img')
num_images = len(images)
print('Number of Images:', num_images)

# List the packages that have been imported
imported_packages = soup.find_all('pre')
packages = set()
for package in imported_packages:
    lines = package.get_text().split('\n')
    for line in lines:
        if line.startswith('import') or line.startswith('from'):
            package_name = line.split()[1]
            packages.add(package_name)
print('Imported Packages:', packages)

# Check models and their performance
models = soup.find_all(lambda tag: tag.name == 'h3' and tag.string == 'Model')
for model in models:
    model_name = model.find_next_sibling().get_text().strip()
    performance = model.find_next('p').get_text()
    print('Model:', model_name)
    print('Performance:', performance)
    print()