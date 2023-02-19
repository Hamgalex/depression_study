import pandas as pd
import numpy as np
import fuzzywuzzy
from fuzzywuzzy import process
import charset_normalizer

depression_study = pd.read_csv("datasets/depression_study.1000copy.csv",encoding='utf-8')
np.random.seed(0)

medicinas = depression_study['medication'].unique()
#print(medicinas)

matches = fuzzywuzzy.process.extract("savella", medicinas, limit=200, scorer=fuzzywuzzy.fuzz.token_sort_ratio)
#print(matches)

def replace_matches_in_column(df, column, string_to_match, min_ratio):
    # get a list of unique strings
    strings = df[column].unique()
    
    # get the top 500 closest matches to our input string
    matches = fuzzywuzzy.process.extract(string_to_match, strings,limit=500, scorer=fuzzywuzzy.fuzz.token_sort_ratio)

    # only get matches with a ratio > 90
    close_matches = [matches[0] for matches in matches if matches[1] >= min_ratio]

    # get the rows of all the close matches in our dataframe
    rows_with_matches = df[column].isin(close_matches)

    # replace all rows with close matches with the input matches 
    df.loc[rows_with_matches, column] = string_to_match
    


replace_matches_in_column(df=depression_study, column='medication', string_to_match="cymbalta",min_ratio=87)
replace_matches_in_column(df=depression_study, column='medication', string_to_match="lexapro",min_ratio=71)
replace_matches_in_column(df=depression_study, column='medication', string_to_match="effexor",min_ratio=70)
replace_matches_in_column(df=depression_study, column='medication', string_to_match="wellbutrin",min_ratio=79)
replace_matches_in_column(df=depression_study, column='medication', string_to_match="zoloft",min_ratio=54)
replace_matches_in_column(df=depression_study, column='medication', string_to_match="remeron",min_ratio=70)
replace_matches_in_column(df=depression_study, column='medication', string_to_match="savella",min_ratio=85)
replace_matches_in_column(df=depression_study, column='medication', string_to_match="paxil",min_ratio=59)
replace_matches_in_column(df=depression_study, column='medication', string_to_match="prozac",min_ratio=66)
replace_matches_in_column(df=depression_study, column='medication', string_to_match="celexa",min_ratio=66)

medicinas = depression_study['medication'].unique()
print(medicinas)




