# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2015, Numenta, Inc.  Unless you have purchased from
# Numenta, Inc. a separate commercial license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

"""Unit test of the unicorn_backend.model_runner_2 module"""

import logging
from mock import patch
import sys
import unittest

##from nta.utils.logging_support_raw import LoggingSupport
from unicorn_backend import model_runner_2



_LOGGER = logging.getLogger("unicorn_model_runner_2_test")



##def setUpModule():
##  LoggingSupport.initTestApp()



class ModelRunnerTestCase(unittest.TestCase):

  def testParseArgs(self):
    """ Invalid CLI arguments are rejected
    """

    def _assertArgumentPatternFails(argumentPattern=None):
      if argumentPattern is None:
        argumentPattern = []

      argumentPattern = ["unicorn_backend/model_runner_2.py"] + argumentPattern

      with patch.object(sys, "argv", argumentPattern):
        # pylint: disable=W0212
        with self.assertRaises(model_runner_2._CommandLineArgError):
          model_runner_2._parseArgs()

    _assertArgumentPatternFails()

    _assertArgumentPatternFails(["--input="])
    _assertArgumentPatternFails(['--input="1"'])
    _assertArgumentPatternFails(['--input="{}"'])

    _assertArgumentPatternFails(["--agg="])
    _assertArgumentPatternFails(['--agg="1"'])
    _assertArgumentPatternFails(['--agg="{}"'])

    _assertArgumentPatternFails(["--model="])
    _assertArgumentPatternFails(['--model="1"'])
    _assertArgumentPatternFails(['--model="{}"'])

    _assertArgumentPatternFails(['--input="{}"', '--model="{}"'])
