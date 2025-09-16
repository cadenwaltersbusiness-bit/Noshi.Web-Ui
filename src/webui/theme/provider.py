"""
Theme provider for managing theme state and switching
"""
import gradio as gr
from typing import Tuple, Dict, Any
from .theme import get_replit_theme
from .styles import get_replit_css

class ThemeProvider:
    """Manages theme state and provides theme switching functionality"""
    
    def __init__(self, default_dark_mode: bool = True):
        self.dark_mode = default_dark_mode
        self._theme_callbacks = []
    
    def get_current_theme(self) -> gr.Theme:
        """Get the current theme object"""
        return get_replit_theme(self.dark_mode)
    
    def get_current_css(self) -> str:
        """Get the current CSS"""
        return get_replit_css(self.dark_mode)
    
    def toggle_theme(self) -> Tuple[str, Dict[str, Any]]:
        """Toggle between dark and light mode"""
        self.dark_mode = not self.dark_mode
        
        # Return new CSS and any other updates needed
        new_css = self.get_current_css()
        theme_class = "" if self.dark_mode else "light-mode"
        
        # Return updates for any components that need to know about theme change
        updates = {
            "css": new_css,
            "theme_class": theme_class,
            "dark_mode": self.dark_mode
        }
        
        # Call any registered callbacks
        for callback in self._theme_callbacks:
            callback(self.dark_mode)
        
        return new_css, updates
    
    def register_theme_callback(self, callback):
        """Register a callback to be called when theme changes"""
        self._theme_callbacks.append(callback)
    
    def get_theme_toggle_js(self) -> str:
        """Get JavaScript for theme toggling"""
        return """
        function toggleTheme() {
            const body = document.body;
            const isDark = !body.classList.contains('light-mode');
            
            if (isDark) {
                body.classList.add('light-mode');
                localStorage.setItem('theme', 'light');
            } else {
                body.classList.remove('light-mode');
                localStorage.setItem('theme', 'dark');
            }
            
            // Trigger theme toggle in Gradio
            return !isDark;
        }
        
        // Apply saved theme on load
        function applySavedTheme() {
            const savedTheme = localStorage.getItem('theme');
            const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
            const useDark = savedTheme ? savedTheme === 'dark' : prefersDark;
            
            if (!useDark) {
                document.body.classList.add('light-mode');
            }
            
            return useDark;
        }
        
        // Initialize theme on page load
        document.addEventListener('DOMContentLoaded', applySavedTheme);
        """

# Global theme provider instance
theme_provider = ThemeProvider()

def create_theme_toggle_button() -> gr.Button:
    """Create a theme toggle button component"""
    return gr.Button(
        "🌙",
        elem_id="theme-toggle",
        elem_classes=["theme-toggle"],
        scale=0,
        min_width=40,
    )

def setup_theme_toggle(theme_button: gr.Button) -> None:
    """Setup theme toggle functionality for a button"""
    def toggle_theme_handler():
        css, updates = theme_provider.toggle_theme()
        icon = "☀️" if theme_provider.dark_mode else "🌙"
        return gr.update(value=icon)
    
    theme_button.click(
        fn=toggle_theme_handler,
        outputs=[theme_button],
        js=theme_provider.get_theme_toggle_js()
    )