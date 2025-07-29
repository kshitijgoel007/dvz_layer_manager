"""Datoviz Layer Manager - A layered visualization wrapper on top of Datoviz."""

__version__ = "0.0.1"
__author__ = "Kshitij Goel"
__email__ = "kshitijgoel16061995@gmail.com"

from .panel_manager import PanelManager
from .composite_visuals import vector_field_visuals

__all__ = ["PanelManager", "vector_field_visuals", "__version__"]
