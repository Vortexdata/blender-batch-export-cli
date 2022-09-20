<div id="top"></div>

<br />
<div align="center">
  <img src="images/logo.png" alt="Logo" width="120" height="120">
  <h3 align="center">B-BEC</h3>

  <p align="center">
    Batch export Blender files and objects contained therein.
    <br />
    <br />
    <a href="/issues/new?template=bug_report.md">Report Bug</a>
    ·
    <a href="/issues/new?template=feature_request.md">Request Feature</a>
  </p>
</div>



<details>
  <summary>Table of Contents</summary>
  <ol>
	<li><a href="#demo">Demo</a></li>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#installation">Known issues</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## Demo

<WIP>


## Requirements

* [Python3](https://www.python.org/downloads/)
* [Blender 3.2](https://www.blender.org/download/)


## Installation

* Make sure all requirements are met.
* Download the [latest release](https://github.com/Vortexdata/blender-batch-export-cli/releases/latest).
* Extract the `bbec.py` from archive.

## Usage

### Running the script

```bash
# Default installation
blender -b --python <path to 'bbec.py'> -- <B-BEC args>

# Flatpak version of Blender
flatpak run org.blender.Blender -b --python <absolute (!) path to 'bbec.py'> -- <B-BEC args (paths must be absolute!)>
```

> As the Flatpak version of Blender is running within a sandbox, Blender will be unable to find relative paths. Therefore, you must use absolute paths at all times.


### CLI Arguments

* **-f** / **--format**: Desired format of the exported objects (fbx, obj, x3d, gltf).
* **-s** / **--sourcedir**: Path to directory containing source `.blend` files.
* **-o** / **--outputdir**: Path to directory exported objects will be stored in.
* **-rl** / **--reset-location**: Each objects world location will be set to X=0 / Y=0 / Z=0, removing any world offset from the object export. This can be useful if exported objects are later re-imported in other programs (e.g. Unreal Engine, Unity, Maya, ...).

## Known issues

### BlenderGIS incompatibility

During testing, the [BlenderGIS](https://github.com/domlysz/BlenderGIS) addon caused Blender to exit unexpectedly, stopping the export process. Disable the addon if you wish to use this script.


## License

Distributed under the GNU General Public License v3.0. See `LICENSE.txt` for more information.


## Acknowledgments

Helpful resources and projects that helped bring this project to life:

* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [blender-batch-export-obj](https://github.com/mcvnh/blender-batch-export-obj)

