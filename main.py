from bs4 import BeautifulSoup
import requests
def scrape_aljazeera(url):
    # Send a request to the URL
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return

    # Parse the page content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all article tags (adjust the tag and class based on actual page structure)
    articles = soup.find_all('article', class_='some-article-class')
    print(soup)

    # Extract titles and URLs
    for article in articles:
        title = article.find('h2', class_='title-class').get_text(strip=True)
        article_url = article.find('a')['href']
        print(f"Title: {title}\nURL: {article_url}\n")

# Replace with the actual Al Jazeera URL you want to scrape
scrape_aljazeera('https://www.aljazeera.com/')
