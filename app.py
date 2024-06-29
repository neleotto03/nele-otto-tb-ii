# Tech Basics 1: GrandHelp prototype from Nele Otto


import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import math
import random
import requests


'New'
#test data:
volunteers = {"neleotto03": {"name": "Nele Otto", "age":20, "status": "ready to help", "location": "Helmbrechts",
                            "stars":0, "points":2000, "password":"1","profile pic": None},
            "Volunteer3": {"name": "Thomas", "age":28, "status": "ready to help", "location": "Berlin",
                            "stars":0, "points":0, "password":"qwe","profile pic": None},
              "Volunteer2": {"name": "victoria", "age":22, "status": "not ready to help", "location": "Munich",
                            "stars":0, "points":0, "password":"123", "profile pic": None}
              }
elderlys = {"Senior1": {"name": "Helga", "age": 83, "location": "Münchberg",
                       "stars":0 , "password": "2", "profile pic": None},
           "Senior2": {"name": "Victoria", "age": 70, "location": "Munich",
                        "stars": 0, "password": "123", "profile pic": None}}

inquiries = [{"elderly": "Senior1", "volunteer": "neleotto03", "service": "Shopping",
              "describtion": "Buy me some milk and bread.", "distance": 5, "status": "Accept!"}]

selected_user_type = None
selected_user_name = None


# Tkinter GUI setup
root = tk.Tk()
root.title("GrandHelp App")
root.geometry("650x450")
root.config(bg="white")


