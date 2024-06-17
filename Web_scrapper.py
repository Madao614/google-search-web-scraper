import requests
from bs4 import BeautifulSoup
import re
import socket
import os
from datetime import datetime
import tldextract
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Google Custom Search API
API_KEY = 'AIzaSyC6xY51ulwPp6tj6q47NStHp0F9Ia5x8Jo'  # Replace with your actual API key
CSE_ID = '24b484e78ed2b41f4'    # Replace with your actual CSE ID

def google_search(query, api_key, cse_id, num=10): # The default number of results is 10 according to a google search page in the custom API
    results = []
    start_index = 1  # Start fetching from the first result
    while len(results) < num:
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cse_id}&start={start_index}"
        response = requests.get(url)
        data = response.json()
        items = data.get('items', [])
        if not items:
            break
        results.extend(items)
        start_index += len(items)  # Move to the next page of results
    
    return results[:num]  # Return only the desired number of results

def get_ip_and_dns(url):
    extracted = tldextract.extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"
    try:
        ip_address = socket.gethostbyname(domain)
    except socket.gaierror:
        ip_address = "N/A"
    dns = domain
    return ip_address, dns

def get_meta_content(soup, meta_name):
    tag = soup.find("meta", attrs={"name": meta_name})
    if tag:
        return tag.get("content", "N/A")
    return "N/A"

def get_author(soup):
    author = get_meta_content(soup, "author")
    if author == "N/A":
        author = soup.find("meta", attrs={"property": "article:author"})
        if author:
            return author.get("content", "N/A")
    return author

def estimate_reading_time(text):
    words = text.split()
    words_per_minute = 200  # Average reading speed
    reading_time_minutes = len(words) // words_per_minute
    return reading_time_minutes

def scrape_website(url, timeout=10):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        
        text = soup.get_text()
        meta_description = get_meta_content(soup, "description")
        author = get_author(soup)
        estimated_reading_time = estimate_reading_time(text)

        return {
            "url": url,
            "meta_description": meta_description,
            "author": author,
            "estimated_reading_time": f"{estimated_reading_time} minutes"
        }
    except requests.RequestException as e:
        print(f"Failed to scrape {url}: {e}")
        return None

def save_to_pdf(data_list, query, save_dir="scraped_files"):
    # Create the directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)
    
    file_name = os.path.join(save_dir, f"{query.replace(' ', '_')}.pdf")
    c = canvas.Canvas(file_name, pagesize=letter)
    c.setFont("Helvetica", 12)

    c.drawString(100, 800, f"Search Query: {query}")

    y_position = 780
    for data in data_list:
        y_position -= 20
        c.drawString(100, y_position, f"URL: {data['url']}")
        y_position -= 15
        c.drawString(100, y_position, f"IP Address: {data['ip_address']}")
        y_position -= 15
        c.drawString(100, y_position, f"DNS: {data['dns']}")
        y_position -= 15
        c.drawString(100, y_position, f"Snippet: {data['snippet']}")
        y_position -= 15
        c.drawString(100, y_position, f"Publication Date: {data['publication_date']}")
        y_position -= 15
        c.drawString(100, y_position, f"Meta Description: {data['meta_description']}")
        y_position -= 15
        c.drawString(100, y_position, f"Author: {data['author']}")
        y_position -= 15
        c.drawString(100, y_position, f"Estimated Reading Time: {data['estimated_reading_time']}")
        y_position -= 30

    c.save()
    print(f"Saved data to {file_name}")

def main():
    query = input("Enter your search query: ")
    search_results = google_search(query, API_KEY, CSE_ID, num=10)
    
    data_list = []

    for result in search_results:
        url = result.get('link')
        snippet = result.get('snippet', 'N/A')
        publication_date = result.get('pagemap', {}).get('metatags', [{}])[0].get('og:updated_time', 'N/A')
        if publication_date != 'N/A':
            try:
                publication_date = datetime.fromisoformat(publication_date).strftime('%Y-%m-%d')
            except ValueError:
                publication_date = 'N/A'
        
        print(f"Scraping {url}...")
        website_data = scrape_website(url)
        
        if website_data:
            ip_address, dns = get_ip_and_dns(url)
            website_data.update({
                "ip_address": ip_address,
                "dns": dns,
                "url": url,
                "snippet": snippet,
                "publication_date": publication_date
            })
            data_list.append(website_data)
            print(f"Added {url} content to data list.")
        else:
            print(f"Failed to add {url} content to data list.")

    save_to_pdf(data_list, query)

if __name__ == "__main__":
    main()
