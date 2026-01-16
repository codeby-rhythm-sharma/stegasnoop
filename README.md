# StegaSnoop

## Overview
StegaSnoop is a lightweight educational tool for detecting potential image steganography.
It uses simple heuristic techniques to analyze images for suspicious patterns.

## How It Works
StegaSnoop applies the following heuristic checks:
- Least Significant Bit (LSB) analysis
- Shannon entropy calculation
- Adjacent pixel correlation analysis

These techniques help highlight anomalies that may indicate hidden data.

## What This Tool Does NOT Do
- It does not guarantee detection of all steganography techniques
- It is not a forensic or enterprise-grade security tool
- It should not be used as the sole decision-making mechanism

## How to Run
```bash
python stegasnoop.py image.png
## Contributing
Contributions are welcome!
## ACWOC Contributions

This project is part of ACWOC and is open for beginner-friendly
open-source contributions.

New contributors can start with:
- Documentation improvements
- Adding test images
- Improving detection heuristics
- Enhancing CLI output

All contribution tasks are listed under the **Issues** tab.

To contribute:
1. Fork this repository
2. Create a new branch for your changes
3. Make your changes and commit them
4. Open a pull request describing what you changed
Problem Statement
Image steganography can be used to hide malicious data inside images, making detection difficult. This project aims to help beginners understand how simple statistical and heuristic techniques can be used to flag suspicious images
Why This Project Matters
Steganography is commonly used in malware delivery and data exfiltration. This project introduces foundational detection concepts useful for cybersecurity students and beginners
Why This Project Matters
Steganography is commonly used in malware delivery and data exfiltration. This project introduces foundational detection concepts useful for cybersecurity students and beginners
Future Improvements

Support for additional image formats

Visualization of entropy graphs

Machine learning–based detection

Batch image scanning
## ⚠️ Notice
This is the official repository maintained by @codeby-rhythm-sharma.
Any forks are community copies and are not officially maintained.
