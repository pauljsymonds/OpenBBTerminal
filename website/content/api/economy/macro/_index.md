To obtain charts, make sure to add `chart=True` as the last parameter

## Get underlying data 
### economy.macro(parameters: list = None, countries: list = None, transform: str = '', start_date: str = '1900-01-01', end_date=datetime.date(2022, 9, 23), symbol: str = '') -> Tuple[Any, Dict[Any, Dict[Any, Any]], str]

This functions groups the data queried from the EconDB database [Source: EconDB]

    Parameters
    ----------
    parameters: list
        The type of data you wish to download. Available parameters can be accessed through economy.macro_parameters().
    countries : list
        The selected country or countries. Available countries can be accessed through economy.macro_countries().
    transform : str
        The selected transform. Available transforms can be accessed through get_macro_transform().
    start_date : str
        The starting date, format "YEAR-MONTH-DAY", i.e. 2010-12-31.
    end_date : str
        The end date, format "YEAR-MONTH-DAY", i.e. 2020-06-05.
    symbol : str
        In what currency you wish to convert all values.

    Returns
    ----------
    pd.DataFrame
        A DataFrame with the requested macro data of all chosen countries
    Dictionary
        A dictionary containing the units of each country's parameter (e.g. EUR)
    str
        Denomination which can be Trillions, Billions, Millions, Thousands

## Getting charts 
### economy.macro(parameters: list = None, countries: list = None, transform: str = '', start_date: str = '1900-01-01', end_date: str = '2022-09-23', symbol: str = '', raw: bool = False, external_axes: Optional[List[axes]] = None, export: str = '', chart=True)

Show the received macro data about a company [Source: EconDB]

    Parameters
    ----------
    parameters: list
        The type of data you wish to display. Available parameters can be accessed through get_macro_parameters().
    countries : list
        The selected country or countries. Available countries can be accessed through get_macro_countries().
    transform : str
        select data transformation from:
            '' - no transformation
            'TPOP' - total percentage change on period,
            'TOYA' - total percentage since 1 year ago,
            'TUSD' - level USD,
            'TPGP' - Percentage of GDP,
            'TNOR' - Start = 100
    start_date : str
        The starting date, format "YEAR-MONTH-DAY", i.e. 2010-12-31.
    end_date : str
        The end date, format "YEAR-MONTH-DAY", i.e. 2020-06-05.
    symbol : str
        In what currency you wish to convert all values.
    raw : bool
        Whether to display the raw output.
    external_axes: Optional[List[plt.axes]]
        External axes to plot on
    export : str
        Export data to csv,json,xlsx or png,jpg,pdf,svg file

    Returns
    ----------
    Plots the Series.
