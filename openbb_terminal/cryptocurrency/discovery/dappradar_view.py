"""DappRadar view"""
__docformat__ = "numpy"

import logging
import os
import numpy as np

from openbb_terminal.cryptocurrency.dataframe_helpers import (
    lambda_very_long_number_formatter,
)
from openbb_terminal.cryptocurrency.discovery import dappradar_model
from openbb_terminal.decorators import log_start_end
from openbb_terminal.helper_funcs import export_data, print_rich_table
from openbb_terminal.rich_config import console

logger = logging.getLogger(__name__)


@log_start_end(log=logger)
def display_top_nfts(limit: int = 10, sortby: str = "", export: str = "") -> None:
    """Displays top nft collections [Source: https://dappradar.com/]

    Parameters
    ----------
    limit: int
        Number of records to display
    sortby: str
        Key by which to sort data
    export : str
        Export dataframe data to csv,json,xlsx file
    """

    df = dappradar_model.get_top_nfts(sortby, limit)
    if df.empty:
        console.print("Failed to fetch data from DappRadar\n")
        return
    for col in ["Floor Price [$]", "Avg Price [$]", "Market Cap [$]", "Volume [$]"]:
        if col in df.columns:
            df[col] = (
                df[col]
                .fillna(-1)
                .apply(lambda x: lambda_very_long_number_formatter(x))
                .replace(-1, np.nan)
            )
    print_rich_table(
        df,
        headers=list(df.columns),
        show_index=False,
        title="Top NFT collections",
    )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "drnft",
        df,
    )


@log_start_end(log=logger)
def display_top_games(limit: int = 10, export: str = "", sortby: str = "") -> None:
    """Displays top blockchain games [Source: https://dappradar.com/]

    Parameters
    ----------
    limit: int
        Number of records to display
    sortby: str
        Key by which to sort data
    export : str
        Export dataframe data to csv,json,xlsx file
    """

    df = dappradar_model.get_top_games(sortby, limit)
    if df.empty:
        console.print("Failed to fetch data from DappRadar\n")
        return
    for col in ["Daily Users", "Daily Volume [$]"]:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: lambda_very_long_number_formatter(x))
    print_rich_table(
        df,
        headers=list(df.columns),
        show_index=False,
        title="Top Blockchain Games",
    )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "drgames",
        df,
    )


@log_start_end(log=logger)
def display_top_dexes(limit: int = 10, export: str = "", sortby: str = "") -> None:
    """Displays top decentralized exchanges [Source: https://dappradar.com/]

    Parameters
    ----------
    limit: int
        Number of records to display
    sortby: str
        Key by which to sort data
    export : str
        Export dataframe data to csv,json,xlsx file
    """

    df = dappradar_model.get_top_dexes(sortby, limit)
    if df.empty:
        console.print("Failed to fetch data from DappRadar\n")
        return
    for col in ["Daily Users", "Daily Volume [$]"]:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: lambda_very_long_number_formatter(x))
    print_rich_table(
        df,
        headers=list(df.columns),
        show_index=False,
        title="Top Decentralized Exchanges",
    )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "drdex",
        df,
    )


@log_start_end(log=logger)
def display_top_dapps(limit: int = 10, export: str = "", sortby: str = "") -> None:
    """Displays top decentralized exchanges [Source: https://dappradar.com/]

    Parameters
    ----------
    limit: int
        Number of records to display
    sortby: str
        Key by which to sort data
    export : str
        Export dataframe data to csv,json,xlsx file
    """

    df = dappradar_model.get_top_dapps(sortby, limit)
    if df.empty:
        console.print("Failed to fetch data from DappRadar\n")
        return
    for col in ["Daily Users", "Daily Volume [$]"]:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: lambda_very_long_number_formatter(x))
    print_rich_table(
        df,
        headers=list(df.columns),
        show_index=False,
        title="Top Decentralized Applications",
    )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "drdapps",
        df,
    )
