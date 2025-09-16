"""
Enhanced Interface with improved components while maintaining backward compatibility
"""
import gradio as gr

from src.webui.webui_manager import WebuiManager
# Original components
from src.webui.components.agent_settings_tab import create_agent_settings_tab
from src.webui.components.browser_settings_tab import create_browser_settings_tab
from src.webui.components.browser_use_agent_tab import create_browser_use_agent_tab
from src.webui.components.deep_research_agent_tab import create_deep_research_agent_tab
from src.webui.components.load_save_config_tab import create_load_save_config_tab

# Enhanced components
from src.webui.components.enhanced_agent_settings_tab import create_enhanced_agent_settings_tab
from src.webui.components.enhanced_browser_settings_tab import create_enhanced_browser_settings_tab
from src.webui.components.enhanced_browser_use_agent_tab import create_enhanced_browser_use_agent_tab

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


def create_enhanced_ui(theme_name="Replit", use_enhanced_components=True):
    """
    Create enhanced UI with improved components and theming
    
    Args:
        theme_name: Theme to use ("Replit", "ReplitLight", or legacy theme names)
        use_enhanced_components: Whether to use enhanced component versions
    """
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
            title="Browser Use WebUI - Enhanced", 
            theme=theme_map[theme_name], 
            css=css, 
            js=js_func,
    ) as demo:
        # Enhanced header with theme toggle
        with gr.Row():
            with gr.Column(scale=12):
                gr.Markdown(
                    """
                    # 🌐 Browser Use WebUI - Enhanced
                    ### Next-generation browser automation with AI assistance
                    """,
                    elem_classes=["header-text"],
                )
            with gr.Column(scale=1, min_width=60):
                theme_toggle = create_theme_toggle_button()
                setup_theme_toggle(theme_toggle)

        # Enhanced tabs with better organization
        with gr.Tabs(elem_classes=["tab-nav"]) as tabs:
            # Agent Settings Tab
            with gr.TabItem("⚙️ Agent Settings", elem_classes=["tab-content"]):
                if use_enhanced_components:
                    create_enhanced_agent_settings_tab(ui_manager)
                else:
                    create_agent_settings_tab(ui_manager)

            # Browser Settings Tab
            with gr.TabItem("🌐 Browser Settings", elem_classes=["tab-content"]):
                if use_enhanced_components:
                    create_enhanced_browser_settings_tab(ui_manager)
                else:
                    create_browser_settings_tab(ui_manager)

            # Run Agent Tab
            with gr.TabItem("🤖 Run Agent", elem_classes=["tab-content"]):
                if use_enhanced_components:
                    create_enhanced_browser_use_agent_tab(ui_manager)
                else:
                    create_browser_use_agent_tab(ui_manager)

            # History & Logs Tab (New Enhanced Tab)
            with gr.TabItem("📊 History & Logs", elem_classes=["tab-content"]):
                create_history_logs_tab(ui_manager)

            # Inspector & DevTools Tab (New Enhanced Tab)
            with gr.TabItem("🔍 Inspector", elem_classes=["tab-content"]):
                create_inspector_tab(ui_manager)

            # Agent Marketplace Tab
            with gr.TabItem("🎁 Agent Marketplace", elem_classes=["tab-content"]):
                gr.Markdown(
                    """
                    ### Agents built on Browser-Use
                    Discover and use specialized agent configurations
                    """,
                    elem_classes=["tab-header-text"],
                )
                with gr.Tabs():
                    with gr.TabItem("Deep Research"):
                        create_deep_research_agent_tab(ui_manager)
                    
                    with gr.TabItem("E-commerce Assistant"):
                        create_ecommerce_agent_tab(ui_manager)
                    
                    with gr.TabItem("Data Extraction"):
                        create_data_extraction_agent_tab(ui_manager)

            # Load & Save Config Tab
            with gr.TabItem("📁 Config Manager", elem_classes=["tab-content"]):
                create_enhanced_config_tab(ui_manager)

    return demo