# function that adds background image
def add_image(root, file_path):
    global pic, f1

    f1 = tk.Frame(root)
    img = Image.open(file_path)
    img = img.resize((650, 450), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()


'New:' # Function that adds 2 background images next to each other
def add_two_images(root, left_image_path, right_image_path):
    # Create a Frame to hold the images
    f1 = tk.Frame(root)

    # Open and resize the left image
    left_img = Image.open(left_image_path)
    left_img = left_img.resize((325, 450), Image.LANCZOS)
    left_pic = ImageTk.PhotoImage(left_img)

    # Open and resize the right image
    right_img = Image.open(right_image_path)
    right_img = right_img.resize((325, 450), Image.LANCZOS)
    right_pic = ImageTk.PhotoImage(right_img)

    # Create Labels to display the images
    left_label = tk.Label(f1, image=left_pic)
    left_label.image = left_pic  # Keep a reference to avoid garbage collection
    right_label = tk.Label(f1, image=right_pic)
    right_label.image = right_pic  # Keep a reference to avoid garbage collection

    # Pack the labels side by side
    left_label.pack(side=tk.LEFT)
    right_label.pack(side=tk.RIGHT)

    # Pack the Frame
    f1.pack()


#function that destroys all widgets
def clear_widgets(root): #source: https://github.com/shaq31415926/python_tech_basics/blob/main/tech_basics_two/12Lecture/sarah-haq-tbii-exam-streamA/src/helpers.py
    for i in root.winfo_children():
        i.destroy()


# function that selects the user type and turns the button red or white
def select_user_type(user_type):
    global selected_user_type
    selected_user_type = user_type
    volunteer_button.config(bg="green" if selected_user_type == "Volunteer" else "white")
    eldery_button.config(bg="green" if selected_user_type == "Elderly" else "white")


#Code of the different pages in the following:

def welcome_page():
    clear_widgets(root)  
    add_image(root, file_path="images/welcome_page.png")

    enter_button = tk.Button(text="Start",
                             font='Montserrat 20 bold',
                             command=lambda: start_page(),
                             fg="black", bg="white")
    enter_button.place(x=285, y=370)

    info_button = tk.Button(text="Information",
                             font='Montserrat 20 bold',
                             command=lambda: first_info_page(),
                             fg="black", bg="white")
    info_button.place(x=20, y=370)


def start_page():
    clear_widgets(root)
    add_image(root, file_path="images/Log_in_page.png")

    log_in_button = tk.Button(root, text="Log in", command=lambda: log_in_page(), font='lucida 15 bold', bg="white")
    log_in_button.place(x=290, y=230)
    register_button = tk.Button(root, text="Register", command=lambda: register_page(),
                                font='lucida 15 bold', bg="white")
    register_button.place(x=280, y=330)
    back_button = tk.Button(text="back", font='lucida 15 bold', bg="white", command=lambda: welcome_page(),
                            fg="blue")
    back_button.place(x=540, y=400)


'New:'
def information_volunteer():
    clear_widgets(root)
    add_image(root, file_path="images/Information_volunteer.png")
    button_next = tk.Button(root, text="Next", font='lucida 15 bold', command= lambda:volunteer_info_page_1(), fg="blue", bg="white")
    button_next.place(x=430, y=400)

    back_button = tk.Button(text="back", font='lucida 15 bold', bg="white", command=lambda: first_info_page(),
                            fg="blue")
    back_button.place(x=540, y=400)


'New:'
def information_elderly():
    clear_widgets(root)
    add_image(root, file_path="images/Information_elderly.png")
    button_next = tk.Button(root, text="Next", font='lucida 15 bold', command= lambda:elderly_info_page_1(), fg="blue", bg="white")
    button_next.place(x=430, y=400)

    back_button = tk.Button(text="back", font='lucida 15 bold', bg="white", command=lambda: first_info_page(),
                            fg="blue")
    back_button.place(x=540, y=400)


'New:'
#info page
def first_info_page():
    clear_widgets(root)
    add_image(root, file_path="images/Choice.png")
    vol_button = tk.Button(root, text="I could help people", font='lucida 15 bold', bg="white",
                                 command=lambda: information_volunteer())
    vol_button.place(x=230, y=150)

    eld_button = tk.Button(root, text="I need some help", font='lucida 15 bold', bg="white",
                              command=lambda: information_elderly())
    eld_button.place(x=240, y=220)

    back_button = tk.Button(text="back", font='lucida 15 bold', bg="white", command=lambda: welcome_page(),
                            fg="blue")
    back_button.place(x=540, y=400)


'New:'
def volunteer_info_page_1():
    clear_widgets(root)
    add_image(root, file_path="images/Volunteer_info_1.png")
    button_next = tk.Button(root, text="Next", font='lucida 15 bold', command= lambda:volunteer_info_page_2(), fg="blue", bg="white")
    button_next.place(x=430, y=400)

    back_button = tk.Button(text="back", font='lucida 15 bold', bg="white", command=lambda: information_volunteer(),
                            fg="blue")
    back_button.place(x=540, y=400)


'New:'
def volunteer_info_page_2():
    clear_widgets(root)
    add_image(root, file_path="images/Volunteer_info_2.png")
    button_next = tk.Button(root, text="Next", font='lucida 15 bold', command= lambda:welcome_page(), fg="blue", bg="white")
    button_next.place(x=430, y=400)

    back_button = tk.Button(text="back", font='lucida 15 bold', bg="white", command=lambda: volunteer_info_page_1(),
                            fg="blue")
    back_button.place(x=540, y=400)


'New:'
def elderly_info_page_1():
    clear_widgets(root)
    add_image(root, file_path="images/Elderly_info_1.png")
    button_next = tk.Button(root, text="Next", font='lucida 15 bold', command= lambda:elderly_info_page_2(), fg="blue", bg="white")
    button_next.place(x=430, y=400)

    back_button = tk.Button(text="back", font='lucida 15 bold', bg="white", command=lambda: information_elderly(),
                            fg="blue")
    back_button.place(x=540, y=400)


'New:'
def elderly_info_page_2():
    clear_widgets(root)
    add_image(root, file_path="images/Elderly_info_2.png")
    button_next = tk.Button(root, text="Next", font='lucida 15 bold', command= lambda:welcome_page(), fg="blue", bg="white")
    button_next.place(x=430, y=400)

    back_button = tk.Button(text="back", font='lucida 15 bold', bg="white", command=lambda: elderly_info_page_1(),
                            fg="blue")
    back_button.place(x=540, y=400)
    

##registration page
def register_page():
    clear_widgets(root)
    add_image(root, file_path="images/Register.png")
    global entry_username, entry_password, entry_name, entry_age, entry_location, volunteer_button, eldery_button

    volunteer_button = tk.Button(root, text="I am a helper", font='lucida 15 bold', bg="white",
                                 command=lambda: select_user_type("Volunteer"))
    volunteer_button.place(x=20, y=70)

    eldery_button = tk.Button(root, text="I am an elderly person", font='lucida 15 bold', bg="white",
                              command=lambda: select_user_type("Elderly"))
    eldery_button.place(x=190, y=70)

    label_username = tk.Label(root, text="Username:", font='lucida 15 bold', bg="white")
    label_username.place(x=20, y=125)

    entry_username = tk.Entry(root, font= 'lucida 15 bold', bg="white")
    entry_username.place(x=20, y=160, width=220, height=25)

    label_password = tk.Label(root, text="Password:", font='lucida 15 bold', bg="white")
    label_password.place(x=20, y=190)

    entry_password = tk.Entry(root, font= 'lucida 15 bold', bg="white")
    entry_password.place(x=20, y=225, width=220, height=25)

    label__name = tk.Label(root, text="Full Name:", font='lucida 15 bold', bg="white")
    label__name.place(x=20, y=255)

    entry_name = tk.Entry(root, font= 'lucida 15 bold', bg="white")
    entry_name.place(x=20, y=290, width=220, height=25)

    label_age = tk.Label(root, text="Age:", font='lucida 15 bold', bg="white")
    label_age.place(x=20, y=320)

    entry_age = tk.Entry(root, font= 'lucida 15 bold', bg="white")
    entry_age.place(x=20, y=355, width=220, height=25)

    label_location = tk.Label(root, text="Location:", font='lucida 15 bold', bg="white")
    label_location.place(x=20, y=385)

    entry_location = tk.Entry(root, font= 'lucida 15 bold', bg="white")
    entry_location.place(x=20, y=420, width=220, height=25)

    button_register = tk.Button(root, text="Next", font='lucida 15 bold', command=register_user, fg="blue", bg="white")
    button_register.place(x=430, y=400)

    back_button = tk.Button(text="back", font='lucida 15 bold', bg="white", command=lambda: start_page(),
                            fg="blue")
    back_button.place(x=540, y=400)

# complimentary functions for registration page

# # function to register users
def register_user():
    username = entry_username.get()
    name = entry_name.get()
    password = entry_password.get()
    age = entry_age.get()
    location = entry_location.get()
    if name and password and age and username and selected_user_type:
        if selected_user_type == "Volunteer":  # If the Volunteer button is selected
            if username not in volunteers:
                volunteers[username] = {"name": name, "age": age, "status": "ready to help", "location": location,
                                        "stars": 0, "points": 0, "password": password, "profile pic" : None}
                print(volunteers)
                upload_profile_pic_page(username, "registration page")
            else:
                error_username_in_use()
        elif selected_user_type == "Elderly":  # If the Elderly button is selected
            if username not in elderlys:
                elderlys[username] = {"name": name, "age": age, "location": location, "stars": 0, "password": password,
                                      "profile pic" : None}
                print(elderlys)
                upload_profile_pic_page(username, "registration page")
            else:
                error_username_in_use()
        else:
            error_incomplete_information()
    else:
        error_incomplete_information()


#username is aready in use
def error_username_in_use():
    clear_widgets(root)
    add_image(root, file_path="images/GH_pic4.jpg")
    error_registration = tk.Label(root, text="Username is already in use!\nPlease think of a different one.",
                                  font = 'lucida 20 bold', fg="red")
    error_registration.place(x=20, y=25)
    okay_button = tk.Button(text="Okay", command=lambda: register_page(), font = 'lucida 15 bold')
    okay_button.place(x=20, y=150)


#information is incomplete
def error_incomplete_information():
    clear_widgets(root)
    add_image(root, file_path="images/GH_pic4.jpg")
    error_registration = tk.Label(root, text="Incomplete Information! \n Please fill in all the fields.",
                                  font = 'lucida 20 bold', fg="red")
    error_registration.place(x=20, y=25)
    okay_button = tk.Button(text="Okay", command=lambda: register_page(), font = 'lucida 15 bold')
    okay_button.place(x=20, y=150)


## page that shows that the registration is approved
def reg_approved():
    clear_widgets(root)
    add_image(root, file_path="images/GH_pic4.jpg")
    approve = tk.Label(root, text="Your registration was successful!", font='lucida 20 bold', fg="green")
    approve.place(x=95, y=40)
    continue_button = tk.Button(root, text="Continue", font='lucida 15 bold', command=lambda: log_in_page())
    continue_button.place(x=260, y=90)


'New:'
# page to upload the profile picture of the user
def upload_profile_pic_page(user, route):
    clear_widgets(root)
    global image_label, file_path
    file_path = None
    upload_button = tk.Button(root, text="Upload your profile picture", command=lambda:select_image(), font='lucida 20 bold', fg="white", bg="lightblue")
    upload_button.pack(pady=10)

    image_label = tk.Label(root)
    image_label.pack(pady=10)

    save_button = tk.Button(root, text="Save Profile Picture", command=lambda:save_image(user, file_path, route), font='lucida 20 bold', fg="black")
    save_button.pack(pady=10)


'New:'
# Function to save the selected image (to be integrated with database storage)
def save_image(user, file_path, route):
    if file_path:
        if user in volunteers:
            volunteers[user]["profile pic"] = file_path #saves the file_path in the database (Array) for volunteers or seniors
        else:
            elderlys[user]["profile pic"] = file_path
        print("Image saved to database.")
    else:
        print("No image to save.")

    if route == "profile page":
        profile_page(user)
    else:
        reg_approved()


'New:'
# Function to handle image selection and display
def select_image():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]) #source: https://www.w3resource.com/python-exercises/tkinter/python-tkinter-dialogs-and-file-handling-exercise-8.php
    if file_path:
        display_image(file_path)
    else:
        file_path = None


