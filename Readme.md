# Web Scraping with Selenium and BeautifulSoup

## Description
This Python script uses Selenium and BeautifulSoup to scrape data from web pages and save it to a CSV file. It navigates through multiple pages of a website, extracts specific data (words in this case), and writes it into a file named `Words.csv`.

## Requirements
- Python 3
- Selenium
- BeautifulSoup4
- WebDriver (e.g., geckodriver for Firefox)

## Installation
To install the required libraries, run the following command:
```bash
pip install selenium beautifulsoup4
```

Make sure you have the appropriate WebDriver installed for your browser (e.g., geckodriver for Firefox).

## Usage
- Place the `geckodriver.exe` in the same directory as the script.
- Modify first_page_url in the script to the website you want to scrape.
- Run the script:
```bash
python main.py
```

- Follow the on-screen instructions for manual login and navigation if required.

## Configuration
You can configure the script by changing the `first_page_url` and the range in the for-loop to adjust the number of pages to scrape.

## Contributing
Feel free to fork this project and submit pull requests with any enhancements.

## License
This project is released under the [MIT License](https://opensource.org/license/mit/).