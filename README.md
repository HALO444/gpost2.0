![logo.png](https://raw.githubusercontent.com/HALO444/gpost2.0/refs/heads/main/logo.png)

# gpost v2.0

**gpost** is a lightweight, asynchronous brute-forcing tool for **directories** and **subdomains**, inspired by tools like Gobuster but written in Python for easier modification and learning. It’s designed to be fast, clean, and beginner-friendly, with features like automatic progress tracking, result logging, and clean CLI interaction.

---

## 🚀 Features

- 🔍 Subdomain and directory scanning (`dns` and `dir` modes)
- ⚡ Asynchronous HTTP requests with `aiohttp`
- 📊 Progress bar using `tqdm`
- 🧾 Result logging to auto-named `.txt` files
- ✅ URL validation and basic error handling
- 🎯 CLI-friendly with built-in help

---

## 📂 Project Structure

```text

├── main.py           # Entry point
├── dir.py            # Directory brute-forcing
├── dns.py            # Subdomain brute-forcing
├── error.py          # Error handler for invalid commands
├── help.py           # CLI help display
├── start_msg.py      # Startup info print
├── wordlist.txt      # (Optional) Sample wordlist
```
---
## 📦 Requirements

Before running, make sure you have the following Python packages installed:

```text
pip install aiohttp tqdm validators
```
---
## 🧑‍💻 Usage

```text
python main.py [command] [wordlist] [url]
```
---
## 🔍 Commands

```text
dir – Perform directory brute-force
dns – Perform subdomain brute-force
-h, --help – Show help
```
---
## 📌 Examples

```text
python main.py dir wordlist.txt https://example.com
python main.py dns wordlist.txt https://example.com
python main.py --help
```
---



