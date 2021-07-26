import re
import os
import pandas as pd
from glob import glob

def get_dataframe_from_json(dirLoc):
    df = pd.concat([pd.read_json(file, lines=True) for file in glob(os.path.join(dirLoc, '*.json'))])
    df['cleanedContent'] = df.content.apply(lambda x: re.sub(r"http\S+", "", x))
    return df[df.lang == 'en']

if __name__ == '__main__':
    pass