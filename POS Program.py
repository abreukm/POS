#Importing all relevant modules
from tkinter import*
from tkinter import Tk, StringVar, ttk
import time;
import datetime
import sqlite3

#Connecting to SQlite database
conn = sqlite3.connect('salon3.db')
c = conn.cursor()

root = Tk()
root.geometry('1000x500+80+20')
root.title('Hair Salon')
root.configure(background='white')

#Top frame, the header row
Tops = Frame(root, width = 1000, height = 80, bd=6, relief='groove')
Tops.pack(side=TOP)

TopsR = Frame(Tops, width = 600, bg='white', height = 80, relief='groove')
TopsR.pack(side=RIGHT)
TopsL = Frame(Tops, width = 400, bg='white', height = 80, relief='groove')
TopsL.pack(side=LEFT)

#----------------------LEFT FRAME, where the Service Menu is located------------------
leftFrame = Frame(root, width = 600, height = 500, bd=6, relief='groove')
leftFrame.pack(side=LEFT)

leftFrame_Service_Menu1 = Frame(leftFrame, width = 275, height = 500, bd=4, relief='groove')
leftFrame_Service_Menu1.pack(side=LEFT)
leftFrame_Service_Menu2 = Frame(leftFrame, width = 274, height = 500, bd=4, relief='groove')
leftFrame_Service_Menu2.pack(side=RIGHT)


leftFrame_Service_Menu2_Top = Frame(leftFrame_Service_Menu2, width = 275, height = 250, bd=4, relief='groove')
leftFrame_Service_Menu2_Top.pack(side=TOP)

leftFrame_Service_Menu2_Bottom = Frame(leftFrame_Service_Menu2, width = 275, height = 250, bd=4, relief='groove')
leftFrame_Service_Menu2_Bottom.pack(side=BOTTOM)


leftFrame_Service_Menu1_Top = Frame(leftFrame_Service_Menu1, width = 275, height = 250, bd=4, relief='groove')
leftFrame_Service_Menu1_Top.pack(side=TOP)

leftFrame_Service_Menu1_Bottom = Frame(leftFrame_Service_Menu1, width = 275, height = 270, relief='groove')
leftFrame_Service_Menu1_Bottom.pack(side=BOTTOM)


#-------------------------RIGHT FRAME, where the Receipt box and Expenses Menu is located--------------------
rightFrame = Frame(root, width = 500, height = 500, bg='white', bd=6, relief='groove')
rightFrame.pack(side=RIGHT)

leftFrame_receiptBox = Frame(rightFrame, width = 250, bg='white', height = 500, bd=6, relief='groove')
leftFrame_receiptBox.pack(side=LEFT)
leftFrame_Expenses_Menu = Frame(rightFrame, width = 250,  bg='white', height = 500, bd=6, relief='groove')
leftFrame_Expenses_Menu.pack(side=RIGHT)

leftFrame_Expenses_Menu_Top = Frame(leftFrame_Expenses_Menu, width = 250,  bg='white', height = 250, bd=4, relief='groove')
leftFrame_Expenses_Menu_Top.pack(side=TOP)

leftFrame_Expenses_Menu_Bottom = Frame(leftFrame_Expenses_Menu, width = 250,  bg='white', height = 270, relief='groove')
leftFrame_Expenses_Menu_Bottom.pack(side=BOTTOM)

Tops.configure(background='white')
leftFrame.configure(background='white')
rightFrame.configure(background='white')


#===============================Variables===================
Date=StringVar()
Date.set(time.strftime('%Y-%m-%d'))
selection = IntVar()
selection.set(1)

hair_cut_woman = 'Hair Cut - Woman'
hair_cut_man = 'Hair Cut - Man'
hair_cut_child = 'Hair Cut - Child'
blow_dry = 'Blow Dry'
hair_colour = 'Hair Colour'
relaxer = 'Relaxer'
high_lights = 'High Lights'
perm = 'Perm'
up_do = 'Up Do'
hair_ext =  'Hair Extentions'
deep_conditioner = 'Deep Conditioner'
eyebrows = 'Eyebrows'
waxing = 'Waxing'
jap_perm= 'Japanese Perm'
hair_styling =  'Hair Styling'
hair_treatment = 'Hair Treatment'
facial = 'Facial'
product_sale = 'Product Sale'

Shampoo = 'Shampoo 200ml' 
Conditioner = 'Conditioner 200ml' 
Hair_Colour1 = 'Wella Colour 70ml' 
Hair_Colour2 = 'Wella Colour 150ml' 
Peroxide1 = 'Perodixe 10% 200ml' 
Latex_gloves = 'Gloves 200 pack' 
Peroxide2 = 'Perodixe 20% 200ml' 
Relaxer_cream = 'Relaxer Cream 300ml' 

hair_cut_woman_price = IntVar()
hair_cut_man_price = IntVar()
hair_cut_child_price = IntVar()
blow_dry_price = IntVar()
hair_colour_price = IntVar()
relaxer_price = IntVar()
highlight_price = IntVar()
perm_price = IntVar()
up_do_price = IntVar()
hair_ext_price = IntVar()
deep_cond_price = IntVar()
other1_price = IntVar()
other2_price = IntVar()
eyebrow_price = IntVar()
waxing_price = IntVar()
jap_perm_price = IntVar()
hair_styling_price = IntVar()
hair_treatment_price = IntVar()
facial_price = IntVar()
product_sale_price = IntVar()
shampoo_price = IntVar()
conditioner_price = IntVar()
hair_colour1_price = IntVar()
hair_colour2_price = IntVar()
peroxide1_price = IntVar()
latex_gloves_price = IntVar()
peroxide2_price = IntVar()
relaxer_cream_price = IntVar()
other3_price = IntVar()
other4_price = IntVar()

Cash = IntVar()
Change = IntVar()

hair_cut_woman_qty = IntVar()
hair_cut_man_qty = IntVar()
hair_cut_child_qty =IntVar()
blow_dry_qty =IntVar()
hair_colour_qty =IntVar()
relaxer_qty =IntVar()
high_lights_qty =IntVar()
perm_qty =IntVar()
up_do_qty =IntVar()
hair_ext_qty =IntVar()
deep_conditioner_qty =IntVar()
other1_qty =IntVar()
other2_qty =IntVar()
eyebrows_qty =IntVar()
waxing_qty =IntVar()
jap_perm_qty =IntVar()
hair_styling_qty =IntVar()
hair_treatment_qty =IntVar()
facial_qty =IntVar()
product_sale_qty =IntVar()

conditioner_qty =IntVar()
conditioner_qty =IntVar()
hair_colour1_qty =IntVar()
hair_colour2_qty = IntVar()
peroxide1_qty = IntVar()
latex_gloves_qty =IntVar()
relaxer_cream_qty =IntVar()
relaxer_cream_qty =IntVar()
other3_qty =IntVar()
other4_qty =IntVar()

hair_cut_woman_qty.set(1)
hair_cut_man_qty.set(1)
hair_cut_child_qty.set(1)
blow_dry_qty.set(1)
hair_colour_qty.set(1)
relaxer_qty.set(1)
high_lights_qty.set(1)
perm_qty.set(1)
up_do_qty.set(1)
hair_ext_qty.set(1)
deep_conditioner_qty.set(1)
other1_qty.set(1)
other2_qty.set(1)
eyebrows_qty.set(1)
waxing_qty.set(1)
jap_perm_qty.set(1)
hair_styling_qty.set(1)
hair_treatment_qty.set(1)
facial_qty.set(1)
product_sale_qty.set(1)
conditioner_qty.set(1)
conditioner_qty.set(1)
hair_colour1_qty.set(1)

hair_colour2_qty.set(1)
peroxide1_qty.set(1)
latex_gloves_qty.set(1)
relaxer_cream_qty.set(1)
relaxer_cream_qty.set(1)
other3_qty.set(1)
other4_qty.set(1)

other1=StringVar()
other2=StringVar()
other3=StringVar()
other4=StringVar()
Receipt = StringVar()
Total = IntVar()
text_Input = StringVar()
operator = ''


#===============================Functions===================
 
# Function for clicking buttons on calculator 
def buttonClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)
    
# Function to clear display on calculator    
def btnClearDisplay():
    global operator
    operator=''
    text_Input.set('')

#Function for equal button on calculator    
def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=''
    
