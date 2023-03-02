import pandas as pd
import numpy as np

depression_study = pd.read_csv("datasets/depression_study.10000.csv",encoding='utf-8')
np.random.seed(0)

recetas = depression_study[~depression_study["medication"].isna()]