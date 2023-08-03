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

