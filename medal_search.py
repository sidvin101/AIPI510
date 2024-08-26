import pandas as pd
import argparse

def main(search_term):

    # First, test if the input is empty
    if not search_term:
        return "You have not entered a Country or Country Code. Please type one."

    search_term = search_term.upper()

    df = pd.read_csv("olympics2024.csv")

    df['Country'] = df['Country'].str.upper()
    countries = df['Country'].tolist()
    country_abr = df['Country Code'].tolist()


    # Then, test if the input is not recognized
    if search_term not in countries and search_term not in country_abr:
        return """
I'm sorry, either this country does not exist or have not participated in this
year's Olympics. If you believe that this is not the case, please check your
spelling. The full name of the country or the abbreviation are enough.
"""

    # Otherwise, we are free to return the result
    if search_term in countries:
        row = df.loc[(df['Country'] == search_term)]
    elif search_term in country_abr:
        row = df.loc[(df['Country Code'] == search_term)]

    return f"{row['Country'].iloc[0]} has {row['Gold'].iloc[0]} Gold medals, {row['Silver'].iloc[0]} Silver medals, and {row['Bronze'].iloc[0]} Bronze medals. A total of {row['Total'].iloc[0]} medals."

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("search_term", type=str)
    args = parser.parse_args()

    result = main(args.search_term)
    if result:
        print(result)
