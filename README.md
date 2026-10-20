# 📚 Books to Scrape — Web Scraping Project

## 📌 Project Overview

This project uses Python to scrape book information from [Books to Scrape](https://books.toscrape.com/).

The script extracts book titles, prices, ratings, and categories, and saves the data into a CSV file as output.

## 📂 Repository Structure

| File | Description |
|---|---|
| `scrape.py` | Python script that scrapes book information from the website. |
| `requirements.txt` | Lists the Python libraries required to run the project. |
| `books_to_scrape.csv` | CSV file containing the scraped book data. |
| `.gitignore` | Specifies files and folders Git should ignore. |
| `README.md` | Project documentation. |

## 🛠️ Tools & Technologies

- **Python** — Main programming language
- **BeautifulSoup** — Parses HTML and extracts book information
- **Requests** — Retrieves webpage content

## 📊 Output

The scraped data is saved as a `.csv` file in a tabular format with the following columns:

| Column | Description |
|---|---|
| `book title` | Title of the book |
| `price` | Listed price of the book |
| `ratings` | Star rating of the book |
| `category` | Category the book belongs to |

## 🎯 Key Learnings

Through this project, I practiced:

- **Web Scraping:** Extracting structured information from a website.
- **HTML Fundamentals:** Understanding HTML elements, tags, attributes, and page structure.
- **Python Data Extraction:** Using BeautifulSoup to navigate HTML and locate specific elements.
- **Automation:** Automating data collection and saving the results to a CSV file.

## 🚀 Getting Started

### 1. Install Dependencies

Install the required libraries using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 2. Run the Script

```bash
python scraper.py
```

### 3. View the Output

Open the generated `books_to_scrape.csv` file to explore the scraped book data.

