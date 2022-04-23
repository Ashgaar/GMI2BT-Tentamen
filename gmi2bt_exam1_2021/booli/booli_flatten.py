# -*- coding: utf-8 -*-
'''booli_flatten.py'''

import json
import pandas as pd
# pip install cherrypicker
from cherrypicker import CherryPicker

def main():
    with open('json_file.json') as jf:
        result = json.load(jf)
    picker = CherryPicker(result)
    flat = picker['sold'].flatten().get()
    df_cherry = pd.DataFrame(flat)
    print(f'\ndf_cherry\n{df_cherry}')
    # using pandas to write CSV, ';'-separator, do not write the index, header/column names will be on first row
    df_cherry.to_csv('villa_county_xyz.csv', index=False, sep=';')

if __name__ == "__main__":
    main()
