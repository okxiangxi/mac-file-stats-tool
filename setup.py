from setuptools import setup

APP = ['count_folder_files.py']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter', 'os'],
    'plist': {
        'LSUIElement': False,  # 关键：不隐藏App的UI，允许弹窗
        'CFBundleName': '文件统计工具',
        'CFBundleDisplayName': '文件统计工具',
    }
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)