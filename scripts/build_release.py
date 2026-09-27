#!/usr/bin/env python3
"""Build deterministic Claude uploads from the public skill sources."""

from io import BytesIO
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]


def archive(entries):
    buffer = BytesIO()
    with ZipFile(buffer, "w", compression=ZIP_DEFLATED, compresslevel=9) as result:
        for name, content in sorted(entries):
            info = ZipInfo(name, date_time=(2026, 9, 27, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            result.writestr(info, content)
    return buffer.getvalue()


def main():
    folders = sorted(path.parent for path in (ROOT / "skills").glob("*/SKILL.md"))
    if len(folders) != 12:
        raise SystemExit(f"Expected 12 skills, found {len(folders)}")
    output = ROOT / "downloads"
    output.mkdir(exist_ok=True)
    license_bytes = (ROOT / "LICENSE").read_bytes()
    catalog = (ROOT / "VC-SKILLS-CATALOG.md").read_bytes()
    bundle = [("LICENSE", license_bytes), ("VC-SKILLS-CATALOG.md", catalog)]
    suite = [("LICENSE", license_bytes)]
    for folder in folders:
        entries = []
        for path in sorted(folder.rglob("*")):
            if path.is_symlink():
                raise SystemExit(f"Unexpected symlink: {path.relative_to(ROOT)}")
            if path.is_file():
                if path.suffix not in {".md", ".yaml"}:
                    raise SystemExit(f"Unexpected skill file: {path.relative_to(ROOT)}")
                entries.append((f"{folder.name}/{path.relative_to(folder).as_posix()}", path.read_bytes()))
        suite.extend(entries)
        entries.append((f"{folder.name}/LICENSE", license_bytes))
        content = archive(entries)
        name = f"{folder.name}.zip"
        (output / name).write_bytes(content)
        bundle.append((name, content))
    (output / "vc-skills-claude-uploads.zip").write_bytes(archive(bundle))
    (output / "vc-stress-test-suite.zip").write_bytes(archive(suite))
    print(f"Built {len(folders)} individual skill ZIPs and 2 collection ZIPs")


if __name__ == "__main__":
    main()
