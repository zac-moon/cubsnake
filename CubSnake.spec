# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['CubSnake.py'],
    pathex=[],
    binaries=[],
    datas=[('imgs/player/player_UP.png', 'imgs/player'), ('imgs/player/player_DOWN.png', 'imgs/player'), ('imgs/player/player_LEFT.png', 'imgs/player'), ('imgs/player/player_RIGHT.png', 'imgs/player')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='CubSnake',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['imgs/icon.icns'],
)
app = BUNDLE(
    exe,
    name='CubSnake.app',
    icon='imgs/icon.icns',
    bundle_identifier=None,
)
