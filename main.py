import os
if not os.path.exists("currentuser.txt"):
  open("currentuser.txt", "x")
from tkinter import *
from catalogue import *
from PIL import ImageTk, Image

catopen = False
uname = ""
########################## Shop GUI #################################

# ^^^^^^^^^^^^^^^^^ make these 2 lines of
global basket_items
basket_items = []

def shopstart():
  global shopcat, shopdog

  def Back(parent):
      parent.destroy()

  def update_greeting():
      home_label.config(
          text=f"Hello, {uname}" if catopen else f"Welcome, {uname}")

  def display_search_results(catalogue_window, search_results, shopdog):
      for widget in catalogue_window.winfo_children():
          if widget != search_frame:  # Ensure the search frame is not destroyed
              widget.destroy()

      if not search_results:
          Label(catalogue_window,
                text="No items found",
                bg="white",
                fg="black",
                font=("Arial", 16)).pack(pady=10)
          Backbutton = Button(catalogue_window,
                              text="Back",
                              command=lambda: Back(catalogue_window))
          Backbutton.place(x=25, y=15)
          return

      product_frame = Frame(catalogue_window, bg="white")
      product_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
      display_catalogue(product_frame, search_results, shopdog)

      Backbutton = Button(catalogue_window,
                          text="Back",
                          command=lambda: Back(catalogue_window))
      Backbutton.place(x=25, y=15)

  def search_function(catalogue, catalogue_window, shopdog):
     
      search_term = search_entry.get().strip().upper()
      search_results = search_catalogue(catalogue, search_term)
      display_search_results(catalogue_window, search_results, shopdog)

  def open_catalogue(catalogue, shopdog):
      # Open and resize the image
      image = Image.open("searchicon.png")
      image = image.resize((20, 20), Image.Resampling.LANCZOS)  # Resize as needed
      photo = ImageTk.PhotoImage(image)

      global catopen
      catopen = True

      global catalogue_window
      catalogue_window = Toplevel(shop_home)
      catalogue_window.title(shopdog)
      catalogue_window.geometry("800x600")
      catalogue_window.configure(background="white")

      global search_frame
      search_frame = Frame(catalogue_window, bg="white")
      search_frame.pack(pady=10)

      global search_entry
      global search_button

      search_entry = Entry(search_frame, bd=5)

      # Keep a reference to the image
      search_button = Button(search_frame,
                           image=photo,
                           command=lambda: search_function(catalogue, catalogue_window, shopdog))
      search_entry.pack(side=LEFT, padx=5)
      search_button.pack(side=LEFT, padx=5)

      # Keep a reference to avoid garbage collection
      search_button.image = photo

      product_frame = Frame(catalogue_window, bg="white")
      product_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

      display_catalogue(product_frame, catalogue, shopdog)

      update_greeting()

      Backbutton = Button(catalogue_window,
                        text="Back",
                        command=lambda: Back(catalogue_window))
      Backbutton.place(x=25, y=15)


  def tesco_cat():
      shopcat = TESCO_C
      shopdog = "Tesco Catalogue"
      open_catalogue(shopcat, shopdog)

  def sains_cat():
      shopcat = SAINSBURYS_C
      shopdog = "Sainsbury's Catalogue"
      open_catalogue(shopcat, shopdog)

  def lidl_cat():
      shopcat = LIDL_C
      shopdog = "Lidl Catalogue"
      open_catalogue(shopcat, shopdog)

  def account():
      global catopen
      catopen = True
      catalogue_window = Toplevel(shop_home)
      catalogue_window.title("Your Account")
      catalogue_window.geometry("800x600")
      catalogue_window.configure(background="white")
      Label(catalogue_window,
            text="Your Account",
            bg="white",
            fg="black",
            font=("Arial", 16)).pack(pady=10)
      update_greeting()
      Backbutton = Button(catalogue_window,
                          text="Back",
                          command=lambda: Back(catalogue_window))
      Backbutton.place(x=25, y=15)

  def reoccuring():

      global catopen
      catopen = True
      catalogue_window = Toplevel(shop_home)
      catalogue_window.title("Reoccuring Purchases")
      catalogue_window.geometry("800x600")
      catalogue_window.configure(background="white")
      Label(catalogue_window,
            text="Reoccuring Purchases",
            bg="white",
            fg="black",
            font=("Arial", 16)).pack(pady=10)
      update_greeting()
      Backbutton = Button(catalogue_window,
                          text="Back",
                          command=lambda: Back(catalogue_window))
      Backbutton.place(x=25, y=15)

  def basket():
      global catopen
      catopen = True
      baskwin = Toplevel(shop_home)
      baskwin.title("Your Basket")
      baskwin.geometry("800x600")
      baskwin.configure(background="white")
      Label(baskwin,
            text="Your Basket",
            bg="white",
            fg="blue",
            font=("Arial", 16)).pack(pady=10)
      update_greeting()
      Backbutton = Button(baskwin,
                          text="Back",
                          command=lambda: Back(baskwin))
      Backbutton.place(x=25, y=15)
      View_Basket(baskwin)

  shop_home = Tk()
  shop_home.title("Welcome")
  shop_home.geometry("500x500")
  shop_home.configure(background="white")

  home_label = Label(shop_home,
                     text=f"Welcome, {uname}",
                     bg="white",
                     fg="black",
                     font=("Arial", 16))
  view_tesco_button = Button(shop_home,
                             text="View Tesco Catalogue",
                             command=tesco_cat)
  view_sains_button = Button(shop_home,
                             text="View Sainsbury's Catalogue",
                             command=sains_cat)
  view_lidl_button = Button(shop_home,
                            text="View Lidl Catalogue",
                            command=lidl_cat)
  account_button = Button(shop_home, text="Your Account", command=account)
  reoccuring_button = Button(shop_home,
                             text="Reoccuring Purchases",
                             command=reoccuring)


  #Icon by apien. thx for the only decent one i could find
    # Open and resize the image
  image = Image.open("basketicon.png")
  image = image.resize((20, 20), Image.Resampling.LANCZOS)  
  #Resize as needed
  photo = ImageTk.PhotoImage(image)
  basketbutton = Button(shop_home, image=photo, command=basket)
  basketbutton.image = photo


    
  home_label.pack(pady=20)
  view_tesco_button.pack(pady=10)
  view_sains_button.pack(pady=10)
  view_lidl_button.pack(pady=10)
  account_button.pack(pady=10)
  reoccuring_button.pack(pady=10)
  basketbutton.pack()
  shop_home.mainloop()


