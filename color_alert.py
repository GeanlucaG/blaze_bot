import PySimpleGUI as sg

def red_alert():
    """ Add your new theme colors and settings. Open a popup with the color red. """
    my_new_theme = {'BACKGROUND': '#8B0000',
                    'TEXT': '#f4f4f4',
                    'INPUT': '#c7e78b',
                    'TEXT_INPUT': '#000000',
                    'SCROLL': '#c7e78b',
                    'BUTTON': ('white', '#C4302B'),
                    'PROGRESS': ('#01826B', '#D0D0D0'),
                    'BORDER': 1,
                    'SLIDER_DEPTH': 0,
                    'PROGRESS_DEPTH': 0}


    sg.theme_add_new('MyNewTheme', my_new_theme)
    sg.theme('MyNewTheme')
    sg.popup_no_buttons(' Bet on the Red. ', auto_close=True, auto_close_duration=10)


def black_alert():
    """ Add your new theme colors and settings. Open a popup with the color black. """
    my_new_theme = {'BACKGROUND': '#000',
                    'TEXT': '#f4f4f4',
                    'INPUT': '#c7e78b',
                    'TEXT_INPUT': '#000000',
                    'SCROLL': '#c7e78b',
                    'BUTTON': ('white', '#C4302B'),
                    'PROGRESS': ('#01826B', '#D0D0D0'),
                    'BORDER': 1,
                    'SLIDER_DEPTH': 0,
                    'PROGRESS_DEPTH': 0}

    sg.theme_add_new('MyNewTheme', my_new_theme)
    sg.theme('MyNewTheme')
    sg.popup_no_buttons('Bet on the Black.', auto_close=True, auto_close_duration=10)


def white_alert():
    """ Add your new theme colors and settings. Open a popup with the color white. """
    my_new_theme = {'BACKGROUND': '#fff',
                    'TEXT': '#000',
                    'INPUT': '#c7e78b',
                    'TEXT_INPUT': '#000000',
                    'SCROLL': '#c7e78b',
                    'BUTTON': ('white', '#C4302B'),
                    'PROGRESS': ('#01826B', '#D0D0D0'),
                    'BORDER': 1,
                    'SLIDER_DEPTH': 0,
                    'PROGRESS_DEPTH': 0}

    sg.theme_add_new('MyNewTheme', my_new_theme)
    sg.theme('MyNewTheme')
    sg.popup_no_buttons('Bet on the White.', auto_close=True, auto_close_duration=10)

