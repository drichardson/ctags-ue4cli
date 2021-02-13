import os
import os.path
import shutil
import subprocess


def find_ctags():
    ctags = shutil.which('ctags')
    if ctags is None:
        raise 'ctags not found. Install Universal Ctags. ' \
              'https://github.com/universal-ctags/ctags'
    return ctags


def verbose(argv):
    return '--verbose' in argv


def ctags(tags, basedir, tagtype, argv):
    # ctags options:
    # https://docs.ctags.io/en/latest/man/ctags.1.html
    args = [
        find_ctags(),
        '-f', tags,
        '--languages=C,C++,C#',
        '--recurse',
        '--extras=+f',  # also index file names
        basedir
    ]

    if verbose(argv):
        print('running: {}'.format(' '.join(args)))

    p = subprocess.run(args)

    if p.returncode == 0:
        if verbose(argv):
            print(f'Done generating {tagtype} tags.')
    else:
        raise f'Error generating {tagtype} tags.'


def project(manager, argv):
    project_file = manager.getProjectDescriptor(os.getcwd())
    project_dir = os.path.dirname(project_file)
    tags = os.path.join(project_dir, 'tags')
    source = os.path.join(project_dir, 'Source')
    ctags(tags, source, 'project', argv)


def engine_tags(manager, argv):
    return os.path.join(manager.getEngineRoot(), 'tags')


def engine(manager, argv):
    source = os.path.join(manager.getEngineRoot(), 'Engine')
    ctags(engine_tags(manager, argv), source, 'engine', argv)


def update(manager, argv):
    tags = engine_tags(manager, argv)
    if not os.path.exists(tags):
        engine(manager, argv)
    else:
        if verbose(argv):
            print(f'Will not generate engine tags because {tags} exists.')

    project(manager, argv)


def get_engine_path(manager, argv):
    print(engine_tags(manager, argv))
