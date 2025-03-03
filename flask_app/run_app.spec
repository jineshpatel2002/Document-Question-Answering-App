# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

package_names = [
    'chromadb'
]

# Initialize empty lists for datas, binaries, and hiddenimports
datas = [('templates', 'templates')]
binaries = []
hiddenimports = ['scipy._lib.array_api_compat.numpy.fft', 'scipy.special._special_ufuncs', 'scipy.sparse._sputils', 'scipy._lib._array_api', 'scipy._lib.array_api_compat.numpy', 'scipy.spatial._geometric_slerp', 'scipy.spatial.distance', 'scipy.sparse._base', 'scipy.stats._stats_py', 'scipy.sparse', 'scipy.spatial', 'scipy.special', 'scipy.stats', 'scipy._lib']

# Iterate over each package name and collect the information
for package in package_names[0:2]:
    tmp_ret = collect_all(package)
    datas += tmp_ret[0]
    binaries += tmp_ret[1]
    hiddenimports += tmp_ret[2]

a = Analysis(
    ['run_app.py'],
    pathex=['.'],
    binaries= binaries,
    datas= datas,
    hiddenimports= hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='run_app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
