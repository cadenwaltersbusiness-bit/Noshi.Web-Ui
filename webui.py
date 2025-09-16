from dotenv import load_dotenv
load_dotenv()
import argparse
from src.webui.interface import theme_map, create_ui
from src.webui.enhanced_interface import create_enhanced_ui


def main():
    parser = argparse.ArgumentParser(description="Gradio WebUI for Browser Agent")
    parser.add_argument("--ip", type=str, default="127.0.0.1", help="IP address to bind to")
    parser.add_argument("--port", type=int, default=7788, help="Port to listen on")
    parser.add_argument("--theme", type=str, default="Replit", choices=theme_map.keys(), help="Theme to use for the UI")
    parser.add_argument("--enhanced", action="store_true", help="Use enhanced UI components")
    args = parser.parse_args()

    if args.enhanced:
        print("🚀 Starting Enhanced Browser Use WebUI...")
        demo = create_enhanced_ui(theme_name=args.theme, use_enhanced_components=True)
    else:
        print("🌐 Starting Browser Use WebUI...")
        demo = create_ui(theme_name=args.theme)
    
    demo.queue().launch(server_name=args.ip, server_port=args.port)


if __name__ == '__main__':
    main()
