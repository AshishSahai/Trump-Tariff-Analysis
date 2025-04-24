import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#Load CSV and reading data
def read_data(data):
    df = pd.read_csv(data, sep=";", on_bad_lines= "warn")
    return df
# EDA- Exploratory data analysis
def explore_data(data):
    pd.set_option("display.max_columns", None)
    print(data.head(10))
    print("\nData information: \n",data.info())
    print("\nData summary: \n",data.describe())
    print("\n Missing values: \n", data.isnull().sum())
#Filling missing values in Populaton column with Zero(0)
    data["Population"] = data["Population"].fillna(0)
#Trade deficit by country
    print("\n US trade deficit by country: \n", data.groupby("Country")["US 2024 Deficit"].sum().sort_values(ascending=False))
    data["US 2024 Exports"] = pd.to_numeric(data["US 2024 Exports"], errors="coerce")
    data["US 2024 Imports (Customs Basis)"] = pd.to_numeric(data["US 2024 Imports (Customs Basis)"], errors="coerce")
    data = data.dropna(subset=["US 2024 Exports", "US 2024 Imports (Customs Basis)"]).copy()
    print("\n Missing values: \n", data.isnull().sum())
#rate of export by import
    data["Export_by_Import"] = (data["US 2024 Exports"]/data["US 2024 Imports (Customs Basis)"])*100
    us_export_import_rate_by_country =  data.groupby("Country")["Export_by_Import"].sum().nlargest(10)
    print("\n rate\n", data.groupby("Country")["Export_by_Import"].sum().nlargest(10))
    print("\n Rate of US Export Import by country: \n",data.groupby("Country")["Export_by_Import"].sum().sort_values(ascending=False))
#Top 10 countries export by US
    us_export_by_country_top10 = data.groupby("Country")["US 2024 Exports"].sum().nlargest(10)
    print("\n Us Export By Import: \n", data.groupby(["Country", "US 2024 Exports"])["US 2024 Imports (Customs Basis)"].sum())
#Renaming column
    data.rename(columns={"US 2024 Imports (Customs Basis)": "US 2024 Imports"}, inplace=True)
    us_import_export_top10 = data.groupby("Country")[["US 2024 Imports", "US 2024 Exports"]].sum().sort_values(by="US 2024 Imports", ascending=False).head(10)
    #countries = data["Country"]

    print("\nlist all the columns: \n", data.columns)
#Renaming columns to make it easier for use in other functions
    data.columns = data.columns.str.strip().str.lower().str.replace(" ", "_").str.replace(r"[()]", "", regex=True)
    return data, us_export_by_country_top10, us_import_export_top10, us_export_import_rate_by_country

def save_new_csv(data):
    data.to_csv("cleaned_tariff_data.csv", index=False)

#bar-chart of export data of top 10 countries
def top10_export(data):
    plt.figure(figsize=(10,6))
    ax = data.plot(kind="bar", color= "blue")
    plt.title("Top 10 countries by export")
    plt.xlabel("Country", )
    plt.ylabel("Export by US")
    plt.xticks(rotation=45)
    for i,v in enumerate(data.values):
        ax.text(i,v + max(data.values)*0.01, f'{v:,.0f}', ha="center", va="bottom", fontsize=9)
    plt.tight_layout()
    plt.savefig("Top10_countries_by_export.png")
    plt.show()

#pie- chart
def export_import_rate(data):
    country = list(data.index)
    rate_export_import = list(data.values)
    total = sum(rate_export_import)

    legend_labels = [f"{c} - {r/total:.1%}" for c, r in zip(country, rate_export_import)]
    plt.figure(figsize=(12,10))

    wedges, _ = plt.pie(rate_export_import, startangle=90)

    plt.legend(wedges, legend_labels, title= "Countries", loc = "center left", bbox_to_anchor = (1.2, 0.5))
    plt.title("Export to import rate by country(top 10)")
    plt.axis("equal")
    plt.tight_layout()
    plt.savefig("export_to_import_rate_by_countries.png")
    plt.show()



#import export bar chart
def import_export(data):
    plt.figure(figsize=(10,7))
    ax = data.plot(kind="bar", color = ["skyblue", "salmon"])
    plt.title("Top 10 countries import export by US")
    plt.xlabel("Country")
    plt.ylabel("Trade value (USD)")
    plt.xticks(rotation = 45, ha="right")
    for container in ax.containers:
        ax.bar_label(container, fmt = '%.0f', label_type = 'edge', fontsize=8)
    plt.tight_layout()
    plt.savefig("import_export_by_US_Top10.png")
    plt.show()



#Main Program
def main():

    tariff_data = read_data("Tariff Calculations plus Population.csv")
    new_data, export_by_country, import_export_2024, export_import_rate_data = explore_data(tariff_data)
    save_new_csv(new_data)
    top10_export(export_by_country)
    export_import_rate(export_import_rate_data)
    import_export(import_export_2024)


if __name__ ==  "__main__":
    main()




