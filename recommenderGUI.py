import tkinter as tk
# Building GUI

# Take a instance of gui window
window = tk.Tk()
# Set title of window
window.title('Movie Recommender')
# Position the window in center of screen 
window.geometry('+{}+{}'.format(int(window.winfo_screenwidth()/8),int(window.winfo_screenheight()/2 - window.winfo_reqheight() - 50)))
# Add a frame for adding widgets
frame = tk.Frame(window)
frame.pack()

# Adding input box 
tk.Label(frame, text='SELECT OR WRITE YOUR FAVOURITE MOVIE ').grid(row=0)
inputBox = tk.Entry(frame, width=40)
inputBox.grid(row=0, column=1)

# Adding Placeholder
inputBox.insert(0, '(PRESS ENTER TO SUBMIT)')
inputBox.configure(state=tk.DISABLED)

# For removing text
def onClick(event):
    inputBox.configure(state=tk.NORMAL)
    inputBox.delete(0,tk.END)
    # Detach event
    inputBox.unbind('<Button-1>', onClickId)
# Attach on-click event
onClickId = inputBox.bind('<Button-1>', onClick)

# Adding output box
tk.Label(frame, text='Available Movies').grid(row=2)
tk.Label(frame, text='Recommended Movies').grid(row=2, column=1)

# Available list
availMovies = tk.Frame(frame)
availMovies.grid(row=3)
scrollBarAvailList = tk.Scrollbar(availMovies)
scrollBarAvailList.pack(side=tk.RIGHT)
availList = tk.Listbox(availMovies, yscrollcommand=scrollBarAvailList.set, height=20, width=60)
availList.pack(side=tk.LEFT)

# Output list
recMovies = tk.Frame(frame, height=300)
recMovies.grid(row=3, column=1)
scrollBarOutputList = tk.Scrollbar(recMovies)
scrollBarOutputList.pack(side=tk.RIGHT)
outputList = tk.Listbox(recMovies, yscrollcommand=scrollBarOutputList.set, height=20, width=60)
outputList.pack(side=tk.LEFT)

# Menu
menu = tk.Menu(window)
window.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='Options', menu=filemenu)


