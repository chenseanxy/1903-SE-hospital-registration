from tkinter import *
import backend

class dbUpdate(object):
    def __init__(self):

        self.tk = Tk()
        self.tk.title("DBUpdate")

        self.ops = ["Add New", "Update Existing"]
        self.op = StringVar(self.tk)
        self.op.set(self.ops[0])
        self.opOption = OptionMenu(self.tk, self.op, *self.ops, command = self.updateFrame)
        self.opOption.configure(pady=5, width=20)
        self.opOption.grid(row=0, column=0)


        self.modes = ["Flight", "Hotel", "Bus"]
        self.mode = StringVar(self.tk)
        self.mode.set(self.modes[0])
        self.modeOption = OptionMenu(self.tk, self.mode, *self.modes, command = self.updateFrame)
        self.modeOption.configure(pady=5, width=20)
        self.modeOption.grid(row=0, column=1)

        self.createFrame()

        self.commitButton = Button(self.tk, text="Commit Changes", pady=5, width=20, command=self.commitChanges)
        self.commitButton.grid(columnspan=2, pady=10)

        self.tk.mainloop()

    def createFrame(self):
        op = self.op.get()
        mode = self.mode.get()
        # print(op, mode)
        self.modifyFrame = Frame(self.tk)
        self.modifyFrame.grid(row=2, column=0, columnspan=2, padx=20, pady=20) 
        
        self.primaryKeyText = Label(self.modifyFrame, text="Flight Number", anchor="e", width=20)
        self.primaryKeyText.grid(row=0, column=0)
        self.primaryKey = Entry(self.modifyFrame, width=40)
        self.primaryKey.grid(row=0, column=1)

        self.priceText = Label(self.modifyFrame, text="Price", anchor="e", width=20)
        self.priceText.grid(row=1, column=0)
        self.price = Entry(self.modifyFrame, width=40)
        self.price.grid(row=1, column=1)

        self.totalNumText = Label(self.modifyFrame, text="Seats", anchor="e", width=20)
        self.totalNumText.grid(row=2, column=0)
        self.totalNum = Entry(self.modifyFrame, width=40)
        self.totalNum.grid(row=2, column=1)

        self.availNumText = Label(self.modifyFrame, text="Available Seats", anchor="e", width=20)
        self.availNumText.grid(row=3, column=0)
        self.availNum = Entry(self.modifyFrame, width=40)
        self.availNum.grid(row=3, column=1)

        self.paramText = Label(self.modifyFrame, text="Paramaters(JSON)", anchor="e", width=20)
        self.paramText.grid(row=9, column=0)
        self.param = Entry(self.modifyFrame, width=40)
        self.param.grid(row=9, column=1)

        if(mode == "Flight"):
            self.fromCityText = Label(self.modifyFrame, text="Departure City", anchor="e", width=20)
            self.fromCityText.grid(row=4, column=0)
            self.fromCity = Entry(self.modifyFrame, width=40)
            self.fromCity.grid(row=4, column=1)

            self.arivCityText = Label(self.modifyFrame, text="Arrival City", anchor="e", width=20)
            self.arivCityText.grid(row=5, column=0)
            self.arivCity = Entry(self.modifyFrame, width=40)
            self.arivCity.grid(row=5, column=1)
        
        else:
            self.locationText = Label(self.modifyFrame, text="Location", anchor="e", width=20)
            self.locationText.grid(row=4, column=0)
            self.location = Entry(self.modifyFrame, width=40)
            self.location.grid(row=4, column=1)

            if(mode == "Hotel"):
                self.primaryKeyText.configure(text="Hotel Number")
                self.totalNumText.configure(text="Rooms")
                self.availNumText.configure(text="Available Rooms")
            
            if(mode == "Bus"):
                self.primaryKeyText.configure(text="Bus Number")
            

        if(op=="Update Existing"):
            self.fillValuesButton = Button(self.modifyFrame, text="Fill Values", command=self.fillValues)
            self.fillValuesButton.grid(row=0, column=2)

    def updateFrame(self, *args):
        self.modifyFrame.destroy()
        self.createFrame()
    
    def commitChanges(self, *args):
        mode = self.mode.get()
        op = self.op.get()

        #Construct object
        if(mode == "Flight"):
            obj = backend.Flight((
                self.primaryKey.get(),
                int(self.price.get()),
                int(self.totalNum.get()),
                int(self.availNum.get()),
                self.fromCity.get(),
                self.arivCity.get(),
                self.param.get()
            ))
        elif(mode == "Hotel"):
            obj = backend.Hotel((
                self.primaryKey.get(),
                self.location.get(),
                int(self.price.get()),
                int(self.totalNum.get()),
                int(self.availNum.get()),
                self.param.get()
            ))
        else:
            obj = backend.Bus((
                self.primaryKey.get(),
                self.location.get(),
                int(self.price.get()),
                int(self.totalNum.get()),
                int(self.availNum.get()),
                self.param.get()
            ))
            
        # print(obj)

        # Sends to dbUpdate
        if(op == "Add New"):
            backend.add(obj)
        else:
            backend.update(obj)
        

    def fillValues(self, *args):
        mode = self.mode.get()
        ##Mode to table name:
        if(mode == "Flight" or mode == "Hotel"):
            table = mode.lower() + "s"
        else:
            table = mode.lower()
        ##
        primaryKey = self.primaryKey.get()
        print(f"Fill Values from {table} on {primaryKey}")
        obj = backend.getValue(primaryKey, table)
        
        if(type(obj)==backend.Bus):
            self.location.delete(0, last="end")
            self.location.insert(0, obj.location)
            self.price.delete(0, last="end")
            self.price.insert(0, obj.price)
            self.totalNum.delete(0, last="end")
            self.totalNum.insert(0, obj.numSeats)
            self.availNum.delete(0, last="end")
            self.availNum.insert(0, obj.numAvail)

        
        if(type(obj)==backend.Hotel):
            self.location.delete(0, last="end")
            self.location.insert(0, obj.location)
            self.price.delete(0, last="end")
            self.price.insert(0, obj.price)
            self.totalNum.delete(0, last="end")
            self.totalNum.insert(0, obj.numRooms)
            self.availNum.delete(0, last="end")
            self.availNum.insert(0, obj.numAvail)
        
        if(type(obj)==backend.Flight):
            self.fromCity.delete(0, last="end")
            self.fromCity.insert(0, obj.fromCity)
            self.arivCity.delete(0, last="end")
            self.arivCity.insert(0, obj.arivCity)
            self.price.delete(0, last="end")
            self.price.insert(0, obj.price)
            self.totalNum.delete(0, last="end")
            self.totalNum.insert(0, obj.numSeats)
            self.availNum.delete(0, last="end")
            self.availNum.insert(0, obj.numAvail)
        
        self.param.delete(0, last="end")
        self.param.insert(0, obj.param)

if __name__ == "__main__":
    dbUpdate()

