"""
Task 3 — Task Automation with Python Scripts
CodeAlpha Python Programming Internship

Three automation scripts in one interactive suite:
  Module A — File Organizer (move .jpg files)
  Module B — Email Extractor (regex-based)
  Module C — Web Scraper (fetch page title)
"""

import os
import re
import sys
import shutil
from pathlib import Path
from datetime import datetime

# ── Constants ──────────────────────────────────
OUTPUT_DIR: str = "output"

EMAIL_REGEX: re.Pattern = re.compile(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
)

TITLE_REGEX: re.Pattern = re.compile(
    r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL
)


# ══════════════════════════════════════════════
#  SHARED UTILITIES
# ══════════════════════════════════════════════

def clear_screen() -> None:
    """Clear the terminal screen (cross-platform)."""
    os.system("cls" if os.name == "nt" else "clear")


def print_banner(title: str) -> None:
    """Print a formatted section banner.

    Args:
        title: The banner text to display.
    """
    print(f"\n {'=' * 45}")
    print(f"  {title}")
    print(f" {'=' * 45}")


def log_success(message: str) -> None:
    """Print a success message."""
    print(f" [OK] {message}")


def log_warning(message: str) -> None:
    """Print a warning message."""
    print(f" [WARN] {message}")


def log_error(message: str) -> None:
    """Print an error message."""
    print(f" [ERROR] {message}")


def log_info(message: str) -> None:
    """Print an info message."""
    print(f" [INFO] {message}")


def save_results_to_txt(filename_prefix: str, content: str) -> str:
    """Save content to a timestamped text file in the output directory.

    Args:
        filename_prefix: Prefix for the output filename.
        content: The text content to save.

    Returns:
        The path to the saved file.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp: str = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath: str = os.path.join(OUTPUT_DIR, f"{filename_prefix}_{timestamp}.txt")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath


# ══════════════════════════════════════════════
#  MODULE A — File Organizer
# ══════════════════════════════════════════════

def get_jpg_files(source_dir: Path) -> list[Path]:
    """Scan a directory and return all .jpg/.jpeg file paths.

    Args:
        source_dir: The directory to scan.

    Returns:
        A list of Path objects for .jpg/.jpeg files.
    """
    extensions: set[str] = {".jpg", ".jpeg"}
    return [f for f in source_dir.iterdir() if f.is_file() and f.suffix.lower() in extensions]


def move_jpg_files(files: list[Path], target_dir: Path) -> tuple[int, int, int]:
    """Move .jpg files to the target directory.

    Args:
        files: List of file paths to move.
        target_dir: Destination directory.

    Returns:
        A tuple of (moved, skipped, errors) counts.
    """
    moved: int = 0
    skipped: int = 0
    errors: int = 0

    for file in files:
        target_path: Path = target_dir / file.name
        if target_path.exists():
            log_warning(f"Skipped (already exists): {file.name}")
            skipped += 1
            continue
        try:
            shutil.move(str(file), str(target_path))
            log_success(f"Moved: {file.name}")
            moved += 1
        except OSError as e:
            log_error(f"Failed to move {file.name}: {e}")
            errors += 1

    return moved, skipped, errors


def run_file_organizer() -> None:
    """Module A: Move .jpg/.jpeg files from source to target folder."""
    print_banner("MODULE A: File Organizer")

    source: str = input("\n Enter SOURCE directory path: ").strip()
    target: str = input(" Enter TARGET directory path: ").strip()

    source_dir: Path = Path(source)
    target_dir: Path = Path(target)

    if not source_dir.exists():
        log_error(f"Source folder '{source}' does not exist.")
        return

    target_dir.mkdir(parents=True, exist_ok=True)

    files: list[Path] = get_jpg_files(source_dir)

    if not files:
        log_info("No .jpg/.jpeg files found in source folder.")
        return

    log_info(f"Found {len(files)} .jpg/.jpeg file(s).\n")
    moved, skipped, errors = move_jpg_files(files, target_dir)

    print(f"\n --- Summary ---")
    print(f" Moved   : {moved}")
    print(f" Skipped : {skipped}")
    print(f" Errors  : {errors}")


# ══════════════════════════════════════════════
#  MODULE B — Email Extractor
# ══════════════════════════════════════════════

def extract_emails_from_file(filepath: Path) -> list[str]:
    """Extract unique email addresses from a text file using regex.

    Args:
        filepath: Path to the .txt file to scan.

    Returns:
        A sorted list of unique email addresses found.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content: str = f.read()

    emails: list[str] = re.findall(EMAIL_REGEX, content)
    unique_emails: list[str] = sorted(set(emails))
    return unique_emails