#shopstart()


def Account_Create():

    def Account_File():
        global uname, upass
        uname = newuserentry.get()
        upass = newpassentry.get()
        q = questionentry.get()
        a = answerentry.get()
        with open(f"{uname}.txt", 'w') as file:
            file.write(f"{uname}\n{upass}\n{q}\n{a}\n{0}")
        tesco = open(f"{uname}_t.txt", "a")
        sainsburys = open(f"{uname}_s.txt", "a")
        lidl = open(f"{uname}_l.txt", "a")
        for i in range(499):
            tesco.write("\n")
            sainsburys.write("\n")
            lidl.write("\n")
        rg.destroy()

    rg = Tk()
    rg.title("Create Account")
    rg.geometry("500x500")
    rg.configure(bg="white")

    Create_account = Label(rg,
                           text='Create account',
                           padx=5,
                           pady=5,
                           font=("Arial", 16),
                           bg="white",
                           fg="black")
    newuserlabel = Label(rg,
                         text="Username",
                         padx=5,
                         pady=5,
                         bg="white",
                         fg="black")
    newpasslabel = Label(rg,
                         text="Password",
                         padx=5,
                         pady=5,
                         bg="white",
                         fg="black")
    newuserentry = Entry(rg, bd=5)
    newpassentry = Entry(rg, bd=5, show="*")
    questionlabel = Label(rg,
                          text="Security question",
                          padx=5,
                          pady=5,
                          bg="white",
                          fg="black")
    answerlabel = Label(rg,
                        text="Answer",
                        padx=5,
                        pady=5,
                        bg="white",
                        fg="black")
    questionentry = Entry(rg, bd=5)
    answerentry = Entry(rg, bd=5)
    Registerbutton = Button(rg, text="Register", command=Account_File)

    #####################################PACKING#####################
    Create_account.pack(pady=10)
    newuserlabel.pack()
    newuserentry.pack()
    newpasslabel.pack()
    newpassentry.pack()
    questionlabel.pack()
    questionentry.pack()
    answerlabel.pack()
    answerentry.pack()
    Registerbutton.pack(pady=10)
    rg.mainloop()


