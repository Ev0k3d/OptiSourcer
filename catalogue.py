#imports
from tkinter import *

global totalprice

with open("currentuser.txt", "r") as cuser:
    uname = cuser.read().strip()
# Catalogues
SAINSBURYS_C = [
    ["Item 1", "Sainsbury's", "WARBURTONS WHITE MEDIUM", 1.25, 800, "G"],
       ["Item 2", "Sainsbury's", "DAILY'S WHITE BREAD MEDIUM", 0.39, 800, "G"],
       [
           "Item 3", "Sainsbury's", "WARBURTONS TOASTIE WHITE THICK", 0.95, 400,
           "G"
       ], ["Item 4", "Sainsbury's", "DAILY'S WHOLEMEAL MEDIUM", 0.39, 800, "G"],
       ["Item 5", "Sainsbury's", "WARBURTONS WHOLEMEAL MEDIUM", 0.92, 400, "G"]
    
]

TESCO_C = [["Item 1", "Tesco", "WARBURTONS WHITE MEDIUM", 1.25, 800, "G"],
           ["Item 2", "Tesco", "DAILY'S WHITE BREAD MEDIUM", 0.39, 800, "G"],
           [
               "Item 3", "Tesco", "WARBURTONS TOASTIE WHITE THICK", 0.95, 400,
               "G"
           ], ["Item 4", "Tesco", "DAILY'S WHOLEMEAL MEDIUM", 0.39, 800, "G"],
           ["Item 5", "Tesco", "WARBURTONS WHOLEMEAL MEDIUM", 0.92, 400, "G"]]

LIDL_C = [["Item 1", "Lidl", "WARBURTONS WHITE MEDIUM", 1.25, 800, "G"],
          ["Item 2", "Lidl", "DAILY'S WHITE BREAD MEDIUM", 0.39, 800, "G"],
          ["Item 3", "Lidl", "WARBURTONS TOASTIE WHITE THICK", 0.95, 400, "G"],
          ["Item 4", "Lidl", "DAILY'S WHOLEMEAL MEDIUM", 0.39, 800, "G"],
          ["Item 5", "Lidl", "WARBURTONS WHOLEMEAL MEDIUM", 0.95, 400, "G"]]

def Change_Basket(lbl, idx, calc, store_filename,pricelabel,price,catalogue):
    new_quantity=0
    # Open the store file and read the lines
    with open(store_filename, "r") as store:
        lines = store.readlines()
    # Check and update the quantity
    quantity = lines[idx].strip()
    if quantity == "":
      if calc==1:
        new_quantity = 1 
      else:
        new_quantity=0
        return
    elif calc == 2 and int(quantity) <= 1:
        new_quantity = 0

    else:
        if calc == 1:
            new_quantity = int(quantity) + 1
        elif calc == 2:
            new_quantity = int(quantity) - 1
        else:
            new_quantity = 0

    lines[idx] = str(new_quantity) + "\n"

    # Write the updated lines back to the file
    if new_quantity >= 0:
        with open(store_filename, "w") as store:
            if new_quantity == 0:
                lines[idx] = "" + "\n"
            store.writelines(lines)
                
    # Update the corresponding label
    price=catalogue[idx][3]
    lbl.config(text=str(new_quantity))
    with open (f"{uname}.txt") as pricing:
      line=pricing.readlines()
    totalprice=float(line[4].strip())
    float(totalprice)
    float(price)
    if calc==2:
      price=-price
    totalprice+=price
    totalprice=round(totalprice,2)
    #number formatting into price format
    whole=round(totalprice,0)
    whole2=round(totalprice,1)
    if totalprice==0.0:
      totalprice=str(totalprice)+"0"
    elif whole==totalprice:
      totalprice=str(totalprice)+"0"
    elif whole2==totalprice:
      totalprice=str(totalprice)+"0"
    else:
      str(totalprice)
    ####################################
    line[4]=str(totalprice)+"\n"
    with open (f"{uname}.txt","w") as newprice:
      newprice.writelines(line)
      pricelabel.configure(text="£"+str(totalprice))

