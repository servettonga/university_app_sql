#!python3
# University app

from src.app import App


def main():
    app = App()
    while True:
        app.clear()
        print(app.header)
        for choice in app.choices:
            print(f"{choice}: {app.choices[choice]}")

        choice = int(input("\nEnter your choice: "))

        print(f"\n{choice}: {app.choices[choice]}")

        try:
            match choice:
                case 1:
                    app.create_lecturer()
                case 2:
                    app.create_student()
                case 3:
                    app.create_course()
                case 4:
                    app.add_student_to_course()
                case 5:
                    app.add_grade()
                case 6:
                    app.update_lecturer()
                case 7:
                    app.update_student()
                case 8:
                    app.update_course()
                case 9:
                    app.update_grade()
                case 10:
                    app.print_lecturer()
                case 11:
                    app.print_student()
                case 12:
                    app.print_course()
                case 0:
                    exit(0)
                case _:
                    print("Invalid choice!")
        except ValueError:
            print("Invalid input!")
            app.clear(1)


if __name__ == '__main__':
    main()
    exit(0)
