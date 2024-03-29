from gui.language_learning_gui import LanguageLearningGui


def initialize_gui() -> None:
    gui = LanguageLearningGui.initialize_gui()
    gui.run()


if __name__ == '__main__':
    initialize_gui()
