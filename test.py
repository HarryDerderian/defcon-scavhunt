import tkinter as tk
from tkinter import messagebox

begs = [
    "Hi, I'm an underfunded ransomware strain.\n"
    "Due to the rough tech job market, I can't afford proper encryption.\n"
    "Please delete an important file yourself and send me to a friend.\n\n"
    "Best regards,\nBrokeRansomware",
    "Are you sure?",
    "Pretty please?",
]

attempt = 0

def center_window(window, width=400, height=150):
    """Center a window on screen"""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    window.geometry(f"{width}x{height}+{x}+{y}")

def final_message():
    """Create a centered dialog with two OK buttons"""
    top = tk.Toplevel(root)
    top.title("Really?")
    
    tk.Label(top, text="Stop being a fucking dork...", 
            font=('Helvetica', 12), pady=20).pack()
    
    def close():
        top.destroy()
        root.destroy()
    
    btn_frame = tk.Frame(top)
    btn_frame.pack(pady=10)    
    ok_btn = tk.Button(btn_frame, text="OK", command=close, width=10)
    ok_btn.pack(side='left', padx=10)
    ok_btn2 = tk.Button(btn_frame, text="OK", command=close, width=10)
    ok_btn2.pack(side='left', padx=10)    
    center_window(top)
    top.resizable(False, False)
    top.grab_set()
    top.protocol("WM_DELETE_WINDOW", lambda: None)    
    ok_btn.focus_set()

def ask_nicely():
    global attempt
    
    if attempt < len(begs):
        text = begs[attempt]
        answer = messagebox.askyesno("Ransomware Alert!", text)

        if not answer:
            attempt += 1
            root.after(500, ask_nicely)
        else:
            root.destroy()
    else:
        final_message()

root = tk.Tk()
root.withdraw()

ask_nicely()
root.mainloop()