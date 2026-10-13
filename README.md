# Zelda3 — fork for Z3-Launcher

This repository is a fork of [snesrev/zelda3](https://github.com/snesrev/zelda3), a C reimplementation of **The Legend of Zelda: A Link to the Past**.

**The sole purpose of this fork is to provide the executables and resource tools used by [Z3-Launcher](https://github.com/legluondunet/Z3-Launcher).** It lets the launcher download prebuilt game binaries and prepare game resources without requiring users to compile the project.

Using Z3-Launcher is recommended. The program can also be used directly; instructions are provided below.

No ROM or extracted game resources are included in the downloads. To play, you must provide your own US ROM and extract its resources.

## Differences from the upstream project

| Addition or change in this fork | Purpose |
|---|---|
| GitHub Actions workflow | Automatically build Linux and Windows x86_64 executables and a Linux AppImage. |
| ZIP packages published in Releases | Provide downloads that Z3-Launcher can use directly. |
| Bundled runtime libraries | Include Windows DLLs and bundle SDL2 in the AppImage. |
| Standalone extractor in `extractor/` | Generate resources without separately installing Python, Pillow or PyYAML. |
| `tools/extract-assets.py` | Prepare a workspace and invoke the upstream resource tool; also provide an optional ROM language check. |
| `tools/package-release.py` | Create ZIP archives with relative paths and preserve Unix executable permissions. |
| Fix in `assets/tables.py` | Avoid a Python warning about escape sequences. |
| Fork version and build information | Identify releases by version and commit; provide `VERSION`, `BUILD-INFO.txt` and `SHA256SUMS`. |
| Licensing for new files | Apply GPL-3.0-or-later to legluondunet's additions while preserving upstream licenses and credits. |

The game engine and its features — widescreen, shaders, enhanced Mode 7, MSU-1 audio and gameplay options — come from the upstream project. They are not additions made by this fork.

## Version and downloads

The current fork version is **0.1.0**, defined in [VERSION](VERSION). It is independent of the Z3-Launcher version.

Releases use names such as `Zelda3 0.1.0 (abcdef0)` and tags such as `v0.1.0-abcdef0`. The commit identifies the exact source used for the build.

Downloads: [Releases](https://github.com/legluondunet/zelda3/releases).

| Platform | Public package |
|---|---|
| Linux x86_64 | `zelda3-linux-x86_64.zip`, containing `zelda3.AppImage` and the standalone extractor. |
| Windows x86_64 | `zelda3-windows-x86_64.zip`, containing `zelda3.exe`, runtime DLLs and the standalone extractor. |

The workflow also provides a regular Linux executable in its [GitHub Actions artifacts](https://github.com/legluondunet/zelda3/actions), under the name `zelda3-linux-x86_64`. This build requires SDL2 to be installed on the system.

## Using the program without Z3-Launcher

### 1. Download and extract

Download the ZIP for your platform from Releases. Extract **all of its contents** into a directory where you have write permission.

Keep the entire `extractor/` directory, including its `_internal/` subdirectory. The extractor needs these files to run.

Prepare your US ROM of **A Link to the Past**. The examples use the filename `zelda3.sfc`; adjust its path for your installation.

### 2. Generate resources on Linux

Open a terminal in the extracted package directory and run:

```bash
chmod +x ./extractor/zelda3-extractor ./zelda3.AppImage

./extractor/zelda3-extractor \
  --workspace "$PWD/resources" \
  --extract-from-rom \
  --rom "/path/to/zelda3.sfc"

cp ./resources/zelda3_assets.dat ./zelda3_assets.dat
```

Use an absolute ROM path: the tool changes directories during extraction. Keep paths quoted to handle spaces.

Once `zelda3_assets.dat` has been generated and copied next to the AppImage, run:

```bash
./zelda3.AppImage
```

If your system reports a FUSE error, try:

```bash
./zelda3.AppImage --appimage-extract-and-run
```

For the regular Linux executable downloaded from Actions artifacts, also place `zelda3_assets.dat` and `zelda3.ini` in its directory, install SDL2 using your distribution's package manager, then run `./zelda3` from that directory.

### 3. Generate resources on Windows

Open **PowerShell** in the extracted package directory and run:

```powershell
.\extractor\zelda3-extractor.exe --workspace "$PWD\resources" --extract-from-rom --rom "C:\path\to\zelda3.sfc"

Copy-Item .\resources\zelda3_assets.dat .\zelda3_assets.dat

.\zelda3.exe
```

Adjust the absolute ROM path. Keep the supplied DLLs next to `zelda3.exe`.

After this setup, you can also start the game by double-clicking `zelda3.exe`.

### 4. Configure and play

Use `zelda3.ini` to configure controls, rendering, fullscreen mode, audio and gameplay options. Close the game before editing this file.

The default keys are intended for a QWERTY keyboard:

| Action | Key |
|---|---|
| Movement | Arrow keys |
| Start | Enter |
| Select | Right Shift |
| A / B / X / Y buttons | X / Z / S / A |
| L / R buttons | C / V |
| Fullscreen | Alt + Enter |
| Pause | P |
| Save a state | Shift + F1 through F10 |
| Load a state | F1 through F10 |

For an AZERTY keyboard, enable the corresponding `Controls` line in the `[KeyMap]` section of `zelda3.ini` and disable the other `Controls` line.

For `.glsl` or `.glslp` shaders, set `OutputMethod = OpenGL` and enter the shader path in `Shader`, in the `[Graphics]` section.

The program needs `zelda3_assets.dat` every time it starts. The ROM is no longer needed to play once the resources have been generated. Keep game data and configuration in a writable directory; the AppImage uses the directory containing the AppImage.

### Troubleshooting

- **Missing resources**: check that `zelda3_assets.dat` is next to the executable or AppImage. When using the regular executable, launch the game from that directory.
- **Extraction fails**: check the absolute ROM path, compatibility with the expected US ROM, and the presence of `extractor/_internal/`.
- **Permission denied on Linux**: check executable permissions and write access to the directory.
- **Missing DLL on Windows**: extract the complete ZIP again and keep the supplied DLLs with the game.

## Source and credits

The game reimplementation comes from [snesrev/zelda3](https://github.com/snesrev/zelda3). It uses the PPU and DSP implementations from [LakeSnes](https://github.com/elzo-d/LakeSnes), alongside documentation and disassembly work credited by the upstream project.

Source code and build instructions remain available in this repository, including [BUILDING.md](BUILDING.md). This fork's additions mainly concern automated builds, distribution and integration with Z3-Launcher.

## Licenses

- **The fork as a whole and new original files by legluondunet**: GNU GPL version 3 or later, identifier `GPL-3.0-or-later`. Copyright © 2026 legluondunet. See [LICENSE.txt](LICENSE.txt) for scope and [COPYING](COPYING) for the complete license text.
- **Files inherited from upstream**: their original licenses and authors are preserved, including when modified in this fork. The MIT license and credits for **snesrev** and **elzo_d** are preserved in [LICENSE.upstream.txt](LICENSE.upstream.txt).
- **Opus and other third-party components**: these retain their own licenses and copyright notices. See the [Opus license](third_party/opus-1.3.1-stripped/COPYING) and notices in `third_party/`. Libraries bundled in the packages remain subject to their respective licenses.
- **ROMs and extracted game resources**: these are not covered by this repository's software licenses and are not distributed with the packages.
