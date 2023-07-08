import logging

import ZODB
import ZODB.FileStorage
import flet as ft
import transaction


class Application:
    page: ft.Page

    def __init__(self, title: str, width: int = 640, height: int = 480):
        self._title = title
        self._width = width
        self._height = height

        self._db = ZODB.DB(None)
        connection = self._db.open()
        root = connection.root
        root.string = "Hello my World!"
        transaction.commit()
        connection.close()

    def main(self, page: ft.Page):
        self._initialize_page(page)

        connection = self._db.open()
        root = connection.root
        self.page.add(ft.Text(root.string))
        connection.close()

        self.page.update()

    def _initialize_page(self, page: ft.Page):
        self.page = page
        self.page.title = self._title
        self.page.window_max_width = self._width
        self.page.window_max_height = self._height


def main():
    logging.getLogger().setLevel(logging.DEBUG)
    application = Application("ht-planner")
    # ft.app(target=application.main)
    ft.app(target=application.main, view=ft.WEB_BROWSER)


if __name__ == "__main__":
    main()