def create_history_logs_tab(webui_manager: WebuiManager):
    """Create enhanced history and logs viewing interface"""
    with gr.Column(elem_classes=["tab-content"]):
        gr.Markdown("### 📊 Session History & Logs", elem_classes=["section-header"])
        
        # Filter controls
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column(scale=2):
                start_date = gr.Textbox(
                    label="Start Date (YYYY-MM-DD)",
                    placeholder="2023-01-01",
                    elem_classes=["input-field"]
                )
                end_date = gr.Textbox(
                    label="End Date (YYYY-MM-DD)",
                    placeholder="2023-12-31",
                    elem_classes=["input-field"]
                )
            with gr.Column(scale=1):
                status_filter = gr.Dropdown(
                    choices=["All", "Completed", "Failed", "In Progress", "Cancelled"],
                    value="All",
                    label="Status Filter",
                    elem_classes=["dropdown"]
                )
            with gr.Column(scale=1):
                agent_filter = gr.Dropdown(
                    choices=["All Agents", "Browser Agent", "Research Agent", "E-commerce Agent"],
                    value="All Agents",
                    label="Agent Type",
                    elem_classes=["dropdown"]
                )
            with gr.Column(scale=0):
                refresh_button = gr.Button("🔄 Refresh", elem_classes=["btn-secondary"])
        
        # Session list
        with gr.Row(elem_classes=["form-section"]):
            sessions_table = gr.Dataframe(
                headers=["Date", "Duration", "Task", "Status", "Steps", "Actions", "Agent"],
                datatype=["str", "str", "str", "str", "number", "number", "str"],
                interactive=False,
                max_height=400,
                elem_classes=["sessions-table"]
            )
        
        # Session details
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column(scale=1):
                gr.Markdown("### Session Details", elem_classes=["section-header"])
                session_details = gr.JSON(
                    label="Selected Session",
                    elem_classes=["info-display"]
                )
                
                # Export controls
                with gr.Row():
                    export_json_button = gr.Button("📄 Export JSON", elem_classes=["btn-secondary"])
                    export_csv_button = gr.Button("📊 Export CSV", elem_classes=["btn-secondary"])
                    export_report_button = gr.Button("📋 Generate Report", elem_classes=["btn-primary"])
            
            with gr.Column(scale=1):
                gr.Markdown("### Live Logs", elem_classes=["section-header"])
                live_logs = gr.Textbox(
                    label="Real-time Logs",
                    lines=20,
                    max_lines=50,
                    interactive=False,
                    elem_classes=["logs-display"]
                )
                
                # Log controls
                with gr.Row():
                    auto_scroll_logs = gr.Checkbox(
                        label="Auto-scroll",
                        value=True,
                        elem_classes=["checkbox"]
                    )
                    log_level = gr.Dropdown(
                        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
                        value="INFO",
                        label="Log Level",
                        elem_classes=["dropdown"]
                    )


def create_inspector_tab(webui_manager: WebuiManager):
    """Create enhanced inspector and devtools interface"""
    with gr.Column(elem_classes=["tab-content"]):
        gr.Markdown("### 🔍 Browser Inspector & DevTools", elem_classes=["section-header"])
        
        # Inspector controls
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column():
                inspect_button = gr.Button("🔍 Inspect Current Page", variant="primary", elem_classes=["btn-primary"])
                refresh_inspector_button = gr.Button("🔄 Refresh", variant="secondary", elem_classes=["btn-secondary"])
                
                # Inspector options
                with gr.Row():
                    show_dom_tree = gr.Checkbox(label="DOM Tree", value=True, elem_classes=["checkbox"])
                    show_network = gr.Checkbox(label="Network", value=True, elem_classes=["checkbox"])
                    show_console = gr.Checkbox(label="Console", value=True, elem_classes=["checkbox"])
                    show_screenshots = gr.Checkbox(label="Screenshots", value=True, elem_classes=["checkbox"])
        
        # Inspector panels
        with gr.Tabs():
            # DOM Tree Tab
            with gr.TabItem("🌳 DOM Tree"):
                with gr.Row():
                    with gr.Column(scale=1):
                        dom_search = gr.Textbox(
                            label="Search DOM",
                            placeholder="Search by tag, class, id, or text",
                            elem_classes=["input-field"]
                        )
                        dom_tree = gr.Code(
                            label="DOM Structure",
                            language="html",
                            lines=25,
                            elem_classes=["code-editor"]
                        )
                    
                    with gr.Column(scale=1):
                        element_details = gr.JSON(
                            label="Selected Element",
                            elem_classes=["info-display"]
                        )
                        
                        # Element actions
                        with gr.Column():
                            gr.Markdown("### Element Actions")
                            click_element_button = gr.Button("👆 Click", elem_classes=["btn-secondary"])
                            type_text_field = gr.Textbox(label="Text to type", elem_classes=["input-field"])
                            type_element_button = gr.Button("⌨️ Type", elem_classes=["btn-secondary"])
                            scroll_element_button = gr.Button("📜 Scroll to", elem_classes=["btn-secondary"])
            
            # Network Tab
            with gr.TabItem("🌐 Network"):
                with gr.Row():
                    network_filter = gr.Dropdown(
                        choices=["All", "XHR", "Fetch", "JS", "CSS", "Images", "Documents"],
                        value="All",
                        label="Filter",
                        elem_classes=["dropdown"]
                    )
                    clear_network_button = gr.Button("🗑️ Clear", elem_classes=["btn-secondary"])
                
                network_requests = gr.Dataframe(
                    headers=["Method", "URL", "Status", "Type", "Size", "Time"],
                    datatype=["str", "str", "number", "str", "str", "str"],
                    max_height=400,
                    elem_classes=["network-table"]
                )
            
            # Console Tab
            with gr.TabItem("💻 Console"):
                console_output = gr.Textbox(
                    label="Console Output",
                    lines=20,
                    interactive=False,
                    elem_classes=["console-output"]
                )
                
                with gr.Row():
                    console_input = gr.Textbox(
                        label="Execute JavaScript",
                        placeholder="console.log('Hello World');",
                        elem_classes=["input-field"]
                    )
                    execute_js_button = gr.Button("▶️ Execute", elem_classes=["btn-primary"])
            
            # Screenshots Tab
            with gr.TabItem("📸 Screenshots"):
                with gr.Row():
                    take_screenshot_button = gr.Button("📸 Take Screenshot", elem_classes=["btn-primary"])
                    screenshot_full_page = gr.Checkbox(label="Full page", value=True, elem_classes=["checkbox"])
                
                screenshots_gallery = gr.Gallery(
                    label="Session Screenshots",
                    show_label=True,
                    columns=3,
                    rows=3,
                    object_fit="contain",
                    height="auto",
                    elem_classes=["screenshots-gallery"]
                )


