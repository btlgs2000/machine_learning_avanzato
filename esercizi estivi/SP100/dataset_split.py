import numpy as np
from pathlib import Path
import os

import pandas as pd
from tqdm import tqdm

TOP_FOLDER = Path(r'F:\Documenti\machine_learning_avanzato\esercizi estivi\SP100')

_DATASET_SPLITS = {
    'test_post_covid': ('2020-03-20', '2050-01-01'),
    'test_covid': ('2020-02-19', '2020-03-19'),
    'test_set': ('2018-02-19', '2020-02-18'),
    'val_set': ('2015-02-19', '2018-02-18'),
    'train_set': ('1980-01-01', '2015-02-18')
}

DATASET_SPLITS = {key: (np.datetime64(start_date), np.datetime64(end_date)) for key, (start_date, end_date) in _DATASET_SPLITS.items()}

# crea le folder
for key in DATASET_SPLITS.keys():
    os.mkdir(TOP_FOLDER / key)


for file_name in tqdm(os.listdir(TOP_FOLDER / 'dataset')):
    df = pd.read_csv(TOP_FOLDER / 'dataset' / file_name, parse_dates=['date'])
    for key, (start_date, end_date) in DATASET_SPLITS.items():
        df_chunk = df[(df.date >= start_date) & (df.date <= end_date)]
        df_chunk.to_csv(TOP_FOLDER / key / file_name, index=False)