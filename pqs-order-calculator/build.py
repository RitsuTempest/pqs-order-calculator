"""Build automation for the PQS Order Calculator.

Stages: clean -> compile -> unit test -> package.
The build stops if compilation or unit testing fails.
"""

from __future__ import annotations

import compileall
import shutil
import subprocess
import sys
import zipapp
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BUILD_DIR = ROOT / "build"
DIST_DIR = ROOT / "dist"
STAGING_DIR = BUILD_DIR / "pqs_order_calculator"


def clean() -> None:
    print("[1/4] Cleaning previous build outputs...")

    for path in (BUILD_DIR, DIST_DIR, ROOT / ".pytest_cache"):
        if path.exists():
            shutil.rmtree(path)

    for cache in ROOT.rglob("__pycache__"):
        shutil.rmtree(cache)


def compile_source() -> None:
    print("[2/4] Compiling Python source files...")

    success = compileall.compile_dir(
        ROOT / "pqs_checkout",
        quiet=1,
        force=True,
    )

    if not success:
        raise SystemExit("Compilation failed.")


def run_tests() -> None:
    print("[3/4] Running five unit tests...")

    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q"],
        cwd=ROOT,
        check=False,
    )

    if result.returncode != 0:
        raise SystemExit("Unit tests failed.")

    print("All five unit tests passed.")


def package_application() -> Path:
    print("[4/4] Creating deployable package...")

    DIST_DIR.mkdir(parents=True, exist_ok=True)
    STAGING_DIR.mkdir(parents=True, exist_ok=True)

    shutil.copytree(
        ROOT / "pqs_checkout",
        STAGING_DIR / "pqs_checkout",
    )

    shutil.copy2(
        ROOT / "__main__.py",
        STAGING_DIR / "__main__.py",
    )

    artifact = DIST_DIR / "pqs_order_calculator.pyz"

    zipapp.create_archive(
        STAGING_DIR,
        target=artifact,
        interpreter="/usr/bin/env python3",
        compressed=True,
    )

    print(f"Deployable package created: {artifact}")
    return artifact


def main() -> None:
    clean()
    compile_source()
    run_tests()
    artifact = package_application()

    print("\nBuild completed successfully.")
    print(f"Run the package with: {sys.executable} {artifact}")


if __name__ == "__main__":
    main()
