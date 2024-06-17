# Google Search Web Scraper

This Python script utilizes Google's Custom Search API to scrape essential data from search results and organizes it into a PDF report.

## Features

- **Scrapes IP addresses, DNS, URLs, snippets**: Extracts relevant information from search results.
- *Generates a PDF report*: Summarizes scraped data for easy analysis.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/google-search-web-scraper.git
   cd google-search-web-scraper
2. **Install dependencies:**
   pip install requests beautifulsoup4 reportlab tldextract


## Usage

1. **Set up Google Custom Search API:**
   - Obtain your API key and Custom Search Engine (CSE) ID from Google.

2. **Configure the script:**
   - Open `web_scraper.py`.
   - Locate the variables `API_KEY` and `CSE_ID`.
   - Replace `'YOUR_API_KEY'` with your actual API key obtained from Google.
   - Replace `'YOUR_CSE_ID'` with your actual Custom Search Engine ID.

3. **Run the script:**

   ```bash
   python web_scraper.py
### Contributing

Contributions are welcome! Follow these steps to contribute:

1. **Fork the repository:**

   - Click on the "Fork" button at the top right corner of this repository's page on GitHub.

2. **Clone the repository:**

   - Open your terminal (or Git Bash).
   - Clone the forked repository to your local machine:

     ```bash
     git clone https://github.com/yourusername/google-search-web-scraper.git
     cd google-search-web-scraper
     ```

3. **Make your changes:**

   - Modify the `web_scraper.py` script or other project files as needed.

4. **Test your changes:**

   - Ensure that your changes work as expected.

5. **Commit your changes:**

   - Stage your changes for commit:

     ```bash
     git add .
     ```

   - Commit the changes with a descriptive message:

     ```bash
     git commit -m 'Add your descriptive commit message'
     ```

6. **Push to the branch:**

   - Push your changes to your forked repository:

     ```bash
     git push origin master
     ```

7. **Create a new Pull Request:**

   - Go to your forked repository on GitHub.
   - Click on the "New Pull Request" button.
   - Provide a brief description of your changes.
   - Submit the Pull Request for review.

### Code Style

- Follow Python's PEP 8 style guide.
- Use clear and descriptive variable names.
- Comment code where necessary to explain complex logic or algorithms.

### Issues

If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/yourusername/google-search-web-scraper/issues/new) on GitHub.


### Contact

For questions or feedback, feel free to reach out to a.s.rayleigh@gmail.com



