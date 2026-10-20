from bs4 import BeautifulSoup
import requests
import pandas as pd

# Get url links of each book category
home_page = "https://books.toscrape.com/index.html"

home_page_response = requests.get(home_page)
home_page_soup = BeautifulSoup(home_page_response.text, "html")
side_category = home_page_soup.find("div", class_="side_categories")

category_list = []
category_links = side_category.find_all("a")
for link in category_links:
    category_list.append(link.get("href"))

category_list = category_list[1:] # exclude the first category

base_url = "https://books.toscrape.com/"

# Define df and column names
column_names = ["title", "price", "ratings", "category"]
df = pd.DataFrame(columns =  column_names)

for category_url in category_list:
    # Get the category name
    url_split = category_url.split("/")
    category_tag = url_split[-2].split("_")
    category = category_tag[0]
    # Get the first page of each category
    url = base_url + category_url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html")
    # Check the number of pages
    page_tag = soup.find("li", class_="current") 
    if page_tag:
        total_pages = int(page_tag.get_text(strip=True).split()[-1])
    else:
        total_pages = 1
    # Scrape pages
    for page in range(1, total_pages + 1):
        if page == 1:
            page_url = url 
        else:
            page_url = base_url + category_url.replace("index.html", f"page-{page}.html")
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, "html")
        products = soup.find_all("article", class_="product_pod")
        # Extract info in each book product
        for product in products:
            title = product.select_one("h3 a").get("title")
            price_tag = product.find("p", class_="price_color")
            if price_tag:
                    price = price_tag.get_text().replace("Â","") 
            else:
                None
            rating = product.p["class"][1]
            row_data = [title, price, rating, category]
            length = len(df)
            df.loc[length] = row_data

# Save df to .csv file
df.to_csv("books_to_scrape.csv")