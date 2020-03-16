import pandas as pd
import seaborn as sns

@pd.api.extensions.register_dataframe_accessor("eda")
class EDA:
    def __init__(self, df):
        self._df = df

    def corr_plot():
        corr_df = self._df.corr()
        sns.heatmap(corr_df)
        return None
        
