from tkinter import * 
from tkinter.messagebox import showinfo

class MyGUI:
    def __init__(self,master):
        self.master= master 
        # create a title 
        master.title("EAN-13 [by Marcellinus Elbert]")
        # create a window within 500x600 ration
        master.geometry("500x500")
        self.save_label = Label(master,text="Save barcode to PS file:")
        self.save_label.pack()
        self.save = StringVar()
        self.set_save = Entry(master,textvariable=self.save,width=40)
        self.set_save.pack()
        # create a label
        self.enter_label = Label(master,text="Enter code (first 12 decimal digit):")
        self.enter_label.pack()
        self.enter = StringVar()
        # create an input field with enter as input variable
        self.set_enter = Entry(master,textvariable=self.enter,width=40)
        self.set_enter.pack()
        # source: https://www.delftstack.com/howto/python-tkinter/how-to-bind-enter-key-to-a-function-in-tkinter/
        # bind enter with function generate
        self.set_enter.bind('<Return>',self.generate)

        # create a canvas within width 400 height 400 bg white
        self.bar_canvas = Canvas(self.master,width=400,height=400,bg="white")



    def generate(self,event):
        # the code is not twelve then pop up modal will open, please input correct code only
        try:
            # if can be forced to integer then its okay, if error then handle with except, and show modal.
            check_type = int(self.enter.get())
            output_save = self.save.get()
            # if output file is not .eps then trigger the modal
            if output_save[-4:] != ".eps":
                showinfo(message=f"Please enter correct output file name")
            elif len(self.enter.get()) != 12:
                showinfo(message=f"Please enter correct input code")
            else:
                # else get the input as code
                # run the check sum digit 
                # convert it to the 7bit 
                # then show bar
                # clean the canvas
                self.bar_canvas.delete("all")
                self.code = self.enter.get()
                self.checkdigit()
                self.convert_to_7bit()
                self.show_bar()

        except ValueError:
            showinfo(message=f"Please enter correct input code")
        

    def checkdigit(self):
        self.checksum=0
        # for odd index multiply with 1
        # for even index multiply with 3
        for idx in range(0,len(self.code)):
            if idx % 2 == 0:
                self.checksum +=  int(self.code[idx]) 
            elif idx % 2 == 1:
                self.checksum += int(self.code[idx]) *3
        
        self.check_modulo = self.checksum % 10
        # if modulo not zero then 10 - modulo
        # else modulo is zero then digit is zero
        if self.check_modulo != 0:
            self.final_digit = 10-(self.check_modulo)
    
        elif self.check_modulo == 0:
            self.final_digit = self.check_modulo


    def convert_to_7bit(self):
        # get the first index
        self.first_index = int(self.code[0])
        # access the list of objects, with index 0 represent the first index 0 combination of first six and last six
        self.structure = structure_ean[self.first_index]["first_six"]+structure_ean[self.first_index]["last_six"]
        # add 101 to the first
        self.converted = "101"
        # remove the first index and add the last index with digit that calculated in checkdigit function
        self.coded = self.code[1:]+str(self.final_digit)
        counter = 0
        # add 01010 to the middle
        for digit,nums_code in zip(self.structure,self.coded):
            if counter == 6:
                self.converted += "01010"
            self.converted += structure_ean[int(nums_code)][digit]
            counter +=1
        # add 101 to the last
        self.converted+= "101"

    def show_bar(self):
    
        counter = 0
        kelipatan_7 = 0
        count_mid_bar = 0
        # loop through code that converted to 7 bit
        for every_digit in self.converted:
            # to give a controll, if we are already in the middle 
            if ((counter-3) % 7) == 0 and counter-3!=0:
                kelipatan_7 +=1
            # if digit is one that it will give the black line
            if every_digit == "1":
                # for first 3, the length of the line is more longer than any digit
                if counter <3:
                    self.bar_canvas.create_rectangle(100+counter*2, 50, 102+counter*2, 200, fill="#009BD2", outline = '#009BD2')
                # if last 3 then the length of the line is same as the first
                elif counter >= (len(self.converted)-3):
                    self.bar_canvas.create_rectangle(100+counter*2, 50, 102+counter*2, 200, fill="#009BD2", outline = '#009BD2')
                # if in the middle, while mid bar less than two than execute the next line
                elif kelipatan_7==6 and count_mid_bar < 2:
                    count_mid_bar+=1
                    self.bar_canvas.create_rectangle(100+counter*2, 50, 102+counter*2, 200, fill="#009BD2", outline = '#009BD2')
                # if not first, middle, and end then the block line is normal
                else:
                    self.bar_canvas.create_rectangle(100+counter*2, 50, 102+counter*2, 190, fill="#439c5b", outline = '#439c5b')
            counter+=1

        counter = 0
        for nums in self.coded:
            # if nums is still lower then middle than dont give space
            if counter <6:
                self.bar_canvas.create_text(115+counter*14,220, fill="darkblue",text=f"{nums}",font='Helvetica 18 bold')
            else:
                # if in middle then give space 
                self.bar_canvas.create_text(115+7+counter*14,220, fill="darkblue",text=f"{nums}",font='Helvetica 18 bold')
            counter+=1
          



        self.bar_canvas.create_text(200,20, fill="darkblue",text="EAN-13 Barcode:",font='Helvetica 18 bold')
        self.bar_canvas.pack()
        self.bar_canvas.create_text(90,220, fill="darkblue",text=f"{self.first_index}",font='Helvetica 18 bold')
        self.bar_canvas.create_text(200,250, fill="#EE5759",text=f"Digit is {self.final_digit}",font='Helvetica 18 bold')
        self.bar_canvas.postscript(file=self.save.get())
        
            

