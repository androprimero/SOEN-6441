#!/usr/bin/python3
import tkinter
from tkinter import *
from Coaster import Coasters
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from FileManager import FileManager
"""
Filename: UserInterfaceModule.py
Author: Alejandro Bernal
version: 1.0
Description:
Module that has UserMainInterface class, to create the user interface.
"""


class UserMainInterface(tkinter.Tk):

    def __init__(self, master=None):
        """
        Create the user interface
        :param master:
        """
        super().__init__(master)
        self.coasters = Coasters()
        self.coasters.calculate_alpha()
        self.data = tkinter.Frame(self)
        self.draws = tkinter.Frame(self)
        self.buttons = tkinter.Frame(self)
        self.draw = tkinter.Canvas(self.draws, cursor="plus",
                                   height="450", width="670", bg="white")
        self.description = tkinter.Label(self.data, text="Radius")
        self.length = tkinter.Label(self.data, text="length =")
        self.length_value = StringVar()
        self.result = tkinter.Label(self.data,
                                    textvariable=self.length_value)
        self.action = tkinter.Button(self.buttons, text="Compute",
                                     command=self.compute_action)
        self.save = tkinter.Button(self.buttons, text="Save",
                                   command=self.save_file)
        self.quit = tkinter.Button(self.buttons, text="Quit",
                                   command=self.destroy)
        self.field = tkinter.Entry(self.data)
        self.add_components()

    def add_components(self):
        """
        Add components to the main window
        :return:
        """
        self.geometry("700x550")
        self.draw.pack(side="top")
        self.description.pack(side="left")
        self.field.pack(side="left")
        self.length.pack(side="left")
        self.result.pack(side="left")
        self.quit.pack(side="right")
        self.save.pack(side="right")
        self.action.pack(side="right")
        self.draws.pack(side="top")
        self.data.pack(side="top")
        self.buttons.pack(side="top")

    def start(self):
        """
        Starts loop of execution
        :return:
        """
        self.mainloop()

    def compute_action(self):
        """
        Compute the length setting the values to coaster
        :return:
        """
        try:
            self.draw.delete("all")
            radius = float(self.field.get())
            if not self.coasters.set_radius(radius):
                messagebox.askretrycancel("Invalid Radius",
                                          'Please Write a valid Radius'
                                          ' greater than 0.0')
            else:
                self.length_value.set(str(self.coasters.calculate_length()))
                self.draw_circles()
        except ValueError:
            messagebox.askretrycancel("Invalid Radius", 'Please type a number')

    def save_file(self):
        """
        Saves the exit file
        :return:
        """
        try:
            file_types = [('Text files', '*.txt'), ('All Files', '*')]
            file_info = asksaveasfilename(title="Save file",
                                          defaultextension=".txt",
                                          filetypes=file_types)
            self.file = FileManager(file_info)
            if self.coasters.get_radius() != 0.0:
                self.file.save(self.coasters.__str__())
            else:
                self.compute_action()
            self.file.close()
        except FileNotFoundError:
            messagebox.showinfo("Invalid file name",
                                "Please write a valid name")

    def create_circle(self, x, y, radius, **option_arguments):
        return self.draw.create_oval(x - radius, y - radius,
                                     x + radius, y + radius,
                                     **option_arguments)

    def draw_circles(self):
        xi = self.validate_radius()
        xc = xi + 10
        yc = xi + 10
        self.create_circle(xc, yc, xi)
        self.create_circle(xc, yc, 1, fill="black")
        x = xc + (self.coasters.get_length()*(xi/self.coasters.get_radius()))
        self.create_circle(x, yc, xi)
        self.create_circle(x, yc, 1, fill="black")
        self.draw.create_line(xc, yc, x, yc)

    def validate_radius(self):
        """
        Function that change the radius to draw,
        warning it does not change the radius
        to compute the length
        :return: the radius that can be drawn
                 in the canvas of the interface.
        """
        x = self.coasters.get_radius()
        while (x < 100) or (x > 200):
            if x < 100:
                x = x + 10
            else:
                x = x - 10
        return x
