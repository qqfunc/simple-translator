"""A simple desktop application for translation services."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from PySide6.QtCore import QLocale, Qt, QUrl
from PySide6.QtWebEngineCore import QWebEngineProfile
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

if TYPE_CHECKING:
    from PySide6.QtGui import QShowEvent

__version__ = "0.1.0"


class SimpleTranslator(QApplication):
    """A simple desktop application for translation services."""

    def __init__(self, argv: list[str]) -> None:
        """Initialize self."""
        super().__init__(argv)

        self.setApplicationName("SimpleTranslator")
        self.setApplicationVersion(__version__)

        self.window = MainWindow()
        self.window.show()


class MainWindow(QMainWindow):
    """A main window of the Simple Translator."""

    def __init__(
        self,
        parent: QWidget | None = None,
        flags: Qt.WindowType = Qt.WindowType.CustomizeWindowHint
        | Qt.WindowType.WindowCloseButtonHint
        | Qt.WindowType.WindowStaysOnTopHint,
    ) -> None:
        """Initialize self."""
        super().__init__(parent, flags)

        self.setGeometry(100, 100, 400, 600)

        webview = WebView(self)
        self.setCentralWidget(webview)


class WebView(QWebEngineView):
    """A web view for translation."""

    def __init__(self, parent: QWidget) -> None:
        """Initialize self."""
        super().__init__(parent)
        self.iconChanged.connect(parent.setWindowIcon)

    def showEvent(self, event: QShowEvent) -> None:  # noqa: N802
        """Widget show event."""
        self.setUrl(QUrl("https://translate.google.com/"))
        return super().showEvent(event)


if __name__ == "__main__":
    app = SimpleTranslator(sys.argv)

    locale = QLocale()
    if (profile := QWebEngineProfile.defaultProfile()) is not None:
        profile.setHttpAcceptLanguage(f"{locale.bcp47Name()},{locale.name()}")

    sys.exit(app.exec())
