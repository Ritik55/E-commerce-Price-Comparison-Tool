# E-commerce Price Comparison Tool

## Overview

This project is an advanced web scraping and data analysis tool designed to compare product prices across multiple e-commerce platforms. It demonstrates expertise in web scraping, data processing, and visualization techniques.

## Features

- Scrapes product data from Amazon and eBay
- Analyzes pricing trends and distributions
- Generates comprehensive price comparison reports
- Creates visualizations of price distributions
- Identifies the cheapest product across platforms

## Technologies Used

- Python 3.8+
- BeautifulSoup4 for web scraping
- Pandas for data manipulation
- Matplotlib for data visualization
- Requests for HTTP requests

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ecommerce-price-comparison.git
   ```
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the main script and follow the prompts:

```
python main.py
```

Enter the product name when prompted to initiate the price comparison.

## Project Structure

- `scraper.py`: Contains the EcommerceScraper class for web scraping
- `analyzer.py`: Implements the PriceAnalyzer class for data analysis
- `main.py`: The main script to run the price comparison tool
- `requirements.txt`: List of required Python packages

## Future Enhancements

- Add support for more e-commerce platforms
- Implement price history tracking
- Create a web interface for easier user interaction
- Add email notifications for price drops

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
