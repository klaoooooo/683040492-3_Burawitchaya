#!/usr/bin/env python3
"""Wrapper script to run the local `pkginfo` module.

Example usage:
  python show_versions.py
  python show_versions.py --json --limit 20
"""
from __future__ import annotations
import argparse
import pkginfo


def parse_args():
    parser = argparse.ArgumentParser(description="Show installed Python packages and versions using local pkginfo module")
    parser.add_argument("--json", dest="json_out", action="store_true", help="Output JSON")
    parser.add_argument("--limit", type=int, help="Limit number of packages displayed")
    parser.add_argument("--no-module-version", dest="module_version", action="store_false", help="Don't print the pkginfo module version")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    pkginfo.main(json_out=args.json_out, limit=args.limit, show_module_version=args.module_version)


if __name__ == "__main__":
    main()
