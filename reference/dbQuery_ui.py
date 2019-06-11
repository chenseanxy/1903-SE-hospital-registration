from tkinter import *
import backend
import reservation_backend

class dbQuery(object):
    def __init__(self):

        self.tk = Tk()
        self.tk.title("DBQuery")
        
        self.modeText = Label(self.tk, text="Table to query", anchor="e", width=15)
        self.modeText.grid(row=1, column=0)

        self.modes = ["Flight", "Hotel", "Bus", "Reservation", "Customer"]
        self.mode = StringVar(self.tk)
        self.mode.set(self.modes[0])
        self.modeOption = OptionMenu(self.tk, self.mode, *self.modes, command=self.updateModifyFrame)
        self.modeOption.configure(pady=5, width=20)
        self.modeOption.grid(row=1, column=1)

        self.queryButton = Button(self.tk, text="Query!", width=20, command=self.updateDataFrame)
        self.queryButton.grid(row=1, column=2)

        self.createModifyFrame()
        self.createDataFrame([])

        self.tk.mainloop()

    def createModifyFrame(self):
        mode = self.mode.get()
        self.modifyFrame = Frame(self.tk)
        self.modifyFrame.grid(row=2, column=0, columnspan=3)
        if(mode == "Reservation"):
            self.custIDEntryText = Label(self.modifyFrame, text="Customer ID", anchor="e")
            self.custIDEntryText.grid(row=0, column=0)
            self.custIDEntry = Entry(self.modifyFrame, width=40)
            self.custIDEntry.grid(row=0, column=1)
            self.custIDQueryButton = Button(self.modifyFrame, text="Query by Customer ID", command=self.custIDQuery)
            self.custIDQueryButton.grid(row=0, column=2)
            
    def updateModifyFrame(self, *args):
        ## Mode Change
        self.modifyFrame.destroy()
        self.createModifyFrame()
        self.dataFrame.destroy()
        self.createDataFrame([])

    def createDataFrame(self, objList):
        mode = self.mode.get()
        self.dataFrame = Frame(self.tk)
        self.dataFrame.grid(row=3, column=0, columnspan=3)
        
        rows = []
        row = 0

        for obj in objList:
            if(mode == "Customer"):
                thisRow = []
                thisRow.append(Label(self.dataFrame, text=obj.custID, anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.custName, anchor="w"))
            
            if(mode == "Reservation"):
                thisRow = []
                thisRow.append(Label(self.dataFrame, text=obj.resvNum, anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.custID, anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.resvType, anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.resvKey, anchor="w"))
            
            if(mode == "Flight"):
                thisRow = []
                thisRow.append(Label(self.dataFrame, text=obj.flightNum, anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.price, anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.numSeats, anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.numAvail, anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.occupancy(), anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.fromCity, anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.arivCity, anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.param, anchor="w"))
            
            if(mode == "Hotel"):
                thisRow = []
                thisRow.append(Label(self.dataFrame, text=obj.hotelNum, anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.location, anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.price, anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.numRooms, anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.numAvail, anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.occupancy(), anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.param, anchor="w"))
            
            if(mode == "Bus"):
                thisRow = []
                thisRow.append(Label(self.dataFrame, text=obj.busNum, anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.location, anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.price, anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.numSeats, anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.numAvail, anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.occupancy(), anchor="w"))
                thisRow.append(Label(self.dataFrame, text=obj.param, anchor="w"))

            col = 0
            for widget in thisRow:
                widget.grid(row = row, column = col, padx=3, pady=1)
                col+=1
            row+=1

            for column in range(col):
                self.dataFrame.grid_columnconfigure(column, weight = 1)        

    def custIDQuery(self):
        ## Click Cust-ID Query
        self.dataFrame.destroy()
        self.createDataFrame(reservation_backend.queryReservation(self.custIDEntry.get()))

    def updateDataFrame(self, *args):
        ## Click "Query"
        self.dataFrame.destroy()
        self.createDataFrame(backend.queryTable(self.getTable()))
        
    
    def getTable(self):
        mode = self.mode.get()
        if(mode in ("Flight", "Hotel", "Reservation", "Customer")):
            table = mode.lower() + "s"
        else:
            table = mode.lower()
        return table
    
if __name__ == "__main__":
    dbQuery()

