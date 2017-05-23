from distutils.core import setup
import py2exe

Mydata_files = [('files', [])]

setup(
    console=['renamer_input.py'],
    data_files = Mydata_files,
    options={
                "py2exe":{
                        "unbuffered": True,
                        "optimize": 2,
                        "excludes": ["email"]
                }
        }
)