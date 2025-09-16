"""
Enhanced Browser Settings Tab with improved organization and controls
"""
import gradio as gr
import os
from typing import Dict, Any
from src.webui.webui_manager import WebuiManager
from src.utils import config


def create_enhanced_browser_settings_tab(webui_manager: WebuiManager):
    """
    Enhanced browser settings tab with better organization and user experience
    """
    tab_components = {}
    
    with gr.Column(elem_classes=["tab-content"]):
        # Browser Configuration Section
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column():
                gr.Markdown("### 🌐 Browser Configuration", elem_classes=["section-header"])
                
                # Browser type selection
                with gr.Row():
                    browser_type = gr.Radio(
                        choices=["chromium", "chrome", "firefox", "webkit"],
                        value="chromium",
                        label="Browser Type",
                        elem_classes=["radio"]
                    )
                    browser_channel = gr.Dropdown(
                        choices=["stable", "beta", "dev", "canary"],
                        value="stable",
                        label="Browser Channel",
                        elem_classes=["dropdown"]
                    )
                
                # Browser path configuration
                with gr.Row():
                    browser_binary_path = gr.Textbox(
                        label="Custom Browser Binary Path",
                        placeholder="Leave empty to use system default",
                        lines=1,
                        elem_classes=["input-field"]
                    )
                    browse_binary_button = gr.Button(
                        "📁 Browse",
                        variant="secondary",
                        scale=0,
                        elem_classes=["btn-secondary"]
                    )
                
                # User data directory
                with gr.Row():
                    browser_user_data_dir = gr.Textbox(
                        label="User Data Directory",
                        placeholder="Leave empty for default profile",
                        lines=1,
                        elem_classes=["input-field"]
                    )
                    browse_userdata_button = gr.Button(
                        "📁 Browse",
                        variant="secondary",
                        scale=0,
                        elem_classes=["btn-secondary"]
                    )
        
        # Browser Behavior Section
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column(scale=1):
                gr.Markdown("### ⚙️ Browser Behavior", elem_classes=["section-header"])
                
                # Mode settings
                with gr.Column():
                    use_own_browser = gr.Checkbox(
                        label="Use existing browser instance",
                        value=False,
                        info="Connect to an already running browser",
                        elem_classes=["checkbox"]
                    )
                    
                    keep_browser_open = gr.Checkbox(
                        label="Keep browser open between tasks",
                        value=True,
                        info="Maintain browser state across sessions",
                        elem_classes=["checkbox"]
                    )
                    
                    headless_mode = gr.Checkbox(
                        label="Headless mode",
                        value=False,
                        info="Run browser without GUI (faster but no visual feedback)",
                        elem_classes=["checkbox"]
                    )
                    
                    disable_security = gr.Checkbox(
                        label="Disable security features",
                        value=False,
                        info="⚠️ Only enable for testing - reduces security",
                        elem_classes=["checkbox"]
                    )
            
            with gr.Column(scale=1):
                gr.Markdown("### 🔧 Advanced Options", elem_classes=["section-header"])
                
                # Advanced settings
                with gr.Column():
                    disable_images = gr.Checkbox(
                        label="Disable image loading",
                        value=False,
                        info="Faster browsing but no images",
                        elem_classes=["checkbox"]
                    )
                    
                    disable_javascript = gr.Checkbox(
                        label="Disable JavaScript",
                        value=False,
                        info="⚠️ May break many websites",
                        elem_classes=["checkbox"]
                    )
                    
                    block_ads = gr.Checkbox(
                        label="Block advertisements",
                        value=True,
                        info="Improves performance and reduces distractions",
                        elem_classes=["checkbox"]
                    )
                    
                    incognito_mode = gr.Checkbox(
                        label="Incognito/Private mode",
                        value=False,
                        info="Don't save browsing history or cookies",
                        elem_classes=["checkbox"]
                    )
        
        # Viewport & Display Section
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column():
                gr.Markdown("### 📱 Viewport & Display", elem_classes=["section-header"])
                
                # Viewport presets
                with gr.Row():
                    viewport_preset = gr.Dropdown(
                        choices=[
                            "Custom",
                            "Desktop HD (1920×1080)", 
                            "Desktop FHD (1280×720)",
                            "Laptop (1366×768)",
                            "Tablet Portrait (768×1024)",
                            "Tablet Landscape (1024×768)",
                            "Mobile Portrait (375×667)",
                            "Mobile Landscape (667×375)"
                        ],
                        value="Desktop FHD (1280×720)",
                        label="Viewport Preset",
                        elem_classes=["dropdown"]
                    )
                
                # Custom dimensions
                with gr.Row():
                    window_width = gr.Number(
                        label="Window Width",
                        value=1280,
                        minimum=320,
                        maximum=3840,
                        elem_classes=["input-field"]
                    )
                    window_height = gr.Number(
                        label="Window Height", 
                        value=1100,
                        minimum=240,
                        maximum=2160,
                        elem_classes=["input-field"]
                    )
                
                # Display options
                with gr.Row():
                    device_scale_factor = gr.Slider(
                        minimum=0.5,
                        maximum=3.0,
                        value=1.0,
                        step=0.1,
                        label="Device Scale Factor",
                        elem_classes=["slider"]
                    )
                    
                    user_agent_preset = gr.Dropdown(
                        choices=[
                            "Default",
                            "Chrome Desktop",
                            "Firefox Desktop", 
                            "Safari Desktop",
                            "Chrome Mobile",
                            "Safari Mobile",
                            "Custom"
                        ],
                        value="Default",
                        label="User Agent",
                        elem_classes=["dropdown"]
                    )
                
                # Custom user agent
                custom_user_agent = gr.Textbox(
                    label="Custom User Agent",
                    placeholder="Enter custom user agent string",
                    visible=False,
                    lines=2,
                    elem_classes=["input-field"]
                )
        
        # Connection & Debugging Section
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column(scale=1):
                gr.Markdown("### 🔌 Remote Debugging", elem_classes=["section-header"])
                
                # Remote debugging configuration
                with gr.Column():
                    enable_cdp = gr.Checkbox(
                        label="Enable Chrome DevTools Protocol",
                        value=True,
                        info="Required for advanced browser automation",
                        elem_classes=["checkbox"]
                    )
                    
                    cdp_port = gr.Number(
                        label="CDP Port",
                        value=9222,
                        minimum=1024,
                        maximum=65535,
                        elem_classes=["input-field"]
                    )
                    
                    cdp_url = gr.Textbox(
                        label="CDP URL",
                        placeholder="e.g., http://localhost:9222",
                        elem_classes=["input-field"]
                    )
                    
                    wss_url = gr.Textbox(
                        label="WebSocket URL",
                        placeholder="e.g., ws://localhost:9222/devtools/browser",
                        elem_classes=["input-field"]
                    )
            
            with gr.Column(scale=1):
                gr.Markdown("### 🌐 Network & Proxy", elem_classes=["section-header"])
                
                # Network settings
                with gr.Column():
                    use_proxy = gr.Checkbox(
                        label="Use proxy server",
                        value=False,
                        elem_classes=["checkbox"]
                    )
                    
                    proxy_server = gr.Textbox(
                        label="Proxy Server",
                        placeholder="http://proxy.example.com:8080",
                        visible=False,
                        elem_classes=["input-field"]
                    )
                    
                    proxy_username = gr.Textbox(
                        label="Proxy Username",
                        placeholder="username",
                        visible=False,
                        elem_classes=["input-field"]
                    )
                    
                    proxy_password = gr.Textbox(
                        label="Proxy Password",
                        placeholder="password",
                        type="password",
                        visible=False,
                        elem_classes=["input-field"]
                    )
        
        # Recording & Session Management Section
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column():
                gr.Markdown("### 📹 Recording & Session Management", elem_classes=["section-header"])
                
                # Recording settings
                with gr.Row():
                    enable_recording = gr.Checkbox(
                        label="Enable session recording",
                        value=True,
                        info="Record browser actions as GIF/MP4",
                        elem_classes=["checkbox"]
                    )
                    
                    recording_format = gr.Dropdown(
                        choices=["gif", "mp4", "webm"],
                        value="gif",
                        label="Recording Format",
                        elem_classes=["dropdown"]
                    )
                    
                    recording_quality = gr.Slider(
                        minimum=1,
                        maximum=10,
                        value=7,
                        step=1,
                        label="Recording Quality",
                        elem_classes=["slider"]
                    )
                
                # Path settings
                with gr.Row():
                    recording_path = gr.Textbox(
                        label="Recording Output Path",
                        value="./tmp/recordings",
                        placeholder="Directory to save recordings",
                        elem_classes=["input-field"]
                    )
                    
                    browse_recording_button = gr.Button(
                        "📁 Browse",
                        variant="secondary",
                        scale=0,
                        elem_classes=["btn-secondary"]
                    )
                
                with gr.Row():
                    trace_path = gr.Textbox(
                        label="Trace Output Path",
                        value="./tmp/traces",
                        placeholder="Directory to save browser traces",
                        elem_classes=["input-field"]
                    )
                    
                    browse_trace_button = gr.Button(
                        "📁 Browse",
                        variant="secondary",
                        scale=0,
                        elem_classes=["btn-secondary"]
                    )
                
                # Download settings
                with gr.Row():
                    downloads_path = gr.Textbox(
                        label="Downloads Directory",
                        value="./tmp/downloads",
                        placeholder="Directory for downloaded files",
                        elem_classes=["input-field"]
                    )
                    
                    browse_downloads_button = gr.Button(
                        "📁 Browse",
                        variant="secondary",
                        scale=0,
                        elem_classes=["btn-secondary"]
                    )
                
                # History settings
                with gr.Row():
                    history_path = gr.Textbox(
                        label="Agent History Path",
                        value="./tmp/agent_history",
                        placeholder="Directory to save agent session history",
                        elem_classes=["input-field"]
                    )
                    
                    browse_history_button = gr.Button(
                        "📁 Browse",
                        variant="secondary",
                        scale=0,
                        elem_classes=["btn-secondary"]
                    )
        
        # Test & Validation Section
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column():
                gr.Markdown("### 🧪 Test & Validation", elem_classes=["section-header"])
                
                # Browser test controls
                with gr.Row():
                    test_browser_button = gr.Button(
                        "🧪 Test Browser Setup",
                        variant="primary",
                        elem_classes=["btn-primary"]
                    )
                    
                    open_browser_button = gr.Button(
                        "🌐 Open Test Browser",
                        variant="secondary",
                        elem_classes=["btn-secondary"]
                    )
                    
                    reset_settings_button = gr.Button(
                        "↺ Reset to Defaults",
                        variant="secondary",
                        elem_classes=["btn-secondary"]
                    )
                
                # Status display
                browser_test_status = gr.Textbox(
                    label="Browser Test Status",
                    value="Not tested",
                    interactive=False,
                    elem_classes=["status-display"]
                )
                
                # Browser info display
                browser_info = gr.JSON(
                    label="Browser Information",
                    value={
                        "version": "Not detected",
                        "userAgent": "Not detected",
                        "platform": "Not detected"
                    },
                    elem_classes=["info-display"]
                )
        
        # Performance & Resource Section
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column():
                gr.Markdown("### ⚡ Performance & Resources", elem_classes=["section-header"])
                
                # Performance settings
                with gr.Row():
                    max_concurrent_tabs = gr.Slider(
                        minimum=1,
                        maximum=10,
                        value=1,
                        step=1,
                        label="Max Concurrent Tabs",
                        elem_classes=["slider"]
                    )
                    
                    page_load_timeout = gr.Slider(
                        minimum=5,
                        maximum=120,
                        value=30,
                        step=5,
                        label="Page Load Timeout (seconds)",
                        elem_classes=["slider"]
                    )
                
                with gr.Row():
                    memory_limit = gr.Slider(
                        minimum=256,
                        maximum=8192,
                        value=2048,
                        step=256,
                        label="Memory Limit (MB)",
                        elem_classes=["slider"]
                    )
                    
                    cpu_limit = gr.Slider(
                        minimum=10,
                        maximum=100,
                        value=80,
                        step=10,
                        label="CPU Usage Limit (%)",
                        elem_classes=["slider"]
                    )
    
    # Store all components
    tab_components = {
        "browser_type": browser_type,
        "browser_channel": browser_channel,
        "browser_binary_path": browser_binary_path,
        "browser_user_data_dir": browser_user_data_dir,
        "use_own_browser": use_own_browser,
        "keep_browser_open": keep_browser_open,
        "headless_mode": headless_mode,
        "disable_security": disable_security,
        "disable_images": disable_images,
        "disable_javascript": disable_javascript,
        "block_ads": block_ads,
        "incognito_mode": incognito_mode,
        "viewport_preset": viewport_preset,
        "window_width": window_width,
        "window_height": window_height,
        "device_scale_factor": device_scale_factor,
        "user_agent_preset": user_agent_preset,
        "custom_user_agent": custom_user_agent,
        "enable_cdp": enable_cdp,
        "cdp_port": cdp_port,
        "cdp_url": cdp_url,
        "wss_url": wss_url,
        "use_proxy": use_proxy,
        "proxy_server": proxy_server,
        "proxy_username": proxy_username,
        "proxy_password": proxy_password,
        "enable_recording": enable_recording,
        "recording_format": recording_format,
        "recording_quality": recording_quality,
        "recording_path": recording_path,
        "trace_path": trace_path,
        "downloads_path": downloads_path,
        "history_path": history_path,
        "test_browser_button": test_browser_button,
        "open_browser_button": open_browser_button,
        "reset_settings_button": reset_settings_button,
        "browser_test_status": browser_test_status,
        "browser_info": browser_info,
        "max_concurrent_tabs": max_concurrent_tabs,
        "page_load_timeout": page_load_timeout,
        "memory_limit": memory_limit,
        "cpu_limit": cpu_limit
    }
    
    # Add interactive behaviors
    def update_viewport_from_preset(preset):
        """Update viewport dimensions based on preset selection"""
        presets = {
            "Desktop HD (1920×1080)": (1920, 1080),
            "Desktop FHD (1280×720)": (1280, 720),
            "Laptop (1366×768)": (1366, 768),
            "Tablet Portrait (768×1024)": (768, 1024),
            "Tablet Landscape (1024×768)": (1024, 768),
            "Mobile Portrait (375×667)": (375, 667),
            "Mobile Landscape (667×375)": (667, 375)
        }
        
        if preset in presets:
            width, height = presets[preset]
            return gr.update(value=width), gr.update(value=height)
        return gr.update(), gr.update()
    
    def toggle_custom_user_agent(preset):
        """Show/hide custom user agent field"""
        return gr.update(visible=(preset == "Custom"))
    
    def toggle_proxy_fields(use_proxy):
        """Show/hide proxy configuration fields"""
        return (
            gr.update(visible=use_proxy),
            gr.update(visible=use_proxy),
            gr.update(visible=use_proxy)
        )
    
    # Set up event handlers
    viewport_preset.change(
        fn=update_viewport_from_preset,
        inputs=[viewport_preset],
        outputs=[window_width, window_height]
    )
    
    user_agent_preset.change(
        fn=toggle_custom_user_agent,
        inputs=[user_agent_preset],
        outputs=[custom_user_agent]
    )
    
    use_proxy.change(
        fn=toggle_proxy_fields,
        inputs=[use_proxy],
        outputs=[proxy_server, proxy_username, proxy_password]
    )
    
    # Add components to webui manager
    webui_manager.add_components("enhanced_browser_settings", tab_components)
    
    return tab_components