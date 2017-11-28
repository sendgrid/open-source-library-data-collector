import sys

from argparse import ArgumentParser

from app import update


def cli():
    parser = ArgumentParser(description='Capture external data relating to GitHub hosted Open Source libraries')
    command_parsers = parser.add_subparsers(title="command")
    command_parsers.required = True

    update_parser = command_parsers.add_parser('update',
                                               help="update database with project's data")
    update_parser.add_argument('--disable-email', dest='send_email', action='store_false')
    update_parser.set_defaults(command_function=update)

    args = vars(parser.parse_args())

    command_function = args.pop('command_function')
    return command_function(**args)


if __name__ == "__main__":
    sys.exit(int(cli() or 0))
