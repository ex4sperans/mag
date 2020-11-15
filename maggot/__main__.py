import sys
import argparse

from maggot.scripts import summarize, show_config


COMMANDS = {
    "summarize": summarize,
    "show-config": show_config
}

def collect_args():

    parser = argparse.ArgumentParser(
        prog="maggot",
        usage=(
            "maggot COMMAND ...\n\n"
            "Maggot - lightweight experiment tracker\n\n"
            "Available commands:\n\n"
            "  summarize\tSummarize metrics from all experiments in a given directory.\n"
            "  show-config\tShow experiment config.\n"
        ),
        add_help=False
    )
    parser.add_argument("command", nargs="?")

    args, uargs = parser.parse_known_args()
    if args.command is None:
        parser.print_usage()
        sys.exit()

    return args, uargs


def main():

    args, uargs = collect_args()
    COMMANDS[args.command].main(uargs)

