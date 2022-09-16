<div id="top"></div>

<br />
<div align="center">
  <img src="images/logo.png" alt="Logo" width="120" height="120">
  <h3 align="center">B-BEC</h3>

  <p align="center">
    Batch export multiple blender files and objects contained therein.
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
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## Demo

https://user-images.githubusercontent.com/40140669/190535567-fbd23168-2e8f-4572-be35-c9810170e90b.mp4


## Requirements

This script should run on most Linux distros. You'll need to have access to Bash (duh).



## Installation

* Download the latest release zip.
* Extract the archive contents into a folder.
* Allow execution of scripts (eg. with `chmod 700 fcomb-interactive.sh`) 


## Usage

### Running the script
```bash
# Run the script
./recursive_export.sh <filename> <export directory> <export format> <executable source>
```

### CLI Arguments

- Filename: Filter for filenames to include (eg. *.blend to export all, "myfile.blend" to only export "myfile.blend")
- Export Directory: Directory meshes are exported to.
- Export Format: Container type of exports (eg. FBX, OBJ, etc.).
- Executable source: If unspecified, script will attempt to run blender with `blender` command. If you are using Blender's Flatpak version, this will not work. Instead, write `flatpak` at the end of the command.


## License

Distributed under the GNU General Public License v3.0. See `LICENSE.txt` for more information.



## Acknowledgments

Helpful resources and projects that helped bring this project to life:

* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [blender-batch-export-obj](https://github.com/mcvnh/blender-batch-export-obj)

