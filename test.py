import tkinter as tk
from tkinter import messagebox

begs = [
    "Hi, I'm an underfunded ransomware strain.\n"
    "Due to the rough tech job market, I can't afford proper encryption.\n"
    "Please delete an important file yourself and send me to a friend.\n\n"
    "Best regards,\nBrokeRansomware",
    "Will you do it? please?",
    "Pretty please?",
]

attempt = 0

def center_window(window, width=600, height=150):
    """Center a window on screen"""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    window.geometry(f"{width}x{height}+{x}+{y}")

def show_bitcoin_tip():
    """Show the Bitcoin tipping address"""
    top = tk.Toplevel(root)
    top.title("Tips Appreciated")
    
    message = ("If you decide to be cool,\n"
               "any Bitcoin tips are appreciated:\n\n"
               "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh")
    
    main_frame = tk.Frame(top)
    main_frame.pack(padx=20, pady=20)
    
    tk.Label(main_frame, text=message, 
            font=('Courier', 11),
            justify='center').pack(pady=(0, 20))
    
    def close_all():
        top.destroy()
        root.destroy()  # This ensures complete shutdown
    
    btn = tk.Button(main_frame, text="Close", 
                   command=close_all,  # Changed to close_all
                   width=12,
                   padx=10,
                   relief=tk.RAISED)
    btn.pack()
    
    center_window(top, 850, 220)
    top.resizable(False, False)
    top.grab_set()
    top.protocol("WM_DELETE_WINDOW", lambda: None)
    btn.focus_set()

def final_message():
    """Final message dialog"""
    top = tk.Toplevel(root)
    top.title("Really?")
    
    content_frame = tk.Frame(top)
    content_frame.pack(padx=20, pady=20)
    
    tk.Label(content_frame, text="Stop being a fucking dork...", 
            font=('Helvetica', 12)).pack(pady=(0, 20))
    
    def close():
        top.destroy()
        show_bitcoin_tip()
    
    btn_frame = tk.Frame(content_frame)
    btn_frame.pack()
    
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
        answer = messagebox.askyesno("Ransomware", text)

        if not answer:
            attempt += 1
            root.after(500, ask_nicely)
        else:
            show_bitcoin_tip()
    else:
        final_message()

root = tk.Tk()
root.withdraw()

ask_nicely()
root.mainloop()
