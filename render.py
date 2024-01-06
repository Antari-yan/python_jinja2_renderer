#!/usr/bin/env python3

"""
This rendering script intakes a yaml file and a jinja2 template file and
renders the template according to the yaml data.
"""

from sys import exit as sys_exit, stdout as sys_stdout
from argparse import ArgumentParser
from yaml import load as yaml_load, BaseLoader as yaml_base_loader, dump as yaml_dump
from jinja2 import Environment as jinja2_env, FileSystemLoader as jinja2_loader

# Clear screen
#import os
#os.system('cls' if os.name == 'nt' else 'clear')

# Adding positional arguments (parameters) using argparse
parser = ArgumentParser()
parser.add_argument("--yaml", "-y")
parser.add_argument("--jinja", "-j", "--jinja2", "-j2")
arguments = parser.parse_args()


def get_options(args):
    """
    Parses the command line arguments into the corresponding variables
    """

    if args.yaml:
        yamlfile = args.yaml
    if args.jinja:
        jinjafile = args.jinja

    return yamlfile, jinjafile

def main(): # pylint: disable=C0116
    yamlfile, jinjafile = get_options(arguments)


    with open(yamlfile, 'r', encoding='utf-8') as file:
        yamldict = yaml_load(file,Loader=yaml_base_loader)

    print('--- YAML dict in '+yamlfile+' ---')
    yaml_dump(yamldict, sys_stdout)
    print   # pylint: disable=W0104


    env = jinja2_env(loader=jinja2_loader('.'))

    print('\n--- Jinja2 rendered template '+jinjafile+' ---')
    template = env.get_template(jinjafile)
    print(template.render(**yamldict))

# Start program
if __name__ == "__main__":
    main()
