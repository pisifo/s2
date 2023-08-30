#task1：Try adding codes to extract the latest 10 record
import requests
url = 'https://data.gov.sg/api/action/datastore_search?resource_id=68289dd4-e9d1-41cf-afe6-b093d04b60af&limit=10'
response = requests.get(url)
data = response.json()
print(data)
print(data['help'])
print(data.keys())
print(data['result'])
print(data['result'].keys())
print(data['result']['records'])
for record in data['result']['records']:
    print(f"On week {record['epi_week']} of year {record['epi_year']}, estimated count: {record['est_count']}")
#task2获取新闻标题，在抓取后处理文本
import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.channelnewsasia.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
# Utilize find_all to get the relevant tags from html file.
# <type class=“class_name”> From the name of tags, fill in the relevant tags information below.
data = soup.find_all("h6","h6 list-object__heading")#, class_="class_name")
print(data)  # Take a look at the output before proceed.
count=1
for each in data: # loop through all data
# Get text from tag
    each_title = each.text.strip()  # Get the text information from each title.
    print(count,'.',each_title) # print out the title one by one
    count+=1
#cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
import requests
from bs4 import BeautifulSoup

# Get user's keyword of interest
keyword = input("Enter a keyword to search: ")

url = "https://www.channelnewsasia.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# Utilize find_all to get the relevant tags from html file.
# <type class=“class_name”> From the name of tags, fill in the relevant tags information below.
data = soup.find_all("h6", "h6 list-object__heading")#, class_="class_name")

count = 1
keyword_count = 0  # Initialize keyword count

for each in data:  # loop through all data
    each_title = each.text.strip()  # Get the text information from each title.
    print(count, '.', each_title)  # print out the title one by one

    # Check if the keyword exists in the title (case-insensitive)
    if keyword.lower() in each_title.lower():
        keyword_count += 1

    count += 1

print(f"Total occurrences of '{keyword}': {keyword_count}")
#c22222222222222222222222222222222222222222222222222222222222222222222222222222222222
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox


def search_keyword():
    keyword = keyword_entry.get()

    url = "https://www.channelnewsasia.com/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    data = soup.find_all("h6", "h6 list-object__heading")

    count = 1
    keyword_count = 0

    for each in data:
        each_title = each.text.strip()
        output_text.insert(tk.END, f"{count}. {each_title}\n")

        if keyword.lower() in each_title.lower():
            keyword_count += 1

        count += 1

    output_text.insert(tk.END, f"Total occurrences of '{keyword}': {keyword_count}\n")
    messagebox.showinfo("Search Complete", f"Total occurrences of '{keyword}': {keyword_count}")


# Create GUI window
window = tk.Tk()
window.title("News Keyword Search")

# Create and place widgets
keyword_label = tk.Label(window, text="Enter keyword:")
keyword_label.pack()

keyword_entry = tk.Entry(window)
keyword_entry.pack()

search_button = tk.Button(window, text="Search", command=search_keyword)
search_button.pack()

output_text = tk.Text(window, height=20, width=80)
output_text.pack()

# Start GUI event loop
window.mainloop()

#task3====================================================================================================
import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.courts.com.sg/computing-mobile/tablets/all-tablets"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
# Utilize find_all to get the relevant tags from html file.
# <type class=“class_name”> From the name of tags, fill in the relevant tags information below.
product_title = soup.find_all("h3",class_="product name product-item-name")
print(product_title) # Take a look at the output before proceed.
product_titles =[] # define an empty list to keep each product titles.
for title in product_title: # loop through all product titles
# Get text from tag
    each_title =title.text.strip() # Get the text information from each title.
    product_titles.append(each_title)# print out the title one by one
    # See if you get to see all listed product titles from your program.

# Utilize find_all to get the relevant tags from html file.
# <type class=“class_name”> From the name of tags, fill in the relevant tags information below.
price = soup.find_all("span", class_="price")
prices =[]
for each in price:
    # Get content from tag
    each_price =each.text.strip()
    prices.append(each_price)
    print(prices) # See if you get to see all listed product prices from your program.
#requests是link 让网站反应

import requests
from bs4 import BeautifulSoup


# Define a function to scrape product titles from a given URL
def scrape_product_titles(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    product_titles = soup.find_all("h3",class_="product name product-item-name")
    product_titles_list = [title.a.text.strip() for title in product_titles]
    return product_titles_list


# Define a function to scrape product prices from a given URL
def scrape_product_prices(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    product_prices = soup.find_all("span", class_="price")
    product_prices_list = [price.text.strip() for price in product_prices]
    return product_prices_list


# Iterate through multiple pages and scrape product titles and prices
base_url = "https://www.courts.com.sg/computing-mobile/tablets/all-tablets?page="
start_page = 2
end_page = 4

all_product_titles = []
all_product_prices = []

for page in range(start_page, end_page + 1):
    current_url = base_url + str(page)
    product_titles = scrape_product_titles(current_url)
    product_prices = scrape_product_prices(current_url)

    all_product_titles.extend(product_titles)
    all_product_prices.extend(product_prices)

# Print the scraped data
for title, price in zip(all_product_titles, all_product_prices):
    print(f"Product: {title}, Price: {price}")


#=======================================================================
import pandas as pd


# Create a DataFrame
data = {'Product Title': all_product_titles, 'Product Price': all_product_prices}
df = pd.DataFrame(data)

# Write DataFrame to a CSV file
csv_filename = 'products.csv'
df.to_csv(csv_filename, index=False)

print(f"Data saved to {csv_filename}")


import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_soup(url):
 r = requests.get(url)
 soup = BeautifulSoup(r.content, 'html.parser')
 return soup

def get_products(soup, tagname, classname, result=[]):
 soup_obj = soup.find_all(tagname, classname)
 for each in soup_obj:
   content = each.text.strip()
   result.append(content)
 return result

def get_prices(soup, tagname, classname, sub_tagname, sub_classname, content_name, result=[]):
 soup_obj = soup.find_all(tagname, classname)
 for each in soup_obj:
     each_span = each.find(sub_tagname, sub_classname)
     each_price = float(each_span.get(content_name))
     result.append(each_price)
 return result

def get_pages():
   prices = []
   products = []
   for i in range(2, 5):
     url = "https://www.courts.com.sg/computing-mobile/tablets?p=" + str(i)
     soup = get_soup(url)
     prices = get_prices(soup, "div", "price-box price-final_price", "span", "price-wrapper", "data-price-amount", prices)
     products = get_products(soup, "h3", "product name product-item-name", products)

   df = pd.DataFrame({
       "products": products,
       "prices": prices}
   )
   print(df.head())

   print('c')