#Function to clear and re-set all text inputs in system     
def Clear():
    other1.set('') 
    other2.set('') 
    other3.set('') 
    other4.set('')   
    Total.set(0)
    txtReceipt.config(state=NORMAL)
    txtReceipt.delete('1.0', END)      
    Cash.set(0)
    Change.set(0)
    
    hair_cut_woman_price.set(0)
    hair_cut_man_price.set(0)
    hair_cut_child_price.set(0)
    blow_dry_price.set(0)
    hair_colour_price.set(0)
    relaxer_price.set(0)
    highlight_price.set(0)
    perm_price.set(0)
    up_do_price.set(0)
    hair_ext_price.set(0)
    deep_cond_price.set(0)
    other1_price.set(0)
    other2_price.set(0)
    eyebrow_price.set(0)
    waxing_price.set(0)
    jap_perm_price.set(0)
    hair_styling_price.set(0)
    hair_treatment_price.set(0)
    facial_price.set(0)
    product_sale_price.set(0)

    shampoo_price.set(0)
    conditioner_price.set(0) 
    hair_colour1_price.set(0)
    hair_colour2_price.set(0)
    peroxide1_price.set(0)
    latex_gloves_price.set(0)
    peroxide2_price.set(0)
    relaxer_cream_price.set(0)
    other3_price.set(0)
    other4_price.set(0)


    hair_cut_woman_qty.set(1)
    hair_cut_man_qty.set(1)
    hair_cut_child_qty.set(1)
    blow_dry_qty.set(1)
    hair_colour_qty.set(1)
    relaxer_qty.set(1)
    high_lights_qty.set(1)
    perm_qty.set(1)
    up_do_qty.set(1)
    hair_ext_qty.set(1)
    deep_conditioner_qty.set(1)
    other1_qty.set(1)
    other2_qty.set(1)
    eyebrows_qty.set(1)
    waxing_qty.set(1)
    jap_perm_qty.set(1)
    hair_styling_qty.set(1)
    hair_treatment_qty.set(1)
    facial_qty.set(1)
    product_sale_qty.set(1)

    conditioner_qty.set(1)
    conditioner_qty.set(1)
    hair_colour1_qty.set(1)
    hair_colour2_qty.set(1)
    peroxide1_qty.set(1)
    latex_gloves_qty.set(1)
    relaxer_cream_qty.set(1)
    relaxer_cream_qty.set(1)
    other3_qty.set(1)
    other4_qty.set(1)

   
sum_total = 0

#Function to calculate total for prices and quantities entered on system
def calTotal():     
    #This section calculates totals
    Total.set(0)
    sum_total =  (hair_cut_woman_price.get() * hair_cut_woman_qty.get()) + (hair_cut_man_price.get() * hair_cut_man_qty.get()) + (hair_cut_child_price.get() * hair_cut_child_qty.get()) + (blow_dry_price.get() * blow_dry_qty.get()) + (hair_colour_price.get() * hair_colour_qty.get()) + (relaxer_price.get() * relaxer_qty.get()) + (highlight_price.get() * high_lights_qty.get()) + (perm_price.get() * perm_qty.get()) + (up_do_price.get() * up_do_qty.get()) + (hair_ext_price.get() * hair_ext_qty.get()) + (deep_cond_price.get() * deep_conditioner_qty.get()) + (other1_price.get() * other1_qty.get()) + (other2_price.get() * other2_qty.get()) + (eyebrow_price.get() * eyebrows_qty.get()) + (waxing_price.get() * waxing_qty.get()) + (jap_perm_price.get() * jap_perm_qty.get()) + (hair_styling_price.get() * hair_styling_qty.get()) + (hair_treatment_price.get() * hair_treatment_qty.get()) + (facial_price.get() * facial_qty.get()) + (product_sale_price.get() * product_sale_qty.get()) + (shampoo_price.get() * conditioner_qty.get()) + (conditioner_price.get()  * conditioner_qty.get()) + (hair_colour1_price.get() * hair_colour1_qty.get()) + (hair_colour2_price.get() * hair_colour2_qty.get()) + (peroxide1_price.get() * peroxide1_qty.get()) + (latex_gloves_price.get() * latex_gloves_qty.get()) + (peroxide2_price.get() * relaxer_cream_qty.get()) + (relaxer_cream_price.get() * relaxer_cream_qty.get()) + (other3_price.get() * other3_qty.get()) + (other4_price.get() * other4_qty.get())  
     # This section prints the total to the Total box                                                                                                                                                             
    Total.set(sum_total)
    #This section prints the items entered on to the receipt box
    if Total.get() > 0:
        txtReceipt.config(state=NORMAL)
        txtReceipt.delete('1.0', END)
        txtReceipt.insert(END, 'Date:  ' + Date.get() + '\n\n' )
    # This is the code for the services section of the program
    if hair_cut_woman_price.get() != 0:    
        txtReceipt.insert(END, hair_cut_woman + ': ' + ' ' + str(hair_cut_woman_qty.get()) + ' ' + '@'  + ' ' + '$' + str(hair_cut_woman_price.get()) + '\t\t\t\t' + '$' + str(hair_cut_woman_qty.get() * hair_cut_woman_price.get()) + '\n') 
    if hair_cut_man_price.get() != 0: 
        txtReceipt.insert(END, hair_cut_man + ': ' + ' ' + str(hair_cut_man_qty.get()) + ' ' + '@'  + ' ' + '$' + str(hair_cut_man_price.get()) + '\t\t\t\t' + '$' + str(hair_cut_man_qty.get() * hair_cut_man_price.get()) + '\n')
    if hair_cut_child_price.get() != 0: 
        txtReceipt.insert(END, hair_cut_child + ': ' + ' ' +str(hair_cut_child_qty.get()) + ' ' + '@'  + ' ' + '$' + str(hair_cut_child_price.get()) + '\t\t\t\t' + '$' + str(hair_cut_child_qty.get() * hair_cut_child_price.get()) + '\n')
    if blow_dry_price.get() != 0: 
        txtReceipt.insert(END, blow_dry + ': ' + ' ' +str(blow_dry_qty.get()) + ' ' + '@'  + ' ' + '$' + str(blow_dry_price.get()) + '\t\t\t\t' + '$' + str(blow_dry_qty.get() * blow_dry_price.get()) + '\n')
    if hair_colour_price.get() != 0: 
        txtReceipt.insert(END, hair_colour + ': ' + ' ' +str(hair_colour_qty.get()) + ' ' + '@'  + ' ' + '$' + str(hair_colour_price.get()) + '\t\t\t\t' + '$' + str(hair_colour_qty.get() * hair_colour_price.get()) + '\n')
    if relaxer_price.get() != 0: 
        txtReceipt.insert(END, relaxer + ': ' + ' ' +str(relaxer_qty.get()) + ' ' + '@'  + ' ' + '$' + str(relaxer_price.get()) + '\t\t\t\t' + '$' + str(relaxer_qty.get() * relaxer_price.get()) + '\n')
    if highlight_price.get() != 0: 
        txtReceipt.insert(END, high_lights + ': ' + ' ' +str(high_lights_qty.get()) + ' ' + '@'  + ' ' + '$' + str(highlight_price.get()) + '\t\t\t\t' + '$' + str(high_lights_qty.get() * highlight_price.get()) + '\n')
    if perm_price.get() != 0: 
        txtReceipt.insert(END, perm + ': ' + ' ' +str(perm_qty.get()) + ' ' + '@'  + ' ' + '$' + str(perm_price.get()) + '\t\t\t\t' + '$' + str(perm_qty.get() * perm_price.get()) + '\n')
    if up_do_price.get() != 0: 
        txtReceipt.insert(END, up_do + ': ' + ' ' +str(up_do_qty.get()) + ' ' + '@'  + ' ' + '$' + str(up_do_price.get()) + '\t\t\t\t' + '$' + str(up_do_qty.get() * up_do_price.get()) + '\n')
    if deep_cond_price.get() != 0: 
        txtReceipt.insert(END, deep_conditioner + ': ' + ' ' + str(deep_conditioner_qty.get()) + ' ' + '@'  + ' ' + '$' + str(deep_cond_price.get()) + '\t\t\t\t' + '$' + str(deep_conditioner_qty.get() * deep_cond_price.get()) + '\n')   
    if eyebrow_price.get() != 0: 
        txtReceipt.insert(END, eyebrows + ': ' + ' ' + str(eyebrows_qty.get()) + ' ' + '@'  + ' ' + '$' + str(eyebrow_price.get()) + '\t\t\t\t' + '$' + str(eyebrows_qty.get() * eyebrow_price.get()) + '\n')
    if waxing_price.get() != 0: 
        txtReceipt.insert(END, waxing + ': ' + ' ' + str(waxing_qty.get()) + ' ' + '@'  + ' ' + '$' + str(waxing_price.get()) + '\t\t\t\t' + '$' + str(waxing_qty.get() * waxing_price.get()) + '\n')
    if jap_perm_price.get() != 0: 
        txtReceipt.insert(END, jap_perm + ': ' + ' ' + str(jap_perm_qty.get()) + ' ' + '@'  + ' ' + '$' + str(jap_perm_price.get()) + '\t\t\t\t' + '$' + str(jap_perm_qty.get() * jap_perm_price.get()) + '\n')
    if hair_styling_price.get() != 0:
        txtReceipt.insert(END, hair_styling + ': ' + ' ' +str(hair_styling_qty.get()) + ' ' + '@'  + ' ' + '$' + str(hair_styling_price.get()) + '\t\t\t\t' + '$' + str(hair_styling_qty.get() * hair_styling_price.get()) + '\n')
    if hair_treatment_price.get() != 0: 
        txtReceipt.insert(END, hair_treatment + ': ' + ' ' +str(hair_treatment_qty.get()) + ' ' + '@'  + ' ' + '$' + str(hair_treatment_price.get()) + '\t\t\t\t' + '$' + str(hair_treatment_qty.get() * hair_treatment_price.get()) + '\n')
        
    if hair_ext_price.get() != 0: 
        txtReceipt.insert(END, hair_ext + ': ' + ' ' +str(hair_ext_qty.get()) + ' ' + '@'  + ' ' + '$' + str(hair_ext_price.get()) + '\t\t\t\t' + '$' + str(hair_ext_qty.get() * hair_ext_price.get()) + '\n')        
    if facial_price.get() != 0: 
        txtReceipt.insert(END, facial + ': ' + ' ' +str(facial_qty.get()) + ' ' + '@'  + ' ' + '$' + str(facial_price.get()) + '\t\t\t\t' + '$' + str(facial_qty.get() * facial_price.get()) + '\n')       
    if product_sale_price.get() != 0: 
        txtReceipt.insert(END, product_sale + ': ' + ' ' +str(product_sale_qty.get()) + ' ' + '@'  + ' ' + '$' + str(product_sale_price.get()) + '\t\t\t\t' + '$' + str(product_sale_qty.get() * product_sale_price.get()) + '\n')
    if other1_price.get() != 0: 
        txtReceipt.insert(END, other1.get() + ':' + ' ' + str(other1_qty.get()) + ' ' + '@'  + ' ' + '$' + str(other1_price.get()) + '\t\t\t\t' + '$' + str(other1_qty.get() * other1_price.get()) + '\n')
    if other2_price.get() != 0: 
        txtReceipt.insert(END, other2.get()  + ':' + ' ' + str(other2_qty.get()) + ' ' + '@'  + ' ' + '$' + str(other2_price.get()) + '\t\t\t\t' + '$' + str(other2_qty.get() * other2_price.get()) + '\n')    
        
