from scraper import EcommerceScraper
from analyzer import PriceAnalyzer

def main():
    product_name = input("Enter the product name to compare prices: ")
    
    scraper = EcommerceScraper()
    print("Scraping product data...")
    products = scraper.scrape_all(product_name)
    
    if not products:
        print("No products found. Please try a different search term.")
        return
    
    analyzer = PriceAnalyzer(products)
    print("\nGenerating price analysis report...")
    report = analyzer.generate_report()
    print(report)
    
    print("Generating price distribution chart...")
    analyzer.get_price_distribution()
    print("Chart saved as 'price_distribution.png'")

if __name__ == "__main__":
    main()
