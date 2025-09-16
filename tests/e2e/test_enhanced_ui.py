"""
End-to-end smoke tests for the enhanced Browser Use WebUI
Tests basic navigation and functionality without performing actual browser automation
"""
import asyncio
import subprocess
import time
import requests
from playwright.sync_api import sync_playwright
import pytest


class TestEnhancedUI:
    """Smoke tests for enhanced UI functionality"""
    
    @classmethod
    def setup_class(cls):
        """Start the enhanced webui server"""
        cls.process = subprocess.Popen([
            "python", "webui.py", 
            "--enhanced", 
            "--port", "7790",
            "--theme", "Replit"
        ], cwd="/home/runner/work/Noshi.Web-Ui/Noshi.Web-Ui")
        
        # Wait for server to start
        for _ in range(30):
            try:
                response = requests.get("http://127.0.0.1:7790")
                if response.status_code == 200:
                    break
            except requests.exceptions.ConnectionError:
                pass
            time.sleep(1)
        else:
            raise Exception("Server failed to start")
    
    @classmethod
    def teardown_class(cls):
        """Stop the webui server"""
        cls.process.terminate()
        cls.process.wait()
    
    def test_page_loads(self):
        """Test that the enhanced interface loads successfully"""
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            # Navigate to the enhanced interface
            page.goto("http://127.0.0.1:7790")
            
            # Wait for page to load
            page.wait_for_selector("h1", timeout=10000)
            
            # Check that the enhanced title is present
            title = page.inner_text("h1")
            assert "Browser Use WebUI - Enhanced" in title
            
            browser.close()
    
    def test_theme_toggle(self):
        """Test theme toggle functionality"""
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            page.goto("http://127.0.0.1:7790")
            page.wait_for_selector("h1", timeout=10000)
            
            # Find and click theme toggle button
            theme_button = page.locator("button:has-text('🌙')")
            assert theme_button.is_visible()
            
            # Click the theme toggle (test JavaScript functionality)
            theme_button.click()
            
            # Verify button is still present (may change icon)
            time.sleep(1)  # Allow theme change to process
            
            browser.close()
    
    def test_tab_navigation(self):
        """Test navigation between all tabs"""
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            page.goto("http://127.0.0.1:7790")
            page.wait_for_selector("h1", timeout=10000)
            
            # List of tabs to test
            tabs = [
                "⚙️ Agent Settings",
                "🌐 Browser Settings", 
                "🤖 Run Agent",
                "📊 History & Logs",
                "🔍 Inspector"
            ]
            
            for tab_name in tabs:
                # Click on each tab
                tab = page.locator(f"button:has-text('{tab_name}')")
                assert tab.is_visible(), f"Tab '{tab_name}' not found"
                tab.click()
                
                # Wait for tab content to load
                time.sleep(0.5)
                
                # Verify tab is active/selected
                active_tab = page.locator(f"[role='tab'][aria-selected='true']:has-text('{tab_name}')")
                assert active_tab.is_visible(), f"Tab '{tab_name}' is not active after clicking"
            
            browser.close()
    
    def test_agent_settings_tab(self):
        """Test Agent Settings tab functionality"""
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            page.goto("http://127.0.0.1:7790")
            page.wait_for_selector("h1", timeout=10000)
            
            # Navigate to Agent Settings
            agent_tab = page.locator("button:has-text('⚙️ Agent Settings')")
            agent_tab.click()
            
            # Check for key elements
            assert page.locator("h3:has-text('🧠 System Prompts')").is_visible()
            assert page.locator("h3:has-text('🤖 Primary LLM Configuration')").is_visible()
            assert page.locator("h3:has-text('🔌 MCP Server Configuration')").is_visible()
            
            # Test LLM provider dropdown
            provider_dropdown = page.locator("label:has-text('LLM Provider') + * select")
            assert provider_dropdown.is_visible()
            
            # Test temperature slider
            temp_slider = page.locator("label:has-text('Temperature') + * input[type='range']")
            assert temp_slider.is_visible()
            
            browser.close()
    
    def test_run_agent_tab(self):
        """Test Run Agent tab functionality"""
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            page.goto("http://127.0.0.1:7790")
            page.wait_for_selector("h1", timeout=10000)
            
            # Navigate to Run Agent
            run_tab = page.locator("button:has-text('🤖 Run Agent')")
            run_tab.click()
            
            # Check for key sections
            assert page.locator("h3:has-text('🤖 Agent Status')").is_visible()
            assert page.locator("h3:has-text('📝 Task Input')").is_visible()
            assert page.locator("h3:has-text('🎮 Controls')").is_visible()
            assert page.locator("h3:has-text('💬 Agent Interaction')").is_visible()
            
            # Test task input field
            task_input = page.locator("textarea[placeholder*='task']")
            assert task_input.is_visible()
            
            # Test control buttons
            start_button = page.locator("button:has-text('▶️ Start Task')")
            assert start_button.is_visible()
            
            # Test example tasks
            example_buttons = page.locator("button:has-text('Search for information')")
            assert example_buttons.is_visible()
            
            browser.close()
    
    def test_browser_settings_tab(self):
        """Test Browser Settings tab functionality"""
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            page.goto("http://127.0.0.1:7790")
            page.wait_for_selector("h1", timeout=10000)
            
            # Navigate to Browser Settings
            browser_tab = page.locator("button:has-text('🌐 Browser Settings')")
            browser_tab.click()
            
            # Check for key sections
            assert page.locator("h3:has-text('🌐 Browser Configuration')").is_visible()
            assert page.locator("h3:has-text('⚙️ Browser Behavior')").is_visible()
            assert page.locator("h3:has-text('📱 Viewport & Display')").is_visible()
            
            # Test browser type selection
            browser_type = page.locator("input[value='chromium']")
            assert browser_type.is_visible()
            
            # Test viewport preset dropdown
            viewport_preset = page.locator("label:has-text('Viewport Preset') + * select")
            assert viewport_preset.is_visible()
            
            browser.close()
    
    def test_inspector_tab(self):
        """Test Inspector tab functionality"""
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            page.goto("http://127.0.0.1:7790")
            page.wait_for_selector("h1", timeout=10000)
            
            # Navigate to Inspector
            inspector_tab = page.locator("button:has-text('🔍 Inspector')")
            inspector_tab.click()
            
            # Check for key elements
            assert page.locator("h3:has-text('🔍 Browser Inspector & DevTools')").is_visible()
            assert page.locator("button:has-text('🔍 Inspect Current Page')").is_visible()
            
            # Test inspector sub-tabs
            dom_tab = page.locator("button:has-text('🌳 DOM Tree')")
            assert dom_tab.is_visible()
            
            network_tab = page.locator("button:has-text('🌐 Network')")
            assert network_tab.is_visible()
            
            console_tab = page.locator("button:has-text('💻 Console')")
            assert console_tab.is_visible()
            
            browser.close()
    
    def test_history_logs_tab(self):
        """Test History & Logs tab functionality"""
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            page.goto("http://127.0.0.1:7790")
            page.wait_for_selector("h1", timeout=10000)
            
            # Navigate to History & Logs
            history_tab = page.locator("button:has-text('📊 History & Logs')")
            history_tab.click()
            
            # Check for key elements
            assert page.locator("h3:has-text('📊 Session History & Logs')").is_visible()
            assert page.locator("h3:has-text('Session Details')").is_visible()
            assert page.locator("h3:has-text('Live Logs')").is_visible()
            
            # Test filter controls
            status_filter = page.locator("label:has-text('Status Filter') + * select")
            assert status_filter.is_visible()
            
            browser.close()
    
    def test_responsive_design(self):
        """Test responsive design at different screen sizes"""
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            page.goto("http://127.0.0.1:7790")
            page.wait_for_selector("h1", timeout=10000)
            
            # Test desktop size
            page.set_viewport_size({"width": 1920, "height": 1080})
            assert page.locator("h1").is_visible()
            
            # Test tablet size
            page.set_viewport_size({"width": 768, "height": 1024})
            assert page.locator("h1").is_visible()
            
            # Test mobile size
            page.set_viewport_size({"width": 375, "height": 667})
            assert page.locator("h1").is_visible()
            
            browser.close()
    
    def test_no_javascript_errors(self):
        """Test that no JavaScript errors occur during basic usage"""
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            # Collect console messages
            console_messages = []
            page.on("console", lambda msg: console_messages.append(msg))
            
            page.goto("http://127.0.0.1:7790")
            page.wait_for_selector("h1", timeout=10000)
            
            # Navigate through tabs
            tabs = ["🤖 Run Agent", "🌐 Browser Settings", "🔍 Inspector"]
            for tab_name in tabs:
                tab = page.locator(f"button:has-text('{tab_name}')")
                tab.click()
                time.sleep(0.5)
            
            # Click theme toggle
            theme_button = page.locator("button:has-text('🌙')")
            theme_button.click()
            time.sleep(1)
            
            # Check for JavaScript errors (excluding network errors)
            js_errors = [msg for msg in console_messages 
                        if msg.type == "error" and "net::" not in msg.text]
            
            assert len(js_errors) == 0, f"JavaScript errors found: {[msg.text for msg in js_errors]}"
            
            browser.close()


if __name__ == "__main__":
    # Run tests directly
    test_instance = TestEnhancedUI()
    test_instance.setup_class()
    
    try:
        test_instance.test_page_loads()
        test_instance.test_theme_toggle()
        test_instance.test_tab_navigation()
        test_instance.test_agent_settings_tab()
        test_instance.test_run_agent_tab()
        test_instance.test_browser_settings_tab()
        test_instance.test_inspector_tab()
        test_instance.test_history_logs_tab()
        test_instance.test_responsive_design()
        test_instance.test_no_javascript_errors()
        
        print("✅ All smoke tests passed!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        raise
    finally:
        test_instance.teardown_class()