def View_Basket(parent):
  # Set the background color to white
  background_color = "#ffffff"

  # Create a frame that will hold the scrollbar and the content
  main_frame = Frame(parent, bg=background_color)
  main_frame.pack(fill=BOTH, expand=True)

  # Add a scrollbar to the main frame
  scrollbar = Scrollbar(main_frame, orient=VERTICAL)
  scrollbar.pack(side=RIGHT, fill=Y)

  # Create a canvas to contain the frame where items will be displayed
  canvas = Canvas(main_frame,
                  bg=background_color,
                  yscrollcommand=scrollbar.set)
  canvas.pack(side=LEFT, fill=BOTH, expand=True)

  # Associate the scrollbar with the canvas
  scrollbar.config(command=canvas.yview)

  # Create a frame within the canvas to actually hold the catalogue items
  catalogue_frame = Frame(canvas, bg=background_color)
  canvas.create_window((0, 0), window=catalogue_frame, anchor="nw")

  # Configure the scroll region based on the content size
  def on_frame_configure(event):
      canvas.configure(scrollregion=canvas.bbox("all"))

  # Bind the configure event to update the scroll region
  catalogue_frame.bind("<Configure>", on_frame_configure)

  current_row = 0  # Initialize a row counter

  for name in ["Tesco:", "Sainsbury's:", "Lidl:"]:
      Label(catalogue_frame,
            text=name,
            bg=background_color,
            font=("Arial", 10, "bold")).grid(row=current_row,
                                             column=0,
                                             columnspan=6,
                                             padx=5,
                                             pady=10,
                                             sticky="w")
      if name == "Tesco:":
          catalogue = TESCO_C
          file = f"{uname}_t.txt"
      elif name == "Sainsbury's:":
          catalogue = SAINSBURYS_C
          file = f"{uname}_s.txt"
      else:
          catalogue = LIDL_C
          file = f"{uname}_l.txt"

      with open(file) as shop:
          basket_contents = shop.readlines()

      for index, quantity in enumerate(basket_contents):
          quantity = quantity.strip(
          )  # Ensure there's no leading/trailing whitespace

          if quantity.isdigit() and int(quantity) > 0:
              item = catalogue[index]

              #Pricing
              with open (f"{uname}.txt") as pricing:
                line=pricing.readlines()
              totalprice=line[4].strip()
              price = catalogue[index][3]
              pricelabel= Label(parent, text=f"£{totalprice}", bg=background_color, fg="green")
              pricelabel.place(x=730,y=10)


              # Add item name, price, and quantity to the basket display
              for k in range(len(item)):
                  if k == 5 or item[k] == "":
                      continue
                  elif k == 3:
                      Label(catalogue_frame,
                            text="£" + str(item[k]),
                            bg=background_color).grid(row=current_row + 1,
                                                      column=k,
                                                      padx=5,
                                                      pady=5,
                                                      sticky="w")
                  elif k == 4:
                      Label(catalogue_frame,
                            text=str(item[k]) + str(item[k + 1]),
                            bg=background_color).grid(row=current_row + 1,
                                                      column=k,
                                                      padx=5,
                                                      pady=5,
                                                      sticky="w")

                      if quantity == "":
                          quantity = 0
                      number = Label(catalogue_frame,
                                    text=quantity,
                                    bg=background_color)
                      number.grid(row=current_row + 1,
                            column=len(item)+2,
                            padx=5,
                            pady=5,
                            sticky="w")

                      
                      if name=="Tesco:":
                        T_minbtn = Button(catalogue_frame,
                          text="-",
                          bg=background_color,
                          command=lambda lbl=number, idx=index: Change_Basket(lbl, idx, 2, f"{uname}_t.txt",pricelabel,price,catalogue))
                        T_minbtn.grid(row=current_row + 1,
                        column=len(item)+1,
                        padx=5,
                        pady=5,
                        sticky="w")
                        T_plusbtn = Button(catalogue_frame,
                           text="+",
                           bg=background_color,
                           command=lambda lbl=number, idx=index:
                           Change_Basket(lbl, idx, 1, f"{uname}_t.txt",pricelabel,price,catalogue))
                        T_plusbtn.grid(row=current_row + 1,
                        column=len(item)+3,
                        padx=5,
                        pady=5,
                        sticky="w")
                      elif name=="Sainsbury's:":
                        S_minbtn = Button(catalogue_frame,
                        text="-",
                        bg=background_color,
                        command=lambda lbl=number, idx=index: Change_Basket(lbl, idx, 2, f"{uname}_s.txt",pricelabel,price,catalogue))
                        S_minbtn.grid(row=current_row + 1,
                        column=len(item)+1,
                        padx=5,
                        pady=5,
                        sticky="w")
                        S_plusbtn = Button(catalogue_frame,
                        text="+",
                        bg=background_color,
                        command=lambda lbl=number, idx=index:
                        Change_Basket(lbl, idx, 1, f"{uname}_s.txt",pricelabel,price,catalogue))
                        S_plusbtn.grid(row=current_row + 1,
                        column=len(item)+3,
                        padx=5,
                        pady=5,
                        sticky="w")
                      elif name=="Lidl:":
                        L_minbtn = Button(catalogue_frame,
                        text="-",
                        bg=background_color,
                        command=lambda lbl=number, idx=index: Change_Basket(lbl, idx, 2, f"{uname}_l.txt",pricelabel,price,catalogue))
                        L_minbtn.grid(row=current_row + 1,
                        column=len(item)+1,
                        padx=5,
                        pady=5,
                        sticky="w")
                        L_plusbtn = Button(catalogue_frame,
                        text="+",
                        bg=background_color,
                        command=lambda lbl=number, idx=index:
                        Change_Basket(lbl, idx, 1, f"{uname}_l.txt",pricelabel,price,catalogue))
                        L_plusbtn.grid(row=current_row + 1,
                        column=len(item)+3,
                        padx=5,
                        pady=5,
                        sticky="w")
                      
                      
                  else:
                      Label(catalogue_frame,
                            text=item[k],
                            bg=background_color).grid(row=current_row + 1,
                                                      column=k,
                                                      padx=5,
                                                      pady=5,
                                                      sticky="w")
        
              # Move to the next row for the next item
              current_row += 1

      # Add a separator for each store
      current_row += 1
      current_row += 1
      #pricelabel.configure(text=str(totalprice))

