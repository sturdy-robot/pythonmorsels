import os
from pathlib import Path
from typing import Union
from tempfile import mkdtemp
import shutil


class cd:
    def __init__(self, current: Union[Path, str] = None):
        self.current = current
        self.previous = None
        self.tmp_dir = None

    def enter(self):
        return self.__enter__()

    def exit(self, *args):
        return self.__exit__(*args)
    
    def __enter__(self):
        self.previous = os.getcwd()
        
        if self.current is None:
            self.tmp_dir = os.path.realpath(mkdtemp())
            self.current = self.tmp_dir
        
        os.chdir(self.current)
        return self

    def __exit__(self, *args):
        os.chdir(self.previous)
        if self.tmp_dir is not None:
            self.current = None
            shutil.rmtree(self.tmp_dir)
