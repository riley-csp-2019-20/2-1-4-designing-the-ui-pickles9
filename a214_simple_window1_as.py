##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

# main window
root = tk.Tk()
frame_login = tk.Frame(root)
root.wm_geometry("250x250")
root.title("Authorization")
frame_login.grid(row = 0, column = 0, sticky = "news")
user_pass = ""

def login():
    frame_auth.tkraise()
    user_pass = ent_password.get()
    auth_password = tk.Label(frame_auth, text ="Dumb dumb, your password is " + user_pass + "?")
    auth_password.pack()

lbl_username = tk.Label(frame_login, text='Username:', padx = 25)
lbl_username.pack()
ent_username = tk.Entry(frame_login, bd=3, )
ent_username.pack(pady=5)
lbl_password = tk.Label(frame_login, text='Password:')
lbl_password.pack()
ent_password = tk.Entry(frame_login, bd=3, show = "A")
ent_password.pack(pady=5)
btn_login = tk.Button(frame_login, text = "Login", command = login)
btn_login.pack()

frame_auth = tk.Frame(root)
frame_auth.grid(row = 0, column = 0, sticky = "news")

frame_login.tkraise()

root.mainloop()