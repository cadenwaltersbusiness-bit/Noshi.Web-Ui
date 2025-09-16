# Replit-inspired theme tokens for Gradio UI
"""
Theme tokens inspired by Replit's design system
Provides centralized design tokens for colors, spacing, typography, and layout
"""

# Color Palette - Replit inspired
COLORS = {
    # Primary brand colors
    "primary": {
        "50": "#f0f9ff",
        "100": "#e0f2fe", 
        "200": "#bae6fd",
        "300": "#7dd3fc",
        "400": "#38bdf8",
        "500": "#0ea5e9",  # Main brand color
        "600": "#0284c7",
        "700": "#0369a1",
        "800": "#075985",
        "900": "#0c4a6e",
    },
    
    # Neutral grays
    "neutral": {
        "50": "#fafafa",
        "100": "#f5f5f5",
        "200": "#e5e5e5",
        "300": "#d4d4d4",
        "400": "#a3a3a3",
        "500": "#737373",
        "600": "#525252",
        "700": "#404040",
        "800": "#262626",
        "900": "#171717",
        "950": "#0a0a0a",
    },
    
    # Success, warning, error
    "success": {
        "50": "#f0fdf4",
        "500": "#22c55e",
        "600": "#16a34a",
        "700": "#15803d",
    },
    
    "warning": {
        "50": "#fffbeb",
        "500": "#f59e0b",
        "600": "#d97706",
        "700": "#b45309",
    },
    
    "error": {
        "50": "#fef2f2",
        "500": "#ef4444",
        "600": "#dc2626",
        "700": "#b91c1c",
    },
}

# Dark mode colors
DARK_COLORS = {
    "background": {
        "primary": "#0a0a0a",      # Main background
        "secondary": "#171717",    # Card/panel background
        "tertiary": "#262626",     # Elevated surfaces
    },
    "text": {
        "primary": "#fafafa",      # Primary text
        "secondary": "#d4d4d4",    # Secondary text
        "tertiary": "#a3a3a3",     # Muted text
    },
    "border": {
        "default": "#404040",      # Default borders
        "subtle": "#262626",       # Subtle borders
        "emphasis": "#525252",     # Emphasized borders
    }
}

# Light mode colors  
LIGHT_COLORS = {
    "background": {
        "primary": "#ffffff",      # Main background
        "secondary": "#fafafa",    # Card/panel background
        "tertiary": "#f5f5f5",     # Elevated surfaces
    },
    "text": {
        "primary": "#171717",      # Primary text
        "secondary": "#404040",    # Secondary text
        "tertiary": "#737373",     # Muted text
    },
    "border": {
        "default": "#e5e5e5",      # Default borders
        "subtle": "#f5f5f5",       # Subtle borders
        "emphasis": "#d4d4d4",     # Emphasized borders
    }
}

# Spacing scale (in pixels)
SPACING = {
    "0": "0px",
    "1": "4px",
    "2": "8px", 
    "3": "12px",
    "4": "16px",
    "5": "20px",
    "6": "24px",
    "8": "32px",
    "10": "40px",
    "12": "48px",
    "16": "64px",
    "20": "80px",
    "24": "96px",
}

# Border radius scale
RADIUS = {
    "none": "0px",
    "sm": "4px",
    "md": "8px",
    "lg": "12px",
    "xl": "16px",
    "2xl": "20px",
    "full": "9999px",
}

# Typography scale
TYPOGRAPHY = {
    "font_family": {
        "sans": "Inter, system-ui, -apple-system, sans-serif",
        "mono": "JetBrains Mono, Consolas, Monaco, monospace",
    },
    "font_size": {
        "xs": "12px",
        "sm": "14px", 
        "base": "16px",
        "lg": "18px",
        "xl": "20px",
        "2xl": "24px",
        "3xl": "30px",
        "4xl": "36px",
    },
    "line_height": {
        "tight": "1.25",
        "normal": "1.5", 
        "relaxed": "1.75",
    },
    "font_weight": {
        "normal": "400",
        "medium": "500",
        "semibold": "600",
        "bold": "700",
    }
}

# Shadow scale for subtle depth
SHADOWS = {
    "sm": "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
    "md": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    "lg": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
    "xl": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
}

# Animation durations
TRANSITIONS = {
    "fast": "150ms",
    "normal": "250ms", 
    "slow": "350ms",
}

# Component-specific tokens
COMPONENTS = {
    "button": {
        "height": "40px",
        "padding_x": "16px",
        "border_radius": RADIUS["md"],
        "font_weight": TYPOGRAPHY["font_weight"]["medium"],
    },
    "input": {
        "height": "40px",
        "padding_x": "12px",
        "border_radius": RADIUS["md"],
        "border_width": "1px",
    },
    "card": {
        "padding": SPACING["6"],
        "border_radius": RADIUS["lg"],
        "border_width": "1px",
    },
    "tab": {
        "height": "44px",
        "padding_x": SPACING["4"],
        "border_radius": RADIUS["md"],
    }
}