# Automated Steam Marketplace Scraper

A modular data engineering script written in Python that automates network sessions, connects to live document trees using fake browser authentication headers, and parses raw HTML nodes into structured tabular CSV datasets.

## 🚀 Script Architecture & Extraction Logic
* **Network Session Simulation:** Uses the `requests` layer configured with customized `User-Agent` hardware header definitions to bypass global platform rate limits and prevent socket blocking routines.
* **Document Tree Interception:** Integrates an HTML parser pipeline via `BeautifulSoup` to scan through multi-layered tag arrays and selectively capture targeted node strings (`search_result_row`).
* **Tabular Matrix Formatting:** Loops through isolated text nodes, cleanly stripping carriage breaks and white spaces via a structured string parsing algorithm before writing the results directly into an appendable stream writer (`csv.writer`).

## 🛠️ Software Stack
* **Language Environment:** Python 3.x
* **Core Subsystems:** Requests Session Library, BeautifulSoup4 Parser Engine, Native CSV Storage Stream