#Expenses receipt items----------------------------------------------        
     # This is the code for the expenses section of the program
    if shampoo_price.get() != 0: 
        txtReceipt.insert(END,  Shampoo + ': ' + ' ' +str(conditioner_qty.get()) + ' ' + '@'  + ' ' + '$' + str(shampoo_price.get()) + '\t\t\t\t' + '$' + str(conditioner_qty.get() * shampoo_price.get()) + '\n')
    if conditioner_price.get() != 0: 
        txtReceipt.insert(END, Conditioner + ': ' + ' ' + str(conditioner_qty.get()) + ' ' + '@'  + ' ' + '$' + str(conditioner_price.get()) + '\t\t\t\t' + '$' + str(conditioner_qty.get() * conditioner_price.get()) + '\n')
    if hair_colour1_price.get() != 0: 
        txtReceipt.insert(END, Hair_Colour1 + ': ' + ' ' + str(hair_colour1_qty.get()) + ' ' + '@'  + ' ' + '$' + str(hair_colour1_price.get()) + '\t\t\t\t' + '$' + str(hair_colour1_qty.get() * hair_colour1_price.get()) + '\n')
    if hair_colour2_price.get() != 0:
        txtReceipt.insert(END, Hair_Colour2 + ': ' + ' ' + str(hair_colour2_qty.get()) + ' ' + '@'  + ' ' + '$' + str(hair_colour2_price.get()) + '\t\t\t\t' + '$' + str(hair_colour2_qty.get() * hair_colour2_price.get()) + '\n')
    if peroxide1_price.get() != 0: 
        txtReceipt.insert(END, Peroxide1 + ': ' + ' ' + str(peroxide1_qty.get()) + ' ' + '@'  + ' ' + '$' + str(peroxide1_price.get()) + '\t\t\t\t' + '$' + str(peroxide1_qty.get() * peroxide1_price.get()) + '\n')        
    if latex_gloves_price.get() != 0: 
        txtReceipt.insert(END, Latex_gloves + ': ' + ' ' + str(latex_gloves_qty.get()) + ' ' + '@'  + ' ' + '$' + str(latex_gloves_price.get()) + '\t\t\t\t' + '$' + str(latex_gloves_qty.get() * latex_gloves_price.get()) + '\n')       
    if peroxide2_price.get() != 0: 
        txtReceipt.insert(END, Peroxide2 + ': ' + ' ' + str(relaxer_cream_qty.get()) + ' ' + '@'  + ' ' + '$' + str(peroxide2_price.get()) + '\t\t\t\t' + '$' + str(relaxer_cream_qty.get() * peroxide2_price.get()) + '\n')
    if relaxer_cream_price.get() != 0: 
        txtReceipt.insert(END, Relaxer_cream + ': ' + ' ' + str(relaxer_cream_qty.get()) + ' ' + '@'  + ' ' + '$' + str(relaxer_cream_price.get()) + '\t\t\t\t' + '$' + str(relaxer_cream_qty.get() * relaxer_cream_price.get()) + '\n')   
    if other3_price.get() != 0: 
        txtReceipt.insert(END, other3.get() + ':' + ' ' + str(other3_qty.get()) + ' ' + '@'  + ' ' + '$' + str(other3_price.get()) + '\t\t\t\t' + '$' + str(other3_qty.get() * other3_price.get()) + '\n')
    if other4_price.get() != 0: 
        txtReceipt.insert(END, other4.get()  + ':' + ' ' + str(other4_qty.get()) + ' ' + '@'  + ' ' + '$' + str(other4_price.get()) + '\t\t\t\t' + '$' + str(other4_qty.get() * other4_price.get()) + '\n')        
    # The receipt box is disbaled after everything is printed

    txtReceipt.config(state=DISABLED)

#This function calculates the change based on the total and the value of the Cash entry box
chn = 0
def calChange(event):
    Change.set(0)
    chn = (Cash.get() - Total.get())
    Change.set(chn)
 
