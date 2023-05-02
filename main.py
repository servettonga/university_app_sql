#!python3
# University Management System

from src.app import App


def main() -> None:
    app = App()
    while True:
        app.run()

if __name__ == '__main__':
    main()
