"""
The main program should use functions from music_reports and display modules
"""

import file_handling
import music_reports
import display

def inputs(inputs_list, prompt='select an option: '):
    answers_list = []
    for item in inputs_list:
        pass


def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """

    menu = ['Display albums list',
            'Delete album',
            'Add album',
            'Get albums by genre',
            'Display oldest album',
            'Display oldest album in selected genre'
            'Show genre statistics',
            'Display longest album',
            'Display total albums lenght'
            ]

    albums = file_handling.import_data()

    while True:
        display.print_command_result('Welcome in albums database app')
        display.print_command_result('Select an option')
        display.print_program_menu(menu)









if __name__ == '__main__':
    main()