def main():
    root = Tk()
    gui = MyGUI(root)
    root.mainloop()

# define the structure combination
structure_ean = [{
    "first_digit":0,
    "first_six":"LLLLLL",
    "last_six":"RRRRRR",
    "L":"0001101",
    "G":"0100111",
    "R":"1110010"
},
{
    "first_digit":1,
    "first_six":"LLGLGG",
    "last_six":"RRRRRR",
    "L":"0011001",
    "G":"0110011",
    "R":"1100110"
},
{
    "first_digit":2,
    "first_six":"LLGGLG",
    "last_six":"RRRRRR",
    "L":"0010011",
    "G":"0011011",
    "R":"1101100"
},
{
    "first_digit":3,
    "first_six":"LLGGGL",
    "last_six":"RRRRRR",
    "L":"0111101",
    "G":"0100001",
    "R":"1000010"
},
{
    "first_digit":4,
    "first_six":"LGLLGG",
    "last_six":"RRRRRR",
    "L":"0100011",
    "G":"0011101",
    "R":"1011100"
},
{
    "first_digit":5,
    "first_six":"LGGLLG",
    "last_six":"RRRRRR",
    "L":"0110001",
    "G":"0111001",
    "R":"1001110"
},
{
    "first_digit":6,
    "first_six":"LGGGLL",
    "last_six":"RRRRRR",
    "L":"0101111",
    "G":"0000101",
    "R":"1010000"
},
{
    "first_digit":7,
    "first_six":"LGLGLG",
    "last_six":"RRRRRR",
    "L":"0111011",
    "G":"0010001",
    "R":"1000100"
},
{
    "first_digit":8,
    "first_six":"LGLGGL",
    "last_six":"RRRRRR",
    "L":"0110111",
    "G":"0001001",
    "R":"1001000"
},
{
    "first_digit":9,
    "first_six":"LGGLGL",
    "last_six":"RRRRRR",
    "L":"0001011",
    "G":"0010111",
    "R":"1110100"
}]



if __name__ == "__main__":
    main()