#This function reads the position of the radio button and enables only the section selected with the radio button  
def Disabling():
    #If the services section is selected
    if selection.get() == 1:
        Clear()
        txtReceipt.config(state=DISABLED)
        txtp1.config(state=DISABLED)
        txtp2.config(state=DISABLED)
        txtp21.config(state=DISABLED)
        txtp22.config(state=DISABLED) 
        txtp31.config(state=DISABLED) 
        txtp32.config(state=DISABLED)  
        txtp41.config(state=DISABLED) 
        txtp42.config(state=DISABLED)
        txtp51.config(state=DISABLED)
        txtp52.config(state=DISABLED)
        txtp61.config(state=DISABLED)
        txtp62.config(state=DISABLED)
        txtp71.config(state=DISABLED)
        txtp72.config(state=DISABLED)
        txtp81.config(state=DISABLED)
        txtp82.config(state=DISABLED)  
        txtOther31.config(state=DISABLED)
        txtOther32.config(state=DISABLED)
        txtOther3.config(state=DISABLED) 
        txtOther41.config(state=DISABLED)
        txtOther42.config(state=DISABLED)
        txtOther4.config(state=DISABLED)

        txtH_cut_women1.config(state=NORMAL)
        txtH_cut_women2.config(state=NORMAL)
        txtH_cut_man1.config(state=NORMAL)
        txtH_cut_man2.config(state=NORMAL)
        txtH_cut_child1.config(state=NORMAL)
        txtH_cut_child2.config(state=NORMAL)
        txtB_Dry1.config(state=NORMAL)
        txtB_Dry2.config(state=NORMAL)
        txtH_colour1.config(state=NORMAL)
        txtH_colour2.config(state=NORMAL)
        txtRelexer1.config(state=NORMAL)
        txtRelexer2.config(state=NORMAL) 
        txtH_lighthair_cut_woman.config(state=NORMAL)
        txtH_lighthair_cut_man.config(state=NORMAL)
        txtPerm1.config(state=NORMAL)
        txtPerm2.config(state=NORMAL)
        txtUp1.config(state=NORMAL)
        txtUp2.config(state=NORMAL) 
        txtdeep1.config(state=NORMAL)
        txtdeep2.config(state=NORMAL)
        
        txteyebrow1.config(state=NORMAL)
        txteyebrow2.config(state=NORMAL)
        txtwax1.config(state=NORMAL)
        txtwax2.config(state=NORMAL)
        txtjap1.config(state=NORMAL)
        txtjap2.config(state=NORMAL)
        txtstyling1.config(state=NORMAL) 
        txtstyling2.config(state=NORMAL)
        txttreat1.config(state=NORMAL) 
        txttreat2.config(state=NORMAL)
        txtxtentionhair_cut_woman.config(state=NORMAL) 
        txtxtentionhair_cut_man.config(state=NORMAL) 
        txtfacial1.config(state=NORMAL)
        txtfacial2.config(state=NORMAL)
        txtproduct1.config(state=NORMAL)
        txtproduct2.config(state=NORMAL)        
        txtOther1.config(state=NORMAL)
        txtOther12.config(state=NORMAL)
        txtOther13.config(state=NORMAL)
        txtOther2.config(state=NORMAL)
        txtOther22.config(state=NORMAL)
        txtOther23.config(state=NORMAL)        
        
        txtCash.config(state=NORMAL)
    #If the expenses section is selected    
    if selection.get() == 2:
        Clear() 
        txtp1.config(state=NORMAL)
        txtp2.config(state=NORMAL)
        txtp21.config(state=NORMAL)
        txtp22.config(state=NORMAL)
        txtp31.config(state=NORMAL)
        txtp32.config(state=NORMAL)  
        txtp41.config(state=NORMAL) 
        txtp42.config(state=NORMAL)
        txtp51.config(state=NORMAL)
        txtp52.config(state=NORMAL)
        txtp61.config(state=NORMAL)
        txtp62.config(state=NORMAL)
        txtp71.config(state=NORMAL)
        txtp72.config(state=NORMAL)
        txtp81.config(state=NORMAL)
        txtp82.config(state=NORMAL)  
        txtOther31.config(state=NORMAL)
        txtOther32.config(state=NORMAL)
        txtOther3.config(state=NORMAL)
        txtOther41.config(state=NORMAL)
        txtOther42.config(state=NORMAL)
        txtOther4.config(state=NORMAL) 
        
        txtReceipt.config(state=DISABLED)
        txtH_cut_women1.config(state=DISABLED)
        txtH_cut_women2.config(state=DISABLED)
        txtH_cut_man1.config(state=DISABLED)
        txtH_cut_man2.config(state=DISABLED)
        txtH_cut_child1.config(state=DISABLED)
        txtH_cut_child2.config(state=DISABLED) 
        txtB_Dry1.config(state=DISABLED)
        txtB_Dry2.config(state=DISABLED)
        txtH_colour1.config(state=DISABLED)
        txtH_colour2.config(state=DISABLED)
        txtRelexer1.config(state=DISABLED)
        txtRelexer2.config(state=DISABLED) 
        txtH_lighthair_cut_woman.config(state=DISABLED)
        txtH_lighthair_cut_man.config(state=DISABLED)
        txtPerm1.config(state=DISABLED)
        txtPerm2.config(state=DISABLED) 
        txtUp1.config(state=DISABLED)
        txtUp2.config(state=DISABLED) 
        txtdeep1.config(state=DISABLED)
        txtdeep2.config(state=DISABLED) 

        txteyebrow1.config(state=DISABLED) 
        txteyebrow2.config(state=DISABLED) 
        txtwax1.config(state=DISABLED) 
        txtwax2.config(state=DISABLED) 
        txtjap1.config(state=DISABLED) 
        txtjap2.config(state=DISABLED) 
        txtstyling1.config(state=DISABLED) 
        txtstyling2.config(state=DISABLED) 
        txttreat1.config(state=DISABLED) 
        txttreat2.config(state=DISABLED) 
        txtxtentionhair_cut_woman.config(state=DISABLED) 
        txtxtentionhair_cut_man.config(state=DISABLED)  
        txtfacial1.config(state=DISABLED) 
        txtfacial2.config(state=DISABLED) 
        txtproduct1.config(state=DISABLED) 
        txtproduct2.config(state=DISABLED)         
        txtOther1.config(state=DISABLED) 
        txtOther12.config(state=DISABLED) 
        txtOther13.config(state=DISABLED)
        txtOther2.config(state=DISABLED) 
        txtOther22.config(state=DISABLED) 
        txtOther23.config(state=DISABLED)  
     
        txtCash.config(state=DISABLED)
  
#Functions which writes the transation to the database

class Transactions:
    def __init__(self, t_id, service, qty, price, date): 
        self.service = service
        self.qty = qty
        self.price = price
        self.date = date
#this statement creates the transactions table in the database	
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Transactions(service text, qty integer, price real, date text)')
    c.execute('CREATE TABLE IF NOT EXISTS Expenses(product text, qty integer, price real, date text)')
    
create_table()

def insert_services():
    '''This functions inserts new trasaction to the database into the appropriate table, inserts the transation (t_id, service, qty, price and date) to the trasanctions table, or ...... to the expenses table. The table writen to depends on the radio botton position (services or expenses). Lastly, the function clears the system.
    '''    
       #If the system is in service mode

    if hair_cut_woman_price.get() != 0:  
      
        c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?)", (hair_cut_woman, hair_cut_woman_qty.get(), hair_cut_woman_price.get(), Date.get()))        
    if hair_cut_man_price.get() != 0:    
        c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?)", (hair_cut_man , hair_cut_man_qty.get(), hair_cut_man_price.get(), Date.get())) 
        
    if hair_cut_child_price.get() != 0:    
        c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?)", (hair_cut_child , hair_cut_child_qty.get(), hair_cut_child_price.get(), Date.get())) 
         
    if blow_dry_price.get() != 0:    
        c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?)", (blow_dry , blow_dry_qty.get(), blow_dry_price.get(), Date.get())) 
             
    if hair_colour_price.get() != 0:    
        c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?)", (hair_colour , hair_colour_qty.get(), hair_colour_price.get(), Date.get())) 
       
    if relaxer_price.get() != 0:    
        c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?)", (relaxer , relaxer_qty.get(), relaxer_price.get(), Date.get())) 
           
    if highlight_price.get() != 0:  
        c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?)", (high_lights , high_lights_qty.get(), highlight_price.get(), Date.get())) 
     
    if perm_price.get() != 0:    
        c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?)", (perm , perm_qty.get(), perm_price.get(), Date.get())) 
          
    if up_do_price.get() != 0:    
        c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?)", (up_do , up_do_qty.get(), up_do_price.get(), Date.get())) 
          
    if hair_ext_price.get() != 0:    
        c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?)", (hair_ext , hair_ext_qty.get(), hair_ext_price.get(), Date.get())) 
                      
    if deep_cond_price.get() != 0:  
        c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?)", (deep_conditioner , deep_conditioner_qty.get(), deep_cond_price.get(), Date.get())) 
          
    if other1_price.get() != 0:    
        c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?)", (other1.get() , other1_qty.get(), other1_price.get(), Date.get())) 
           
    if other2_price.get() != 0:    
        c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?)", (other2.get(), other2_qty.get(), other2_price.get(), Date.get())) 
           
    if eyebrow_price.get() != 0:    
        c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?)", (eyebrows , eyebrows_qty.get(), eyebrow_price.get(), Date.get())) 
               
    if waxing_price.get() != 0:    
        c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?)", (waxing , waxing_qty.get(), waxing_price.get(), Date.get())) 
          
    if jap_perm_price.get() != 0:    
        c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?)", (jap_perm , jap_perm_qty.get(), jap_perm_price.get(), Date.get())) 
             
    if hair_styling_price.get() != 0:  
        c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?)", (hair_styling , hair_styling_qty.get(), hair_styling_price.get(), Date.get())) 
            
    if hair_treatment_price.get() != 0:    
        c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?)", (hair_treatment , hair_treatment_qty.get(), hair_treatment_price.get(), Date.get())) 
    if facial_price.get() != 0:    
        c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?)", (facial , facial_qty.get(), facial_price.get(), Date.get())) 
            
    if product_sale_price.get() != 0:    
        c.execute("INSERT INTO Transactions VALUES (?, ?, ?, ?)", (product_sale , product_sale_qty.get(), product_sale_price.get(), Date.get())) 
    conn.commit()
    
                
    #Call on the Clear() function to clear the system.     
    if Total.get() > 0:
        Clear()
                #Print completion message to the receipt box
        txtReceipt.config(state=NORMAL)               
        txtReceipt.insert(END, 'Transaction Complete!')
        txtReceipt.config(state=DISABLED) 
               

