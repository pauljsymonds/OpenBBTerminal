""" Options Screener Controller Module """
__docformat__ = "numpy"

import argparse
import logging
from typing import List

from prompt_toolkit.completion import NestedCompleter

from openbb_terminal import feature_flags as obbff
from openbb_terminal.decorators import log_start_end
from openbb_terminal.helper_funcs import EXPORT_ONLY_RAW_DATA_ALLOWED, check_positive
from openbb_terminal.menu import session
from openbb_terminal.parent_classes import BaseController
from openbb_terminal.rich_config import MenuText, console
from openbb_terminal.stocks.comparison_analysis import ca_controller
from openbb_terminal.stocks.options.screen import syncretism_view, syncretism_model

# pylint: disable=E1121


logger = logging.getLogger(__name__)


class ScreenerController(BaseController):
    """Screener Controller class"""

    CHOICES_COMMANDS = ["view", "set", "scr"]
    CHOICES_MENUS = [
        "ca",
    ]

    preset_choices = syncretism_model.get_preset_choices()

    PATH = "/stocks/options/screen/"

    def __init__(self, queue: List[str] = None):
        """Constructor"""
        super().__init__(queue)

        self.preset = "high_IV"
        self.screen_tickers: List = list()

        if session and obbff.USE_PROMPT_TOOLKIT:
            choices: dict = {c: {} for c in self.controller_choices}
            choices["view"] = {c: None for c in self.preset_choices}
            choices["set"] = {c: None for c in self.preset_choices}
            self.completer = NestedCompleter.from_nested_dict(choices)

    def print_help(self):
        """Print help"""
        mt = MenuText("stocks/options/screen/")
        mt.add_cmd("view")
        mt.add_cmd("set")
        mt.add_raw("\n")
        mt.add_param("_preset", self.preset)
        mt.add_raw("\n")
        mt.add_cmd("scr")
        mt.add_raw("\n")
        mt.add_param("_screened_tickers", ", ".join(self.screen_tickers))
        mt.add_raw("\n")
        mt.add_menu("ca")
        console.print(text=mt.menu_text, menu="Stocks - Options - Screener")

    @log_start_end(log=logger)
    def call_view(self, other_args: List[str]):
        """Process view command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            prog="view",
            description="""View available presets under presets folder.""",
        )
        parser.add_argument(
            "-p",
            "--preset",
            action="store",
            dest="preset",
            type=str,
            help="View specific custom preset",
            default="",
            choices=self.preset_choices,
        )
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "-p")
        ns_parser = self.parse_known_args_and_warn(parser, other_args)
        if ns_parser:
            if ns_parser.preset:
                syncretism_view.view_available_presets(preset=ns_parser.preset)

            else:
                for preset in self.preset_choices:
                    console.print(preset)
                console.print("")

    @log_start_end(log=logger)
    def call_set(self, other_args: List[str]):
        """Process set command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            prog="set",
            description="""Set preset from custom and default ones.""",
        )
        parser.add_argument(
            "-p",
            "--preset",
            action="store",
            dest="preset",
            type=str,
            default="template",
            help="Filter presets",
            choices=self.preset_choices,
        )
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "-p")
        ns_parser = self.parse_known_args_and_warn(parser, other_args)
        if ns_parser:
            self.preset = ns_parser.preset
        console.print("")

    @log_start_end(log=logger)
    def call_scr(self, other_args: List[str]):
        """Process scr command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="scr",
            description="""Screener filter output from https://ops.syncretism.io/index.html.
        Where: CS: Contract Symbol; S: Symbol, T: Option Type; Str: Strike; Exp v: Expiration;
        IV: Implied Volatility; LP: Last Price; B: Bid; A: Ask; V: Volume; OI: Open Interest;
        Y: Yield; MY: Monthly Yield; SMP: Regular Market Price; SMDL: Regular Market Day Low;
        SMDH: Regular Market Day High; LU: Last Trade Date; LC: Last Crawl; ITM: In The Money;
        PC: Price Change; PB: Price-to-book. """,
        )
        parser.add_argument(
            "-p",
            "--preset",
            action="store",
            dest="preset",
            type=str,
            default=self.preset,
            help="Filter presets",
            choices=self.preset_choices,
        )
        parser.add_argument(
            "-l",
            "--limit",
            type=check_positive,
            default=10,
            help="Limit of random entries to display. Default shows all",
            dest="limit",
        )

        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "-p")
        ns_parser = self.parse_known_args_and_warn(
            parser, other_args, EXPORT_ONLY_RAW_DATA_ALLOWED
        )
        if ns_parser:
            self.screen_tickers = syncretism_view.view_screener_output(
                preset=ns_parser.preset,
                limit=ns_parser.limit,
                export=ns_parser.export,
            )

    @log_start_end(log=logger)
    def call_ca(self, _):
        """Call the comparison analysis menu with selected tickers"""
        if self.screen_tickers:
            self.queue = ca_controller.ComparisonAnalysisController(
                self.screen_tickers, self.queue
            ).menu(custom_path_menu_above="/stocks/")
        else:
            console.print(
                "Some tickers must be screened first through one of the presets!\n"
            )
