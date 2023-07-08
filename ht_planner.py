import logging

import flet as ft


class Application:
    page: ft.Page

    def __init__(self, title: str, width: int = 640, height: int = 480):
        self._title = title
        self._width = width
        self._height = height

    def main(self, page: ft.Page):
        self._initialize_page(page)

        self.page.add(ft.Text("Hello World!"))

        self.page.update()

    def _initialize_page(self, page: ft.Page):
        self.page = page
        self.page.title = self._title
        self.page.window_max_width = self._width
        self.page.window_max_height = self._height


def main():
    logging.getLogger().setLevel(logging.DEBUG)
    application = Application("ht-planner")
    ft.app(target=application.main)
    # ft.app(target=application.main, view=ft.WEB_BROWSER)


if __name__ == "__main__":
    main()