def insert_expenses():

    if shampoo_price.get() != 0:    
        c.execute("INSERT INTO Expenses VALUES (?, ?, ?, ?)",(Shampoo , conditioner_qty.get(), shampoo_price.get(), Date.get())) 
                 
    if conditioner_price.get() != 0: 
        c.execute("INSERT INTO Expenses VALUES (?, ?, ?, ?)",(Conditioner , conditioner_qty.get(), conditioner_price.get(), Date.get())) 
           
    if hair_colour1_price.get() != 0: 
        c.execute("INSERT INTO Expenses VALUES (?, ?, ?, ?)",(Hair_Colour1 , hair_colour1_qty.get(), hair_colour1_price.get(), Date.get())) 
          
    if hair_colour2_price.get() != 0:
        c.execute("INSERT INTO Expenses VALUES (?, ?, ?, ?)",(Hair_Colour2 , hair_colour2_qty.get(), hair_colour2_price.get(), Date.get())) 
         
    if peroxide1_price.get() != 0: 
        c.execute("INSERT INTO Expenses VALUES (?, ?, ?, ?)",(Peroxide1 , peroxide1_qty.get(), peroxide1_price.get(), Date.get())) 
                 
    if latex_gloves_price.get() != 0: 
        c.execute("INSERT INTO Expenses VALUES (?, ?, ?, ?)",(Latex_gloves , latex_gloves_qty.get(), latex_gloves_price.get(), Date.get())) 
               
    if peroxide2_price.get() != 0: 
        c.execute("INSERT INTO Expenses VALUES (?, ?, ?, ?)",(Peroxide2 , relaxer_cream_qty.get(), peroxide2_price.get(), Date.get())) 
         
    if relaxer_cream_price.get() != 0: 
        c.execute("INSERT INTO Expenses VALUES (?, ?, ?, ?)",(Relaxer_cream , relaxer_cream_qty.get(), relaxer_cream_price.get(), Date.get())) 
        
    if other3_price.get() != 0:    
        c.execute("INSERT INTO Expenses VALUES (?, ?, ?, ?)",(other3.get(), other3_qty.get(), other3_price.get(), Date.get())) 
          
    if other4_price.get() != 0:    
        c.execute("INSERT INTO Expenses VALUES (?, ?, ?, ?)", (other4.get(), other4_qty.get(), other4_price.get(), Date.get())) 
 
    conn.commit()
   
    #Call on the Clear() function to clear the system.     
    if Total.get() > 0:
        Clear()
    #Print completion message to the receipt box
        txtReceipt.config(state=NORMAL)               
        txtReceipt.insert(END, 'Transaction Complete!')
        txtReceipt.config(state=DISABLED) 
        
#this function calls other functions to write to the transactions or expenses table, as appropriate 
def insert_transaction():
    if selection.get() == 1:
        insert_services()
    
    if selection.get() == 2:
        insert_expenses()


def Exit():
    root.destroy()
	
 
def get_trans_by_date(date):
    c.execute("SELECT * FROM Transactions WHERE date=:date", {'date': date})
    return c.fetchall()

total_trans = get_trans_by_date('12/12/2018')
print(total_trans)
      
	#this function grabs data from the database and displays it in the receipt textbox
def read_from_db():
    txtReceipt.config(state=NORMAL)
    txtReceipt.delete('1.0', END)
    txtReceipt.insert(END, 'Date:  ' + Date.get() + '\n\n' )    
    c.execute("SELECT * FROM Transactions WHERE date BETWEEN date('2019-01-03') AND date('2019-01-07')")
    for row in c.fetchall():
        txtReceipt.insert(END, row)
        
        
    txtReceipt.config(state=DISABLED)        
         
#txtReceipt.insert(END, other3.get() + ':' + ' ' + str(other3_qty.get()) + ' ' + '@'  + ' ' + '$' + str(other3_price.get()) + '\t\t\t\t' + '$' + #str(other3_qty.get() * other3_price.get()) + '\n')
  
#===========================Total box - right frame=====================

lblTotalCost = Label(leftFrame_receiptBox, font=('arial', 25, 'bold'), text='Total:', bg='white', bd=6, anchor='w')
lblTotalCost.grid(row=0, column=0, sticky=W)
txtTotalCost = Entry(leftFrame_receiptBox, font=('arial', 25, 'bold'), relief='groove', textvariable=Total, bd=6, width=10, bg='#ffffff', state=DISABLED)
txtTotalCost.grid(row=0, column=0, sticky=E)

lblCash = Label(leftFrame_receiptBox, font=('arial', 14, 'bold'), text='Cash:', bg='white', bd=6, anchor='w')
lblCash.grid(row=1, column=0)
txtCash = Entry(leftFrame_receiptBox, font=('arial', 14, 'bold'), relief='groove', textvariable=Cash, bd=6, width=10, bg='#ffffff', state=NORMAL)
txtCash.grid(row=1, column=0, sticky=E)
txtCash.bind('<Button-1>', lambda e: txtCash.delete(0, END))
txtCash.bind('<Return>', calChange)

lblchange = Label(leftFrame_receiptBox, font=('arial', 14, 'bold'), text='Change:', bg='white', bd=6, anchor='w')
lblchange.grid(row=2, column=0)
txtchange = Entry(leftFrame_receiptBox, font=('arial', 14, 'bold'), relief='groove', textvariable=Change, bd=6, width=10, bg='#ffffff', state=DISABLED)
txtchange.grid(row=2, column=0, sticky=E)

lblReceipt = Label(leftFrame_receiptBox, font=('arial', 14, 'bold'), text='Receipt:', bg='white', bd=2, anchor='w')
lblReceipt.grid(row=3, column=0, sticky=W)
txtReceipt = Text(leftFrame_receiptBox, font=('arial', 12, 'bold'), width= 40, height = 16, bg = 'white', bd=8, relief='groove')
txtReceipt.grid(row=4, column=0)

#===============================Services Menu1===================


lblservice1 = Label(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold', 'italic'), text='Service Menu', bd=8, justify='center')
lblservice1.grid(row=0, column=0, sticky=EW)

lblDescription = Label(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), text='Price', bd=8)
lblDescription.grid(row=0, column=1, sticky=W)
lblQty = Label(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), text='Qty', bd=8)
lblQty.grid(row=0, column=2, sticky=W)

lblH_cut_women = Label(leftFrame_Service_Menu1_Top, width=18, anchor='w', font=('arial', 12, 'bold'), text=hair_cut_woman, bd=8)
lblH_cut_women.grid(row=1, column=0, sticky=W)
txtH_cut_women1 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = hair_cut_woman_price, bd=2, width=5)
txtH_cut_women1.grid(row=1, column=1, sticky=W)
txtH_cut_women1.bind('<Button-1>', lambda e: txtH_cut_women1.delete(0, END))
txtH_cut_women2 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = hair_cut_woman_qty, bd=2, width=3)
txtH_cut_women2.grid(row=1, column=2, sticky=W)
lblmoney = Label(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), text='$', bd=8)
lblmoney.grid(row=1, column=0, sticky=E)

lblH_cut_man = Label(leftFrame_Service_Menu1_Top, width=14, anchor='w', font=('arial', 12, 'bold'), text=hair_cut_man, bd=8)
lblH_cut_man.grid(row=2, column=0, sticky=W)
txtH_cut_man1 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = hair_cut_man_price, bd=2, width=5)
txtH_cut_man1.grid(row=2, column=1, sticky=W)
txtH_cut_man1.bind('<Button-1>', lambda e: txtH_cut_man1.delete(0, END))
txtH_cut_man2 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = hair_cut_man_qty, bd=2, width=3)
txtH_cut_man2.grid(row=2, column=2, sticky=W)
lblmoney1 = Label(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), text='$', bd=8)
lblmoney1.grid(row=2, column=0, sticky=E)

lblH_cut_child = Label(leftFrame_Service_Menu1_Top, width=14, anchor='w', font=('arial', 12, 'bold'), text=hair_cut_child, bd=8)
lblH_cut_child.grid(row=3, column=0, sticky=W)
txtH_cut_child1 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = hair_cut_child_price, bd=2, width=5)
txtH_cut_child1.grid(row=3, column=1, sticky=W)
txtH_cut_child1.bind('<Button-1>', lambda e: txtH_cut_child1.delete(0, END))
txtH_cut_child2 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = hair_cut_child_qty, bd=2, width=3)
txtH_cut_child2.grid(row=3, column=2, sticky=W)
lblmoney2 = Label(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), text='$', bd=8)
lblmoney2.grid(row=3, column=0, sticky=E)

lblB_Dry = Label(leftFrame_Service_Menu1_Top, width=14,  anchor='w', font=('arial', 12, 'bold'), text=blow_dry, bd=8)
lblB_Dry.grid(row=4, column=0, sticky=W)
txtB_Dry1 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = blow_dry_price, bd=2, width=5)
txtB_Dry1.grid(row=4, column=1, sticky=W)
txtB_Dry1.bind('<Button-1>', lambda e: txtB_Dry1.delete(0, END))
txtB_Dry2 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = blow_dry_qty, bd=2, width=3)
txtB_Dry2.grid(row=4, column=2, sticky=W)
lblmoney7 = Label(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), text='$', bd=8)
lblmoney7.grid(row=4, column=0, sticky=E)