def display_catalogue(parent, catalogue, shopdog):
    # Define which shop's catalogue is being displayed
    if shopdog == "Sainsbury's Catalogue":
        dog = "sainsburys"
    elif shopdog == "Tesco Catalogue":
        dog = "tesco"
    elif shopdog == "Lidl Catalogue":
        dog = "lidl"
    else:
        print("Unknown catalogue")
        return

    with open("currentuser.txt", "r") as cuser:

        uname = cuser.read().strip()

    file_map = {
        "sainsburys": f"{uname}_s.txt",
        "tesco": f"{uname}_t.txt",
        "lidl": f"{uname}_l.txt"
    }  

    store_filename = file_map.get(dog)
    if store_filename is None:
        return

    # Set the background color to white
    background_color = "#ffffff"
  
    # Create a frame that will hold the scrollbar and the content
    main_frame = Frame(parent, bg=background_color)
    main_frame.pack(fill=BOTH, expand=True)

    # Add a scrollbar to the main frame
    scrollbar = Scrollbar(main_frame, orient=VERTICAL)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Create a canvas to contain the frame where items will be displayed
    canvas = Canvas(main_frame,
                    bg=background_color,
                    yscrollcommand=scrollbar.set)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Associate the scrollbar with the canvas
    scrollbar.config(command=canvas.yview)

    # Create a frame within the canvas to actually hold the catalogue items
    catalogue_frame = Frame(canvas, bg=background_color)
    canvas.create_window((0, 0), window=catalogue_frame, anchor="nw")

    # Configure the scroll region based on the content size
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    # Bind the configure event to update the scroll region
    catalogue_frame.bind("<Configure>", on_frame_configure)

    with open(store_filename, "r") as store:
        lines = store.readlines()

    for i in range(len(catalogue)):
        
        with open (f"{uname}.txt") as pricing:
          line=pricing.readlines()
        totalprice=line[4].strip()
        price = catalogue[i][3]
        shoppricelabel= Label(parent, text=f"£{totalprice}", bg=background_color, fg="green")
        shoppricelabel.place(x=730,y=10)
        for j in range(len(catalogue[i])):
            if j == 5 or catalogue[i][j] == "":
                continue
            elif j == 3:
                Label(catalogue_frame,
                      text="£" + str(catalogue[i][j]),
                      bg=background_color).grid(row=i + 1,
                                                column=j,
                                                padx=5,
                                                pady=5,
                                                sticky="w")
            elif j == 4:
                Label(catalogue_frame,
                      text=str(catalogue[i][j]) + str(catalogue[i][j + 1]),
                      bg=background_color).grid(row=i + 1,
                                                column=j,
                                                padx=5,
                                                pady=5,
                                                sticky="w")

                idx = i

                quantity = lines[idx].strip()
                if quantity == "":
                    quantity = 0
                number = Label(catalogue_frame,
                               text=quantity,
                               bg=background_color)
                number.grid(row=i + 1,
                            column=j + 4,
                            padx=5,
                            pady=5,
                            sticky="w")

                minbtn = Button(catalogue_frame,
                                text="-",
                                bg=background_color,
                                command=lambda lbl=number, idx=i:
                                Change_Basket(lbl, idx, 2, store_filename,shoppricelabel,price,catalogue))
                minbtn.grid(row=i + 1,
                            column=j + 3,
                            padx=5,
                            pady=5,
                            sticky="w")

                plusbtn = Button(catalogue_frame,
                                 text="+",
                                 bg=background_color,
                                 command=lambda lbl=number, idx=i:
                                 Change_Basket(lbl, idx, 1, store_filename,shoppricelabel,price,catalogue))
                plusbtn.grid(row=i + 1,
                             column=j + 5,
                             padx=5,
                             pady=5,
                             sticky="w")

            else:
                Label(catalogue_frame,
                      text=catalogue[i][j],
                      bg=background_color).grid(row=i + 1,
                                                column=j,
                                                padx=5,
                                                pady=5,
                                                sticky="w")

        Label(catalogue_frame, text="",
              bg=background_color).grid(row=i + 1, column=len(
                  catalogue[i]))  # Add a blank line for spacing


def search_catalogue(catalogue, search_term):
    search_results = []
    for item in catalogue:
        if any(term in item[2] for term in search_term.upper().split()):
            search_results.append(item)
    return search_results     
  
                        

################
