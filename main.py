import tkinter as tk
import tkinter.ttk

screens = ["Screen 1", "Screen 2", "Screen 3", "Screen 4", "Screen 5", "Screen 6"]

movies = {"Horror": ["Hereditary", "Scream", "Shining", "Anabelle","The Grudge", "A Quiet Place"],
          "Sci Fi": ["Robocop", "Terminator", "Star Trek", "Interstellar", "Oppenheimer", "Arrival"],
          "Action": ["James Bond", "Mission Impossible", "John Wick", "Spider Man", "Aquaman", "Batman"],
          "Drama": ["Spotlight", "Irishman", "Joker"],
          "Comedy": ["Step Brothers", "Booksmart", "Horrible Bosses", "Superbad", "The Other Guys"],
          "Romance": ["The Fault in our Stars", "Pride And Prejudice", "The Notebook", "The Tourist", "Titanic", "Crazy Rich Asians"]}

times = ["10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30"]

seat_list = []
seat_selected = []

class Application(tk.Tk):

    def __int__(self):
        super().__init__()
        self.title("Movie Booking App")
        self.create_widgets()

    def update_movies(self, event=None):
        self.movie_combo["values"] = movies[self.genre_combo.get()]

    def create_widgets(self):
        header = tk.Label(self, text="Cinema Seat Booking", font="Arial 12 bold")
        header.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="w")
        tkinter.ttk.Separator(self, orient="horizontal").grid(row=1, column=0, columnspan=5, sticky="ew")
        day = tk.Frame(self)
        tk.Label(day, text="______").pack()
        tk.Label(day, text="Today", font="Arial 10 bold").pack()
        tk.Label(day, text="").pack()
        day.grid(row=2, column=0, padx=10)
        tk.Label(self, text="Genre: ").grid(row=2, column=1, padx=(10,0))
        self.genre_combo = tkinter.ttk.Combobox(self, width=15, values=list(movies.keys()), state="readonly")
        self.genre_combo.set("Select Genre")
        self.genre_combo.bind("<<ComboboxSelected>>", self.update_movies)
        self.genre_combo.grid(row=2, column=2)

        tk.Label(self, text="Movie: ").grid(row=2, column=3, padx=(10,0))
        self.movie_combo = tkinter.ttk.Combobox(self, width=15, state="readonly")
        self.movie_combo.bind("<<ComboboxSelected>>", self.create_time_buttons)
        self.movie_combo.set("Select Movie")
        self.movie_combo.grid(row=2, column=2, padx=(10,0))
        tkinter.ttk.Separator(self, orient="horizontal").grid(row=3, column=0, columnspan=5, sticky="ew")

    def create_time_buttons(self, event=None):
        tk.Label(self, text="Select Time Slot", font="Arial 11 bold underline").grid(row=4, column=2, columnspan=2, pady=5)
        time = tk.Frame(self)
        time.grid(row=5, column=0, columnspan=5)
        for i in range(14):
            tk.Button(time, text=times[i], command=self.seat_selection).grid(row=4+i//7, column=i%7)

    def seat_selection(self):
        window = tk.Toplevel()
        window.title("Select Your Seat")
        checkout_heading = tk.Label(window, text="Seat(s) Selection", font="Arial 12")
        checkout_heading.grid(row=0, column=0, columnspan=5, padx=10, pady=(10, 0), sticky="w")
        infer = tk.Frame(window)
        infer.grid(row=1, column=0)
        tk.Label(infer, text="BLUE = SELECTED", fg="blue").grid(row=0, column=0, padx=10)
        tk.Label(infer, text="GREEN = AVAILABLE", fg="green").grid(row=0, column=2, padx=10)
        tk.Label(infer, text="RED = BOOKED", fg="red").grid(row=0, column=1, padx=10)
        tkinter.ttk.Separator(window, orient="horizontal").grid(row=2, column=0, pady=(0, 5), sticky="ew")

        w = tk.canvas(window, width=500, height=15)
        w.create_rectangle(10, 0, 490, 10, fill="black")
        w.grid(row=3, column=0)
        tk.screen(window, text="SCREEN").grid(row=4, column=0, pady=(0, 10))
        seats = tk.Frame(window)
        seats.grid(row=5, column=0)
        seat_list.clear()
        seat_selected.clear()
        for i in range(4):
            temp=[]
            for j in range(15):
                button = tk.Button(seats, bd=2, bg="green", activebackground="forestgreen", command=lambda x=i, y=j: self.selected(x,y))
                temp.append(button)
                button.grid(row=i, column=j, padx=5, pady=5)
            seat_list.append(temp)
        tk.Button(window, text="Book Seats", bg="black", fg="white", command=self.book_seat).grid(row=6, column=0, pady=10)





app = Application()
app.mainloop()