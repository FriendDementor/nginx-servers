import argparse
import jinja2

from sites import sites_function # pylint: disable=import-error
from add import add_static # pylint: disable=import-error
from delete import delete_static # pylint: disable=import-error
from enable import enable # pylint: disable=import-error
from disable import disable # pylint: disable=import-error

# from .add import add
# from .delete import delete
# from .ssl import ssl
# from .enable import enable
# from .disable import disable

def consume_and_print(function):
    return lambda args: print(function(args))

def extract_domain_attribute(function):
    return lambda args: print(function(args.domain))

# create the top-level parser
nsc_parser = argparse.ArgumentParser()
subparsers = nsc_parser.add_subparsers()

# create the parser for the "sites" command
parser_list = subparsers.add_parser('list')
parser_list.set_defaults(func=consume_and_print(sites_function))

# # create the parser for the "add" command
parser_add = subparsers.add_parser('add')
parser_add.add_argument('domain')
parser_add.set_defaults(func=extract_domain_attribute(add_static))

# # create the parser for the "delete" command
parser_delete = subparsers.add_parser('delete')
parser_delete.add_argument('domain')
parser_delete.set_defaults(func=extract_domain_attribute(delete_static))

# # create the parser for the "ssl" command
# parser_ssl = subparsers.add_parser('ssl')
# parser_ssl.add_argument('domain')
# parser_ssl.set_defaults(func=ssl)

# # create the parser for the "enable" command
parser_enable = subparsers.add_parser('enable')
parser_enable.add_argument('domain')
parser_enable.set_defaults(func=extract_domain_attribute(enable))

# # create the parser for the "disable" command
parser_disable = subparsers.add_parser('disable')
parser_disable.add_argument('domain')
parser_disable.set_defaults(func=extract_domain_attribute(disable))

