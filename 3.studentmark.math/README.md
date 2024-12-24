# Student Mark OOP Project

This project is designed to manage student information, courses, and marks using object-oriented programming principles in Python. It includes functionality to round down student scores, calculate GPAs, and provides a user interface using the `curses` module.

## Project Structure

```
student.mark.oop.math.py
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── student.py
│   ├── course.py
│   ├── marks.py
│   └── ui.py
├── requirements.txt
└── README.md
```

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the application, execute the following command:

```bash
python src/main.py
```

## Features

- **Student Management**: Add, list, and manage student information.
- **Course Management**: Add, list, and manage course details.
- **Marks Management**: Input and manage student marks for courses.
- **GPA Calculation**: Calculate the average GPA for students using a weighted sum of credits and marks.
- **User Interface**: Interactive UI using the `curses` module for a better user experience.

## Dependencies

- numpy
- (any other necessary packages)

## Contributing

Feel free to submit issues or pull requests for improvements and bug fixes.