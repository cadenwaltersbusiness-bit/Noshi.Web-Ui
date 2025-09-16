"""
Enhanced Browser Use Agent Tab with improved UI controls and progress visualization
"""
import gradio as gr
from typing import Dict, Any
from src.webui.webui_manager import WebuiManager


def create_enhanced_browser_use_agent_tab(webui_manager: WebuiManager):
    """
    Enhanced version of the browser use agent tab with better UI and controls
    """
    webui_manager.init_browser_use_agent()
    
    # Enhanced UI components with better organization
    tab_components = {}
    
    with gr.Column(elem_classes=["tab-content"]):
        # Status and Progress Section
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column(scale=3):
                gr.Markdown("### 🤖 Agent Status", elem_classes=["section-header"])
                
                # Status indicators
                with gr.Row():
                    agent_status = gr.Textbox(
                        value="Ready",
                        label="Status",
                        interactive=False,
                        elem_classes=["status-display"]
                    )
                    steps_progress = gr.Textbox(
                        value="0/100",
                        label="Steps",
                        interactive=False,
                        elem_classes=["progress-display"]
                    )
                    actions_progress = gr.Textbox(
                        value="0/10",
                        label="Actions",
                        interactive=False,
                        elem_classes=["progress-display"]
                    )
                
                # Progress bars
                overall_progress = gr.Slider(
                    minimum=0,
                    maximum=100,
                    value=0,
                    label="Overall Progress",
                    interactive=False,
                    elem_classes=["progress-bar"]
                )
                
                step_progress = gr.Slider(
                    minimum=0,
                    maximum=100,
                    value=0,
                    label="Current Step Progress",
                    interactive=False,
                    elem_classes=["progress-bar"]
                )
            
            with gr.Column(scale=1):
                gr.Markdown("### ⚡ Quick Actions", elem_classes=["section-header"])
                
                # Quick action buttons
                with gr.Column():
                    emergency_stop = gr.Button(
                        "🚨 Emergency Stop",
                        variant="stop",
                        elem_classes=["btn-emergency"]
                    )
                    take_screenshot = gr.Button(
                        "📸 Screenshot",
                        variant="secondary",
                        elem_classes=["btn-secondary"]
                    )
                    save_session = gr.Button(
                        "💾 Save Session",
                        variant="secondary",
                        elem_classes=["btn-secondary"]
                    )
        
        # Task Input Section
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column():
                gr.Markdown("### 📝 Task Input", elem_classes=["section-header"])
                
                # Enhanced task input with suggestions
                task_input = gr.Textbox(
                    label="Describe your task",
                    placeholder="e.g., 'Navigate to Google and search for Python tutorials'",
                    lines=3,
                    max_lines=10,
                    elem_classes=["input-field"],
                    elem_id="enhanced_task_input"
                )
                
                # Task suggestions
                with gr.Row():
                    gr.Examples(
                        examples=[
                            "Search for information about AI on Wikipedia",
                            "Navigate to GitHub and find trending Python repositories",
                            "Go to Amazon and search for 'wireless headphones'",
                            "Find the weather forecast for San Francisco",
                            "Visit YouTube and search for programming tutorials"
                        ],
                        inputs=[task_input],
                        label="Example Tasks"
                    )
        
        # Control Buttons Section
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column():
                gr.Markdown("### 🎮 Controls", elem_classes=["section-header"])
                
                with gr.Row():
                    start_button = gr.Button(
                        "▶️ Start Task",
                        variant="primary",
                        scale=2,
                        elem_classes=["btn-primary"]
                    )
                    pause_button = gr.Button(
                        "⏸️ Pause",
                        variant="secondary",
                        scale=1,
                        interactive=False,
                        elem_classes=["btn-secondary"]
                    )
                    resume_button = gr.Button(
                        "⏯️ Resume",
                        variant="secondary",
                        scale=1,
                        interactive=False,
                        visible=False,
                        elem_classes=["btn-secondary"]
                    )
                    stop_button = gr.Button(
                        "⏹️ Stop",
                        variant="stop",
                        scale=1,
                        interactive=False,
                        elem_classes=["btn-secondary"]
                    )
                    clear_button = gr.Button(
                        "🗑️ Clear",
                        variant="secondary",
                        scale=1,
                        elem_classes=["btn-secondary"]
                    )
        
        # Agent Interaction Section
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column():
                gr.Markdown("### 💬 Agent Interaction", elem_classes=["section-header"])
                
                # Enhanced chatbot with better styling
                chatbot = gr.Chatbot(
                    lambda: webui_manager.bu_chat_history,
                    elem_id="enhanced_browser_use_chatbot",
                    label="Conversation",
                    type="messages",
                    height=500,
                    show_copy_button=True,
                    show_share_button=False,
                    elem_classes=["chatbot"]
                )
                
                # User response input
                user_response = gr.Textbox(
                    label="Your response (when agent asks for input)",
                    placeholder="Type your response here when the agent asks for clarification...",
                    lines=2,
                    interactive=True,
                    elem_classes=["input-field"]
                )
                
                send_response_button = gr.Button(
                    "💬 Send Response",
                    variant="secondary",
                    elem_classes=["btn-secondary"]
                )
        
        # Browser View Section
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column():
                gr.Markdown("### 🌐 Browser View", elem_classes=["section-header"])
                
                # Browser view controls
                with gr.Row():
                    show_browser_toggle = gr.Checkbox(
                        label="Show Live Browser View",
                        value=False,
                        elem_classes=["checkbox"]
                    )
                    auto_scroll_toggle = gr.Checkbox(
                        label="Auto-scroll to action",
                        value=True,
                        elem_classes=["checkbox"]
                    )
                    highlight_elements_toggle = gr.Checkbox(
                        label="Highlight interacted elements",
                        value=True,
                        elem_classes=["checkbox"]
                    )
                
                # Enhanced browser view
                browser_view = gr.HTML(
                    value="""
                    <div class="browser-placeholder" style="
                        width: 100%; 
                        height: 400px; 
                        display: flex; 
                        flex-direction: column;
                        justify-content: center; 
                        align-items: center; 
                        border: 2px dashed var(--border-default); 
                        border-radius: var(--radius-md);
                        background: var(--bg-tertiary);
                        color: var(--text-secondary);
                        font-family: var(--font-mono);
                    ">
                        <div style="font-size: 48px; margin-bottom: 16px;">🌐</div>
                        <div style="font-size: 18px; margin-bottom: 8px;">Browser View</div>
                        <div style="font-size: 14px; opacity: 0.7;">Enable "Show Live Browser View" to see the browser in action</div>
                    </div>
                    """,
                    label="Live Browser View",
                    elem_id="enhanced_browser_view",
                    visible=True,
                    elem_classes=["browser-view"]
                )
        
        # Action Timeline Section
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column():
                gr.Markdown("### 📋 Action Timeline", elem_classes=["section-header"])
                
                # Action list with timestamps
                action_timeline = gr.Dataframe(
                    headers=["Time", "Action", "Target", "Status", "Details"],
                    datatype=["str", "str", "str", "str", "str"],
                    interactive=False,
                    wrap=True,
                    elem_classes=["action-timeline"],
                    max_height=300
                )
                
                # Timeline controls
                with gr.Row():
                    export_timeline_button = gr.Button(
                        "📄 Export Timeline",
                        variant="secondary",
                        scale=1,
                        elem_classes=["btn-secondary"]
                    )
                    clear_timeline_button = gr.Button(
                        "🗑️ Clear Timeline",
                        variant="secondary",
                        scale=1,
                        elem_classes=["btn-secondary"]
                    )
                    auto_update_timeline = gr.Checkbox(
                        label="Auto-update timeline",
                        value=True,
                        scale=2,
                        elem_classes=["checkbox"]
                    )
        
        # Outputs Section
        with gr.Row(elem_classes=["form-section"]):
            with gr.Column(scale=1):
                gr.Markdown("### 📁 Session Outputs", elem_classes=["section-header"])
                
                # File outputs with better organization
                with gr.Tabs():
                    with gr.TabItem("📄 History"):
                        agent_history_file = gr.File(
                            label="Agent History JSON",
                            interactive=False,
                            elem_classes=["file-output"]
                        )
                    
                    with gr.TabItem("🎬 Recording"):
                        recording_gif = gr.Image(
                            label="Task Recording GIF",
                            format="gif",
                            interactive=False,
                            elem_classes=["recording-output"]
                        )
                    
                    with gr.TabItem("📸 Screenshots"):
                        screenshots_gallery = gr.Gallery(
                            label="Session Screenshots",
                            show_label=True,
                            elem_id="screenshots_gallery",
                            columns=3,
                            rows=2,
                            object_fit="contain",
                            height="auto",
                            elem_classes=["screenshots-gallery"]
                        )
            
            with gr.Column(scale=1):
                gr.Markdown("### ⚙️ Session Settings", elem_classes=["section-header"])
                
                # Session configuration
                with gr.Column():
                    session_name = gr.Textbox(
                        label="Session Name",
                        placeholder="My Browser Task",
                        elem_classes=["input-field"]
                    )
                    
                    max_steps_display = gr.Number(
                        label="Max Steps",
                        value=100,
                        interactive=False,
                        elem_classes=["input-field"]
                    )
                    
                    max_actions_display = gr.Number(
                        label="Max Actions per Step",
                        value=10,
                        interactive=False,
                        elem_classes=["input-field"]
                    )
                    
                    timeout_setting = gr.Slider(
                        minimum=30,
                        maximum=300,
                        value=60,
                        step=30,
                        label="Action Timeout (seconds)",
                        elem_classes=["slider"]
                    )
    
    # Store components for external access
    tab_components.update({
        "task_input": task_input,
        "chatbot": chatbot,
        "user_response": user_response,
        "start_button": start_button,
        "pause_button": pause_button,
        "resume_button": resume_button,
        "stop_button": stop_button,
        "clear_button": clear_button,
        "send_response_button": send_response_button,
        "agent_status": agent_status,
        "steps_progress": steps_progress,
        "actions_progress": actions_progress,
        "overall_progress": overall_progress,
        "step_progress": step_progress,
        "browser_view": browser_view,
        "show_browser_toggle": show_browser_toggle,
        "action_timeline": action_timeline,
        "agent_history_file": agent_history_file,
        "recording_gif": recording_gif,
        "screenshots_gallery": screenshots_gallery,
        "emergency_stop": emergency_stop,
        "take_screenshot": take_screenshot,
        "save_session": save_session,
        "session_name": session_name,
        "timeout_setting": timeout_setting
    })
    
    # Add components to webui manager
    webui_manager.add_components("enhanced_browser_use_agent", tab_components)
    
    # TODO: Add event handlers here (preserve existing handler logic)
    # This would include the same async handlers as the original tab
    # but with enhanced UI updates for progress, timeline, etc.
    
    return tab_components