"""
Enhanced Agent Settings Tab with better LLM management and configuration
"""
import gradio as gr
import json
import os
from typing import Dict, Any
from src.webui.webui_manager import WebuiManager
from src.utils import config


def create_enhanced_agent_settings_tab(webui_manager: WebuiManager):
    """
    Enhanced agent settings tab with improved LLM configuration and management
    """
    tab_components = {}
    
    with gr.Column(elem_classes=["tab-content"]):
        # System Prompts Section
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column():
                gr.Markdown("### 🧠 System Prompts", elem_classes=["section-header"])
                
                # Prompt presets
                prompt_preset = gr.Dropdown(
                    choices=[
                        "Default",
                        "Web Navigation Expert",
                        "Data Extraction Specialist", 
                        "E-commerce Assistant",
                        "Research Assistant",
                        "Testing & QA Bot",
                        "Custom"
                    ],
                    value="Default",
                    label="Prompt Preset",
                    elem_classes=["dropdown"]
                )
                
                # System prompt override
                override_system_prompt = gr.Textbox(
                    label="Override System Prompt",
                    placeholder="Enter a complete system prompt to override the default behavior",
                    lines=8,
                    max_lines=20,
                    elem_classes=["input-field"]
                )
                
                # Extend system prompt
                extend_system_prompt = gr.Textbox(
                    label="Extend System Prompt",
                    placeholder="Add additional instructions to the default system prompt",
                    lines=4,
                    max_lines=10,
                    elem_classes=["input-field"]
                )
                
                # Prompt templates
                with gr.Row():
                    load_prompt_button = gr.Button(
                        "📁 Load Template",
                        variant="secondary",
                        elem_classes=["btn-secondary"]
                    )
                    save_prompt_button = gr.Button(
                        "💾 Save Template",
                        variant="secondary",
                        elem_classes=["btn-secondary"]
                    )
                    test_prompt_button = gr.Button(
                        "🧪 Test Prompt",
                        variant="primary",
                        elem_classes=["btn-primary"]
                    )
        
        # Primary LLM Configuration
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column():
                gr.Markdown("### 🤖 Primary LLM Configuration", elem_classes=["section-header"])
                
                # Provider and model selection
                with gr.Row():
                    llm_provider = gr.Dropdown(
                        choices=list(config.model_names.keys()),
                        value="openai",
                        label="LLM Provider",
                        elem_classes=["dropdown"]
                    )
                    
                    llm_model_name = gr.Dropdown(
                        choices=config.model_names.get("openai", []),
                        value="gpt-4o",
                        label="LLM Model",
                        allow_custom_value=True,
                        elem_classes=["dropdown"]
                    )
                
                # Model parameters
                with gr.Row():
                    llm_temperature = gr.Slider(
                        minimum=0.0,
                        maximum=2.0,
                        value=0.6,
                        step=0.1,
                        label="Temperature",
                        info="Controls randomness in responses",
                        elem_classes=["slider"]
                    )
                    
                    max_tokens = gr.Slider(
                        minimum=100,
                        maximum=200000,
                        value=4096,
                        step=100,
                        label="Max Tokens",
                        info="Maximum response length",
                        elem_classes=["slider"]
                    )
                
                # Advanced parameters
                with gr.Accordion("Advanced Parameters", open=False):
                    with gr.Row():
                        top_p = gr.Slider(
                            minimum=0.1,
                            maximum=1.0,
                            value=1.0,
                            step=0.1,
                            label="Top P",
                            info="Nucleus sampling parameter",
                            elem_classes=["slider"]
                        )
                        
                        frequency_penalty = gr.Slider(
                            minimum=-2.0,
                            maximum=2.0,
                            value=0.0,
                            step=0.1,
                            label="Frequency Penalty",
                            info="Reduces repetition",
                            elem_classes=["slider"]
                        )
                    
                    with gr.Row():
                        presence_penalty = gr.Slider(
                            minimum=-2.0,
                            maximum=2.0,
                            value=0.0,
                            step=0.1,
                            label="Presence Penalty",
                            info="Encourages new topics",
                            elem_classes=["slider"]
                        )
                        
                        timeout = gr.Slider(
                            minimum=10,
                            maximum=300,
                            value=60,
                            step=10,
                            label="Request Timeout (seconds)",
                            elem_classes=["slider"]
                        )
                
                # API Configuration
                with gr.Row():
                    base_url = gr.Textbox(
                        label="Base URL",
                        placeholder="Leave empty for default provider endpoint",
                        elem_classes=["input-field"]
                    )
                    
                    api_key = gr.Textbox(
                        label="API Key",
                        placeholder="Leave empty to use environment variables",
                        type="password",
                        elem_classes=["input-field"]
                    )
                
                # Vision and capabilities
                with gr.Row():
                    use_vision = gr.Checkbox(
                        label="Enable Vision",
                        value=True,
                        info="Input screenshots into LLM for visual understanding",
                        elem_classes=["checkbox"]
                    )
                    
                    use_tools = gr.Checkbox(
                        label="Enable Function Calling",
                        value=True,
                        info="Allow LLM to use browser automation tools",
                        elem_classes=["checkbox"]
                    )
                    
                    stream_responses = gr.Checkbox(
                        label="Stream Responses",
                        value=True,
                        info="Show responses as they are generated",
                        elem_classes=["checkbox"]
                    )
        
        # Planner LLM Configuration (Optional)
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column():
                gr.Markdown("### 🎯 Planner LLM Configuration (Optional)", elem_classes=["section-header"])
                
                # Enable planner LLM
                use_planner_llm = gr.Checkbox(
                    label="Use separate planning LLM",
                    value=False,
                    info="Use a different LLM for high-level task planning",
                    elem_classes=["checkbox"]
                )
                
                # Planner configuration (initially hidden)
                with gr.Column(visible=False) as planner_config:
                    with gr.Row():
                        planner_provider = gr.Dropdown(
                            choices=list(config.model_names.keys()),
                            value="openai",
                            label="Planner Provider",
                            elem_classes=["dropdown"]
                        )
                        
                        planner_model_name = gr.Dropdown(
                            choices=config.model_names.get("openai", []),
                            value="gpt-4o",
                            label="Planner Model",
                            allow_custom_value=True,
                            elem_classes=["dropdown"]
                        )
                    
                    with gr.Row():
                        planner_temperature = gr.Slider(
                            minimum=0.0,
                            maximum=2.0,
                            value=0.3,
                            step=0.1,
                            label="Planner Temperature",
                            elem_classes=["slider"]
                        )
                        
                        planner_vision = gr.Checkbox(
                            label="Planner Vision",
                            value=False,
                            info="Enable vision for planning LLM",
                            elem_classes=["checkbox"]
                        )
                    
                    with gr.Row():
                        planner_base_url = gr.Textbox(
                            label="Planner Base URL",
                            placeholder="Leave empty for default",
                            elem_classes=["input-field"]
                        )
                        
                        planner_api_key = gr.Textbox(
                            label="Planner API Key",
                            placeholder="Leave empty to use environment variables",
                            type="password",
                            elem_classes=["input-field"]
                        )
        
        # MCP (Model Context Protocol) Configuration
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column():
                gr.Markdown("### 🔌 MCP Server Configuration", elem_classes=["section-header"])
                
                # MCP file upload
                mcp_config_file = gr.File(
                    label="MCP Configuration JSON",
                    file_types=[".json"],
                    elem_classes=["file-input"]
                )
                
                # MCP configuration editor
                mcp_config_editor = gr.Code(
                    label="MCP Configuration",
                    language="json",
                    value='{\n  "mcpServers": {\n    "example": {\n      "command": "npx",\n      "args": ["-y", "@example/mcp-server"]\n    }\n  }\n}',
                    lines=10,
                    elem_classes=["code-editor"]
                )
                
                # MCP controls
                with gr.Row():
                    validate_mcp_button = gr.Button(
                        "✅ Validate Config",
                        variant="secondary",
                        elem_classes=["btn-secondary"]
                    )
                    
                    test_mcp_button = gr.Button(
                        "🧪 Test Connection",
                        variant="secondary",
                        elem_classes=["btn-secondary"]
                    )
                    
                    reset_mcp_button = gr.Button(
                        "↺ Reset to Default",
                        variant="secondary",
                        elem_classes=["btn-secondary"]
                    )
                
                # MCP status
                mcp_status = gr.Textbox(
                    label="MCP Status",
                    value="Not configured",
                    interactive=False,
                    elem_classes=["status-display"]
                )
        
        # Agent Behavior Configuration
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column(scale=1):
                gr.Markdown("### ⚙️ Agent Behavior", elem_classes=["section-header"])
                
                # Execution parameters
                with gr.Column():
                    max_run_steps = gr.Slider(
                        minimum=1,
                        maximum=1000,
                        value=100,
                        step=1,
                        label="Max Run Steps",
                        info="Maximum steps the agent will take",
                        elem_classes=["slider"]
                    )
                    
                    max_actions_per_step = gr.Slider(
                        minimum=1,
                        maximum=100,
                        value=10,
                        step=1,
                        label="Max Actions per Step",
                        info="Maximum actions in a single step",
                        elem_classes=["slider"]
                    )
                    
                    step_timeout = gr.Slider(
                        minimum=5,
                        maximum=300,
                        value=30,
                        step=5,
                        label="Step Timeout (seconds)",
                        info="Maximum time per step",
                        elem_classes=["slider"]
                    )
            
            with gr.Column(scale=1):
                gr.Markdown("### 🎯 Tool Configuration", elem_classes=["section-header"])
                
                # Tool calling settings
                with gr.Column():
                    tool_calling_method = gr.Dropdown(
                        choices=["auto", "required", "none"],
                        value="auto",
                        label="Tool Calling Method",
                        info="How the LLM should use browser tools",
                        elem_classes=["dropdown"]
                    )
                    
                    max_input_tokens = gr.Number(
                        label="Max Input Tokens",
                        value=128000,
                        minimum=1000,
                        maximum=1000000,
                        elem_classes=["input-field"]
                    )
                    
                    retry_attempts = gr.Slider(
                        minimum=0,
                        maximum=10,
                        value=3,
                        step=1,
                        label="Retry Attempts",
                        info="Number of retries for failed actions",
                        elem_classes=["slider"]
                    )
        
        # Safety & Monitoring
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column():
                gr.Markdown("### 🛡️ Safety & Monitoring", elem_classes=["section-header"])
                
                # Safety settings
                with gr.Row():
                    content_filter = gr.Checkbox(
                        label="Enable content filtering",
                        value=True,
                        info="Filter inappropriate content",
                        elem_classes=["checkbox"]
                    )
                    
                    debug_mode = gr.Checkbox(
                        label="Debug mode",
                        value=False,
                        info="Enable detailed logging",
                        elem_classes=["checkbox"]
                    )
                    
                    auto_save_sessions = gr.Checkbox(
                        label="Auto-save sessions",
                        value=True,
                        info="Automatically save session data",
                        elem_classes=["checkbox"]
                    )
                
                # Rate limiting
                with gr.Row():
                    rate_limit_requests = gr.Slider(
                        minimum=1,
                        maximum=100,
                        value=60,
                        step=1,
                        label="Rate Limit (requests/minute)",
                        elem_classes=["slider"]
                    )
                    
                    concurrent_sessions = gr.Slider(
                        minimum=1,
                        maximum=10,
                        value=1,
                        step=1,
                        label="Max Concurrent Sessions",
                        elem_classes=["slider"]
                    )
        
        # Test & Validation Section
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column():
                gr.Markdown("### 🧪 Test & Validation", elem_classes=["section-header"])
                
                # Test controls
                with gr.Row():
                    test_llm_button = gr.Button(
                        "🧪 Test Primary LLM",
                        variant="primary",
                        elem_classes=["btn-primary"]
                    )
                    
                    test_planner_button = gr.Button(
                        "🧪 Test Planner LLM",
                        variant="secondary",
                        elem_classes=["btn-secondary"]
                    )
                    
                    benchmark_button = gr.Button(
                        "📊 Run Benchmark",
                        variant="secondary",
                        elem_classes=["btn-secondary"]
                    )
                
                # Test results
                test_results = gr.Textbox(
                    label="Test Results",
                    value="No tests run yet",
                    interactive=False,
                    lines=5,
                    elem_classes=["status-display"]
                )
                
                # Performance metrics
                performance_metrics = gr.JSON(
                    label="Performance Metrics",
                    value={
                        "latency": "Not measured",
                        "tokens_per_second": "Not measured",
                        "success_rate": "Not measured"
                    },
                    elem_classes=["info-display"]
                )
    
    # Store all components
    tab_components = {
        "prompt_preset": prompt_preset,
        "override_system_prompt": override_system_prompt,
        "extend_system_prompt": extend_system_prompt,
        "llm_provider": llm_provider,
        "llm_model_name": llm_model_name,
        "llm_temperature": llm_temperature,
        "max_tokens": max_tokens,
        "top_p": top_p,
        "frequency_penalty": frequency_penalty,
        "presence_penalty": presence_penalty,
        "timeout": timeout,
        "base_url": base_url,
        "api_key": api_key,
        "use_vision": use_vision,
        "use_tools": use_tools,
        "stream_responses": stream_responses,
        "use_planner_llm": use_planner_llm,
        "planner_config": planner_config,
        "planner_provider": planner_provider,
        "planner_model_name": planner_model_name,
        "planner_temperature": planner_temperature,
        "planner_vision": planner_vision,
        "planner_base_url": planner_base_url,
        "planner_api_key": planner_api_key,
        "mcp_config_file": mcp_config_file,
        "mcp_config_editor": mcp_config_editor,
        "mcp_status": mcp_status,
        "max_run_steps": max_run_steps,
        "max_actions_per_step": max_actions_per_step,
        "step_timeout": step_timeout,
        "tool_calling_method": tool_calling_method,
        "max_input_tokens": max_input_tokens,
        "retry_attempts": retry_attempts,
        "content_filter": content_filter,
        "debug_mode": debug_mode,
        "auto_save_sessions": auto_save_sessions,
        "rate_limit_requests": rate_limit_requests,
        "concurrent_sessions": concurrent_sessions,
        "test_results": test_results,
        "performance_metrics": performance_metrics
    }
    
    # Set up dynamic behaviors
    def update_model_dropdown(provider):
        """Update model dropdown based on provider"""
        models = config.model_names.get(provider, [])
        if models:
            return gr.update(choices=models, value=models[0])
        return gr.update(choices=[], value="")
    
    def update_planner_model_dropdown(provider):
        """Update planner model dropdown based on provider"""
        models = config.model_names.get(provider, [])
        if models:
            return gr.update(choices=models, value=models[0])
        return gr.update(choices=[], value="")
    
    def toggle_planner_config(use_planner):
        """Show/hide planner configuration"""
        return gr.update(visible=use_planner)
    
    def load_prompt_preset(preset):
        """Load predefined prompt based on preset"""
        presets = {
            "Web Navigation Expert": "You are an expert web navigation assistant. Focus on efficient browsing, understanding web page structures, and completing tasks with minimal steps.",
            "Data Extraction Specialist": "You are a data extraction specialist. Focus on accurately finding and extracting specific information from web pages while respecting website terms of service.",
            "E-commerce Assistant": "You are an e-commerce assistant. Help users find products, compare prices, and navigate shopping websites effectively.",
            "Research Assistant": "You are a research assistant. Focus on finding credible sources, gathering comprehensive information, and organizing research findings.",
            "Testing & QA Bot": "You are a quality assurance bot. Focus on testing website functionality, finding bugs, and verifying that features work as expected."
        }
        
        if preset in presets:
            return gr.update(value=presets[preset])
        return gr.update()
    
    # Set up event handlers
    llm_provider.change(
        fn=update_model_dropdown,
        inputs=[llm_provider],
        outputs=[llm_model_name]
    )
    
    planner_provider.change(
        fn=update_planner_model_dropdown,
        inputs=[planner_provider],
        outputs=[planner_model_name]
    )
    
    use_planner_llm.change(
        fn=toggle_planner_config,
        inputs=[use_planner_llm],
        outputs=[planner_config]
    )
    
    prompt_preset.change(
        fn=load_prompt_preset,
        inputs=[prompt_preset],
        outputs=[override_system_prompt]
    )
    
    # Add components to webui manager
    webui_manager.add_components("enhanced_agent_settings", tab_components)
    
    return tab_components