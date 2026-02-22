import subprocess
import sys
import os

def run():
    subprocess.run([
        sys.executable, "-m", "streamlit",
        "run",
        "streamlit_app.py",
        "--server.headless=true"
    ])

if __name__ == "__main__":
    run()
  pip install streamlit pyinstaller
pyinstaller --onefile --hidden-import=streamlit.runtime.scriptrunner.script_runner run.py
