import os

def addfile(entry_field):
    filepath = entry_field.get()
    upload_file(filepath)
    entry_field.delete(0, 'end')
    return os.path.splitext(filepath)[1]

def upload_file(path):
    pass
    #return path