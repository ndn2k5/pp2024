import curses

def display_menu(stdscr, options):
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    for idx, option in enumerate(options):
        x = width // 2 - len(option) // 2
        y = height // 2 - len(options) // 2 + idx
        if idx == 0:  # Highlight the first option
            stdscr.addstr(y, x, option, curses.A_BOLD)
        else:
            stdscr.addstr(y, x, option)
    stdscr.refresh()
    stdscr.getch()

def show_students(stdscr, students):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    stdscr.addstr(0, 0, "Student List", curses.A_BOLD)
    for idx, student in enumerate(students):
        stdscr.addstr(idx + 1, 0, f"{student.student_id}: {student.name}")
    stdscr.refresh()