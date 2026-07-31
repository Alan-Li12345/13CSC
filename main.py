from tkinter import *
from tkinter import ttk, messagebox
from collections import deque

# a library for nz credits rank score
class Subject:
    def __init__(self, name, achieved, merit, excellence):
        self.name = name
        self.achieved = achieved
        self.merit = merit
        self.excellence = excellence

    def calculate_score(self):

        scores = []

        scores += [4] * self.excellence
        scores += [3] * self.merit
        scores += [2] * self.achieved

        scores.sort(reverse=True)

        return sum(scores[:80])


# program

class RankScoreApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Rank Score Calculator")

        self.subject_tree = {}

        self.stack = []

        self.queue = deque(maxlen=5)

        frm = ttk.Frame(root, padding=10)
        frm.grid()

        ttk.Label(frm, text="Subject").grid(row=0, column=0)
        ttk.Label(frm, text="Achieved").grid(row=1, column=0)
        ttk.Label(frm, text="Merit").grid(row=2, column=0)
        ttk.Label(frm, text="Excellence").grid(row=3, column=0)

        self.subject_entry = ttk.Entry(frm)
        self.subject_entry.grid(row=0, column=1)

        self.achieved_entry = ttk.Entry(frm)
        self.achieved_entry.grid(row=1, column=1)

        self.merit_entry = ttk.Entry(frm)
        self.merit_entry.grid(row=2, column=1)

        self.excellence_entry = ttk.Entry(frm)
        self.excellence_entry.grid(row=3, column=1)

        ttk.Button(frm, text="Add Subject",
                   command=self.add_subject).grid(row=4, column=0)

        ttk.Button(frm, text="Undo",
                   command=self.undo).grid(row=4, column=1)

        ttk.Button(frm, text="Calculate Rank Score",
                   command=self.calculate_total).grid(row=5, column=0)

        ttk.Button(frm, text="Exit",
                   command=root.destroy).grid(row=5, column=1)

        self.output = Text(frm, width=55, height=15)
        self.output.grid(row=6, column=0, columnspan=2)


    def add_subject(self):

        try:

            name = self.subject_entry.get()

            achieved = int(self.achieved_entry.get())
            merit = int(self.merit_entry.get())
            excellence = int(self.excellence_entry.get())

            subject = Subject(name, achieved, merit, excellence)

            self.subject_tree[name] = {
                "object": subject,
                "score": subject.calculate_score()
            }

            self.stack.append(name)

            self.queue.append(name)

            self.output.insert(
                END,
                f"Added {name} (Score: {subject.calculate_score()})\n"
            )

            self.clear_entries()

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")


    def undo(self):

        if len(self.stack) > 0:

            last = self.stack.pop()

            del self.subject_tree[last]

            self.output.insert(
                END,
                f"Removed {last}\n"
            )

        else:
            messagebox.showinfo("Undo", "Nothing to undo.")

# calculte total component
    def calculate_total(self):

        total = 0

        self.output.insert(END, "\n----- Subjects -----\n")

        for subject in self.subject_tree.values():

            score = subject["score"]

            total += score

            self.output.insert(
                END,
                f"{subject['object'].name}: {score}\n"
            )

        if total > 320:
            total = 320

        self.output.insert(
            END,
            f"\nFinal Rank Score = {total}/320\n"
        )

        self.output.insert(
            END,
            "\nRecent Subjects :\n"
        )

        for item in self.queue:
            self.output.insert(END, item + "\n")

        self.output.insert(
            END,
            "----------------------------\n\n"
        )

#clear entries component
    def clear_entries(self):

        self.subject_entry.delete(0, END)
        self.achieved_entry.delete(0, END)
        self.merit_entry.delete(0, END)
        self.excellence_entry.delete(0, END)


root = Tk()
app = RankScoreApp(root)
root.mainloop()