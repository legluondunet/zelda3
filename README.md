# Zelda3

A reimplementation of Zelda 3.

Our discord server is: https://discord.gg/AJJbJAzNNJ

## Fork version

The fork version is **0.1.0**, defined in [VERSION](VERSION). Releases identify both the version and the source commit, for example `Zelda3 0.1.0 (abcdef0)` with tag `v0.1.0-abcdef0`. Each game package includes `VERSION` and `BUILD-INFO.txt`. Archive names remain stable for launcher compatibility.

Increment `VERSION` for a new release: the last number for fixes, the middle number for new features, and the first number for major changes. This version refers to the legluondunet fork, not the upstream project or Z3-Launcher.

## About

This is a reverse engineered clone of Zelda 3 - A Link to the Past.

It's around 70-80kLOC of C code, and reimplements all parts of the original game. The game is playable from start to end.

You need a copy of the ROM to extract game resources (levels, images). Then once that's done, the ROM is no longer needed.

It uses the PPU and DSP implementation from [LakeSnes](https://github.com/elzo-d/LakeSnes), but with lots of speed optimizations.
Additionally, it can be configured to also run the original machine code side by side. Then the RAM state is compared after each frame, to verify that the C implementation is correct.

I got much assistance from spannerism's Zelda 3 JP disassembly and the other ones that documented loads of function names and variables.

## Additional features

A bunch of features have been added that are not supported by the original game. Some of them are: basic widescreen, shaders, 240 vertical res, hi-res mode7 map, MSU-1 audio, item switching, and over 30 bugfixes.

## Building

You must self-build for now. Steps for 64-bit Windows:<br>
(0) Download [Python](https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe) and install with "Add to PATH" checked<br>
(1) Click the green button "Code > Download ZIP" on the github page and extract the ZIP<br>
(2) Place your USA rom named zelda3.sfc in that folder<br>
(3) Download [TCC](https://github.com/FitzRoyX/tinycc/releases/download/tcc_20230519/tcc_20230519.zip) and [SDL2](https://github.com/libsdl-org/SDL/releases/download/release-2.28.2/SDL2-devel-2.28.2-VC.zip) and extract each ZIP into the "third-party" subfolder<br>
(4) Double-click "get_python_libs.bat" in the main dir.<br>
(5) Double-click "extract_assets.bat" in the main dir. This will create zelda3_assets.dat.<br>
(6) Double-click "run_with_tcc.bat" in the main dir. This will create zelda3.exe and run it.<br>
(7) Configure with zelda3.ini in a text editor like notepad++<br>

For other platforms and compilers, see: https://github.com/snesrev/zelda3/blob/main/BUILDING.md

## Usage and controls

The game supports snapshots. The joypad input history is also saved in the snapshot. It's thus possible to replay a playthrough in turbo mode to verify that the game behaves correctly.

The game is run with `./zelda3` and takes an optional path to the ROM-file, which will verify for each frame that the C code matches the original behavior.

| Button | Key         |
| ------ | ----------- |
| Up     | Up arrow    |
| Down   | Down arrow  |
| Left   | Left arrow  |
| Right  | Right arrow |
| Start  | Enter       |
| Select | Right shift |
| A      | X           |
| B      | Z           |
| X      | S           |
| Y      | A           |
| L      | C           |
| R      | V           |

The keys can be reconfigured in zelda3.ini

Additionally, the following commands are available:

| Key | Action                |
| --- | --------------------- |
| Tab | Turbo mode |
| W   | Fill health/magic     |
| Shift+W   | Fill rupees/bombs/arrows     |
| Ctrl+E | Reset            |
| P   | Pause (with dim)                |
| Shift+P   | Pause (without dim)                |
| Ctrl+Up   | Increase window size                |
| Ctrl+Down   | Decrease window size                |
| T   | Toggle replay turbo mode  |
| O   | Set dungeon key to 1  |
| K   | Clear all input history from the joypad log  |
| L   | Stop replaying a shapshot  |
| R   | Toggle between fast and slow renderer |
| F   | Display renderer performance |
| F1-F10 | Load snapshot      |
| Alt+Enter | Toggle Fullscreen     |
| Shift+F1-F10 | Save snapshot |
| Ctrl+F1-F10 | Replay the snapshot |
| 1-9 | Load a dungeons playthrough snapshot |
| Ctrl+1-9 | Run a dungeons playthrough in turbo mode |


## License

This fork as a whole and new original files by **legluondunet** are licensed under **GNU GPL version 3 or later** (`GPL-3.0-or-later`). See [LICENSE.txt](LICENSE.txt) for scope and [COPYING](COPYING) for the full license.

Existing upstream files retain their original licenses and authors, including **snesrev** and **elzo_d**. The original MIT and Opus notices are preserved verbatim in [LICENSE.upstream.txt](LICENSE.upstream.txt). Third-party components retain their own notices. Newly imported third-party files are not automatically relicensed.

## Public binaries and standalone ROM extractor

Successful builds of `master` publish Windows and Linux x86_64 ZIP packages in Releases, together with `SHA256SUMS`. Linux includes the SDL2-bundled AppImage; Windows includes runtime DLLs. Each package contains an `extractor/` directory with a standalone Python-based resource tool (Python, Pillow and PyYAML included). No ROM or Nintendo resources are bundled.

To generate assets from your own US ROM, run:

```sh
./extractor/zelda3-extractor --workspace /absolute/path/to/resources --extract-from-rom --rom /absolute/path/to/zelda3.sfc
```

On Windows, use `extractor\zelda3-extractor.exe`. Copy the resulting `resources/zelda3_assets.dat` next to the game executable or AppImage. Z3-Launcher handles these steps automatically. Keep the extractor directory intact; its `_internal` directory contains required runtime files. The extractor version is built from the same commit as the game.
