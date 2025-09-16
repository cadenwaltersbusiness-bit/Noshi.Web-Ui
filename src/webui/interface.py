import gradio as gr

from src.webui.webui_manager import WebuiManager
from src.webui.components.agent_settings_tab import create_agent_settings_tab
from src.webui.components.browser_settings_tab import create_browser_settings_tab
from src.webui.components.browser_use_agent_tab import create_browser_use_agent_tab
from src.webui.components.deep_research_agent_tab import create_deep_research_agent_tab
from src.webui.components.load_save_config_tab import create_load_save_config_tab
from src.webui.theme import get_replit_theme, get_replit_css, create_theme_toggle_button, setup_theme_toggle

# Legacy theme map for backward compatibility
theme_map = {
    "Default": gr.themes.Default(),
    "Soft": gr.themes.Soft(),
    "Monochrome": gr.themes.Monochrome(),
    "Glass": gr.themes.Glass(),
    "Origin": gr.themes.Origin(),
    "Citrus": gr.themes.Citrus(),
    "Ocean": gr.themes.Ocean(),
    "Base": gr.themes.Base(),
    "Replit": get_replit_theme(dark_mode=True),
    "ReplitLight": get_replit_theme(dark_mode=False)
}


def create_ui(theme_name="Replit"):
    # Use Replit theme by default, with enhanced CSS
    if theme_name in ["Replit", "ReplitLight"]:
        css = get_replit_css(dark_mode=(theme_name == "Replit"))
    else:
        # Legacy CSS for other themes
        css = """
        .gradio-container {
            width: 70vw !important; 
            max-width: 70% !important; 
            margin-left: auto !important;
            margin-right: auto !important;
            padding-top: 10px !important;
        }
        .header-text {
            text-align: center;
            margin-bottom: 20px;
        }
        .tab-header-text {
            text-align: center;
        }
        .theme-section {
            margin-bottom: 10px;
            padding: 15px;
            border-radius: 10px;
        }
        """

    # Enhanced dark mode JavaScript with theme detection
    js_func = """
    function refresh() {
        const url = new URL(window.location);
        const savedTheme = localStorage.getItem('theme');
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        const useDark = savedTheme ? savedTheme === 'dark' : prefersDark;

        if (url.searchParams.get('__theme') !== 'dark' && useDark) {
            url.searchParams.set('__theme', 'dark');
            window.location.href = url.href;
        }
        
        // Apply theme class based on preference
        if (!useDark) {
            document.body.classList.add('light-mode');
        }
    }
    """

    ui_manager = WebuiManager()

    with gr.Blocks(
            title="Browser Use WebUI", theme=theme_map[theme_name], css=css, js=js_func,
    ) as demo:
        # Theme toggle button in the top-right corner
        with gr.Row():
            with gr.Column(scale=12):
                gr.Markdown(
                    """
                    # 🌐 Browser Use WebUI
                    ### Control your browser with AI assistance
                    """,
                    elem_classes=["header-text"],
                )
            with gr.Column(scale=1, min_width=60):
                theme_toggle = create_theme_toggle_button()
                setup_theme_toggle(theme_toggle)

        with gr.Tabs(elem_classes=["tab-nav"]) as tabs:
            with gr.TabItem("⚙️ Agent Settings", elem_classes=["tab-content"]):
                create_agent_settings_tab(ui_manager)

            with gr.TabItem("🌐 Browser Settings", elem_classes=["tab-content"]):
                create_browser_settings_tab(ui_manager)

            with gr.TabItem("🤖 Run Agent", elem_classes=["tab-content"]):
                create_browser_use_agent_tab(ui_manager)

            with gr.TabItem("🎁 Agent Marketplace", elem_classes=["tab-content"]):
                gr.Markdown(
                    """
                    ### Agents built on Browser-Use
                    """,
                    elem_classes=["tab-header-text"],
                )
                with gr.Tabs():
                    with gr.TabItem("Deep Research"):
                        create_deep_research_agent_tab(ui_manager)

            with gr.TabItem("📁 Load & Save Config", elem_classes=["tab-content"]):
                create_load_save_config_tab(ui_manager)

    return demo
