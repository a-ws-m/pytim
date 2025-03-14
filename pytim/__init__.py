# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#from pytim.patches import patchTrajectory, patchOpenMM, patchMDTRAJ

import warnings

from . import datafiles, observables, utilities
from .gitim import GITIM
from .itim import ITIM
from .patches import patchMDTRAJ_ReplacementTables
from .sasa import SASA
from .simple_interface import SimpleInterface
from .version import __version__
from .willard_chandler import WillardChandler

patchMDTRAJ_ReplacementTables()

warnings.filterwarnings(
    "ignore",
    'Failed to guess the mass for the following*')  # To ignore warnings in MDA
