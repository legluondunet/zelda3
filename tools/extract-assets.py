"""Standalone resource tool: Python, Pillow and YAML are bundled by PyInstaller.
No ROM or extracted Nintendo resources are included in the distribution.
"""
import argparse
import os
from pathlib import Path
import runpy
import shutil
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--workspace', required=True)
parser.add_argument('--check-language')
args, rest = parser.parse_known_args()
workspace = Path(args.workspace).resolve()
assets = workspace / 'assets'
assets.mkdir(parents=True, exist_ok=True)
(assets / 'sprites').mkdir(exist_ok=True)
source = Path(getattr(sys, '_MEIPASS', Path(__file__).resolve().parent.parent)) / 'assets'
for path in source.iterdir():
    if path.suffix in ('.py', '.bin'):
        shutil.copyfile(path, assets / path.name)
sys.path.insert(0, str(assets))
other_source = source.parent / 'other'
if other_source.is_dir():
    (workspace / 'other').mkdir(exist_ok=True)
    shutil.copyfile(other_source / '3x5_font.png', workspace / 'other/3x5_font.png')
if args.check_language:
    import util
    rom_arg = rest[rest.index('--rom') + 1]
    rom = util.load_rom(rom_arg, True)
    if rom.language != args.check_language:
        raise ValueError('ROM language mismatch: expected ' + args.check_language + ', got ' + str(rom.language))
sys.argv = [str(assets / 'restool.py'), *rest]
# restool writes generated data into workspace/zelda3_assets.dat.
runpy.run_path(str(assets / 'restool.py'), run_name='__main__')
