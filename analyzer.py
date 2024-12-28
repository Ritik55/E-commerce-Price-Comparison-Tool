import pandas as pd
import matplotlib.pyplot as plt

class PriceAnalyzer:
    def __init__(self, data):
        self.df = pd.DataFrame(data)

    def get_average_price(self):
        return self.df['price'].mean()

    def get_price_range(self):
        return self.df['price'].min(), self.df['price'].max()

    def get_cheapest_product(self):
        return self.df.loc[self.df['price'].idxmin()]

    def get_price_distribution(self):
        plt.figure(figsize=(10, 6))
        self.df['price'].hist(bins=20)
        plt.title('Price Distribution')
        plt.xlabel('Price')
        plt.ylabel('Frequency')
        plt.savefig('price_distribution.png')
        plt.close()

    def get_source_comparison(self):
        return self.df.groupby('source')['price'].agg(['mean', 'min', 'max'])

    def generate_report(self):
        report = f"Price Analysis Report\n"
        report += f"Average Price: ${self.get_average_price():.2f}\n"
        min_price, max_price = self.get_price_range()
        report += f"Price Range: ${min_price:.2f} - ${max_price:.2f}\n"
        cheapest = self.get_cheapest_product()
        report += f"Cheapest Product: {cheapest['title']} (${cheapest['price']:.2f} on {cheapest['source']})\n"
        report += f"\nSource Comparison:\n{self.get_source_comparison()}\n"
        return report
