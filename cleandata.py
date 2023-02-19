import pandas as pd
import numpy as np
import fuzzywuzzy
from fuzzywuzzy import process
import charset_normalizer

depression_study = pd.read_csv("datasets/depression_study.1000copy.csv",encoding='utf-8')
print(depression_study)