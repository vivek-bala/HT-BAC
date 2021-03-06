#!/usr/bin/env python

"""This module implements radical-bac-fecalc --benchmark.
"""

__author__    = "Ole Weidner"
__email__     = "ole.weidner@rutgers.edu"
__copyright__ = "Copyright 2013-2014, The RADICAL Project at Rutgers"
__license__   = "MIT"

import imp
import os, sys, uuid
import urllib
import optparse
import radical.pilot 

from radical.ensemblemd.htbac.callbacks import *
from radical.ensemblemd.htbac.kernel import KERNEL


# ----------------------------------------------------------------------------
#
def run_benchmark(config):
    PILOT_SIZES = config.BENCHMARK_PILOT_SIZES
    TASK_BATCHES = config.BENCHMARK_TASK_BATCHES