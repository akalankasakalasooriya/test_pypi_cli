import logging
import argparse
import json
import shutil
import sys
import os
from _xxsubinterpreters import destroy

import pkg_resources
from pathlib import Path

log = logging.getLogger(__name__)


def main(args=None, catch=None):

    parser = argparse.ArgumentParser(prog='jsonify', description='Command line interface for the jsonify package')
    parser.add_argument(
        '--file', default='info', help='Log level',
    )
    parser.add_argument(
        '--init', default='no-init', help='create dirs',
    )
    # subparsers = parser.add_subparsers(help='Sub-commands')

    # Parse all command line arguments
    args = parser.parse_args(args)

    # This is not a good way to handle the cases
    # where help should be printed.
    # if hasattr(args, 'func'):
    #     # Call the desired subcommand function
    #     logging.basicConfig(level=args.loglevel.upper())
    #     print(f"loglevel is: {args.loglevel}")
    #     return 0
    # else:
    #     parser.print_help()
    #     return 0
    print(f"file is: {args.file}")
    file = args.file
    init = args.init

    if init == "init":
        try:
            path = pkg_resources.resource_filename(__name__, "initial_project")
            shutil.copytree(src=path, dst="./test", ignore=shutil.ignore_patterns('__init__.py', '__pycache__'))
            shutil.move("./test/test.py.bak", "./test/test.py")
        except Exception as e:
            print(f"init failed due to: {e}")
    else:
        print("no init dir created")

    try:
        with open(file=file, encoding='utf8', mode="r") as f:
            lines = f.readlines()

        formatted = json.dumps(json.loads(lines[0]), indent=2)
        print(formatted)
    except Exception as e:
        print(f"jsonifying failed due to: {e}")