'New:'
# Function to display selected image
def display_image(file): #source: https://www.w3resource.com/python-exercises/tkinter/python-tkinter-dialogs-and-file-handling-exercise-8.php
    global profile_image, image_label
    image = Image.open(file)
    image = image.resize((325, 225),Image.Resampling.LANCZOS)  # Resize image as needed
    profile_image = ImageTk.PhotoImage(image)
    image_label.config(image=profile_image)
    image_label.image = profile_image
    

#Page to log in for registrated users
def log_in_page():
    clear_widgets(root)
    add_image(root, file_path="images/Log_in.png")
    global username_entry, password_entry
    label_name = tk.Label(root, text="Username:", font='lucida 15 bold', bg="white")
    label_name.place(x=280, y=170)
    username_entry = tk.Entry(root, font= 'lucida 15 bold', bg="white")
    username_entry.place(x=225, y=210, width=220, height=25)
    label_n = tk.Label(root, text="Password:", font='lucida 15 bold', bg="white")
    label_n.place(x=280, y=250)
    password_entry = tk.Entry(root, font= 'lucida 15 bold', show="*", bg="white")
    password_entry.place(x=225, y=290, width=220, height=25)
    sign_in_button = tk.Button(root, text="log in", font='lucida 15 bold', command=log_in, bg="white")
    sign_in_button.place(x=295, y=330)
    back_button = tk.Button(text="back", font='lucida 15 bold', command= lambda: start_page(),
                            fg="blue", bg="white")
    back_button.place(x=540, y=370)


#complimentary function for the log in page that compares password and username
def log_in():
    username = username_entry.get()
    password = password_entry.get()
    if username in volunteers:
        if volunteers[username]["password"] == password:
            menu_page(username)
        else:
            error_p()
    elif username in elderlys:
        if elderlys[username]["password"] == password:
            menu_page(username)
        else:
            error_p()
    else:
        error_u()


##pop-up page when the passwort is wrong
def error_p():
    clear_widgets(root)
    add_image(root, file_path="images/GH_pic1.jpg")
    error_result = tk.Label(root, text="Wrong password! Try it again!",font='lucida 20 bold', fg="red", bg="white")
    error_result.place(x=20, y=30)
    ok_button = tk.Button(text="Okay", command=lambda: log_in_page(), font='lucida 15 bold', bg="white")
    ok_button.place(x=20, y=100)

##pop-up page when the username is wrong
def error_u():
    clear_widgets(root)
    add_image(root, file_path="images/GH_pic1.jpg")
    error_result = tk.Label(root, text="The username doesn't exist! Try it again",font='lucida 20 bold', fg="red", bg="white")
    error_result.place(x=20, y=30)
    ok_button = tk.Button(text="Okay", command=lambda: log_in_page(), font='lucida 15 bold', bg="white")
    ok_button.place(x=20, y=100)

