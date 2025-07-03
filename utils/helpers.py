# utils/helpers.py

import os
from datetime import datetime

def save_to_file(label: str, content: str, output_dir: str = "outputs"):
    """
    Saves content to a uniquely named text file inside outputs/.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{label}.txt"
    filepath = os.path.join(output_dir, filename)

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Output saved to: {filepath}")
    except Exception as e:
        print(f"❌ Failed to save file: {e}")
