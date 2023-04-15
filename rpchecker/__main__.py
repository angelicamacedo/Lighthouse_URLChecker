# __main__.py

import sys
import pathlib

from rpchecker.cli import read_user_cli_args, display_check_result
from rpchecker.checker import site_is_online

def main():
    """Run Site Checker."""
    user_args = read_user_cli_args()
    urls = _get_websites_urls(user_args)
    
    if not urls:
        print("Erro: sem URLs para analisar.", file=sys.stderr)
        sys.exit(1)
    else:
        _site_check(urls)

def _get_websites_urls(user_args):
    """Join the urls"""
    urls = user_args.urls
    if user_args.file:
        urls += _read_urls_from_file(user_args.file)
    return urls

def _site_check(urls):
    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)

def _read_urls_from_file(file):
    """Open a file based on the given path"""
    file_path = pathlib.Path(file[0])
    if file_path.is_file():
        with file_path.open() as urls_file:
            urls = [url.replace(",", "") for url in urls_file]
            if urls:
                return urls
            print(f"Error: O arquivo esta vazio, {file}", file=sys.stderr)
    else:
        print("Error: Arquivo nao encontrado", file=sys.stderr)
    return []
           
if __name__ == "__main__":
    main()