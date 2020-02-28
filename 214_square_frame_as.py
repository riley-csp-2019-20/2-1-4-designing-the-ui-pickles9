import tkinter as tk

root = tk.Tk()
root.wm_geometry("400x400")
root.title("OG windows logo")

blue_frame = tk.Frame(root, bg = "blue", height = 200, width = 300)
blue_frame.grid(row = 0, column = 0, sticky = "news")

red_frame = tk.Frame(root, bg = "red", height = 200, width = 300)
red_frame.grid(row = 1, column = 0, sticky = "news")

green_frame = tk.Frame(root, bg = "green", height = 200, width = 100)
green_frame.grid(row = 0, column = 1, sticky = "news")

yellow_frame = tk.Frame(root, bg = "yellow", height = 200, width = 100)
yellow_frame.grid(row = 1, column = 1, sticky = "news")

root.mainloop()