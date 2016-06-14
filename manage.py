#!env/bin/python

import pprint
pp = pprint.PrettyPrinter(indent=4)

import os, sys
PROJECT_PATH = os.path.abspath('.')
sys.path.append(PROJECT_PATH)

from flask import current_app

from flask.ext.script import Manager
from flask.ext.script import Command, Option, Shell

from approot import create_app, db
#----------------------------------------------


manager = Manager(create_app)
manager.add_option('-c', '--config', dest='config', required=False, default='development')


@manager.command
def dump_config():
    pp.pprint(current_app.config)


def _make_context():
    return dict(app=current_app, db=db, models=models)
manager.add_command('shell', Shell(make_context=_make_context))


if __name__ == '__main__':
    manager.run()