# main page for the user to navigate; with overview
def menu_page( user):
    clear_widgets(root)
    add_image(root, file_path="images/menu_page.png.")

    if user in volunteers:
        x = volunteers[user]["name"]
    else:
        x = elderlys[user]["name"]
    l = tk.Label(root, text="Hello "+x+"!", font = 'lucida 15 bold', fg = "green", bg= "white")
    l.place(x=20, y=100)
    profile_button = tk.Button(text="Show profile!", font='lucida 15 bold', bg= "white",
                               command=lambda: profile_page(user))
    profile_button.place(x=20, y=150)
    if user in elderlys:
        inquiry_button = tk.Button(text="I could need some help!", font='lucida 15 bold', bg= "white",
                                   command=lambda: asking_for_help_window(user))
        inquiry_button.place(x=20, y=220)
        sent_inquiry_button = tk.Button(text= "Sent inquiries", font='lucida 15 bold', bg= "white",
                                   command=lambda: sent_inquiry_window(user))
        sent_inquiry_button.place(x=20, y=290)
    elif user in volunteers:
        set_status_button = tk.Button(text="Set your status here", font='lucida 15 bold', bg= "white",
                                        command=lambda: set_status_window(user))
        set_status_button.place(x=20, y=220)
        incoming_inquiry_button = tk.Button(text="Incoming inquiries", font='lucida 15 bold', bg= "white",
                                        command=lambda: incoming_inquiry_window(user))
        incoming_inquiry_button.place(x=20, y=290)
        points_button = tk.Button(text="Redeem points", font='lucida 15 bold', bg= "white",
                                            command=lambda: points_window(user))
        points_button.place(x=20, y=360)

    log_out_button = tk.Button(text="Log out", font='lucida 15 bold', command= lambda: welcome_page(), fg="blue", bg= "white")
    log_out_button.place(x=540, y=370)

# page that shows the profile of the user with different features
def profile_page(user):
    clear_widgets(root)
    if user in volunteers:
        if volunteers[user]["profile pic"] is not None:
            add_two_images(root, "images/Half_background.png", volunteers[user]["profile pic"])
            print("1v")
        else: add_two_images(root, "images/Half_background.png", "images/no_profile_pic.png")
    elif user in elderlys:
        if elderlys[user]["profile pic"] is not None:
            add_two_images(root, "images/Half_background.png", elderlys[user]["profile pic"])
            print("2v")
        else:add_two_images(root, "images/Half_background.png", "images/no_profile_pic.png")

        print("two")
    profile_data = None
    if user in volunteers:
        profile_data = volunteers[user]
    elif user in elderlys:
        profile_data = elderlys[user]

    label_profile_window = tk.Label(root, text="Profile of " + user, font = 'lucida 20 bold', fg="white", bg="lightblue")
    label_profile_window.place(x=30, y=25)

    label_name_profile = tk.Label(root, text="Name: " + profile_data["name"], font = 'lucida 15 bold')
    label_name_profile.place(x=20, y=95)

    label_age_profile = tk.Label(root, text="Age: " + str(profile_data["age"]), font = 'lucida 15 bold')
    label_age_profile.place(x=20, y=140)

    age_change_button = tk.Button(root, text="Change Age", command=lambda: open_age_change_window(user),
                                  font = 'lucida 15 bold')
    age_change_button.place(x=20, y=175)

    label_location_profile = tk.Label(root, text="Location: " + profile_data["location"], font = 'lucida 15 bold')
    label_location_profile.place(x=20, y=235)

    location_change_button = tk.Button(root, text="Change Location", command=lambda: open_location_change_window(user),
                                       font = 'lucida 15 bold')
    location_change_button.place(x=20, y=270)

    label_stars_profile = tk.Label(root, text="Stars: " + str(profile_data["stars"]), font = 'lucida 15 bold')
    label_stars_profile.place(x=20, y=330)

    if user in volunteers:
        label_status_profile = tk.Label(root, text="Status: " + profile_data["status"], font = 'lucida 15 bold')
        label_status_profile.place(x=20, y=370)
        label_points_profile = tk.Label(root, text="Points: " + str(profile_data["points"]), font = 'lucida 15 bold')
        label_points_profile.place(x=20, y=410)
    else:
        label_points_profile = tk.Label(root, text="")
        label_points_profile.pack()
        label_status_profile = tk.Label(root, text="")
        label_status_profile.pack()

    back_profile_button = tk.Button(text="Back", command=lambda: menu_page(user),
                                    font = 'lucida 15 bold', fg="blue")
    back_profile_button.place(x=540, y=370)
    Change_profile_pic_button = tk.Button(text="Change picture", command=lambda: upload_profile_pic_page(user, "profile page"),
                                    font='lucida 15 bold')
    Change_profile_pic_button.place(x=350, y=370)


'New:'
#page to change the profile picture
def change_profile_pic_page(user):
    clear_widgets(root)
    upload_button = tk.Button(root, text="Change your profile picture here", command=lambda:select_image(), font='lucida 20 bold', fg="white", bg="lightblue")
    upload_button.pack(pady=10)

    image_label = tk.Label(root)
    image_label.pack(pady=10)

    save_button = tk.Button(root, text="Save new profile picture", command=lambda:save_profile_change(user, file_path), fg="blue")
    save_button.pack(pady=10)


'New:'
## complimentary function for the page to change the profile picture
def save_profile_change(user, pic):
    # Replace with your database integration logic
    if user in volunteers:
        volunteers[user]["profile pic"] = pic
    else:
        elderlys[user]["profile pic"] = pic
    print("Image saved to database.")
    profile_page(user)


# page where the user can change the age
def open_age_change_window(user):
    clear_widgets(root)
    add_image(root, file_path="images/GH_pic2.jpg")
    global new_age_entry
    age_change_window_title = tk.Label(root, text="Change your age", font = 'lucida 20 bold', fg="white", bg="lightblue")
    age_change_window_title.place(x=20, y=40)
    new_age_label = tk.Label(root, text="Enter new age:", font = 'lucida 15 bold')
    new_age_label.place(x=20, y=120)

    new_age_entry = tk.Entry(root)
    new_age_entry.place(x=20, y=170, width=220, height=25)

    save_button_age = tk.Button(root, text="Save", font = 'lucida 15 bold', command=lambda: save_new_age(user),
                                fg = "blue")
    save_button_age.place(x=20, y=230)


##complimentary function to save the changes of age
def save_new_age(user):
    age = new_age_entry.get()
    if age:
        if user in volunteers:
            volunteers[user]["age"] = age
        elif user in elderlys:
            elderlys[user]["age"] = age
        profile_page( user)
    else:
        error_change( user)