lblH_colour = Label(leftFrame_Service_Menu1_Top, width=14, anchor='w', font=('arial', 12, 'bold'), text=hair_colour, bd=8)
lblH_colour.grid(row=5, column=0, sticky=W)
txtH_colour1 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = hair_colour_price, bd=2, width=5)
txtH_colour1.grid(row=5, column=1, sticky=W)
txtH_colour1.bind('<Button-1>', lambda e: txtH_colour1.delete(0, END))
txtH_colour2 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = hair_colour_qty, bd=2, width=3)
txtH_colour2.grid(row=5, column=2, sticky=W)
lblmoney3 = Label(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), text='$', bd=8)
lblmoney3.grid(row=5, column=0, sticky=E)

lblRelexer = Label(leftFrame_Service_Menu1_Top, width=14,  anchor='w', font=('arial', 12, 'bold'), text=relaxer, bd=8)
lblRelexer.grid(row=6, column=0, sticky=W)
txtRelexer1 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = relaxer_price, bd=2, width=5)
txtRelexer1.grid(row=6, column=1, sticky=W)
txtRelexer1.bind('<Button-1>', lambda e: txtRelexer1.delete(0, END))
txtRelexer2 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = relaxer_qty, bd=2, width=3)
txtRelexer2.grid(row=6, column=2, sticky=W)
lblmoney4 = Label(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), text='$', bd=8)
lblmoney4.grid(row=6, column=0, sticky=E)

lblH_lights = Label(leftFrame_Service_Menu1_Top, width=14,  anchor='w', font=('arial', 12, 'bold'), text=high_lights, bd=8)
lblH_lights.grid(row=7, column=0, sticky=W)
txtH_lighthair_cut_woman = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = highlight_price, bd=2, width=5)
txtH_lighthair_cut_woman.grid(row=7, column=1, sticky=W)
txtH_lighthair_cut_woman.bind('<Button-1>', lambda e: txtH_lighthair_cut_woman.delete(0, END))
txtH_lighthair_cut_man = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = high_lights_qty, bd=2, width=3)
txtH_lighthair_cut_man.grid(row=7, column=2, sticky=W)
lblmoney5 = Label(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), text='$', bd=8)
lblmoney5.grid(row=7, column=0, sticky=E)

lblPerm = Label(leftFrame_Service_Menu1_Top, width=14,  anchor='w', font=('arial', 12, 'bold'), text=perm, bd=8)
lblPerm.grid(row=8, column=0, sticky=W)
txtPerm1 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = perm_price, bd=2, width=5)
txtPerm1.grid(row=8, column=1, sticky=W)
txtPerm1.bind('<Button-1>', lambda e: txtPerm1.delete(0, END))
txtPerm2 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = perm_qty, bd=2, width=3)
txtPerm2.grid(row=8, column=2, sticky=W)
lblmoney6 = Label(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), text='$', bd=8)
lblmoney6.grid(row=8, column=0, sticky=E)

lblUp = Label(leftFrame_Service_Menu1_Top, width=14,  anchor='w', font=('arial', 12, 'bold'), text=up_do, bd=8)
lblUp.grid(row=9, column=0, sticky=W)
txtUp1 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = up_do_price, bd=2, width=5)
txtUp1.grid(row=9, column=1, sticky=W)
txtUp1.bind('<Button-1>', lambda e: txtUp1.delete(0, END))
txtUp2 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = up_do_qty, bd=2, width=3)
txtUp2.grid(row=9, column=2, sticky=W)
lblmoney7 = Label(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), text='$', bd=8)
lblmoney7.grid(row=9, column=0, sticky=E)

lbldeep = Label(leftFrame_Service_Menu1_Top, width=14,  anchor='w', font=('arial', 12, 'bold'), text=deep_conditioner, bd=8)
lbldeep.grid(row=10, column=0, sticky=W)
txtdeep1 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = deep_cond_price, bd=2, width=5)
txtdeep1.grid(row=10, column=1, sticky=W)
txtdeep1.bind('<Button-1>', lambda e: txtdeep1.delete(0, END))
txtdeep2 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = deep_conditioner_qty, bd=2, width=3)
txtdeep2.grid(row=10, column=2, sticky=W)
lblmoney7 = Label(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), text='$', bd=8)
lblmoney7.grid(row=10, column=0, sticky=E)

lblwax = Label(leftFrame_Service_Menu1_Top, width=15, anchor='w', font=('arial', 12, 'bold'),  text=waxing, bd=8)
lblwax.grid(row=11, column=0, sticky=W)
txtwax1 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = waxing_price, bd=2, width=5)
txtwax1.grid(row=11, column=1, sticky=W)
txtwax1.bind('<Button-1>', lambda e: txtwax1.delete(0, END))
txtwax2 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'),  textvariable = waxing_qty, bd=2, width=3)
txtwax2.grid(row=11, column=2, sticky=W)
lblmoney13 = Label(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), text='$', bd=8)
lblmoney13.grid(row=11, column=0, sticky=E)

lbljap = Label(leftFrame_Service_Menu1_Top, width=15, anchor='w', font=('arial', 12, 'bold'), text=jap_perm, bd=8)
lbljap.grid(row=12, column=0, sticky=W)
txtjap1 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'),  textvariable = jap_perm_price, bd=2, width=5)
txtjap1.grid(row=12, column=1, sticky=W)
txtjap1.bind('<Button-1>', lambda e: txtjap1.delete(0, END))
txtjap2 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = jap_perm_qty, bd=2, width=3)
txtjap2.grid(row=12, column=2, sticky=W)
lblmoney13 = Label(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), text='$', bd=8)
lblmoney13.grid(row=12, column=0, sticky=E)

lbleyebrow = Label(leftFrame_Service_Menu1_Top, width=18, anchor='w', font=('arial', 12, 'bold'),  text=eyebrows, bd=8)
lbleyebrow.grid(row=13, column=0, sticky=W)
txteyebrow1 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'),  textvariable = eyebrow_price, bd=2, width=5)
txteyebrow1.grid(row=13, column=1, sticky=W)
txteyebrow1.bind('<Button-1>', lambda e: txteyebrow1.delete(0, END))
txteyebrow2 = Entry(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), textvariable = eyebrows_qty, bd=2, width=3)
txteyebrow2.grid(row=13, column=2, sticky=W)
lblmoney12 = Label(leftFrame_Service_Menu1_Top, font=('arial', 12, 'bold'), text='$', bd=8)
lblmoney12.grid(row=13, column=0, sticky=E)

#===============================Services Menu2===================

lblservice = Label(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold', 'italic'), text='Service Menu', bd=8, justify='center')
lblservice.grid(row=1, column=0, sticky=EW)

lblDescription2 = Label(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'),  text='Price', bd=8)
lblDescription2.grid(row=1, column=1, sticky=W)
lblQty = Label(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'),  text='Qty', bd=8)
lblQty.grid(row=1, column=2, sticky=W)

lblstyling = Label(leftFrame_Service_Menu2_Top, width=18, anchor='w', font=('arial', 12, 'bold'), text=hair_styling, bd=8)
lblstyling.grid(row=2, column=0, sticky=W)
txtstyling1 = Entry(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), textvariable = hair_styling_price, bd=2, width=5)
txtstyling1.grid(row=2, column=1, sticky=W)
txtstyling1.bind('<Button-1>', lambda e: txtstyling1.delete(0, END))
txtstyling2 = Entry(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), textvariable = hair_styling_qty, bd=2, width=3)
txtstyling2.grid(row=2, column=2, sticky=W)
lblmoney13 = Label(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), text='$', bd=8)
lblmoney13.grid(row=2, column=0, sticky=E)

lbltreat = Label(leftFrame_Service_Menu2_Top, width=15, anchor='w', font=('arial', 12, 'bold'), text=hair_treatment, bd=8)
lbltreat.grid(row=3, column=0, sticky=W)
txttreat1 = Entry(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), textvariable = hair_treatment_price, bd=2, width=5)
txttreat1.grid(row=3, column=1, sticky=W)
txttreat1.bind('<Button-1>', lambda e: txttreat1.delete(0, END))
txttreat2 = Entry(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), textvariable = hair_treatment_qty, bd=2, width=3)
txttreat2.grid(row=3, column=2, sticky=W)
lblmoney13 = Label(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), text='$', bd=8)
lblmoney13.grid(row=3, column=0, sticky=E)

lblxtentions = Label(leftFrame_Service_Menu2_Top, width=14,  anchor='w', font=('arial', 12, 'bold'), text=hair_ext, bd=8)
lblxtentions.grid(row=4, column=0, sticky=W)
txtxtentionhair_cut_woman = Entry(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), textvariable = hair_ext_price, bd=2, width=5)
txtxtentionhair_cut_woman.grid(row=4, column=1, sticky=W)
txtxtentionhair_cut_woman.bind('<Button-1>', lambda e: txtxtentionhair_cut_woman.delete(0, END))
txtxtentionhair_cut_man = Entry(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), textvariable = hair_ext_qty, bd=2, width=3)
txtxtentionhair_cut_man.grid(row=4, column=2, sticky=W)
lblmoney8 = Label(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), text='$', bd=8)
lblmoney8.grid(row=4, column=0, sticky=E)

