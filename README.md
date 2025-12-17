# EDID Parser (Python)

A lightweight Python-based EDID (Extended Display Identification Data) parser that extracts key display capabilities such as recommended resolution, refresh rate, and supported limits from raw EDID binary data.

---

## 📌 Features

- Parses raw EDID binary files
- Extracts **preferred (recommended) resolution and refresh rate**
- Identifies **maximum supported resolution and refresh rate**
- Decodes **Detailed Timing Descriptors**
- Reads **Display Range Limits Descriptor (GTF / CVT support)**
- Command-line interface using `argparse`
- Clean, readable terminal output

---

## 📂 Project Structure


---

## 🛠 Requirements

- Python 3.8 or higher
- No external dependencies (uses only Python standard library)

---

## ▶️ Usage

Run the script from the terminal or PowerShell:

```bash
python EDID_Parser.py --file <path_to_edid_binary>

Preferred Resolution : 1920 x 1080 @ 60 Hz
Maximum Resolution   : 2560 x 1440 @ 75 Hz
Horizontal Frequency : 30 – 160 kHz
Vertical Frequency   : 50 – 144 Hz
Timing Support       : CVT / CVT-RB
