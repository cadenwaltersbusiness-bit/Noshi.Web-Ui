# Theming Guide for Browser Use WebUI

This document explains the new theming system implemented for the Browser Use WebUI, which provides a Replit-inspired design with enhanced visual components and functionality.

## Overview

The enhanced UI system includes:
- **Replit-inspired theme** with rounded corners, subtle shadows, and modern styling
- **Dark/Light mode toggle** with system preference detection
- **Centralized design tokens** for consistent styling
- **Enhanced components** with better organization and functionality
- **Backward compatibility** with original interface

## Theme Architecture

### Design Tokens (`src/webui/theme/tokens.py`)

Centralized design system with:
- **Color Palette**: Primary brand colors, neutrals, success/warning/error states
- **Dark/Light Mode**: Separate color schemes for each mode
- **Spacing Scale**: Consistent spacing from 4px to 96px
- **Border Radius**: From none to full rounded
- **Typography**: Font families, sizes, weights, line heights
- **Shadows**: Subtle depth effects
- **Component Tokens**: Specific styling for buttons, inputs, cards, etc.

### Theme Implementation (`src/webui/theme/theme.py`)

Custom Gradio themes that extend the base theme system:
- `ReplitTheme`: Dark mode theme with custom styling
- `ReplitLightTheme`: Light mode variant
- `get_replit_theme()`: Helper function to get appropriate theme

### CSS System (`src/webui/theme/styles.py`)

Enhanced CSS with:
- **CSS Variables**: Theme-aware custom properties
- **Component Styling**: Enhanced styling for all UI components
- **Responsive Design**: Mobile-friendly layouts
- **Animation**: Smooth transitions and hover effects

### Theme Provider (`src/webui/theme/provider.py`)

Theme state management:
- `ThemeProvider`: Manages theme state and switching
- `create_theme_toggle_button()`: Creates the theme toggle UI
- `setup_theme_toggle()`: Wires up theme switching functionality

## Using the Theme System

### Basic Usage

```python
from src.webui.theme import get_replit_theme, get_replit_css

# Get the theme
theme = get_replit_theme(dark_mode=True)

# Get the CSS
css = get_replit_css(dark_mode=True)

# Use with Gradio
with gr.Blocks(theme=theme, css=css) as demo:
    # Your UI components
    pass
```

### Adding Theme Toggle

```python
from src.webui.theme import create_theme_toggle_button, setup_theme_toggle

# Create the toggle button
theme_toggle = create_theme_toggle_button()

# Set up the functionality
setup_theme_toggle(theme_toggle)
```

### Using Design Tokens

```python
from src.webui.theme.tokens import COLORS, SPACING, RADIUS

# Use in your custom styling
custom_css = f"""
.my-component {{
    background: {COLORS["primary"]["500"]};
    padding: {SPACING["4"]};
    border-radius: {RADIUS["md"]};
}}
"""
```

## CSS Classes and Styling

### Form Sections
- `.form-section`: Styled container for grouped UI elements
- `.section-header`: Styled headers for sections

### Buttons
- `.btn-primary`: Primary action buttons
- `.btn-secondary`: Secondary action buttons
- `.btn-emergency`: Emergency/danger buttons

### Inputs
- `.input-field`: Text inputs and form fields
- `.dropdown`: Dropdown selections
- `.checkbox`: Checkbox controls
- `.slider`: Range sliders

### Data Display
- `.info-display`: JSON and structured data displays
- `.status-display`: Status indicators
- `.logs-display`: Log output areas
- `.progress-bar`: Progress indicators

### Layout
- `.tab-nav`: Tab navigation styling
- `.tab-content`: Tab content areas
- `.chatbot`: Chat interfaces
- `.browser-view`: Browser preview areas

## Color System

### Primary Colors
- Brand blue: `#0ea5e9` (primary-500)
- Hover: `#0284c7` (primary-600)
- Light: `#38bdf8` (primary-400)

### Dark Mode Colors
- Background: `#0a0a0a` (primary), `#171717` (secondary), `#262626` (tertiary)
- Text: `#fafafa` (primary), `#d4d4d4` (secondary), `#a3a3a3` (tertiary)
- Borders: `#404040` (default), `#262626` (subtle), `#525252` (emphasis)

### Light Mode Colors
- Background: `#ffffff` (primary), `#fafafa` (secondary), `#f5f5f5` (tertiary)
- Text: `#171717` (primary), `#404040` (secondary), `#737373` (tertiary)
- Borders: `#e5e5e5` (default), `#f5f5f5` (subtle), `#d4d4d4` (emphasis)

## Customization

### Adding New Colors

1. Add to `tokens.py`:
```python
COLORS["custom"] = {
    "500": "#your-color",
    "600": "#darker-variant",
    # etc.
}
```

2. Use in CSS:
```css
:root {
    --custom-color: #your-color;
}
```

### Creating Custom Components

1. Use design tokens for consistency:
```python
def create_custom_component():
    return gr.Button(
        "My Button",
        elem_classes=["btn-primary", "my-custom-class"]
    )
```

2. Add custom CSS:
```css
.my-custom-class {
    border: 2px solid var(--accent-primary);
    box-shadow: var(--shadow-lg);
}
```

### Extending the Theme

To create a new theme variant:

1. Extend the base theme:
```python
class MyCustomTheme(ReplitTheme):
    def __init__(self):
        super().__init__()
        self.set(
            # Your custom overrides
            button_primary_background_fill="#custom-color"
        )
```

2. Register in theme map:
```python
theme_map["MyTheme"] = MyCustomTheme()
```

## Best Practices

### Consistency
- Always use design tokens instead of hardcoded values
- Follow the established spacing scale
- Use the color system for consistent brand experience

### Accessibility
- Maintain sufficient color contrast ratios
- Use semantic color names (success, warning, error)
- Ensure focus indicators are visible

### Performance
- Use CSS variables for theme switching
- Minimize CSS specificity conflicts
- Leverage browser caching for static assets

### Maintainability
- Keep styles modular and component-based
- Use meaningful class names
- Document custom CSS additions

## Migration from Old Theme

### Automatic Migration
Most components will automatically pick up the new styling when using the Replit theme.

### Manual Updates Required
- Update any hardcoded colors to use CSS variables
- Replace inline styles with CSS classes
- Update component `elem_classes` for enhanced styling

### Testing
- Test both dark and light modes
- Verify responsive behavior
- Check theme toggle functionality
- Validate accessibility features

## Troubleshooting

### Theme Not Loading
- Ensure CSS is properly injected into Gradio
- Check for CSS syntax errors
- Verify theme is registered in theme_map

### Colors Not Updating
- Check CSS variable names match tokens
- Verify theme class is applied to body
- Clear browser cache

### Component Styling Issues
- Use browser dev tools to inspect CSS
- Check CSS specificity conflicts
- Verify elem_classes are applied correctly

## Future Enhancements

### Planned Features
- More theme variants (high contrast, larger text)
- Component animation system
- Advanced color palette tools
- Theme preview system

### Contributing
When adding new components or styles:
1. Use existing design tokens
2. Follow the established patterns
3. Test in both themes
4. Update documentation
5. Add to component library