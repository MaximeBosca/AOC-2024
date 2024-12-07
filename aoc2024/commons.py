from pathlib import Path


def load_data(day_number: str, prefix: str = '') -> str:
    pathname = Path(__file__).parent.parent / 'data' / f"{prefix}input_{day_number:02}.txt"
    return pathname.read_text()