#page where the useer can change the location
def open_location_change_window(user):
    clear_widgets(root)
    add_image(root, file_path="images/GH_pic2.jpg")
    global new_location_entry
    location_change_window_title = tk.Label(root, text="Change your location", font = 'lucida 20 bold', fg="white", bg="lightblue")
    location_change_window_title.place(x=20, y=40)

    new_location_label = tk.Label(root, text="Enter new location:", font = 'lucida 15 bold')
    new_location_label.place(x=20, y=120)

    new_location_entry = tk.Entry(root)
    new_location_entry.place(x=20, y=170, width=220, height=25)

    save_button_loc = tk.Button(root, text="Save", font = 'lucida 15 bold', command=lambda: save_new_location(user),
                                fg = "blue")
    save_button_loc.place(x=20, y=230)


##complimentary function to save the changes of location
def save_new_location(user):
    location = new_location_entry.get()
    if location:
        if user in volunteers:
            volunteers[user]["location"] = location
        elif user in elderlys:
            elderlys[user]["location"] = location
        profile_page( user)
    else:
        error_change( user)


## pop-up error when information is missing durch the change of profile data
def error_change(user):
    clear_widgets(root)
    add_image(root, file_path="images/GH_pic2.jpg")
    error_reg = tk.Label(root, text="Missing Information! There will be no change!",font = 'lucida 20 bold', fg="red")
    error_reg.place(x=20, y=25)
    okay_error = tk.Button(text="Okay", command=lambda: profile_page( user), font = 'lucida 15 bold',
                           fg="blue")
    okay_error.place(x=20, y=100)


#page to set the status of volunteers, whether they are ready to help now or not
def set_status_window(user):
    clear_widgets(root)
    add_image(root, file_path="images/select_status.png")
    global status_ready_button, status_not_ready_button

    status_ready_button = tk.Button(root, text="ready to help", command= lambda: set_status(user, "ready to help"),
                                    font='lucida 15 bold')
    status_ready_button.place(x=20, y=100)
    status_not_ready_button = tk.Button(root, text="not ready to help",
                                        command= lambda: set_status(user, "not ready to help"), font='lucida 15 bold')
    status_not_ready_button.place(x=20, y=150)
    status_back_button = tk.Button(root, text="Okay", command= lambda: menu_page( user),
                                   font='lucida 15 bold', fg="blue")
    status_back_button.place(x=20, y=230)


##complimentary function to set the status of volunteers
def set_status(user, status):
    volunteers[user]["status"] = status
    status_not_ready_button.config(bg="green" if status == "not ready to help" else "white")
    status_ready_button.config(bg="green" if status == "ready to help" else "white")


#page for elderly people to ask for help and send requests
def asking_for_help_window(user):
    clear_widgets(root)
    add_image(root, file_path="images/GH_pic3.jpg")
    global accompaniment_button, company_button, shopping_button, crafts_button, describtion_entry
    label_asking_for_help = tk.Label(root, text="Please select what type of help you need!",
                                     font='lucida 20 bold', fg="white", bg="lightblue")
    label_asking_for_help.place(x=20, y=25)

    accompaniment_button = tk.Button(text="Accompaniment",
                                     font='lucida 15 bold',
                                     command=lambda: select_service("Accompaniment"))
    accompaniment_button.place(x=20, y=75)
    crafts_button = tk.Button(text="Crafts",
                              font='lucida 15 bold',
                              command=lambda: select_service("Crafts"))
    crafts_button.place(x=20, y=125)
    company_button = tk.Button(text="Company",
                               font='lucida 15 bold',
                               command=lambda: select_service("Company"))
    company_button.place(x=20, y=175)
    shopping_button = tk.Button(text="Shopping",
                                font='lucida 15 bold',
                                command=lambda: select_service("Shopping"))
    shopping_button.place(x=20, y=225)

    describtion = tk.Label(root, text="Describtion of the task:", font='lucida 15 bold')
    describtion.place(x=20, y=290)
    describtion_entry = tk.Entry(root, font= 'lucida 15 bold', bg="white")
    describtion_entry.place(x=20, y=325, width=220, height=25)
    enter_asking_for_help = tk.Button(text="Search", font='lucida 15 bold', command=lambda: search_result_window(user),
                                      fg="blue")
    enter_asking_for_help.place(x=20, y=370)


##complimentary function that marks the service type requested by seniors
def select_service(service_type):
    global selected_service_type
    selected_service_type = service_type
    accompaniment_button.config(bg="green" if selected_service_type == "Accompaniment" else "white")
    crafts_button.config(bg="green" if selected_service_type == "Crafts" else "white")
    company_button.config(bg="green" if selected_service_type == "Company" else "white")
    shopping_button.config(bg="green" if selected_service_type == "Shopping" else "white")


# page that shows the search results for seniors, showing the volunteers that are ready to help nearby
def search_result_window(user):
    global describtions
    describtions = describtion_entry.get()
    clear_widgets(root)
    add_image(root, file_path="images/GH_pic3.jpg")

    result_volunteer_buttons = []
    x = get_ready_to_help_volunteers()

    distances_and_volunteers = []

    for volunteer_id in x:
        distance = calculate_distance_between_users(user, volunteer_id)
        distances_and_volunteers.append((distance, volunteer_id))

    distances_and_volunteers.sort()

    label_result_window = tk.Label(root, text="Here are your results! Please choose one:", font='lucida 20 bold',
                                   fg="blue")
    label_result_window.place(x=20, y=30)
    count = 80

    for i in range(min(5, len(distances_and_volunteers))):
        distance, volunteer_id = distances_and_volunteers[i]
        volunteer = volunteers[volunteer_id]

        result_volunteer = tk.Button(
            text=f"{volunteer['name']}, {volunteer['age']} years old, {volunteer['stars']} stars,"
                 f" {distance:.2f} km distance", font='lucida 12 bold',
            command=lambda vid=volunteer_id: inquiry_volunteer(user, vid))
        result_volunteer.place(x=20, y=count + 30)
        count = count + 40
        result_volunteer_buttons.append(result_volunteer)


