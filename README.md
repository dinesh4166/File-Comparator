📁🔍 File Comparator - Python GUI Tool

📄 Description:
A Python-based GUI application to compare two files (TXT, CSV, or JSON) and highlight the differences line by line.
This tool is designed to make file comparison simple, visual, and efficient — whether you're checking text documents, code files, or exported CSV logs.

🚀 Features:
- Choose any two files using a user-friendly file dialog.
- Supported formats: .txt, .csv, .json
- Highlights differences using color-coded visual cues.
- Scrollable side-by-side display of both files.
- Shows the total number of differing lines.
- GUI built using Tkinter.
- Available as both Python script and a standalone `.exe` application.

💻 Requirements (for Python version):
- Python 3.x
- Standard libraries: tkinter, itertools

🛠️ How to Use:
1. Run the application (either `File_Comparator.py` or `File_Comparator.exe`).
2. From the menu, choose **File > Choose File 1** and select your first file.
3. Choose **File > Choose File 2** and select your second file.
4. Click on **Compare** to see both files side by side with highlighted differences.
5. The number of differing lines is shown at the bottom left.

📦 Executable Version:
- If you don't have Python installed, simply run the compiled `File_Comparator.exe`.
- No additional setup required!

📁 File Structure:
- `File_Comparator.py` – Main Python script.
- `File_Comparator.exe` – Executable version for Windows (optional).
- `README.txt` – You're reading it!

📌 Notes:
- CSV files are opened with BOM handling to avoid encoding issues.
- Differences are highlighted in **magenta** color.
- The tool is ideal for spotting line-by-line mismatches but not character-level differences.

📬 Author:
Developed by Dinesh21212
linkedin.com/in/dinesh-dataengineer/
Feel free to reach out with feedback or suggestions!

