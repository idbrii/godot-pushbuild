#! /usr/bin/env python

import json
import subprocess
from pathlib import Path

import git


def parse_and_build_version(version_path, repo_path):
    """Builds a version from a json and git repo.

    parse_and_build_version(Path, git.Repo) -> str
    """

    with version_path.open("r") as f:
        ver = json.load(f)
    repo = git.Repo(repo_path)
    short_sha = repo.git.rev_parse("HEAD", short=True)
    return f"v{ver['major']}.{ver['minor']}.{short_sha}"


itch_project = "idbrii/seedjump:web"
export_path = Path("C:/code/Builds/seedjump/")
project_root = Path("C:/code/godot/seedjump/")
project_path = project_root / "project.godot"
version_path = project_root / "ci/version.json"

version = parse_and_build_version(version_path, project_root)

print("Building web build...")
subprocess.check_call(
    [
        "godot",
        "--headless",
        "--export-release",
        "web",
        export_path / "index.html",
        project_path,
    ]
)
print("Uploading as version", itch_project, version)
subprocess.check_call(
    ["butler", "push", export_path, itch_project, "--userversion", version]
)