##complimentary function to get the search results of volunteers
def get_ready_to_help_volunteers():
    ready_to_help_volunteers = []

    for volunteer_id, volunteer_data in volunteers.items():
        if volunteer_data["status"] == "ready to help":
            ready_to_help_volunteers.append(volunteer_id)
    return ready_to_help_volunteers


##complimentary function to calculate the distance between requesting senior and to a potential helper
def calculate_distance_between_users(user1, user2):
    user1_location = elderlys[user1]["location"] if user1 in elderlys else volunteers[user1]["location"]
    user2_location = elderlys[user2]["location"] if user2 in elderlys else volunteers[user2]["location"]

    user1_coordinates = [float(coord) for coord in address_in_coordinates(user1_location)]
    user2_coordinates = [float(coord) for coord in address_in_coordinates(user2_location)]

    if user1_coordinates is None or user2_coordinates is None:
        return None  # case where coordinates couldn't be obtained

    user1_lat, user1_lon = user1_coordinates
    user2_lat, user2_lon = user2_coordinates

    distance = calculate_distance(user1_lat, user1_lon, user2_lat, user2_lon)
    return distance


##complimentary function that calculates the distance between to coordinates and returns the value
def calculate_distance(lat1, lon1, lat2, lon2):
    # Convert degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # haversine formula
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371  # Earth radius in km
    d = c * r
    return d


##complimentary function that converts an address into coordinates in oder to calculate the distance between users
## it accesses the webpage of Nominatim to do so, similar to how we accessed the horoscope webpage in one of the exercises of tech basics
##source: https://github.com/shaq31415926/python_tech_basics/blob/main/tech_basics_one/07lecture/horoscope_generator_streamA.py
def address_in_coordinates(address):
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {"format": "json", "q": address}
    response = requests.get(base_url, params=params)
    data = response.json()
    print(data)
    if data:
        location = data[0]
        latitude = location["lat"]
        longitude = location["lon"]
        return latitude, longitude
    else:
        return None, None


#page for the seniors that confirms sent requests and tells them to wait and check the button
def inquiry_volunteer(user, volunteer):
    clear_widgets(root)
    add_image(root, file_path="images/GH_pic3.jpg")
    distance = int(calculate_distance_between_users(user, volunteer))

    inquiries.append({"elderly": user, "volunteer": volunteer, "service": selected_service_type,
                      "describtion": describtions, "distance": distance, "status": "waiting"})

    inquiry_volunteer_window = tk.Label(root, text="Your inquiry was sent!\n Wait and check the sent inquiries "
                                                   "button regularly\n if your helper accepts the task.",
                                        font='lucida 15 bold')
    inquiry_volunteer_window.place(x=70, y=30)
    ok_inquiry_volunteer = tk.Button(
        text="okay", font='lucida 15 bold', command=lambda: menu_page( user), fg="blue")
    ok_inquiry_volunteer.place(x=290, y=160)


#page for the senior that shows their sent inquiries and their status (wait, accepted, declined)
def sent_inquiry_window(user):
    clear_widgets(root)
    count = 0
    label_sent_request_list = []
    status_button_volunteer_list = []
    add_image(root, file_path="images/Sent_inquiries.png")
    for i in range(len(inquiries)):
        if inquiries[i]["elderly"] == user:
            text_inquiry = "Service: " + inquiries[i]["service"] + "\n Describtion: " + inquiries[i]["describtion"]\
                           + "\n Name: " + volunteers[inquiries[i]["volunteer"]]["name"] + ", distance: " + \
                           str(inquiries[i]["distance"]) + "km, age: " + str(volunteers[inquiries[i]["volunteer"]]
                            ["age"]) + ", stars: " + str(volunteers[inquiries[i]["volunteer"]]["stars"])
            label_sent_request = tk.Label(root, text=text_inquiry, font = 'lucida 10 bold')
            label_sent_request.place(x=20, y = count + 115)
            if inquiries[i]["status"] == "Accept!":
                status_button_volunteer = tk.Button(text="Accepted! Please click here", font='lucida 10 bold',
                                                    command=lambda i=i: mission_elderly_window(user, #i=i to freeze the i value for every iteration
                                                    inquiries[i]["volunteer"], text_inquiry, i), fg="blue")
            elif inquiries[i]["status"] == "Decline!":
                status_button_volunteer = tk.Button(text="Declined! Please click here", font='lucida 10 bold',
                                                     command=lambda i=i: inquiry_decline(i, user))
            else:
                status_button_volunteer = tk.Button(text="Wait!", font='lucida 10 bold',
                                                     command=lambda: menu_page( user))
            status_button_volunteer.place(x=80, y=count + 175)
            label_sent_request_list.append(label_sent_request)
            status_button_volunteer_list.append(status_button_volunteer)
            count = count + 100
    back_button_sent_inquiry = tk.Button(text="Back", font='lucida 15 bold', fg = "blue",
                                          command=lambda: menu_page( user))
    back_button_sent_inquiry.place(x=540, y=370)


##complimentary function for seniors to accept an declined request
def inquiry_decline(index, elderly):
    inquiries.pop(index)
    menu_page(elderly)