def run_email_extractor() -> None:
    """Module B: Extract email addresses from a text file."""
    print_banner("MODULE B: Email Extractor")

    file_path: str = input("\n Enter path to .txt file: ").strip()
    filepath: Path = Path(file_path)

    if not filepath.exists():
        log_error(f"File '{file_path}' not found.")
        return

    emails: list[str] = extract_emails_from_file(filepath)

    if not emails:
        log_info("No email addresses found.")
        return

    print(f"\n Found {len(emails)} unique email address(es):\n")
    for i, email in enumerate(emails, 1):
        print(f"     {i}. {email}")

    save: str = input("\n Save emails to file? (y/n): ").lower().strip()
    if save == "y":
        content: str = "\n".join(emails)
        saved_path: str = save_results_to_txt("extracted_emails", content)
        log_success(f"Saved to {saved_path}")


# ══════════════════════════════════════════════
#  MODULE C — Web Scraper
# ══════════════════════════════════════════════

def scrape_page_title(url: str) -> str | None:
    """Fetch a webpage and extract the <title> tag content.

    Uses requests with a custom User-Agent header and regex
    for title extraction.

    Args:
        url: The URL to fetch.

    Returns:
        The page title string, or None if not found.
    """
    try:
        import requests
    except ImportError:
        log_error("'requests' not installed. Run: pip install requests")
        return None

    headers: dict[str, str] = {
        "User-Agent": "Mozilla/5.0 (CodeAlpha-Automation/1.0)"
    }

    try:
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()
    except Exception as e:
        log_error(f"Could not connect: {e}")
        return None

    match = re.search(TITLE_REGEX, response.text)
    if match:
        return match.group(1).strip()
    return None


def run_web_scraper() -> None:
    """Module C: Fetch a webpage and extract its title."""
    print_banner("MODULE C: Web Scraper")

    url: str = input("\n Enter URL (e.g. https://www.python.org): ").strip()
    if not url:
        url = "https://www.python.org"

    log_info(f"Fetching: {url} ...")

    title: str | None = scrape_page_title(url)

    if title is None:
        log_info("No title found on this page.")
        return

    print(f"\n Page Title: \"{title}\"")

    save: str = input("\n Save title to file? (y/n): ").lower().strip()
    if save == "y":
        content: str = f"URL: {url}\nTitle: {title}\n"
        saved_path: str = save_results_to_txt("scraped_title", content)
        log_success(f"Saved to {saved_path}")


# ══════════════════════════════════════════════
#  MAIN MENU
# ══════════════════════════════════════════════

def main() -> None:
    """Entry point: displays the module selection menu."""
    print("\n TASK AUTOMATION SUITE")
    print(" CodeAlpha Python Internship — Task 3\n")

    while True:
        print("\n Choose a module:")
        print(" [1] File Organizer   — Move .jpg files to a folder")
        print(" [2] Email Extractor  — Extract emails from .txt")
        print(" [3] Web Scraper      — Scrape a webpage title")
        print(" [4] Exit")

        choice: str = input("\n Enter choice (1-4): ").strip()

        if choice == "1":
            run_file_organizer()
        elif choice == "2":
            run_email_extractor()
        elif choice == "3":
            run_web_scraper()
        elif choice == "4":
            print("\n Goodbye!")
            sys.exit(0)
        else:
            log_warning("Invalid choice. Enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n Interrupted. Goodbye!")
        sys.exit(0)