lblfacial = Label(leftFrame_Service_Menu2_Top, width=15, anchor='w', font=('arial', 12, 'bold'), text=facial, bd=8)
lblfacial.grid(row=5, column=0, sticky=W)
txtfacial1 = Entry(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), textvariable = facial_price, bd=2, width=5)
txtfacial1.grid(row=5, column=1, sticky=W)
txtfacial1.bind('<Button-1>', lambda e: txtfacial1.delete(0, END))
txtfacial2 = Entry(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), textvariable = facial_qty, bd=2, width=3)
txtfacial2.grid(row=5, column=2, sticky=W)
lblmoney13 = Label(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), text='$', bd=8)
lblmoney13.grid(row=5, column=0, sticky=E)

lblproduct = Label(leftFrame_Service_Menu2_Top, width=15, anchor='w', font=('arial', 12, 'bold'), text=product_sale, bd=8)
lblproduct.grid(row=6, column=0, sticky=W)
txtproduct1 = Entry(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), textvariable = product_sale_price, bd=2, width=5)
txtproduct1.grid(row=6, column=1, sticky=W)
txtproduct1.bind('<Button-1>', lambda e: txtproduct1.delete(0, END))
txtproduct2 = Entry(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), textvariable = product_sale_qty, bd=2, width=3)
txtproduct2.grid(row=6, column=2, sticky=W)
lblmoney13 = Label(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), text='$', bd=8)
lblmoney13.grid(row=6, column=0, sticky=E)

txtOther1 = Entry(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), textvariable = other1, bd=2, width=15)
txtOther1.grid(row=7, column=0, sticky=W)
txtOther12 = Entry(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), textvariable = other1_price, bd=2, width=5)
txtOther12.grid(row=7, column=1, sticky=W)
txtOther12.bind('<Button-1>', lambda e: txtOther12.delete(0, END))
txtOther13 = Entry(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), textvariable = other1_qty, bd=2, width=3)
txtOther13.grid(row=7, column=2, sticky=W)
lblmoney10 = Label(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), text='$', bd=8)
lblmoney10.grid(row=7, column=0, sticky=E)

txtOther2 = Entry(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), textvariable = other2, bd=2, width=15)
txtOther2.grid(row=8, column=0, sticky=W)
txtOther22 = Entry(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), textvariable = other2_price, bd=2, width=5)
txtOther22.grid(row=8, column=1, sticky=W)
txtOther22.bind('<Button-1>', lambda e: txtOther22.delete(0, END))
txtOther23 = Entry(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), textvariable = other2_qty, bd=2, width=3)
txtOther23.grid(row=8, column=2, sticky=W)
lblmoney11 = Label(leftFrame_Service_Menu2_Top, font=('arial', 12, 'bold'), text='$', bd=8)
lblmoney11.grid(row=8, column=0, sticky=E)


#=============================================Expenses Menu=====
lblexpenses = Label(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold', 'italic'), bg='white', text='Expenses',  bd=8, justify='center')
lblexpenses.grid(row=0, column=0, sticky=EW)

lblDescription3 = Label(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'),  bg='white', text='Price', bd=8)
lblDescription3.grid(row=0, column=1, sticky=W)
lblQty3 = Label(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='white', text='Qty', bd=8)
lblQty3.grid(row=0, column=2, sticky=W)

lblp1 = Label(leftFrame_Expenses_Menu_Top, width=18, anchor='w', font=('arial', 12, 'bold'),  bg='white', text=Shampoo, bd=8)
lblp1.grid(row=2, column=0, sticky=W)
txtp1 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='powder blue',textvariable = shampoo_price, bd=2, width=5)
txtp1.grid(row=2, column=1, sticky=W)
txtp1.bind('<Button-1>', lambda e: txtp1.delete(0, END))
txtp2 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='powder blue',textvariable = conditioner_qty, bd=2, width=3)
txtp2.grid(row=2, column=2, sticky=W)
lblmoney12 = Label(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='white',text='$', bd=8)
lblmoney12.grid(row=2, column=0, sticky=E)

lblp2 = Label(leftFrame_Expenses_Menu_Top, width=15, anchor='w', font=('arial', 12, 'bold'),  bg='white', text=Conditioner, bd=8)
lblp2.grid(row=3, column=0, sticky=W)
txtp21 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'),bg='powder blue', textvariable = conditioner_price, bd=2, width=5)
txtp21.grid(row=3, column=1, sticky=W)
txtp21.bind('<Button-1>', lambda e: txtp21.delete(0, END))
txtp22 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='powder blue',textvariable = conditioner_qty, bd=2, width=3)
txtp22.grid(row=3, column=2, sticky=W)
lblmoney13 = Label(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'),  bg='white', text='$', bd=8)
lblmoney13.grid(row=3, column=0, sticky=E)

lblp3 = Label(leftFrame_Expenses_Menu_Top, width=15, anchor='w', font=('arial', 12, 'bold'),  bg='white', text=Hair_Colour1, bd=8)
lblp3.grid(row=4, column=0, sticky=W)
txtp31 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='powder blue',textvariable = hair_colour1_price, bd=2, width=5)
txtp31.grid(row=4, column=1, sticky=W)
txtp31.bind('<Button-1>', lambda e: txtp31.delete(0, END))
txtp32 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='powder blue',textvariable = hair_colour1_qty, bd=2, width=3)
txtp32.grid(row=4, column=2, sticky=W)
lblmoney13 = Label(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='white',text='$', bd=8)
lblmoney13.grid(row=4, column=0, sticky=E)

lblp4 = Label(leftFrame_Expenses_Menu_Top, width=15, anchor='w', font=('arial', 12, 'bold'), bg='white', text=Hair_Colour2, bd=8)
lblp4.grid(row=5, column=0, sticky=W)
txtp41 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'),bg='powder blue', textvariable = hair_colour2_price, bd=2, width=5)
txtp41.grid(row=5, column=1, sticky=W)
txtp41.bind('<Button-1>', lambda e: txtp41.delete(0, END))
txtp42 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'),bg='powder blue', textvariable = hair_colour2_qty, bd=2, width=3)
txtp42.grid(row=5, column=2, sticky=W)
lblmoney13 = Label(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='white', text='$', bd=8)
lblmoney13.grid(row=5, column=0, sticky=E)

lblp5 = Label(leftFrame_Expenses_Menu_Top, width=15, anchor='w', font=('arial', 12, 'bold'),bg='white', text=Peroxide1, bd=8)
lblp5.grid(row=6, column=0, sticky=W)
txtp51 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='powder blue',textvariable = peroxide1_price, bd=2, width=5)
txtp51.grid(row=6, column=1, sticky=W)
txtp51.bind('<Button-1>', lambda e: txtp51.delete(0, END))
txtp52 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='powder blue',textvariable = peroxide1_qty, bd=2, width=3)
txtp52.grid(row=6, column=2, sticky=W)
lblmoney13 = Label(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='white',text='$', bd=8)
lblmoney13.grid(row=6, column=0, sticky=E)

lblp6 = Label(leftFrame_Expenses_Menu_Top, width=14,  anchor='w', font=('arial', 12, 'bold'), bg='white',text=Latex_gloves, bd=8)
lblp6.grid(row=7, column=0, sticky=W)
txtp61 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'),bg='powder blue', textvariable = latex_gloves_price, bd=2, width=5)
txtp61.grid(row=7, column=1, sticky=W)
txtp61.bind('<Button-1>', lambda e: txtp61.delete(0, END))
txtp62 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'),bg='powder blue', textvariable = latex_gloves_qty, bd=2, width=3)
txtp62.grid(row=7, column=2, sticky=W)
lblmoney8 = Label(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='white',text='$', bd=8)
lblmoney8.grid(row=7, column=0, sticky=E)