#page that shows helpers incoming help requests from seniors
def incoming_inquiry_window(user):
    clear_widgets(root)
    add_image(root, file_path="images/Incoming_inquiries.png")
    count = 0
    button_volunteer_list = []
    label_service_type_list = []

    for i in range(len(inquiries)):
        if inquiries[i]["volunteer"] == user and inquiries[i]["status"] != "Decline!" and inquiries[i]["status"] != "Accept!":
            text_inquiry = "Service: " + inquiries[i]["service"] + "\n describtion: " + inquiries[i]["describtion"] +\
                           "\n name: " + elderlys[inquiries[i]["elderly"]]["name"] + ", distance: " + \
                           str(inquiries[i]["distance"]) + "km, age: " + str(elderlys[inquiries[i]["elderly"]]["age"]) + \
                           ", stars: " + str(elderlys[inquiries[i]["elderly"]]["stars"])
            label_service_type = tk.Label(root, text=text_inquiry, font='lucida 10 bold')
            label_service_type.place(x=20, y = count + 115)
            label_service_type_list.append(label_service_type)
            text_mission = text_inquiry + "\n location: " + elderlys[inquiries[i]["elderly"]]["location"]

            accept_button_volunteer = tk.Button(text="Accept!", font='lucida 10 bold',
                                                command=lambda i=i: mission_window(user, inquiries[i]["elderly"],
                                                text_mission, i))
            accept_button_volunteer.place(x=80, y=count + 175)

            # Create a function with a lambda to capture the index value
            decline_button_volunteer = tk.Button(text="Decline!", font='lucida 10 bold',
                                                 command=lambda i=i: set_inquiry_status(i, "Decline!", user))
            decline_button_volunteer.place(x=170, y=count + 175)
            button_volunteer_list.append(decline_button_volunteer)
            button_volunteer_list.append(accept_button_volunteer)
            count = count + 100

    back_button_incoming_inquiry = tk.Button(text="Back", font='lucida 15 bold', fg="blue",
                                              command=lambda: menu_page(user))
    back_button_incoming_inquiry.place(x=540, y=370)


##complimentary function to set the inquiry status
def set_inquiry_status(index, status, user):
    inquiries[index]["status"] = status
    menu_page(user)


'New:'
#page that shows seniors the profile pictures of helpers and the other way around
def show_other_profile_pic(user, other, text_mission, i):
    clear_widgets(root)

    if other in volunteers:
        if volunteers[other]["profile pic"] is not None:
            add_two_images(root, "images/Half_background.png", volunteers[other]["profile pic"])
            print("1v")
        else: add_two_images(root, "images/Half_background.png", "images/no_profile_pic.png")
    elif other in elderlys:
        if elderlys[other]["profile pic"] is not None:
            add_two_images(root, "images/Half_background.png", elderlys[other]["profile pic"])
            print("2v")
        else:add_two_images(root, "images/Half_background.png", "images/no_profile_pic.png")
    label = tk.Label(root, text="This is " + other, font='lucida 20 bold',
                     bg="white")
    label.place(x=20, y=30)
    if user in volunteers:
        back_button = tk.Button(text="Okay!", font='lucida 15 bold',
                                 command=lambda: mission_window(user, other, text_mission, i), fg="blue")
        back_button.place(x=20, y=370)
    else:
        back_button = tk.Button(text="Okay!", font='lucida 15 bold',
                                command=lambda: mission_elderly_window(user, other, text_mission, i), fg="blue")
        back_button.place(x=20, y=370)


#page for to show the helping mission of volunteers with a button to confirm that the aid was given
def mission_window(user, elderly, text_mission, i):
    clear_widgets(root)
    add_image(root, file_path="images/GH_pic3.jpg")
    inquiries[i]["status"]= "Accept!"
    volunteers[user]["status"] = "not ready to help"
    label_mission_window = tk.Label(root, text="Please help your elderly person now!", font='lucida 20 bold', fg="blue")
    label_mission_window.place(x=20, y = 30)
    info_mission_window = tk.Label(root, text= text_mission, font='lucida 15 bold')
    info_mission_window.place(x=20, y = 100)
    aid_given_button = tk.Button(text="aid given!", font='lucida 15 bold',
                                        command=lambda:  volunteer_rating_window(user, elderly), fg="blue")
    aid_given_button.place(x=450, y=370)
    other_profile_pic_button = tk.Button(text="Look at a picture of the person", font='lucida 15 bold',
                                 command=lambda: show_other_profile_pic(user, elderly, text_mission, i), fg="blue")
    other_profile_pic_button.place(x=20, y=370)


#page for to tell seniors to wait for their helpers buttons to confirm that the aid was given or not
def mission_elderly_window(elderly, volunteer, text, i):
    clear_widgets(root)
    add_image(root, file_path="images/GH_pic3.jpg")
    label_mission_window_e = tk.Label(root, text="Please wait for your helper to arrive!", font='lucida 20 bold',
                                      fg="blue")
    label_mission_window_e.place(x=20, y = 30)
    info_mission_window_e = tk.Label(root, text=text,  font='lucida 15 bold')
    info_mission_window_e.place(x=20, y = 100)
    aid_given_button_e = tk.Button(text="click this box when you received help!", font='lucida 15 bold',
                                   command=lambda i=i: elderly_rating_window(volunteer, elderly, i), fg="green")
    aid_given_button_e.place(x=120, y=320)
    aid_not_given_button_e = tk.Button(text="click this box when you did not receive help!", font='lucida 15 bold',
                                 command=lambda i=i: no_help_window(volunteer, elderly, i), fg="red")
    aid_not_given_button_e.place(x=90, y=370)
    other_profile_pic_button = tk.Button(text="Look at a picture of the person", font='lucida 15 bold',
                                         command=lambda: show_other_profile_pic(elderly, volunteer, text, i),
                                         fg="blue")
    other_profile_pic_button.place(x=20, y=200)


#page with an apology for seniors that did not receive help
def no_help_window(volunteer, elderly, i):
    clear_widgets(root)
    add_image(root, file_path="images/GH_pic3.jpg")
    if volunteers[volunteer]["stars"] != 0:
        volunteers[volunteer]["stars"] = volunteers[volunteer]["stars"] / 2
    inquiries.pop(i)
    title_no_help = tk.Label(root, text="We are so sorry that you didn't receive help! \n "
                                        "Please make a new inquiry and\n "
                                        "choose a different helper." ,
                                        font='lucida 20 bold')
    title_no_help.place(x=20, y=40)
    no_help_okay = tk.Button(text="Okay", font='lucida 15 bold', fg= "blue",
                                   command=lambda: menu_page( elderly))
    no_help_okay.place(x=260, y=160)


