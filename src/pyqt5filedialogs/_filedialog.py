import typing
from pathlib import Path
from PySide2.QtWidgets import QApplication, QDialog, QFileDialog

HOME_DIR = Path.home()


class FileDialog(QDialog):

    def __init__(self):
        super().__init__()

    def get_open_directory(
        self,
        caption: typing.Optional[str] = "Open Directory",
        dir: typing.Optional[Path] = HOME_DIR,
        **kwargs: typing.Any
    ) -> Path:
        """
        Get an existing directory path selected by the user.
        """
        options = QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        filename = QFileDialog.getExistingDirectory(self, caption=caption, dir=str(dir), options=options, **kwargs)
        return Path(filename)

    def get_open_filepath(
        self,
        caption: typing.Optional[str] = "Open File",
        dir: typing.Optional[Path] = HOME_DIR,
        **kwargs: typing.Any
    ) -> Path:
        """
        Get an existing filepath selected by the user.
        """
        filename, _ = QFileDialog.getOpenFileName(self, caption=caption, dir=str(dir), **kwargs)
        return Path(filename)
    
    def get_open_filepaths(
        self,
        caption: typing.Optional[str] = "Open Files",
        dir: typing.Optional[Path] = HOME_DIR,
        **kwargs: typing.Any
    ) -> typing.List[Path]:
        """
        Get existing filepaths selected by the user.
        """
        filenames, _ = QFileDialog.getOpenFileName(self, caption=caption, dir=str(dir), **kwargs)
        return [Path(filename) for filename in filenames]

    def get_save_filepath(
        self,
        caption: typing.Optional[str] = "Select File",
        dir: typing.Optional[Path] = HOME_DIR,
        **kwargs: typing.Any
    ) -> Path:
        """
        Get a filepath selected by the user.
        """
        filename, _ = QFileDialog.getSaveFileName(self, caption=caption, dir=str(dir), **kwargs)
        return Path(filename)


def get_open_directory(
    app: typing.Optional[QApplication] = None,
    caption: typing.Optional[str] = "Open Directory",
    dir: typing.Optional[Path] = HOME_DIR,
    **kwargs: typing.Any
) -> Path:
    """
    Get an existing directory path selected by the user.
    """
    app = app if app is not None else QApplication()
    dialog = FileDialog()
    directory = dialog.get_open_directory(caption=caption, dir=dir, **kwargs)
    del dialog
    del app
    return directory


def get_open_filepath(
    app: typing.Optional[QApplication] = None,
    caption: typing.Optional[str] = "Open File",
    dir: typing.Optional[Path] = HOME_DIR,
    **kwargs: typing.Any
) -> Path:
    """
    Get an existing filepath selected by the user.
    """
    app = app if app is not None else QApplication()
    dialog = FileDialog()
    filepath = dialog.get_open_filepath(caption=caption, dir=dir, **kwargs)
    del dialog
    del app
    return filepath


def get_open_filepaths(
    app: typing.Optional[QApplication] = None,
    caption: typing.Optional[str] = "Open Files",
    dir: typing.Optional[Path] = HOME_DIR,
    **kwargs: typing.Any
) -> typing.List[Path]:
    """
    Get existing filepaths selected by the user.
    """
    app = app if app is not None else QApplication()
    dialog = FileDialog()
    filepaths = dialog.get_open_filepaths(caption=caption, dir=dir, **kwargs)
    del dialog
    del app
    return filepaths


def get_save_filepath(
    app: typing.Optional[QApplication] = None,
    caption: typing.Optional[str] = "Select File",
    dir: typing.Optional[Path] = HOME_DIR,
    **kwargs: typing.Any
) -> Path:
    """
    Get a filepath selected by the user.
    """
    app = app if app is not None else QApplication()
    dialog = FileDialog()
    filepath = dialog.get_save_filepath(caption=caption, dir=dir, **kwargs)
    del dialog
    del app
    return filepath