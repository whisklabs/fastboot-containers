#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import scyllasetup
import logging
import commandlineparser

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format="%(message)s")

try:
    arguments = commandlineparser.parse()
    setup = scyllasetup.ScyllaSetup(arguments)
    setup.developerMode()
    setup.cpuSet()
    setup.cqlshrc()
    setup.arguments()
    setup.set_housekeeping()
    os.system("/usr/bin/supervisord -c /etc/supervisord.conf")
except Exception:
    logging.exception('failed!')