#page for helpers to rate the senior they helped
def volunteer_rating_window(volunteer, elderly):
    clear_widgets(root)
    add_image(root, file_path="images/GH_pic3.jpg")
    label_volunteer_rating = tk.Label(root, text="Please rate the elderly person you helped. ", font='lucida 20 bold',
                                   fg="blue")
    label_volunteer_rating.place(x=20, y=30)
    star_1_volunteer = tk.Button(text="1 star", font='lucida 15 bold',
                                        command=lambda: adding_stars_elderly(1, volunteer, elderly))
    star_1_volunteer.place(x=20, y=100)
    star_2_volunteer = tk.Button(text="2 star", font='lucida 15 bold',
                                 command=lambda: adding_stars_elderly(2, volunteer, elderly))
    star_2_volunteer.place(x=20, y=150)
    star_3_volunteer = tk.Button(text="3 star", font='lucida 15 bold',
                                        command=lambda: adding_stars_elderly(3, volunteer, elderly))
    star_3_volunteer.place(x=20, y=200)
    star_4_volunteer = tk.Button(text="4 star", font='lucida 15 bold',
                                        command=lambda: adding_stars_elderly(4, volunteer, elderly))
    star_4_volunteer.place(x=20, y=250)
    star_5_volunteer = tk.Button(text="5 star", font='lucida 15 bold',
                                        command=lambda: adding_stars_elderly(5, volunteer, elderly))
    star_5_volunteer.place(x=20, y=300)


##complimentary function to calculate the new rating of helpers
def adding_stars_volunteer(rating, volunteer, elderly, i):
    if volunteers[volunteer]["stars"] == 0:
        volunteers[volunteer]["stars"] = rating
    else:
        volunteers[volunteer]["stars"] = (volunteers[volunteer]["stars"] + rating) / 2
    volunteers[volunteer]["points"] = volunteers[volunteer]["points"] + 10
    inquiries.pop(i)
    menu_page( elderly)


#page for seniors to rate the helper they received
def elderly_rating_window(volunteer, elderly, i):
    clear_widgets(root)
    add_image(root, file_path="images/GH_pic3.jpg")
    label_rating_window = tk.Label(root, text="Please rate the volunteer that helped you", font='lucida 20 bold',
                                   fg="blue")
    label_rating_window.place(x=20, y=30)
    star_1_elderly = tk.Button(text="1 star", font='lucida 15 bold',
                                 command=lambda i=i: adding_stars_volunteer(1, volunteer, elderly, i))
    star_1_elderly.place(x=20, y=100)
    star_2_elderly = tk.Button(text="2 star", font='lucida 15 bold',
                                 command=lambda i=i: adding_stars_volunteer(2, volunteer, elderly, i))
    star_2_elderly.place(x=20, y=150)
    star_3_elderly = tk.Button(text="3 star", font='lucida 15 bold',
                                 command=lambda i=i: adding_stars_volunteer(3, volunteer, elderly, i))
    star_3_elderly.place(x=20, y=200)
    star_4_elderly = tk.Button(text="4 star", font='lucida 15 bold',
                                 command=lambda i=i: adding_stars_volunteer(4, volunteer, elderly, i))
    star_4_elderly.place(x=20, y=250)
    star_5_elderly = tk.Button(text="5 star", font='lucida 15 bold',
                                 command=lambda i=i: adding_stars_volunteer(5, volunteer, elderly, i))
    star_5_elderly.place(x=20, y=300)


##complimentary function to calculate the new rating of seniors
def adding_stars_elderly(rating, volunteer, elderly):
    if elderlys[elderly]["stars"] == 0:
        elderlys[elderly]["stars"] = rating
    else:
        elderlys[elderly]["stars"] =(elderlys[elderly]["stars"] + rating) / 2
    volunteers[volunteer]["status"] = "ready to help"
    menu_page( volunteer)


#page for helpers to redeem their points to get "vouchers"
def points_window(user):
    clear_widgets(root)
    add_image(root, file_path="images/GH_pic2.jpg")

    label_points_window = tk.Label(root, text="Redeem your points here", font='lucida 20 bold', fg="white", bg="lightblue")
    label_points_window.place(x=20, y=25)
    text_points_window = tk.Label(root, text="You have "+ str(volunteers[user]["points"])+ " points right now",
                                   font='lucida 15 bold')
    text_points_window.place(x=20, y=90)
    if volunteers[user]["points"]>499:
        button_points_window = tk.Button(text="Exchange 500 points for a 30% discount voucher\n "
                                              "from Peter Pane burger restaurants.",
                                         font='lucida 15 bold', fg= "green", command=lambda: exchange_window(user))
        button_points_window.place(x=20, y=150)
    else:
        button_points_window = tk.Label(root, text="No voucher available right now. Help a bit more!",
                                         font='lucida 15 bold')
        button_points_window.place(x=20, y=150)

    back_points_window = tk.Button(text="Back", font='lucida 15 bold', fg= "blue",
                                   command=lambda: menu_page( user))
    back_points_window.place(x=540, y=370)


#page for helpers that shows them their "voucher" for the points they earned by helping seniors (which is in this case just a random number)
def exchange_window(user):
    clear_widgets(root)
    add_image(root, file_path="images/GH_pic2.jpg")

    volunteers[user]["points"] = volunteers[user]["points"] - 500
    coupon_code = ''.join(random.choice('0123456789') for _ in range(20))
    text_exchange_window = tk.Label(root, text="Here is your discount voucher number:\n " + str(coupon_code),
                                     font='lucida 20 bold', fg="white", bg="lightblue")
    text_exchange_window.place(x=20, y=40)
    okay_exchange_window = tk.Button(text="Okay", font='lucida 15 bold', fg= "blue",
                                   command=lambda: menu_page( user))
    okay_exchange_window.place(x=220, y=150)


welcome_page()
root.mainloop()



