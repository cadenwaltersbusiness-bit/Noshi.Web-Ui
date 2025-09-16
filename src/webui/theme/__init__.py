"""
Replit-inspired theme system for Gradio WebUI
"""

from .theme import ReplitTheme, ReplitLightTheme, get_replit_theme
from .styles import get_replit_css, REPLIT_CSS
from .provider import ThemeProvider, theme_provider, create_theme_toggle_button, setup_theme_toggle
from .tokens import COLORS, DARK_COLORS, LIGHT_COLORS, SPACING, RADIUS, TYPOGRAPHY, SHADOWS

__all__ = [
    "ReplitTheme",
    "ReplitLightTheme", 
    "get_replit_theme",
    "get_replit_css",
    "REPLIT_CSS",
    "ThemeProvider",
    "theme_provider", 
    "create_theme_toggle_button",
    "setup_theme_toggle",
    "COLORS",
    "DARK_COLORS",
    "LIGHT_COLORS", 
    "SPACING",
    "RADIUS",
    "TYPOGRAPHY",
    "SHADOWS",
]