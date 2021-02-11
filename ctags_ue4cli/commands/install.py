import shutil


def install(manager, argv):
    print('here')
    ctags = shutil.which('ctags')

    if ctags is None:
        raise "ctags not installed. Get it here: https://github.com/universal-ctags/ctags"

    print(f'ctags is installed at {ctags}')
