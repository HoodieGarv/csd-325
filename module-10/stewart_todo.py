"""
Stewart-ToDo | CSD-325 Module 10
Base code: Listing 2.2 "Our Scrolling To-Do" from Tkinter By Example (David Love)

Modifications applied on top of Listing 2.2:
  1. Window title changed to "Stewart-ToDo"
  2. Colour schemes updated to two complementary colors: gold and purple
  3. Delete trigger changed from left-click <Button-1> to right-click <Button-3>
  4. Default label updated to instruct the user how to delete (right-click)
  5. File -> Exit menu item added so the user can exit the program correctly
"""

import tkinter as tk
import tkinter.messagebox as msg


class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        # Guard against mutable default argument pitfall (see Listing 2.2 notes)
        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        # ------------------------------------------------------------------ #
        # Core canvas/frame/scrollbar structure — unchanged from Listing 2.2
        # ------------------------------------------------------------------ #
        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(
            self.tasks_canvas,
            orient="vertical",
            command=self.tasks_canvas.yview
        )
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        # ------------------------------------------------------------------ #
        # Modification 1: Window title changed to "Stewart-ToDo"
        # (Listing 2.2 used "To-Do App v2")
        # ------------------------------------------------------------------ #
        self.title("Stewart-ToDo")
        self.geometry("300x400")

        # Text input widget — unchanged from Listing 2.2
        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        # Pack order matches Listing 2.2 exactly
        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Draw the tasks_frame inside the canvas (Listing 2.2 technique)
        self.canvas_frame = self.tasks_canvas.create_window(
            (0, 0),
            window=self.tasks_frame,
            anchor="n"
        )

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # ------------------------------------------------------------------ #
        # Modification 4: Instructional label text tells user to RIGHT-CLICK
        # (Listing 2.2 used "--- Add Items Here ---" with no delete hint)
        # ------------------------------------------------------------------ #
        todo1 = tk.Label(
            self.tasks_frame,
            text="Items Added --- ** Right Click Item to Delete **",
            bg="lightgrey",
            fg="black",
            pady=10
        )

        # ------------------------------------------------------------------ #
        # Modification 3: Bind <Button-3> (right-click) instead of <Button-1>
        # (Listing 2.2 bound <Button-1> for deletion)
        # ------------------------------------------------------------------ #
        todo1.bind("<Button-3>", self.remove_task)

        self.tasks.append(todo1)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        # Standard bindings from Listing 2.2
        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        # ------------------------------------------------------------------ #
        # Modification 2: Complementary color scheme — gold and purple
        # (Listing 2.2 used lightgrey/black and grey/white)
        # Gold (#FFD700) and purple (#7B00D4) are opposite on the color wheel,
        # making them true complementary colors with strong visual contrast.
        # ------------------------------------------------------------------ #
        self.colour_schemes = [
            {"bg": "#FFD700", "fg": "#3a006f"},   # Gold background, dark purple text
            {"bg": "#7B00D4", "fg": "#FFD700"}    # Purple background, gold text
        ]

        # ------------------------------------------------------------------ #
        # Modification 5: File -> Exit menu item
        # A Menu bar is created with a single File cascade containing Exit.
        # master.destroy() cleanly shuts down all Tkinter resources and ends
        # the mainloop, which is preferable to quit() on some platforms.
        # ------------------------------------------------------------------ #
        menu_bar = tk.Menu(self, bg="lightgrey", fg="black")
        file_menu = tk.Menu(menu_bar, tearoff=0, bg="lightgrey", fg="black")
        file_menu.add_command(label="Exit", command=self.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu_bar)

    # ---------------------------------------------------------------------- #
    # add_task — identical logic to Listing 2.2, colour binding updated
    # ---------------------------------------------------------------------- #
    def add_task(self, event=None):
        """
        Reads the Text widget, creates a new Label for the task, styles it
        with the alternating complementary colour scheme, and binds right-click
        deletion to it before packing it into the canvas frame.
        """
        task_text = self.task_create.get(1.0, tk.END).strip()

        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)

            self.set_task_colour(len(self.tasks), new_task)

            # Modification 3: right-click binding on every new task label
            new_task.bind("<Button-3>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)

        self.task_create.delete(1.0, tk.END)

    # ---------------------------------------------------------------------- #
    # remove_task — same logic as Listing 2.2, fired by right-click now
    # ---------------------------------------------------------------------- #
    def remove_task(self, event):
        """
        Triggered by a right-click (Button-3) on a task Label.
        Asks the user to confirm, then removes the label and recolours
        remaining tasks to restore the alternating pattern.
        """
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        """Re-applies alternating colours after a deletion."""
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        """
        Uses divmod to determine even/odd position, then applies the
        corresponding colour dictionary from self.colour_schemes.
        This mirrors the Listing 2.2 pattern exactly.
        """
        _, task_style_choice = divmod(position, 2)
        my_scheme_choice = self.colour_schemes[task_style_choice]
        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

    # ---------------------------------------------------------------------- #
    # Canvas sizing and scroll methods — unchanged from Listing 2.2
    # ---------------------------------------------------------------------- #
    def on_frame_configure(self, event=None):
        """Updates the canvas scroll region whenever the window is resized."""
        self.tasks_canvas.configure(
            scrollregion=self.tasks_canvas.bbox("all")
        )

    def task_width(self, event):
        """
        Keeps task labels at full canvas width even after the window
        is resized horizontally.
        """
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def mouse_scroll(self, event):
        """
        Handles mouse-wheel scrolling on both Windows/OSX (delta)
        and Linux (Button-4 / Button-5 events).
        """
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1
            self.tasks_canvas.yview_scroll(move, "units")


# ------------------------------------------------------------------ #
# Entry point
# ------------------------------------------------------------------ #
if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()
