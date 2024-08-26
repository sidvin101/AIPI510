import pandas as pd
import argparse

#Function to collect medal counts
def get_medal_counts(search_term):

    #If no search_term is recognized
    if not search_term:
        return "You have not entered a Country or Country Code. Please type one."

    #Uppercase the search term
    search_term = search_term.upper()

    #Extract the olympics dataset
    df = pd.read_csv("olympics2024.csv")

    #Get a list of countries in the olympics
    df['Country'] = df['Country'].str.upper()
    countries = df['Country'].tolist()
    country_abr = df['Country Code'].tolist()

    #Raise an error if the country does not exist 
    if search_term not in countries and search_term not in country_abr:
        return """
I'm sorry, either this country does not exist or have not participated in this
year's Olympics. If you believe that this is not the case, please check your
spelling. The full name of the country or the abbreviation are enough.
"""

    #Gets the row with the correct country or country abbreviation based on what the user input
    if search_term in countries:
        row = df.loc[(df['Country'] == search_term)]
    elif search_term in country_abr:
        row = df.loc[(df['Country Code'] == search_term)]

        
    #print out the medal count
    return f"{row['Country'].iloc[0]} has {row['Gold'].iloc[0]} Gold medals, {row['Silver'].iloc[0]} Silver medals, and {row['Bronze'].iloc[0]} Bronze medals. A total of {row['Total'].iloc[0]} medals."

def main():
    #Adds an argument parser to allow the user to paste their search_term directly on the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("search_term", type=str)
    args = parser.parse_args()
    result = get_medal_counts(args.search_term)
    if result:
        print(result)

if __name__ == "__main__":
    main()
