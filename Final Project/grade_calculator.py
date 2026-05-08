# Name: William Wade
# Course: Graphical User Interface
# Final Project: Student Grade Calculator

import tkinter as tk
from tkinter import messagebox


class StudentGradeCalculator:
    """
    A desktop GUI application that calculates a student's average grade
    and corresponding letter grade from numeric inputs.
    """

    # ------------------------------------------------------------------ #
    #  Colour palette and font definitions                                 #
    # ------------------------------------------------------------------ #
    BG_COLOR        = "#f0f4f8"
    FRAME_BG        = "#ffffff"
    ACCENT_GREEN    = "#27ae60"
    ACCENT_BLUE     = "#2980b9"
    ACCENT_RED      = "#e74c3c"
    ACCENT_TEAL     = "#1abc9c"
    TEXT_DARK       = "#2c3e50"
    TEXT_MUTED      = "#7f8c8d"
    STATUS_BG       = "#dce3ea"

    FONT_TITLE      = ("Helvetica", 20, "bold")
    FONT_SUBTITLE   = ("Helvetica", 10)
    FONT_LABEL      = ("Helvetica", 11)
    FONT_LABEL_BOLD = ("Helvetica", 11, "bold")
    FONT_ENTRY      = ("Helvetica", 11)
    FONT_BUTTON     = ("Helvetica", 10, "bold")
    FONT_RESULT     = ("Helvetica", 13, "bold")
    FONT_STATUS     = ("Helvetica", 9)

    # ------------------------------------------------------------------ #
    #  Initialiser                                                         #
    # ------------------------------------------------------------------ #
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Student Grade Calculator")
        self.root.resizable(False, False)
        self.root.configure(bg=self.BG_COLOR)

        # Track dynamically created grade-entry widgets and their frames
        self.grade_entries: list[tk.Entry] = []
        self.grade_row_frames: list[tk.Frame] = []

        self._build_ui()
        self._center_window()
        self._add_initial_grade_rows()

    # ------------------------------------------------------------------ #
    #  UI Construction                                                     #
    # ------------------------------------------------------------------ #
    def _build_ui(self) -> None:
        """Build the complete UI layout."""
        self._build_header()
        self._build_grades_section()
        self._build_button_row()
        self._build_results_section()
        self._build_status_bar()

    def _build_header(self) -> None:
        """Create the title and subtitle labels at the top."""
        header_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        header_frame.pack(fill="x", padx=30, pady=(20, 5))

        title_label = tk.Label(
            header_frame,
            text="Student Grade Calculator",
            font=self.FONT_TITLE,
            bg=self.BG_COLOR,
            fg=self.TEXT_DARK,
        )
        title_label.pack(anchor="center")

        subtitle_label = tk.Label(
            header_frame,
            text="Enter numeric grades (0 – 100) and press Calculate",
            font=self.FONT_SUBTITLE,
            bg=self.BG_COLOR,
            fg=self.TEXT_MUTED,
        )
        subtitle_label.pack(anchor="center", pady=(4, 0))

    def _build_grades_section(self) -> None:
        """Create the labelled frame that holds all grade entry rows."""
        grades_outer_frame = tk.LabelFrame(
            self.root,
            text="  Grades  ",
            font=self.FONT_LABEL_BOLD,
            bg=self.BG_COLOR,
            fg=self.TEXT_DARK,
            padx=15,
            pady=10,
            relief="groove",
            bd=2,
        )
        grades_outer_frame.pack(fill="x", padx=30, pady=(15, 5))

        # Inner container – grade rows will be packed inside this
        self.grades_container = tk.Frame(grades_outer_frame, bg=self.BG_COLOR)
        self.grades_container.pack(fill="x")

    def _build_button_row(self) -> None:
        """Create the three action buttons: Add Grade, Calculate, Clear All."""
        button_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        button_frame.pack(pady=12)

        # Button 1 – Add Grade: dynamically appends a new entry field
        self.add_grade_button = tk.Button(
            button_frame,
            text="+ Add Grade",
            command=self._add_grade_row,
            font=self.FONT_BUTTON,
            bg=self.ACCENT_TEAL,
            fg="white",
            activebackground="#16a085",
            activeforeground="white",
            relief="flat",
            padx=16,
            pady=7,
            cursor="hand2",
        )
        self.add_grade_button.grid(row=0, column=0, padx=8)

        # Button 2 – Calculate: compute average and letter grade
        self.calculate_button = tk.Button(
            button_frame,
            text="Calculate",
            command=self._calculate_grades,
            font=self.FONT_BUTTON,
            bg=self.ACCENT_GREEN,
            fg="white",
            activebackground="#1e8449",
            activeforeground="white",
            relief="flat",
            padx=16,
            pady=7,
            cursor="hand2",
        )
        self.calculate_button.grid(row=0, column=1, padx=8)

        # Button 3 – Clear All: reset every entry field and the results panel
        self.clear_button = tk.Button(
            button_frame,
            text="Clear All",
            command=self._clear_all,
            font=self.FONT_BUTTON,
            bg=self.ACCENT_RED,
            fg="white",
            activebackground="#c0392b",
            activeforeground="white",
            relief="flat",
            padx=16,
            pady=7,
            cursor="hand2",
        )
        self.clear_button.grid(row=0, column=2, padx=8)

    def _build_results_section(self) -> None:
        """Create the labelled results panel."""
        results_frame = tk.LabelFrame(
            self.root,
            text="  Results  ",
            font=self.FONT_LABEL_BOLD,
            bg=self.BG_COLOR,
            fg=self.TEXT_DARK,
            padx=20,
            pady=12,
            relief="groove",
            bd=2,
        )
        results_frame.pack(fill="x", padx=30, pady=(5, 20))

        # Helper that adds a two-column result row
        def _result_row(frame, label_text, row_idx, fg_color):
            title = tk.Label(
                frame,
                text=label_text,
                font=self.FONT_LABEL,
                bg=self.BG_COLOR,
                fg=self.TEXT_DARK,
                anchor="w",
                width=18,
            )
            title.grid(row=row_idx, column=0, sticky="w", pady=5)

            value = tk.Label(
                frame,
                text="—",
                font=self.FONT_RESULT,
                bg=self.BG_COLOR,
                fg=fg_color,
                anchor="w",
                width=14,
            )
            value.grid(row=row_idx, column=1, sticky="w", padx=(10, 0), pady=5)
            return value

        self.average_result_label  = _result_row(results_frame, "Average Grade:",   0, self.ACCENT_GREEN)
        self.letter_grade_label    = _result_row(results_frame, "Letter Grade:",     1, self.ACCENT_BLUE)
        self.grade_count_label     = _result_row(results_frame, "Grades Counted:",   2, self.TEXT_MUTED)

    def _build_status_bar(self) -> None:
        """Create a slim status bar at the very bottom of the window."""
        self.status_label = tk.Label(
            self.root,
            text="Enter at least 3 grades, then click Calculate.",
            font=self.FONT_STATUS,
            bg=self.STATUS_BG,
            fg="#555555",
            anchor="w",
            padx=10,
        )
        self.status_label.pack(fill="x", side="bottom", ipady=4)

    # ------------------------------------------------------------------ #
    #  Dynamic Grade Rows                                                  #
    # ------------------------------------------------------------------ #
    def _add_initial_grade_rows(self) -> None:
        """Populate the grades section with the required 3 starting rows."""
        for _ in range(3):
            self._add_grade_row()

    def _add_grade_row(self) -> None:
        """Append a new numbered grade entry row to the grades container."""
        row_index = len(self.grade_entries)

        row_frame = tk.Frame(self.grades_container, bg=self.BG_COLOR)
        row_frame.pack(fill="x", pady=3)

        # Numbered label (e.g. "Grade 1:")
        row_label = tk.Label(
            row_frame,
            text=f"Grade {row_index + 1}:",
            font=self.FONT_LABEL,
            bg=self.BG_COLOR,
            fg=self.TEXT_DARK,
            width=9,
            anchor="e",
        )
        row_label.pack(side="left", padx=(0, 8))

        # Entry field – pressing Enter also triggers calculation
        grade_entry = tk.Entry(
            row_frame,
            font=self.FONT_ENTRY,
            width=12,
            relief="solid",
            bd=1,
        )
        grade_entry.pack(side="left")
        grade_entry.bind("<Return>", lambda _event: self._calculate_grades())

        self.grade_entries.append(grade_entry)
        self.grade_row_frames.append(row_frame)

        self._set_status(
            f"Grade {row_index + 1} field added. "
            "Enter a value between 0 and 100."
        )

    # ------------------------------------------------------------------ #
    #  Validation                                                          #
    # ------------------------------------------------------------------ #
    def _get_valid_grades(self) -> list[float] | None:
        """
        Parse every grade entry field.
        Returns a list of valid float grades, or None if any input is invalid.
        Blank fields are silently skipped (only non-blank bad values trigger an error).
        """
        valid_grades: list[float] = []

        for index, entry in enumerate(self.grade_entries):
            raw_value = entry.get().strip()

            # Skip completely blank fields
            if raw_value == "":
                continue

            # Reject non-numeric input
            try:
                grade = float(raw_value)
            except ValueError:
                messagebox.showerror(
                    "Invalid Input",
                    f'Grade {index + 1} contains a non-numeric value: "{raw_value}"\n\n'
                    "Please enter a number between 0 and 100.",
                )
                entry.focus_set()
                return None  # Abort so the user can fix the error

            # Reject out-of-range values
            if grade < 0 or grade > 100:
                messagebox.showerror(
                    "Value Out of Range",
                    f"Grade {index + 1} must be between 0 and 100.\n\n"
                    f"You entered: {grade}",
                )
                entry.focus_set()
                return None  # Abort so the user can fix the error

            valid_grades.append(grade)

        return valid_grades

    # ------------------------------------------------------------------ #
    #  Grade Logic                                                         #
    # ------------------------------------------------------------------ #
    @staticmethod
    def _get_letter_grade(average: float) -> str:
        """Map a numeric average to a standard letter grade (A – F)."""
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    # ------------------------------------------------------------------ #
    #  Button Handlers                                                     #
    # ------------------------------------------------------------------ #
    def _calculate_grades(self) -> None:
        """
        Validate inputs, compute the average and letter grade,
        and update the results panel.
        """
        valid_grades = self._get_valid_grades()

        # Validation already showed an error; just return
        if valid_grades is None:
            return

        # Require at least 3 valid grades
        if len(valid_grades) < 3:
            messagebox.showwarning(
                "Not Enough Grades",
                f"At least 3 grades are required to calculate.\n\n"
                f"Valid grades entered so far: {len(valid_grades)}",
            )
            self._set_status("Please enter at least 3 valid grades.")
            return

        # Compute results
        average = sum(valid_grades) / len(valid_grades)
        letter  = self._get_letter_grade(average)

        # Update result labels
        self.average_result_label.config(text=f"{average:.2f}")
        self.letter_grade_label.config(text=letter)
        self.grade_count_label.config(text=str(len(valid_grades)))

        self._set_status(
            f"Calculated from {len(valid_grades)} grade(s)  |  "
            f"Average: {average:.2f}  |  Letter grade: {letter}"
        )

    def _clear_all(self) -> None:
        """Clear every grade entry field and reset the results panel."""
        for entry in self.grade_entries:
            entry.delete(0, tk.END)

        self.average_result_label.config(text="—")
        self.letter_grade_label.config(text="—")
        self.grade_count_label.config(text="—")

        self._set_status("All fields cleared. Enter your grades and click Calculate.")

        # Return focus to the first entry for convenience
        if self.grade_entries:
            self.grade_entries[0].focus_set()

    # ------------------------------------------------------------------ #
    #  Helpers                                                             #
    # ------------------------------------------------------------------ #
    def _set_status(self, message: str) -> None:
        """Update the bottom status bar with a new message."""
        self.status_label.config(text=f"  {message}")

    def _center_window(self) -> None:
        """Centre the window on the screen after the UI has been built."""
        self.root.update_idletasks()
        screen_width  = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width  = self.root.winfo_reqwidth()
        window_height = self.root.winfo_reqheight()
        x_offset = (screen_width  - window_width)  // 2
        y_offset = (screen_height - window_height) // 2
        self.root.geometry(f"+{x_offset}+{y_offset}")


# ---------------------------------------------------------------------- #
#  Entry Point                                                             #
# ---------------------------------------------------------------------- #
def main() -> None:
    """Create the Tk root window and start the application."""
    root = tk.Tk()
    StudentGradeCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
