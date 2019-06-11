from tkinter import *
import dbUpdate_ui
import dbQuery_ui
import reservation_ui

def run():
    tk = Tk()
    tk.title("Main")

    db_update_button = Button(tk, text="Update Database", pady=5,  command=dbUpdate_ui.dbUpdate)
    db_update_button.grid(row=0, column=3, rowspan=1, padx=50, pady=20)

    db_Query_button = Button(tk, text="Query Database", pady=5,  command=dbQuery_ui.dbQuery)
    db_Query_button.grid(row=1, column=3, rowspan=1, padx=50, pady=20)

    reservation_button = Button(tk, text="Create & Modify Reservation", pady=5,  command=reservation_ui.ReservationUI)
    reservation_button.grid(row=2, column=3, rowspan=1, padx=50, pady=20)


    tk.mainloop()

if __name__ == "__main__":
    run()