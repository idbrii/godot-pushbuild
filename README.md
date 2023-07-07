# godot-pushbuild
Simple script to create godot builds and push them to itch.io.

Pushes builds using [butler](https://itch.io/docs/butler/) and includes the git commit hash at the end of the verison number:
![itchio build version history](https://github.com/idbrii/godot-pushbuild/assets/43559/c873d23f-0381-48a8-9454-eed291afee6f)


# Setup

1. Copy the ci folder to the root of your godot project.
1. In Godot, [create one build](https://docs.godotengine.org/en/stable/tutorials/export/exporting_projects.html) for each desired platform.
    1. Name your windows build "win"
    1. Name your html5 build "web"
1. Add export_presets.cfg to source control so other people can skip the above step.
1. Modify the version.json file in your ci folder to use your desired major/minor version. pushbuild will use these values to build the final version number that includes your latest git commit hash.
1. Modify the "Configuration" section of pushbuild.py:
```
project = "seedjump"
itch_project = f"idbrii/{project}"
export_path = Path("C:/code/Builds/") / project
project_root = Path("C:/code/godot/") / project
```
1. Commit any local changes (since the latest commit is part of the version number).
1. Optional: Comment out unwanted builds at the bottom of pushbuild.py
1. Run pushbuild.py


# Requirements

See requirements.txt

* GitPython
* [butler](https://itch.io/docs/butler/) -- it's surprisingly easy to setup. Once you can run it from command-line, you're ready to push!
