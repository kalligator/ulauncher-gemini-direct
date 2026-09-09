#!/usr/bin/env python3
"""Audit and validate extension manifest.json, versions.json, and asset integrity."""

import json
import os
import re
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

def audit_manifest() -> int:
    errors = []
    warnings = []

    manifest_path = ROOT_DIR / "manifest.json"
    if not manifest_path.exists():
        print(f"[FAIL] manifest.json not found at {manifest_path}")
        return 1

    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)
    except Exception as e:
        print(f"[FAIL] manifest.json is invalid JSON: {e}")
        return 1

    # Check top-level required fields
    required_keys = ["required_api_version", "name", "description", "developer_name", "icon", "preferences"]
    for key in required_keys:
        if key not in manifest:
            errors.append(f"Missing required manifest field: '{key}'")

    # Verify icon file
    icon_rel = manifest.get("icon")
    if icon_rel:
        icon_path = ROOT_DIR / icon_rel
        if not icon_path.exists():
            errors.append(f"Referenced icon does not exist: {icon_rel}")

    # Check standard images
    for img in ["images/icon.png", "images/error.png", "images/warning.png", "images/gemini.png", "images/log.png"]:
        if not (ROOT_DIR / img).exists():
            warnings.append(f"Recommended asset missing: {img}")

    # Verify preferences
    prefs = manifest.get("preferences", [])
    seen_ids = set()

    for idx, pref in enumerate(prefs):
        pref_id = pref.get("id")
        if not pref_id:
            errors.append(f"Preference at index {idx} missing 'id'")
            continue

        if pref_id in seen_ids:
            errors.append(f"Duplicate preference id: '{pref_id}'")
        seen_ids.add(pref_id)

        pref_type = pref.get("type")
        default_val = pref.get("default_value")

        if pref_type == "select":
            options = pref.get("options", [])
            if not options:
                errors.append(f"Select preference '{pref_id}' has no options")
            else:
                option_values = {opt.get("value") for opt in options}
                if default_val not in option_values:
                    errors.append(
                        f"Select preference '{pref_id}' default_value '{default_val}' not in options: {option_values}"
                    )
        elif pref_type == "input":
            validation = pref.get("validation")
            if validation and validation.get("type") == "regex":
                pat = validation.get("pattern")
                if pat:
                    try:
                        re.compile(pat)
                    except re.error as e:
                        errors.append(f"Regex pattern in preference '{pref_id}' failed to compile: {e}")

    # Verify versions.json
    versions_path = ROOT_DIR / "versions.json"
    if versions_path.exists():
        try:
            with open(versions_path, "r", encoding="utf-8") as f:
                versions = json.load(f)
                if not isinstance(versions, list) or not versions:
                    errors.append("versions.json must be a non-empty list")
        except Exception as e:
            errors.append(f"versions.json is invalid JSON: {e}")
    else:
        warnings.append("versions.json not found")

    # Output results
    print("=== Manifest & Asset Audit Results ===")
    if warnings:
        for w in warnings:
            print(f"[WARN] {w}")
    if errors:
        for err in errors:
            print(f"[ERROR] {err}")
        print(f"\nAudit FAILED with {len(errors)} error(s).")
        return 1

    print(f"[PASS] manifest.json and versions.json are structurally sound ({len(prefs)} preferences checked).")
    return 0

if __name__ == "__main__":
    sys.exit(audit_manifest())
