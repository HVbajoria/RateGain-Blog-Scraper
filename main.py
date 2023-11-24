# importing libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import requests
import pandas as pd

# extracting the maximum number of pages
def extract_max_page_number(base_url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    driver.get(base_url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    pagination_div = soup.find('div', class_='pagination col-xs-12')

    # Check if pagination div exists where the page numbers are present
    if pagination_div:
        links = pagination_div.find_all('a', class_='page-numbers')
        # Extract numerical values from the links using regular expressions
        page_numbers = [int(re.search(r'\d+', link['href']).group()) for link in links]

        # Find the maximum page number
        max_page_number = max(page_numbers)
        return max_page_number
    else:
        print("Pagination div not found.")
        return None

# Extracing the title, date, image url and likes count from the blog posts on a page
def extract_blog_data(url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # To store the extracted data
    blog_data = {
        'Title': [],
        'Date': [],
        'Image URL': [],
        'Likes Count': []
    }

    # Getting the division where all the blog posts are present
    blogs_div = soup.find('div', class_='blog-items')

    # Check if blog posts are present
    if blogs_div is None:
        print("No blog posts found.")
        print(url)
        return extract_blog_data(url)
    else:
        # Extract all the blog posts from the division
        blog_posts = blogs_div.find_all('article', class_='blog-item')
        print(f"Found {len(blog_posts)} blog posts.")

        # Extract the title, date, image url and likes count from each blog post
        for post in blog_posts:
            title = post.find('h6').find('a').text
            title = title.replace('â€™', '\'').strip()
            date = post.find('div', class_='bd-item').find('span').text
            Image_URL = post.find('div', class_='img')
            if Image_URL:
                Image_URL = Image_URL.find('a')['data-bg']
            else:
                Image_URL = ""

            # Extract only the numeric part of the likes count
            Likes_Count_text = post.find('a', class_='zilla-likes').find('span').text
            Likes_Count = int(''.join(filter(str.isdigit, Likes_Count_text)))

            # Append the extracted data to the dictionary
            blog_data['Title'].append(title)
            blog_data['Date'].append(date)
            blog_data['Image URL'].append(Image_URL)
            blog_data['Likes Count'].append(Likes_Count)

    return blog_data

# Extracting the urls of all the pagination pages
def extract_pagination_urls(base_url, max_pages):
    pagination_urls = [f"{base_url}/page/{i}/" for i in range( 2, max_pages + 1)]
    return pagination_urls

# Saving the extracted data to a csv file
def save_to_csv(data, file_path):
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f'Data saved to {file_path}')


if __name__ == "__main__":
    base_url = 'https://rategain.com/blog'
    max_pages = extract_max_page_number(base_url)

    if max_pages is not None:
        print(f"Maximum Page Number: {max_pages}")
    else:
        max_pages = 1
        print("Unable to determine the maximum page number.")

    pagination_urls = extract_pagination_urls(base_url, max_pages)
    for i in pagination_urls:
        print(i)
    all_data = {
        'Title': [],
        'Date': [],
        'Image URL': [],
        'Likes Count': []
    }

    # Extract data from the main page
    main_page_data = extract_blog_data(base_url)
    all_data['Title'].extend(main_page_data['Title'])
    all_data['Date'].extend(main_page_data['Date'])
    all_data['Image URL'].extend(main_page_data['Image URL'])
    all_data['Likes Count'].extend(main_page_data['Likes Count'])

    # Extract data from pagination pages
    for url in pagination_urls:
        page_data = extract_blog_data(url)
        all_data['Title'].extend(page_data['Title'])
        all_data['Date'].extend(page_data['Date'])
        all_data['Image URL'].extend(page_data['Image URL'])
        all_data['Likes Count'].extend(page_data['Likes Count'])

    save_to_csv(all_data, 'blog_data.csv')
    print("Done.")