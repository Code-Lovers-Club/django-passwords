import subprocess


def test():
    """Run all unittests."""
    subprocess.run(["python", "-u", "-m", "unittest"], check=False)  # noqa: S603 S607
