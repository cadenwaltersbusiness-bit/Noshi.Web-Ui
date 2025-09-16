"""
Replit-inspired custom Gradio theme
"""
import gradio as gr
from .tokens import COLORS, DARK_COLORS, LIGHT_COLORS, SPACING, RADIUS, TYPOGRAPHY, SHADOWS

class ReplitTheme(gr.themes.Base):
    """Custom Gradio theme inspired by Replit's design system"""
    
    def __init__(
        self,
        *,
        primary_hue: str = "blue",
        secondary_hue: str = "gray", 
        neutral_hue: str = "gray",
        text_size: str = "md",
        spacing_size: str = "md",
        radius_size: str = "md",
        font: tuple = (
            "Inter",
            "system-ui", 
            "-apple-system",
            "BlinkMacSystemFont",
            "Segoe UI",
            "sans-serif"
        ),
        font_mono: tuple = (
            "JetBrains Mono",
            "Consolas", 
            "Monaco",
            "monospace"
        ),
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            text_size=text_size,
            spacing_size=spacing_size,
            radius_size=radius_size,
            font=font,
            font_mono=font_mono,
        )
        
        # Override default theme variables with Replit-inspired values
        self.set(
            # Background colors - using dark theme as default
            background_fill_primary=DARK_COLORS["background"]["primary"],
            background_fill_secondary=DARK_COLORS["background"]["secondary"],
            
            # Text colors
            body_text_color=DARK_COLORS["text"]["primary"],
            body_text_color_subdued=DARK_COLORS["text"]["secondary"],
            
            # Border colors
            border_color_primary=DARK_COLORS["border"]["default"],
            border_color_accent=COLORS["primary"]["500"],
            
            # Button styling
            button_primary_background_fill=COLORS["primary"]["500"],
            button_primary_background_fill_hover=COLORS["primary"]["600"],
            button_primary_text_color="white",
            button_primary_border_color=COLORS["primary"]["500"],
            
            button_secondary_background_fill=DARK_COLORS["background"]["tertiary"],
            button_secondary_background_fill_hover=DARK_COLORS["border"]["emphasis"],
            button_secondary_text_color=DARK_COLORS["text"]["primary"],
            button_secondary_border_color=DARK_COLORS["border"]["default"],
            
            # Input styling
            input_background_fill=DARK_COLORS["background"]["secondary"],
            input_background_fill_focus=DARK_COLORS["background"]["tertiary"],
            input_border_color=DARK_COLORS["border"]["default"],
            input_border_color_focus=COLORS["primary"]["500"],
            input_placeholder_color=DARK_COLORS["text"]["tertiary"],
            
            # Panel/container styling
            panel_background_fill=DARK_COLORS["background"]["secondary"],
            panel_border_color=DARK_COLORS["border"]["subtle"],
            
            # Spacing and layout
            container_radius=RADIUS["lg"],
            button_border_width="1px",
            input_border_width="1px",
            panel_border_width="1px",
            
            # Shadows
            shadow_drop="0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.2)",
            shadow_drop_lg="0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -2px rgba(0, 0, 0, 0.2)",
        )


class ReplitLightTheme(ReplitTheme):
    """Light mode variant of the Replit theme"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Override with light theme colors
        self.set(
            # Background colors
            background_fill_primary=LIGHT_COLORS["background"]["primary"],
            background_fill_secondary=LIGHT_COLORS["background"]["secondary"],
            
            # Text colors
            body_text_color=LIGHT_COLORS["text"]["primary"],
            body_text_color_subdued=LIGHT_COLORS["text"]["secondary"],
            
            # Border colors
            border_color_primary=LIGHT_COLORS["border"]["default"],
            
            # Button styling
            button_secondary_background_fill=LIGHT_COLORS["background"]["tertiary"],
            button_secondary_background_fill_hover=LIGHT_COLORS["border"]["emphasis"],
            button_secondary_text_color=LIGHT_COLORS["text"]["primary"],
            button_secondary_border_color=LIGHT_COLORS["border"]["default"],
            
            # Input styling
            input_background_fill=LIGHT_COLORS["background"]["primary"],
            input_background_fill_focus=LIGHT_COLORS["background"]["secondary"],
            input_border_color=LIGHT_COLORS["border"]["default"],
            input_placeholder_color=LIGHT_COLORS["text"]["tertiary"],
            
            # Panel styling
            panel_background_fill=LIGHT_COLORS["background"]["secondary"],
            panel_border_color=LIGHT_COLORS["border"]["subtle"],
            
            # Lighter shadows for light mode
            shadow_drop="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
            shadow_drop_lg="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        )


def get_replit_theme(dark_mode: bool = True) -> gr.Theme:
    """Get the appropriate Replit theme based on mode"""
    if dark_mode:
        return ReplitTheme()
    else:
        return ReplitLightTheme()