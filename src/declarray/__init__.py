"""Declarray: fast mining and checking of Declare models over activity sequences."""

from declarray.checker import Checker, Conformance
from declarray.miner import mine
from declarray.model.constraints import Constraint
from declarray.model.declare_model import DeclareModel
from declarray.model.measures import Measures
from declarray.model.settings import MiningSettings
from declarray.model.templates import Template

__version__ = '0.1.0'

__all__ = [
    'Checker',
    'Conformance',
    'Constraint',
    'DeclareModel',
    'Measures',
    'MiningSettings',
    'Template',
    '__version__',
    'mine',
]
