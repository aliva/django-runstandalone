#!/usr/bin/env python3

import os
import sys

if __name__ == '__main__':
    working_dir = os.path.abspath(os.path.dirname(__file__))
    # add project dir to your python path
    # I mean the directory which contains 'manage.py'
    sys.path.insert(0, os.path.abspath(os.path.join(working_dir, 'testproject')))

    # adding runstandalone to python path to make DjangoRunStandAlone importable
    sys.path.insert(0, os.path.abspath(os.path.join(working_dir + '/../')))

    # import DjangoRunStandAlone
    import runstandalone.runstandalone
    dj_runner = runstandalone.runstandalone.DjangoRunStandAlone(
        # this is the wsgi.py in project. it should be importable
        wsgi='testproject.wsgi',
        # django server ip - optional - default: 0.0.0.0
        # ip='127.0.0.1',
        # django server port - optional - default: random
        # port=8000,
        # window icon - optional - path to image file
        # make sure send a valid image file
        icon=os.path.abspath(os.path.abspath(os.path.join(working_dir, 'testproject/testproject/static/django.png')))
    )

    # run!!
    dj_runner.run()
    #dj_runner.run('gtk3')
    #dj_runner.run('gtk2')
    #dj_runner.run('qt4')