lblp7 = Label(leftFrame_Expenses_Menu_Top, width=15, anchor='w', font=('arial', 12, 'bold'),bg='white', text=Peroxide2, bd=8)
lblp7.grid(row=8, column=0, sticky=W)
txtp71 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='powder blue',textvariable = peroxide2_price, bd=2, width=5)
txtp71.grid(row=8, column=1, sticky=W)
txtp71.bind('<Button-1>', lambda e: txtp71.delete(0, END))
txtp72 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='powder blue',textvariable = relaxer_cream_qty, bd=2, width=3)
txtp72.grid(row=8, column=2, sticky=W)
lblmoney13 = Label(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'),bg='white', text='$', bd=8)
lblmoney13.grid(row=8, column=0, sticky=E)

lblp8 = Label(leftFrame_Expenses_Menu_Top, width=15, anchor='w', font=('arial', 12, 'bold'),bg='white', text=Relaxer_cream, bd=8)
lblp8.grid(row=9, column=0, sticky=W)
txtp81 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='powder blue',textvariable = relaxer_cream_price, bd=2, width=5)
txtp81.grid(row=9, column=1, sticky=W)
txtp81.bind('<Button-1>', lambda e: txtp81.delete(0, END))
txtp82 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'),bg='powder blue', textvariable = relaxer_cream_qty, bd=2, width=3)
txtp82.grid(row=9, column=2, sticky=W)
lblmoney13 = Label(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'),bg='white', text='$', bd=8)
lblmoney13.grid(row=9, column=0, sticky=E)

txtOther3 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='white', textvariable = other3, bd=2, width=15)
txtOther3.grid(row=10, column=0, sticky=W)
txtOther31 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='powder blue', textvariable = other3_price, bd=2, width=5)
txtOther31.grid(row=10, column=1, sticky=W)
txtOther31.bind('<Button-1>', lambda e: txtOther31.delete(0, END))
txtOther32 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='powder blue', textvariable = other3_qty, bd=2, width=3)
txtOther32.grid(row=10, column=2, sticky=W)
lblmoney10 = Label(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'),bg='white', text='$', bd=8)
lblmoney10.grid(row=10, column=0, sticky=E)

txtOther4 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='white', textvariable = other4, bd=2, width=15)
txtOther4.grid(row=11, column=0, sticky=W)
txtOther41 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='powder blue', textvariable = other4_price, bd=2, width=5)
txtOther41.grid(row=11, column=1, sticky=W)
txtOther41.bind('<Button-1>', lambda e: txtOther41.delete(0, END))
txtOther42 = Entry(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'), bg='powder blue',textvariable = other4_qty, bd=2, width=3)
txtOther42.grid(row=11, column=2, sticky=W)
lblmoney11 = Label(leftFrame_Expenses_Menu_Top, font=('arial', 12, 'bold'),bg='white',text='$', bd=8)
lblmoney11.grid(row=11, column=0, sticky=E)

#btnTest=Button(leftFrame_Expenses_Menu_Top, padx=16, pady=1, fg='black', font=('arial', 16, 'bold'), height =3, relief='raised',  bd= 7, width=6,text='Test', command=read_from_db).grid(row=17, column=0, sticky=E)

#=============================================Calculator=====

text_Input = StringVar()
txtDisplay = Entry(leftFrame_Service_Menu2_Bottom, font=('arial', 14, 'bold'), textvariable=text_Input, bd=11, bg='powder blue', justify='center')

txtDisplay.grid(columnspan=4, row=0, column=0, sticky=EW)

#--------------------First row of numbers----------------------------------------------
btn7=Button(leftFrame_Service_Menu2_Bottom, padx=8, pady=8, fg='black', font=('arial', 14, 'bold'), text='7', bg='powder blue', width=4, command=lambda: buttonClick(7)).grid(row=1, column=0, sticky=W)

btn8=Button(leftFrame_Service_Menu2_Bottom, padx=8, pady=8, fg='black', font=('arial', 14, 'bold'), text='8', bg='powder blue', width=4, command=lambda: buttonClick(8)).grid(row=1, column=1)

btn9=Button(leftFrame_Service_Menu2_Bottom, padx=8, pady=8, fg='black', font=('arial', 14, 'bold'), text='9', bg='powder blue', width=4, command=lambda: buttonClick(9)).grid(row=1, column=2)

Addittion=Button(leftFrame_Service_Menu2_Bottom, padx=8, pady=8, fg='black', font=('arial', 14, 'bold'), text='+', bg='powder blue', width=4, command=lambda: buttonClick('+')).grid(row=1, column=3)

#--------------------Second row of numbers -----------------------------------------------
btn4=Button(leftFrame_Service_Menu2_Bottom, padx=8, pady=8, fg='black', font=('arial', 14, 'bold'), text='4', bg='powder blue', width=4, command=lambda: buttonClick(4)).grid(row=2, column=0)

btn5=Button(leftFrame_Service_Menu2_Bottom, padx=8, pady=8, fg='black', font=('arial', 14, 'bold'), text='5', bg='powder blue', width=4, command=lambda: buttonClick(5)).grid(row=2, column=1)

btn6=Button(leftFrame_Service_Menu2_Bottom, padx=8, pady=8, fg='black', font=('arial', 14, 'bold'), text='6', bg='powder blue', width=4, command=lambda: buttonClick(6)).grid(row=2, column=2)

Subtraction=Button(leftFrame_Service_Menu2_Bottom, padx=8, pady=8, fg='black', font=('arial', 14, 'bold'), text='-', bg='powder blue', width=4, command=lambda: buttonClick('-')).grid(row=2, column=3)

#----------------------Third row of numbers---------------------------------------------
btn1=Button(leftFrame_Service_Menu2_Bottom, padx=8, pady=8, fg='black', font=('arial', 14, 'bold'), text='1', bg='powder blue', width=4, command=lambda: buttonClick(1)).grid(row=3, column=0)

btn2=Button(leftFrame_Service_Menu2_Bottom, padx=8, pady=8, fg='black', font=('arial', 14, 'bold'), text='2', bg='powder blue', width=4, command=lambda: buttonClick(2)).grid(row=3, column=1)

btn3=Button(leftFrame_Service_Menu2_Bottom, padx=8, pady=8, fg='black', font=('arial', 14, 'bold'), text='3', bg='powder blue', width=4, command=lambda: buttonClick(3)).grid(row=3, column=2)

Multiply=Button(leftFrame_Service_Menu2_Bottom, padx=8, pady=8, fg='black', font=('arial', 14, 'bold'), text='*', bg='powder blue', width=4, command=lambda: buttonClick('*')).grid(row=3, column=3)

#-------------------------Fourth row of numbers------------------------------------------

btn0=Button(leftFrame_Service_Menu2_Bottom, padx=8, pady=8, fg='black', font=('arial', 14, 'bold'), text='0', bg='powder blue', width=4, command=lambda: buttonClick(0)).grid(row=4, column=0)

btnClear=Button(leftFrame_Service_Menu2_Bottom, padx=8, pady=8, fg='black', font=('arial', 14, 'bold'), text='C', width=4, bg='powder blue', command=btnClearDisplay).grid(row=4, column=1)

btnEquals=Button(leftFrame_Service_Menu2_Bottom, padx=8, pady=8, fg='black', font=('arial', 14, 'bold'), text='=', bg='powder blue', width=4, command=btnEqualsInput).grid(row=4, column=2)

Divide=Button(leftFrame_Service_Menu2_Bottom, padx=8, pady=8, fg='black', font=('arial', 14, 'bold'), text='/', bg='powder blue', width=4, command=lambda: buttonClick('/')).grid(row=4, column=3)



#==============Buttons on the bottom of total box ================
btncalTotal=Button(leftFrame_receiptBox, padx=16, pady=1, fg='black', font=('arial', 16, 'bold'), height =3, width=6, text='Total',  bd= 7, relief='raised', command=calTotal, justify='center').grid(row=12, column=0, sticky=W)

btnClear=Button(leftFrame_receiptBox, padx=16,  fg='black', font=('arial', 16, 'bold'), height =3,relief='raised', width=6,  bd= 7, text='Clear', command=Clear).grid(row=12, column=0)

btnComplete=Button(leftFrame_receiptBox, padx=16, pady=1, fg='black', font=('arial', 16, 'bold'), height =3, relief='raised',  bd= 7, width=6,text='Complete', command=insert_transaction).grid(row=12, column=0, sticky=E)

#==============TOP LABELS====================
        
lblTitle=Label(TopsL, font=('arial', 40, 'bold'), text='Carmen\'s Salon', bd=10, width = 45,  anchor='w', bg='white')
lblTitle.grid(row=0, column=0)

lblDate = Label(TopsR, font=('arial', 30, 'bold'), text=Date.get(), bd=10, width = 20, anchor='w',bg='white')
lblDate.grid(row=0, column=1, sticky=W)

R1 = Radiobutton(TopsR, font=('arial', 20, 'bold'), text="Service   ", bg='white',anchor='w', command=Disabling, variable=selection, value=1)
R1.grid(row=0, column=8, sticky=N)
R1.invoke()
R2 = Radiobutton(TopsR, font=('arial', 20, 'bold'), text="Expenses", bg='white', command=Disabling, variable=selection, value=2)
R2.grid(row=0, column=8, sticky=S)

btnExit=Button(TopsR, padx=16, pady=1, fg='black', font=('arial', 16, 'bold'), height =3, relief='raised', bd= 7, command=Exit, width=5,text='Exit')
btnExit.grid(row=0, column=10)


#========================END====================

root.mainloop()
c.close()
conn.close()    

