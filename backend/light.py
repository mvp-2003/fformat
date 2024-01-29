from math import e
import os

def addfile(entry_field):
    filepath = entry_field.get()
    entry_field.delete(0, 'end')
    return os.path.splitext(filepath)[1]