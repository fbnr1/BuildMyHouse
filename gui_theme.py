from dearpygui.dearpygui import *


def create_theme():

    with theme() as global_theme:

        with theme_component(mvAll):
            add_theme_style(mvStyleVar_ChildRounding, 2, category=mvThemeCat_Core)
            add_theme_style(mvStyleVar_FrameRounding, 2, category=mvThemeCat_Core)

            # grau hell (240, 228, 244)
            # grau dunkel
            add_theme_color(mvThemeCol_FrameBg, (254, 247, 255), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_Text, (0, 0, 0), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_WindowBg, (254, 247, 255), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_ChildBg, (254, 247, 255), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_Button, (240, 228, 244), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_MenuBarBg, (240, 228, 244), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_Tab,  (222,216,230), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_TabActive, (240, 228, 244), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_TabHovered, (240, 228, 244), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_Border, (240, 228, 244), category=mvThemeCat_Core)
            add_theme_color(mvThemeCol_PopupBg, (240, 228, 244), category=mvThemeCat_Core)

    return global_theme
