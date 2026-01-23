# StegaSnoop 🕵️‍♂️

## Overview
StegaSnoop is a lightweight, educational Python tool for detecting potential image steganography.
It uses simple statistical and heuristic techniques to analyze images for suspicious patterns that may indicate hidden data.

This project is designed for beginners in cybersecurity and open-source contributions.


## 🔍 How It Works
StegaSnoop performs the following heuristic checks:

- **Least Significant Bit (LSB) analysis**
- **Shannon entropy calculation**
- **Adjacent pixel correlation analysis**

These methods help highlight anomalies commonly associated with steganographic techniques.


## ❌ What This Tool Does NOT Do
- It does **not** guarantee detection of all steganography techniques
- It is **not** a forensic or enterprise-grade security tool
- It should **not** be used as the sole decision-making mechanism


## ⚙️ Installation

```bash
git clone https://github.com/Pranavkale11/stegasnoop.git
cd stegasnoop
pip install -r requirements.txt
````


## 🚀 How to Run

### Basic Scan

```bash
python stegasnoop.py image.png
```

### Example Using Test Image

```bash
python stegasnoop.py test.jpg
```


## 📤 Sample Output

```text
[+] Loading image: test.jpg
[+] Performing LSB analysis...
[+] Calculating entropy...
[+] Checking pixel correlation...
[!] Suspicious patterns detected
[+] Analysis completed
```

> Output may vary depending on image content and encoding method.


## 🗂️ Project Structure

```text
stegasnoop/
│
├── examples/
│   ├── sample_logs.txt
│   └── example images
│
├── generate_samples.py     # Script to generate sample stego images
├── stegasnoop.py           # Main analysis script
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── License                 # MIT License
└── test.jpg                # Sample image
```


## 🧪 Generate Sample Files

```bash
python generate_samples.py
```

This script generates sample images with embedded data for experimentation.


## 🧑‍💻 Contributing

Contributions are welcome! 🎉
This project is beginner-friendly and part of **ACWOC**.

### New contributors can help by:

* Improving documentation
* Adding test images
* Enhancing detection heuristics
* Improving CLI output and usability

### Contribution Steps

1. Fork this repository
2. Create a new branch for your changes
3. Commit your changes
4. Open a pull request explaining your work

All contribution tasks are listed under the **Issues** tab.


## 🧠 Problem Statement

Image steganography can be used to hide malicious data inside images, making detection difficult.
This project helps beginners understand how basic statistical and heuristic techniques can be used to flag suspicious images.


## 🌍 Why This Project Matters

Steganography is often used in malware delivery and data exfiltration.
Understanding detection fundamentals is valuable for cybersecurity students and enthusiasts.


## 🔮 Future Improvements

* Support for additional image formats
* Visualization of entropy graphs
* Machine learning–based detection
* Batch image scanning
* 
⭐ If you find this project useful, please consider giving it a star!
It helps the project grow and motivates maintenance.

## 📜 License

This is the official repository maintained by **@codeby-rhythm-sharma**.
Forks are community-maintained and not officially supported.

