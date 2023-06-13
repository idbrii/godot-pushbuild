#! /usr/bin/env python

import subprocess

export_path = "C:/code/Builds/seedjump/"
project_path = "C:/code/godot/seedjump/project.godot"
subprocess.check_call(
    [
        "godot",
        "--headless",
        "--export-release",
        "web",
        export_path + "index.html",
        project_path,
    ]
)
subprocess.check_call(
    ["butler", "push", export_path, "idbrii/seedjump:web", "--userversion", "v0.2"]
)