def create_ecommerce_agent_tab(webui_manager: WebuiManager):
    """Create specialized e-commerce agent interface"""
    with gr.Column():
        gr.Markdown("### 🛒 E-commerce Assistant Agent")
        gr.Markdown("Specialized for online shopping, price comparison, and product research")
        
        # Implementation placeholder
        gr.Markdown("*Coming soon - Specialized e-commerce automation capabilities*")


def create_data_extraction_agent_tab(webui_manager: WebuiManager):
    """Create specialized data extraction agent interface"""
    with gr.Column():
        gr.Markdown("### 📊 Data Extraction Agent")
        gr.Markdown("Specialized for web scraping, data collection, and structured data extraction")
        
        # Implementation placeholder
        gr.Markdown("*Coming soon - Advanced data extraction capabilities*")


def create_enhanced_config_tab(webui_manager: WebuiManager):
    """Create enhanced configuration management interface"""
    with gr.Column(elem_classes=["tab-content"]):
        gr.Markdown("### 📁 Configuration Manager", elem_classes=["section-header"])
        
        # Config operations
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column(scale=1):
                gr.Markdown("### Load Configuration")
                config_file = gr.File(
                    label="Configuration File",
                    file_types=[".json", ".yaml", ".yml"],
                    elem_classes=["file-input"]
                )
                load_config_button = gr.Button("📁 Load Config", elem_classes=["btn-primary"])
            
            with gr.Column(scale=1):
                gr.Markdown("### Save Configuration")
                config_name = gr.Textbox(
                    label="Configuration Name",
                    placeholder="My Configuration",
                    elem_classes=["input-field"]
                )
                save_config_button = gr.Button("💾 Save Config", elem_classes=["btn-primary"])
        
        # Config editor
        with gr.Row(elem_classes=["form-section"]):
            config_editor = gr.Code(
                label="Configuration Editor",
                language="json",
                lines=20,
                elem_classes=["code-editor"]
            )
        
        # Saved configs
        with gr.Row(elem_classes=["form-section"]):
            saved_configs = gr.Dataframe(
                headers=["Name", "Date", "Description", "Size"],
                datatype=["str", "str", "str", "str"],
                max_height=200,
                elem_classes=["configs-table"]
            )


# Export the original create_ui function for backward compatibility
def create_ui(theme_name="Replit"):
    """
    Original create_ui function for backward compatibility
    """
    return create_enhanced_ui(theme_name, use_enhanced_components=False)