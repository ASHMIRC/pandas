import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    a=weather.pivot(index='month',columns='city',values='temperature')
    return a
