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

root = Tk()
app = RankScoreApp(root)
root.mainloop()