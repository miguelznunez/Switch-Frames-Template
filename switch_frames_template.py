import tkinter as tk

def show_frame(frame):
    frame.tkraise()
    
window = tk.Tk()
window.state('zoomed')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0,column=0,sticky='nsew')
    
#==================Frame 1 code
frame1_title=  tk.Label(frame1, text='Page 1', font='times 35', bg='red')
frame1_title.pack(fill='both', expand=True)

frame1_btn = tk.Button(frame1, text='Enter',command=lambda:show_frame(frame2))
frame1_btn.pack(fill='x', ipady=15)

#==================Frame 2 code
frame2_title=  tk.Label(frame2, text='Page 2', font='times 35', bg='yellow')
frame2_title.pack(fill='both', expand=True)

frame2_btn = tk.Button(frame2, text='Enter',command=lambda:show_frame(frame3))
frame2_btn.pack(fill='x', ipady=15)

#==================Frame 3 code
frame3_title=  tk.Label(frame3, text='Page 3',font='times 35', bg='green')
frame3_title.pack(fill='both', expand=True)

frame3_btn = tk.Button(frame3, text='Enter',command=lambda:show_frame(frame1))
frame3_btn.pack(fill='x',ipady=15)

show_frame(frame1)

window.mainloop()
