## Get underlying data 
### stocks.ba.cnews(symbol: str, start_date: str = '2022-08-24', end_date: str = '2022-09-23') -> List[Dict]

Get news from a company. [Source: Finnhub]

    Parameters
    ----------
    symbol : str
        company ticker to look for news articles
    start_date: str
        date to start searching articles, with format YYYY-MM-DD
    end_date: str
        date to end searching articles, with format YYYY-MM-DD

    Returns
    ----------
    articles : List
        term to search on the news articles
