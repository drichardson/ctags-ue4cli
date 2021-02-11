from .main import main

__PLUGIN_DESCRIPTOR__ = {
    'action': main,
    'description': 'Invokes ctags-ue4cli. Run `ue4 ctags` to '
                   'see the list of supported subcommands.',
    'args': '[SUBCOMMAND] [ARGS]'
}
