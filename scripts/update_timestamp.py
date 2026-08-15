import re
from datetime import datetime, timezone

README_PATH = "README.md"


def main():
    with open(README_PATH, "r") as f:
        content = f.read()

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    content = re.sub(
        r"<!--STATS-TIME-->.*?<!--END-->",
        f"<!--STATS-TIME-->{timestamp}<!--END-->",
        content
    )

    with open(README_PATH, "w") as f:
        f.write(content)


if __name__ == "__main__":
    main()