def login():

    def authuser():
        global uname, upass
        uname = userentry.get()
        try:
            with open(f"{uname}.txt", 'r') as file:
                lines = file.readlines()
                stored_username = lines[0].strip()
                stored_password = lines[1].strip()
                if userentry.get() == stored_username and passentry.get(
                ) == stored_password:
                    try:
                      with open("currentuser.txt", "w") as cuser:
                          cuser.write(stored_username)
                    except FileNotFoundError:
                      with open("currentuser.txt", "x") as cuser:
                        cuser.write(stored_username)
                  
                    lg.destroy()
                    shopstart()
                else:
                    print("Incorrect username or password")#change into label
        except FileNotFoundError:
            print("User not found")

    def securityquestion(fp, answerinputentry, newpassentry):

        def check_answer():
            given_answer = answerinputentry.get()
            if given_answer == stored_answer:
                confirmanswerbutton.destroy()
                newpasslabel = Label(fp,
                                     text="New password",
                                     padx=5,
                                     pady=5,
                                     bg="white",
                                     fg="black")
                newpasslabel.pack()
                newpassentry.pack()

                def update_password():
                    new_password = newpassentry.get()
                  
                    with open(f"{uname}.txt", 'w') as file:
                        file.write(
                            f"{uname}\n{new_password}\n{stored_question}\n{stored_answer}")
                    
                    fp.destroy()

                updatebutton = Button(fp,
                                      text="Update Password",
                                      command=update_password)
                updatebutton.pack(pady=10)
            else:
                error_label = Label(fp,
                                    text="Incorrect answer. Try again.",
                                    fg="red",
                                    bg="white")
                error_label.pack(pady=10)
                fp.after(2000, error_label.destroy
                         )  # Remove the error message after 2 seconds

        global stored_question, stored_answer
        try:
            with open(f"{uname}.txt", 'r') as file:
                confirmbutton.destroy()
                lines = file.readlines()
                stored_question = lines[2].strip()
                stored_answer = lines[3].strip()
                questionbox = Label(fp,
                                    text="Security question",
                                    padx=5,
                                    pady=5,
                                    bg="white",
                                    fg="black")
                questionoutput = Label(fp,
                                       text=stored_question,
                                       padx=5,
                                       pady=5,
                                       bg="white",
                                       fg="black")
                answeroutput = Label(fp,
                                     text="Answer",
                                     padx=5,
                                     pady=5,
                                     bg="white",
                                     fg="black")
                questionbox.pack()
                questionoutput.pack()
                answeroutput.pack()
                answerinputentry.pack()
                global confirmanswerbutton
                confirmanswerbutton = Button(fp,
                                             text="Confirm Answer",
                                             command=check_answer)
                confirmanswerbutton.pack(pady=10)
        except FileNotFoundError:
            error_label = Label(fp,
                                text="User not found",
                                fg="red",
                                bg="white")
            error_label.pack(pady=10)
            fp.after(2000, error_label.destroy)

    def forgot_password():
        global uname
        global confirmbutton
        fp = Tk()
        fp.title("Recover password")
        fp.geometry("500x500")
        fp.configure(bg="white")

        userlabel = Label(fp,
                          text="Username",
                          padx=5,
                          pady=5,
                          bg="white",
                          fg="black")
        userlabel.pack()
        userentry = Entry(fp, bd=5)
        userentry.pack()

        answerinputentry = Entry(fp, bd=5)
        newpassentry = Entry(fp, bd=5, show="*")

        def get_username():

            global uname
            uname = userentry.get()
            securityquestion(fp, answerinputentry, newpassentry)

        confirmbutton = Button(fp, text="Confirm", command=get_username)
        confirmbutton.pack(pady=10)

    lg = Tk()
    lg.title("Sign in")
    lg.geometry("500x500")
    lg.configure(bg="white")

    signin = Label(lg,
                   text="Sign in",
                   padx=5,
                   pady=5,
                   font=("Arial", 16),
                   bg="white",
                   fg="black")
    userlabel = Label(lg,
                      text="Username",
                      padx=5,
                      pady=5,
                      bg="white",
                      fg="black")
    passlabel = Label(lg,
                      text="Password",
                      padx=5,
                      pady=5,
                      bg="white",
                      fg="black")
    userentry = Entry(lg, bd=5)
    passentry = Entry(lg, bd=5, show="*")
    signbutton = Button(lg, text="Sign In", command=authuser)
    forgot_passwordbutton = Button(lg,
                                   text="Forgot Password?",
                                   command=forgot_password)
    Create_Accountbutton = Button(lg,
                                  text="Create Account",
                                  command=Account_Create)

    #####################################PACKING#####################
    signin.pack(pady=10)
    userlabel.pack()
    userentry.pack()
    passlabel.pack()
    passentry.pack()
    signbutton.pack(pady=10)
    forgot_passwordbutton.pack(pady=10)
    Create_Accountbutton.place(x=350, y=350)
    lg.mainloop()

login()
#shopstart()#REMOVE after testing
