US Trump Tariff Analysis (2024)

   

This project analyzes US import and export trade data from 2024, identifying the top trading partners, calculating export-to-import ratios, and visualizing key patterns with bar and pie charts. Built for hands-on data analysis practice using Python.


---

Table of Contents

Features

Installation

Usage

Project Structure

Output

Sample Visuals

Future Improvements

Contributing

License



---

Features

Cleans and preprocesses messy CSV trade data

Calculates:

Total exports/imports by country

Export-to-import ratio

Trade deficits


Visualizes:

Top 10 countries by export

Export-to-import ratio (Pie Chart)

Imports vs Exports (Bar Chart)


Exports cleaned data to a new CSV

Saves charts as PNGs



---

Installation

1. Clone the repository:

git clone https://github.com/AshishSahai/Trump-Tariff-Analysis.git
cd Trump-Tariff-Analysis


2. Install dependencies:

pip install -r requirements.txt


3. Place your dataset: Ensure your file is named Tariff Calculations plus Population.csv and placed in the project root.




---

Usage

Run the analysis with:

python main.py

This will:

Clean and preprocess the data

Display key summaries in terminal

Save visualizations and cleaned CSV



---

Project Structure

us-import-export-analysis/
│
├── main.py                           # Main script
├── README.md                         # Project overview
├── requirements.txt                  # Python dependencies
├── Tariff Calculations plus Population.csv  # Input dataset
├── cleaned_tariff_data.csv          # Output cleaned dataset
├── export_to_import_rate_by_countries.png   # Saved chart


---

Output

Cleaned dataset: cleaned_tariff_data.csv

Visualizations:

Top 10 Export Countries (Bar Chart)

Export-to-Import Ratio (Pie Chart)

Imports vs Exports Comparison (Bar Chart)

Contributing

Contributions are welcome! Here's how you can help:

Report bugs or issues

Suggest improvements

Submit pull requests for enhancements



---

License

This project is licensed under the MIT License.