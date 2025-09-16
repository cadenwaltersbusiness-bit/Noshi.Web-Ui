"""
Enhanced CSS for Replit-inspired Gradio interface
Provides custom styling that works with the theme tokens
"""

from .tokens import COLORS, DARK_COLORS, LIGHT_COLORS, SPACING, RADIUS, TYPOGRAPHY, SHADOWS, TRANSITIONS

# Main CSS that will be injected into Gradio
REPLIT_CSS = f"""
/* Import fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap');

/* CSS Variables for theming */
:root {{
    /* Colors - Dark mode default */
    --bg-primary: {DARK_COLORS["background"]["primary"]};
    --bg-secondary: {DARK_COLORS["background"]["secondary"]};
    --bg-tertiary: {DARK_COLORS["background"]["tertiary"]};
    --text-primary: {DARK_COLORS["text"]["primary"]};
    --text-secondary: {DARK_COLORS["text"]["secondary"]};
    --text-tertiary: {DARK_COLORS["text"]["tertiary"]};
    --border-default: {DARK_COLORS["border"]["default"]};
    --border-subtle: {DARK_COLORS["border"]["subtle"]};
    --border-emphasis: {DARK_COLORS["border"]["emphasis"]};
    --accent-primary: {COLORS["primary"]["500"]};
    --accent-hover: {COLORS["primary"]["600"]};
    --success: {COLORS["success"]["500"]};
    --warning: {COLORS["warning"]["500"]};
    --error: {COLORS["error"]["500"]};
    
    /* Spacing */
    --space-1: {SPACING["1"]};
    --space-2: {SPACING["2"]};
    --space-3: {SPACING["3"]};
    --space-4: {SPACING["4"]};
    --space-6: {SPACING["6"]};
    --space-8: {SPACING["8"]};
    
    /* Radius */
    --radius-sm: {RADIUS["sm"]};
    --radius-md: {RADIUS["md"]};
    --radius-lg: {RADIUS["lg"]};
    --radius-xl: {RADIUS["xl"]};
    
    /* Shadows */
    --shadow-sm: {SHADOWS["sm"]};
    --shadow-md: {SHADOWS["md"]};
    --shadow-lg: {SHADOWS["lg"]};
    
    /* Transitions */
    --transition-fast: {TRANSITIONS["fast"]};
    --transition-normal: {TRANSITIONS["normal"]};
}}

/* Light mode theme variables */
.light-mode {{
    --bg-primary: {LIGHT_COLORS["background"]["primary"]};
    --bg-secondary: {LIGHT_COLORS["background"]["secondary"]};
    --bg-tertiary: {LIGHT_COLORS["background"]["tertiary"]};
    --text-primary: {LIGHT_COLORS["text"]["primary"]};
    --text-secondary: {LIGHT_COLORS["text"]["secondary"]};
    --text-tertiary: {LIGHT_COLORS["text"]["tertiary"]};
    --border-default: {LIGHT_COLORS["border"]["default"]};
    --border-subtle: {LIGHT_COLORS["border"]["subtle"]};
    --border-emphasis: {LIGHT_COLORS["border"]["emphasis"]};
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}}

/* Global container styling */
.gradio-container {{
    width: 80vw !important;
    max-width: 1400px !important;
    margin: 0 auto !important;
    padding: var(--space-6) !important;
    background: var(--bg-primary) !important;
    min-height: 100vh;
    font-family: {TYPOGRAPHY["font_family"]["sans"]} !important;
}}

/* Header styling */
.header-text {{
    text-align: center;
    margin-bottom: var(--space-8);
    padding: var(--space-6);
    background: var(--bg-secondary);
    border-radius: var(--radius-lg);
    border: 1px solid var(--border-subtle);
    box-shadow: var(--shadow-sm);
}}

.header-text h1 {{
    color: var(--text-primary) !important;
    font-size: {TYPOGRAPHY["font_size"]["3xl"]} !important;
    font-weight: {TYPOGRAPHY["font_weight"]["bold"]} !important;
    margin-bottom: var(--space-2) !important;
    background: linear-gradient(135deg, var(--accent-primary), {COLORS["primary"]["600"]});
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}}

.header-text h3 {{
    color: var(--text-secondary) !important;
    font-size: {TYPOGRAPHY["font_size"]["lg"]} !important;
    font-weight: {TYPOGRAPHY["font_weight"]["normal"]} !important;
    margin: 0 !important;
}}

/* Tab styling */
.tab-nav {{
    background: var(--bg-secondary) !important;
    border-radius: var(--radius-lg) !important;
    padding: var(--space-2) !important;
    margin-bottom: var(--space-6) !important;
    border: 1px solid var(--border-subtle) !important;
    box-shadow: var(--shadow-sm) !important;
}}

.tab-nav .tab-item {{
    background: transparent !important;
    border: none !important;
    border-radius: var(--radius-md) !important;
    padding: var(--space-3) var(--space-4) !important;
    margin: 0 var(--space-1) !important;
    color: var(--text-secondary) !important;
    font-weight: {TYPOGRAPHY["font_weight"]["medium"]} !important;
    transition: all var(--transition-fast) ease !important;
    cursor: pointer !important;
}}

.tab-nav .tab-item:hover {{
    background: var(--bg-tertiary) !important;
    color: var(--text-primary) !important;
}}

.tab-nav .tab-item.selected {{
    background: var(--accent-primary) !important;
    color: white !important;
    box-shadow: var(--shadow-sm) !important;
}}

/* Panel/content area styling */
.tab-content {{
    background: var(--bg-secondary) !important;
    border-radius: var(--radius-lg) !important;
    border: 1px solid var(--border-subtle) !important;
    padding: var(--space-8) !important;
    box-shadow: var(--shadow-md) !important;
}}

/* Form section styling */
.form-section {{
    background: var(--bg-tertiary) !important;
    border-radius: var(--radius-md) !important;
    padding: var(--space-6) !important;
    margin-bottom: var(--space-6) !important;
    border: 1px solid var(--border-subtle) !important;
}}

.form-section h3 {{
    color: var(--text-primary) !important;
    font-size: {TYPOGRAPHY["font_size"]["lg"]} !important;
    font-weight: {TYPOGRAPHY["font_weight"]["semibold"]} !important;
    margin-bottom: var(--space-4) !important;
    padding-bottom: var(--space-2) !important;
    border-bottom: 1px solid var(--border-subtle) !important;
}}

/* Button styling */
.btn-primary {{
    background: var(--accent-primary) !important;
    color: white !important;
    border: 1px solid var(--accent-primary) !important;
    border-radius: var(--radius-md) !important;
    padding: var(--space-3) var(--space-6) !important;
    font-weight: {TYPOGRAPHY["font_weight"]["medium"]} !important;
    transition: all var(--transition-fast) ease !important;
    box-shadow: var(--shadow-sm) !important;
    cursor: pointer !important;
}}

.btn-primary:hover {{
    background: var(--accent-hover) !important;
    border-color: var(--accent-hover) !important;
    box-shadow: var(--shadow-md) !important;
    transform: translateY(-1px) !important;
}}

.btn-secondary {{
    background: var(--bg-tertiary) !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--border-default) !important;
    border-radius: var(--radius-md) !important;
    padding: var(--space-3) var(--space-6) !important;
    font-weight: {TYPOGRAPHY["font_weight"]["medium"]} !important;
    transition: all var(--transition-fast) ease !important;
    cursor: pointer !important;
}}

.btn-secondary:hover {{
    background: var(--border-emphasis) !important;
    border-color: var(--border-emphasis) !important;
    transform: translateY(-1px) !important;
}}

/* Input styling */
.input-field {{
    background: var(--bg-primary) !important;
    border: 1px solid var(--border-default) !important;
    border-radius: var(--radius-md) !important;
    padding: var(--space-3) var(--space-4) !important;
    color: var(--text-primary) !important;
    transition: all var(--transition-fast) ease !important;
    font-size: {TYPOGRAPHY["font_size"]["sm"]} !important;
}}

.input-field:focus {{
    border-color: var(--accent-primary) !important;
    box-shadow: 0 0 0 3px rgba(14, 165, 233, 0.1) !important;
    outline: none !important;
}}

.input-field::placeholder {{
    color: var(--text-tertiary) !important;
}}

/* Dropdown styling */
.dropdown {{
    background: var(--bg-primary) !important;
    border: 1px solid var(--border-default) !important;
    border-radius: var(--radius-md) !important;
    color: var(--text-primary) !important;
}}

/* Chatbot/log styling */
.chatbot {{
    background: var(--bg-primary) !important;
    border: 1px solid var(--border-default) !important;
    border-radius: var(--radius-md) !important;
    font-family: {TYPOGRAPHY["font_family"]["mono"]} !important;
    font-size: {TYPOGRAPHY["font_size"]["sm"]} !important;
}}

/* Progress indicators */
.progress-bar {{
    background: var(--bg-tertiary) !important;
    border-radius: var(--radius-sm) !important;
    overflow: hidden !important;
}}

.progress-fill {{
    background: linear-gradient(90deg, var(--accent-primary), {COLORS["primary"]["400"]}) !important;
    transition: width var(--transition-normal) ease !important;
}}

/* Status indicators */
.status-success {{
    color: var(--success) !important;
}}

.status-warning {{
    color: var(--warning) !important;
}}

.status-error {{
    color: var(--error) !important;
}}

/* File upload styling */
.file-upload {{
    background: var(--bg-tertiary) !important;
    border: 2px dashed var(--border-default) !important;
    border-radius: var(--radius-md) !important;
    padding: var(--space-8) !important;
    text-align: center !important;
    transition: all var(--transition-fast) ease !important;
}}

.file-upload:hover {{
    border-color: var(--accent-primary) !important;
    background: var(--bg-secondary) !important;
}}

/* Checkbox and radio styling */
.checkbox, .radio {{
    accent-color: var(--accent-primary) !important;
}}

/* Slider styling */
.slider {{
    accent-color: var(--accent-primary) !important;
}}

/* Responsive design */
@media (max-width: 768px) {{
    .gradio-container {{
        width: 95vw !important;
        padding: var(--space-4) !important;
    }}
    
    .header-text h1 {{
        font-size: {TYPOGRAPHY["font_size"]["2xl"]} !important;
    }}
    
    .tab-nav .tab-item {{
        padding: var(--space-2) var(--space-3) !important;
        font-size: {TYPOGRAPHY["font_size"]["sm"]} !important;
    }}
}}

/* Theme toggle button */
.theme-toggle {{
    position: fixed !important;
    top: var(--space-4) !important;
    right: var(--space-4) !important;
    z-index: 1000 !important;
    background: var(--bg-secondary) !important;
    border: 1px solid var(--border-default) !important;
    border-radius: var(--radius-md) !important;
    padding: var(--space-2) !important;
    cursor: pointer !important;
    transition: all var(--transition-fast) ease !important;
    box-shadow: var(--shadow-md) !important;
}}

.theme-toggle:hover {{
    background: var(--bg-tertiary) !important;
    transform: translateY(-1px) !important;
    box-shadow: var(--shadow-lg) !important;
}}

/* Animation for smooth transitions */
* {{
    transition: background-color var(--transition-fast) ease,
                border-color var(--transition-fast) ease,
                color var(--transition-fast) ease !important;
}}
"""

def get_replit_css(dark_mode: bool = True) -> str:
    """Get the CSS with appropriate theme class"""
    css_class = "" if dark_mode else ".light-mode"
    return REPLIT_CSS