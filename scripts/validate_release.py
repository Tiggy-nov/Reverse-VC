#!/usr/bin/env python3
"""Check self-contained skill resources and source-matched release archives."""

from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "reverse-vc-scaling", "customer-problem-stress-test", "venture-scale-assessment",
    "vc-gtm-stress-test", "vc-product-technology", "vc-market-opportunity",
    "vc-competition-defensibility", "vc-business-model", "vc-scalability",
    "vc-financial-model", "vc-category-creation", "vc-team-governance",
}


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def check_zip(path, expected):
    with ZipFile(path) as archive:
        require(archive.testzip() is None, f"Corrupt ZIP: {path.name}")
        require(len(archive.namelist()) == len(expected), f"Wrong archive entry count: {path.name}")
        require(set(archive.namelist()) == set(expected), f"Wrong archive manifest: {path.name}")
        for name, content in expected.items():
            require(archive.read(name) == content, f"Archive differs from source: {path.name}:{name}")


def main():
    folders = sorted(path.parent for path in (ROOT / "skills").glob("*/SKILL.md"))
    require({path.name for path in folders} == EXPECTED, "Unexpected skill collection")
    license_bytes = (ROOT / "LICENSE").read_bytes()
    shared = {}
    suite = {"LICENSE": license_bytes}
    bundle = {"LICENSE": license_bytes, "VC-SKILLS-CATALOG.md": (ROOT / "VC-SKILLS-CATALOG.md").read_bytes()}
    count = 0
    for folder in folders:
        entry = (folder / "SKILL.md").read_text()
        match = re.match(r"\A---\n(.*?)\n---\n", entry, re.S)
        require(match is not None, f"Missing frontmatter: {folder.name}")
        frontmatter = match.group(1)
        require(re.search(rf"(?m)^name: {re.escape(folder.name)}$", frontmatter), f"Name mismatch: {folder.name}")
        require(re.search(r"(?m)^description: .+", frontmatter), f"Missing description: {folder.name}")
        for name in ("company-calibration.md", "raise-calibration.md"):
            value = (folder / "references" / name).read_bytes()
            require(value == shared.setdefault(name, value), f"Shared calibration differs: {folder.name}/{name}")
        expected = {}
        for path in sorted(folder.rglob("*")):
            require(not path.is_symlink(), f"Symlink: {path}")
            if not path.is_file():
                continue
            require(path.suffix in {".md", ".yaml"}, f"Unexpected skill file: {path}")
            count += 1
            relative = f"{folder.name}/{path.relative_to(folder).as_posix()}"
            content = path.read_bytes()
            expected[relative] = content
            suite[relative] = content
            source = content.decode("utf-8")
            require("/Users/" not in source and "/private/tmp/" not in source, f"Local path leaked: {path}")
            if path.suffix == ".md":
                for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", source):
                    parsed = urlsplit(target.strip("<>"))
                    if parsed.scheme or not parsed.path:
                        continue
                    destination = (path.parent / unquote(parsed.path)).resolve()
                    require(destination == folder.resolve() or folder.resolve() in destination.parents, f"Reference escapes skill: {path}:{target}")
                    require(destination.exists(), f"Missing reference: {path}:{target}")
        expected[f"{folder.name}/LICENSE"] = license_bytes
        zip_path = ROOT / "downloads" / f"{folder.name}.zip"
        check_zip(zip_path, expected)
        bundle[zip_path.name] = zip_path.read_bytes()
    check_zip(ROOT / "downloads/vc-skills-claude-uploads.zip", bundle)
    check_zip(ROOT / "downloads/vc-stress-test-suite.zip", suite)
    require({p.name for p in (ROOT / "downloads").iterdir()} == {f"{name}.zip" for name in EXPECTED} | {"vc-skills-claude-uploads.zip", "vc-stress-test-suite.zip"}, "Unexpected download files")
    print(f"Validated 12 skills, {count} source files, contained resources and all 14 archives")


if __name__ == "__main__":
    main()
