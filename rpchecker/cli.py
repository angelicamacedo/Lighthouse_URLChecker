# cli.py

import argparse

def read_user_cli_args():
    """Handle the CLI arguments and options"""
    parser = argparse.ArgumentParser(
        prog="rpchecker", description="check the availability of websites"
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="insira uma ou mais URLs separadas por espaço",
    )

    parser.add_argument(
        "-f",
        "--file",
        metavar="File",
        nargs="+",
        type=str,
        default="",
        help="insira o caminho completo junto com o nome do arquivo",
    )

    return parser.parse_args()

def display_check_result(result, url, error=""):
    """Display the result of a connectivity check."""
    print(f'O status da "{url}" é:', end=" ")
    if result:
        print('"Online!" 👍')
    else:
        print(f'"Offline?" 👎 \n  Erro: "{error}"')