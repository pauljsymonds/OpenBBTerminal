To obtain charts, make sure to add `chart=True` as the last parameter

## Get underlying data 
### crypto.ov.news(limit: int = 60, post_kind: str = 'news', filter_: Optional[str] = None, region: str = 'en', source: str = 'cp', symbol: str = None, sortby: str = 'published_at', ascend: bool = True) -> pandas.core.frame.DataFrame

Get recent posts from CryptoPanic news aggregator platform. [Source: https://cryptopanic.com/]

    Parameters
    ----------
    limit: int
        number of news to fetch
    post_kind: str
        Filter by category of news. Available values: news or media.
    filter_: Optional[str]
        Filter by kind of news. One from list: rising|hot|bullish|bearish|important|saved|lol
    region: str
        Filter news by regions. Available regions are: en (English), de (Deutsch), nl (Dutch),
        es (Español), fr (Français), it (Italiano), pt (Português), ru (Русский)
    sortby: str
        Key to sort by.
    ascend: bool
        Sort in ascend order.

    Returns
    -------
    pd.DataFrame
        DataFrame with recent news from different sources filtered by provided parameters.

## Getting charts 
### crypto.ov.news(post_kind: str = 'news', region: str = 'en', filter_: Optional[str] = None, limit: int = 25, sortby: str = 'published_at', ascend: bool = False, links: bool = False, export: str = '', chart=True) -> None

Display recent posts from CryptoPanic news aggregator platform.
    [Source: https://cryptopanic.com/]

    Parameters
    ----------
    limit: int
        number of news to display
    post_kind: str
        Filter by category of news. Available values: news or media.
    filter_: Optional[str]
        Filter by kind of news. One from list: rising|hot|bullish|bearish|important|saved|lol
    region: str
        Filter news by regions. Available regions are: en (English), de (Deutsch), nl (Dutch),
        es (Español), fr (Français), it (Italiano), pt (Português), ru (Русский)
    sortby: str
        Key to sort by.
    ascend: bool
        Sort in ascending order.
    links: bool
        Show urls for news
    export : str
        Export dataframe data to csv,json,xlsx file
