import os
import os.path
import shutil
import subprocess

def find_ctags():
    ctags = shutil.which('ctags')
    if ctags is None:
        raise 'ctags not found. Install Universal Ctags. https://github.com/universal-ctags/ctags'
    return ctags

def ctags(tags, basedir, tagtype):
    print(f'Generating {tagtype} tags...')
    print(f'tags={tags} basedir={basedir} tagtype={tagtype}')

    p = subprocess.run([find_ctags(), '-f', tags, '--languages=C,C++,C#', '--recurse', basedir])

    if p.returncode == 0:
        print(f'Done generating {tagtype} tags.')
    else:
        raise f'Error generating {tagtype} tags.'


def project(manager, argv):
    project_file = manager.getProjectDescriptor(os.getcwd())
    project_dir = os.path.dirname(project_file)
    tags = os.path.join(project_dir, 'tags')
    engine = os.path.join(project_dir, 'Source')
    ctags(tags, engine, 'project')

def engine(manager, argv):
    tags = os.path.join(manager.getEngineRoot(), 'tags')
    engine = os.path.join(manager.getEngineRoot(), 'Engine')
    ctags(tags, engine, 'engine')

def update(manager, argv):

    engine_tags_filename = os.path.join(manager.getEngineRoot(), 'tags2')

    if not os.path.exists(engine_tags_filename):
        print(f'{engine_tags_filename} does not exists. Generating.')
    else:
        print(f'{engine_tags_filename} exists. Skipping engine tags generation. Use --force to generate anyway')
