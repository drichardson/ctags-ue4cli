from .commands import ctags
import sys


def main(manager, args):

    # Our supported subcommands
    SUBCOMMANDS = {
        'update': {
            'function': ctags.update,
            'description': 'Generate project tags and generate UE4 engine tags not yet built.'
        },
        'engine': {
            'function': ctags.engine,
            'description': 'Generate engine tags.'
        },
        'project': {
            'function': ctags.project,
            'description': 'Generate project tags.'
        },
        'update': {
            'function': ctags.update,
            'description': 'Generate project tags and generate engine tags if it does not exist.'
        }
    }

    # Determine if a subcommand has been specified
    if len(args) > 0:

        # Verify that the specified subcommand is valid
        subcommand = args[0]
        if subcommand not in SUBCOMMANDS:
            print('Error: unrecognised subcommand "{}".'.format(
                subcommand), file=sys.stderr)
            return

        # Invoke the subcommand
        SUBCOMMANDS[subcommand]['function'](manager, args[1:])

    else:

        # Determine the longest subcommand name so we can format our list in nice columns
        longestName = max([len(c) for c in SUBCOMMANDS])
        minSpaces = 6

        # Print our list of subcommands
        print('Subcommands:')
        for subcommand in SUBCOMMANDS:
            whitespace = ' ' * ((longestName + minSpaces) - len(subcommand))
            print('  {}{}{}'.format(
                subcommand,
                whitespace,
                SUBCOMMANDS[subcommand]['description']
            ))
        print('\nUse --verbose to get extra output.')
