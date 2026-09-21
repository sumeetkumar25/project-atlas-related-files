# atlas/core/__init__.py
"""
Core infrastructure for Project Atlas v2.0
Scientific research framework for market analysis.
"""

from .base_research_module import BaseResearchModule
from .research_result import ResearchResult
from .export_manager import ExportManager
from .logger import AtlasLogger

# Utilities (separated by domain)
from . import math_utils
from . import returns_utils
from . import statistics_utils
from . import formatting_utils
from . import validation_utils

__all__ = [
    'BaseResearchModule',
    'ResearchResult',
    'ExportManager',
    'AtlasLogger',
]