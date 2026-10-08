# SPDX-FileCopyrightText: 2026 legluondunet
# SPDX-License-Identifier: GPL-3.0-or-later

"""Create platform ZIPs with relative paths and Unix executable permissions."""
import pathlib
import sys
import zipfile

root = pathlib.Path(sys.argv[1])
with zipfile.ZipFile(sys.argv[2], 'w', zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(root.rglob('*')):
        if path.is_file():
            archive.write(path, path.relative_to(root).as_posix())
