"""pkginfo - simple module to inspect installed Python packages and versions.

Usage:
- import pkginfo
- print(pkginfo.__version__)
- pkgs = pkginfo.get_installed_packages()
- pkginfo.main()

This module is intentionally small and has no external dependencies.
"""

from __future__ import annotations
import json
from typing import Dict, Optional

try:
    # Python 3.8+
    from importlib.metadata import distributions
except Exception:
    # Backport for older Python versions
    from importlib_metadata import distributions  # type: ignore

__version__ = "0.1.0"


def get_installed_packages() -> Dict[str, str]:
    """Return a dict of installed packages {name: version} sorted by name."""
    pkgs: Dict[str, str] = {}
    for dist in distributions():
        # metadata is usually mapping-like; fall back to dist.name if needed
        name = None
        try:
            name = dist.metadata.get("Name") or dist.metadata.get("name")
        except Exception:
            name = None
        if not name:
            name = getattr(dist, "name", None) or "UNKNOWN"
        pkgs[name] = dist.version

    # Return a stable, alphabetically sorted dictionary
    return dict(sorted(pkgs.items(), key=lambda kv: kv[0].lower()))


def format_packages(pkgs: Dict[str, str]) -> str:
    """Format packages for plain-text display as NAME==VERSION lines."""
    return "\n".join(f"{name}=={ver}" for name, ver in pkgs.items())


def main(json_out: bool = False, limit: Optional[int] = None, show_module_version: bool = True) -> None:
    """Print installed packages to stdout.

    Args:
        json_out: If True, print JSON instead of plain text
        limit: Optional number of packages to show (first N alphabetically)
        show_module_version: If True, print the pkginfo module version first
    """
    if show_module_version:
        print(f"pkginfo module version: {__version__}\n")

    pkgs = get_installed_packages()
    if limit is not None and isinstance(limit, int) and limit > 0:
        pkgs = dict(list(pkgs.items())[:limit])

    if json_out:
        print(json.dumps(pkgs, indent=2))
    else:
        print(format_packages(pkgs))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="List installed Python packages and versions.")
    parser.add_argument("--json", dest="json_out", action="store_true", help="Output JSON")
    parser.add_argument("--limit", type=int, help="Limit number of packages listed")
    parser.add_argument("--no-module-version", dest="module_version", action="store_false", help="Don't print the pkginfo module version")
    args = parser.parse_args()

    main(json_out=args.json_out, limit=args.limit, show_module_version=args.module_version)
