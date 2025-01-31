import tkinter as tk
from tkinter import ttk, PhotoImage, Toplevel, Canvas, Scrollbar
from PIL import Image, ImageTk

# Options for the destination dropdown
destination_options = ["Cubbon Park", "Lalbagh Botanical Garden", "Vidhana Soudha", "Bangalore Palace",
                        "Iskcon Temple Bangalore", "Tipu Sultan's Summer Palace", "Art Of Living",
                        "Bannerghatta National Park", "Nandi Hills", "Bangalore Fort",
                        "HAL Aerospace Museum", "Jawaharlal Nehru Planetarium", "Wonderla Amusement Park",
                        "Commercial Street", "Visvesvaraya museum"]

people_options = ["Solo", "Couple", "Family", "Group"]

# Options for budget range
budget_options = ["Low", "Medium", "High"]

def on_select_destination():
    selected_destination = destination_var.get()
    selected_people = people_var.get()
    selected_budget = budget_var.get()
    
    print(f"Selected Destination: {selected_destination}")
    print(f"Selected People: {selected_people}")
    print(f"Selected Budget: {selected_budget}")

    # Now you can filter and recommend places based on user's selections
    # Add your recommendation logic here

    show_destination_page(selected_destination)

def on_select_destination():
    selected_destination = destination_var.get()
    print(f"Selected Destination: {selected_destination}")
    show_destination_page(selected_destination)

def show_destination_page(selected_destination):
    if selected_destination == "Cubbon Park":
        show_cubbon_park_page()
    elif selected_destination == "Lalbagh Botanical Garden":
        show_lalbagh_page()
    elif selected_destination == "Vidhana Soudha":
        show_vidhana_soudha_page()
    elif selected_destination == "Wonderla Amusement Park":
        show_wonderla_Amusement_Park_page()
    elif selected_destination== "Bangalore Palace":
        show_banglore_palace_page()
    elif selected_destination == "Iskcon Temple Bangalore":
        show_iskcon_page()
    elif selected_destination == "Bannerghatta National Park":
        show_bannerghatta_zoo_page()
    # Add more conditions for other destinations
        
###Cubbon Park###

def show_cubbon_park_page():
cubbon_park_window = Toplevel(root)
cubbon_park_window.title("Cubbon Park")

canvas = Canvas(cubbon_park_window, width=600, height=400, scrollregion=(0, 0, 2000, 2000))
scrollbar = Scrollbar(cubbon_park_window, command=canvas.yview, troughcolor="light gray", activerelief='groove', width=20, orient="vertical")
canvas.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side='right', fill='y')
canvas.pack(side='left', fill='both', expand=True)

# Create a frame inside the canvas to contain all widgets
frame = Label(canvas)
canvas.create_window((0, 0), window=frame, anchor='nw')

heading_label = Label(frame, text="Discover the Beauty of Cubbon Park", font=("Great vibes", 40), fg="purple")
heading_label.pack(padx=20, pady=20)

info_label = Label(frame, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCubbon Park d...", font=("Great Vibes", 16), fg="red", wraplength=1000, justify='left')
info_label.pack(padx=20, pady=20)

additional_info_label = Label(frame, text="\n\n\n\n\n\n\nWeather : 20 - 27°C\nLabel : Must Visit\nTags : Garden & Park...", font=("Great Vibes", 12), fg="dark green", wraplength=500, justify='left')
additional_info_label.pack(padx=20, pady=20)

additional_info_label = Label(frame, text="Things To Do In Cubbon Park:\nA gentle amalgam of natural and man-made sights...", font=("Great Vibes", 12), fg="blue", wraplength=800, justify='left')
additional_info_label.pack(padx=20, pady=20)

additional_info_label = Label(frame, text="""LOCATION :\nCubbon Park\nIn the heart of the city’s business hub is Bangalore’s...""",
                               font=("Great Vibes", 10), fg="maroon", wraplength=800, justify='left')
additional_info_label.pack(padx=20, pady=20)

# Example: Display multiple images using PIL and ImageTk
image_paths = [
    "images/cub1.jpg",
    "images/cub2.jpg",
    "images/cub3.jpg",
    "images/cub4.jpg",
    "images/cub6.jpg"
]

images = [Image.open(image) for image in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

current_image_index = 0
current_image_label = Label(frame, image=photo_images[current_image_index])
current_image_label.image = photo_images[current_image_index]
current_image_label.pack()

# Update scroll region when the frame size changes
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_frame_configure)

cubbon_park_window.mainloop()

###Lalbagh Botanical Garden###

def show_lalbagh_page():
    lalbagh_window = Toplevel(root)
    lalbagh_window.title("Lalbagh Botanical Garden")

    # Create a Canvas with a Scrollbar
    canvas = Canvas(lalbagh_window, width=600, height=400, scrollregion=(0, 0, 2000, 2000))
    scrollbar = Scrollbar(lalbagh_window, command=canvas.yview, troughcolor="light gray", activerelief=tk.GROOVE, width=20, orient="vertical")
    canvas.config(yscrollcommand=scrollbar.set)

    # Add widgets to display detailed information about Lalbagh Botanical Garden
    heading_label = tk.Label(
        canvas,
        text="Welcome to Lalbagh Botanical Garden",
        font=("Great Vibes", 40),
        fg="white",
    )
    heading_label.pack(padx=20, pady=20)

    info_label = tk.Label(
        canvas,
        text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLalbagh is one of Bengaluru’s major attractions. A sprawling garden situated in a 240 acres piece of land in the heart of the city, Lalbagh houses India’s largest collection of tropical plants and sub-tropical plants, including trees that are several centuries old. Exhibits like the Snow White and the seven dwarfs, and a topiary park, an expansive lake, a beautiful glasshouse modelled around the Crystal Palace in London adorn the park giving it a surrealistic atmosphere. A watchtower perched on top of a 3000 million years old rocky outcrop (which is a National Geological Monument), built by Kempegowda, the founder of Bengaluru also adorns the picturesque garden.",
        font=("Great Vibes", 12),
        fg="green",
        wraplength=900,
        justify=tk.LEFT
    )
    info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="\n\n\n\n\n\n\nWeather : 20 - 33.1°C\nLabel : Must Visit\nTags : Botanical Garden\nTimings : 6:00 AM - 7:00 PM \nOpen on all days\nTime Required : 2 - 3 hours\nEntry Fee :\nAdults: INR 20 per person.\nChildren below 12 years: Free entry.\nStill Camera: INR 501.\n",
        font=("Great Vibes", 10),
        fg="red",
        wraplength=500,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="""Things to do in Lalbagh Botanical Garden:\nExplore the Ganesh Temple: The Ganesh Temple is one of the most significant structures within the garden.\nWalk along the garden paths: The garden paths provide a glimpse into the rich flora of the garden.\nLearn about Bangalore’s history: The garden is a great place to learn about the rich history of Bangalore.\nTake a guided tour: A guided tour can provide in-depth information about the garden and its history.\nAttend cultural events: The garden often hosts various cultural events.\nCheck out the floral installations: Marvel at the amazing floral installations like the HMT clock and Snow White’s garden.\nMarvel at the Lotus lake: The pink beauty of the Lotus lake is a sight to behold.\nFeel the cool breeze along Lalbagh lake: Enjoy the serene environment along the lakeside of Lalbagh lake.\nDiscover ancient rocks: Discover 3000 million year old rocks at Peninsular Gneiss Rock.""",
        font=("Great Vibes", 10),
        fg="dark blue",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="Location :\nLalbagh is located 7 km south of the city center (Majestic area) and 38 km from the Bengaluru airport. Lalbagh can be accessed using the Bengaluru metro rail network from different parts of Bengaluru city. Buses, autos or taxis are readily available to reach Lalbagh.",
        font=("Great Vibes", 8),
        fg="green",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    # Example: Display multiple images
    image_paths = [
        r"images\lalbagh.jpg",
        r"images\lalbagh1.jpg",
        r"images\lalbagh2.jpg",
        r"images\lalbagh3.jpg",
        r"images\lalbagh4.jpg",
        r"images\Lalbagh5.jpg",
        r"images\lalbagh6.jpg"
    ]

    # Display images one after the other
    current_image_index = 0
    current_image_label = None

    def show_next_image():
        nonlocal current_image_index, current_image_label
        # Destroy the previous image label if it exists
        if current_image_label:
            current_image_label.destroy()
        current_image_index = (current_image_index + 1) % len(image_paths)
        update_image()

    def update_image():
        nonlocal current_image_index, current_image_label
        img = Image.open(image_paths[current_image_index])
        img = ImageTk.PhotoImage(img)
        current_image_label = tk.Label(canvas, image=img)
        current_image_label.image = img
        canvas.create_window(260, 50, anchor=tk.NW, window=current_image_label)  # Adjust the coordinates

        # Schedule to show the next image after 2000 milliseconds (2 seconds)
        lalbagh_window.after(2000, show_next_image)

    # Initial image display
    update_image()

    # Pack the Canvas and Scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y", expand=False)

###Vidhana Soudha###

def show_vidhana_soudha_page():
    vidhana_soudha_window = Toplevel(root)
    vidhana_soudha_window.title("Vidhana Soudha")

  
    # Create a Canvas with a Scrollbar
    canvas = Canvas(vidhana_soudha_window, width=600, height=400, scrollregion=(0, 0, 2000, 2000))
    scrollbar = Scrollbar(vidhana_soudha_window, command=canvas.yview, troughcolor="light gray", activerelief=tk.GROOVE, width=20, orient="vertical")
    canvas.config(yscrollcommand=scrollbar.set)

    # Add widgets to display detailed information about Vidhana Soudha
    heading_label = tk.Label(
        canvas,
        text="Discover the Beauty of Vidhana Soudha",
        font=("Great vibes", 40),
        fg="purple",
        
    )
    heading_label.pack(padx=20, pady=20)

    info_label = tk.Label(
        canvas,
        text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDescribed by Pandit Jawaharlal Nehru as 'a temple dedicated to the nation', Vidhana Soudha houses the State Legislature and the Secretariat of Karnataka and is one of the most popular attractions in the lively and colourful city of Bengaluru. It also proudly boasts the title of being the largest state legislative building in the country. With four entrances in all four directions and four floors above the ground level and one below it, we surely don't doubt the title. Popularly known as the 'Taj Mahal of South India', it is counted as one of the most magnificent buildings in the city and is sure to impress the onlooker with its sophisticated poise and glorified grandiose. The entire monument is illuminated on Sundays and public holidays and is a sight for sore eyes.",
        font=("Great Vibes", 16),
        fg="red",
        wraplength=1000,
        justify=tk.LEFT
    )
    info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="\n\n\n\n\n\n\nWeather : 20 - 27°C\nLabel : Must Visit\nTags : Monument\nTimings : 10:00 AM - 5:30 PM \nClosed on weekends and public holidays.\nTime Required : 1 - 2 hours\nEntry Fee :\nAdults: INR 20 per person.\nChildren below 12 years: Free entry.\nStill Camera: INR 501.\n",
        font=("Great Vibes", 12),
        fg="DARK GREEN",
        wraplength=500,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="Things To Do In Vidhana Soudha:\nExplore the Building’s Architecture and Art: The building is a splendid structure that covers an area of 60 acres. It boasts of an elegant and truly exquisite Neo-Dravidian style of architecture.\nVisit the Assembly Hall and Council Hall: The building has an assembly hall and a council hall where the legislative assembly and the legislative council of the state meet respectively.\nEnjoy the Light Show and Fountain Show: The entire monument is illuminated on Sundays and public holidays and is a sight for sore eyes.\nExperience the Events and Activities: The Vidhana Soudha often hosts various cultural and official events.",
        font=("Great Vibes", 12),
        fg="blue",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="""LOCATION :\nVidhana Soudha is located in the city of Bangalore, India. The exact address is Dr Ambedkar Rd, Sampangi Ramnagar, Bengaluru, Karnataka, 5600011. It’s situated in the heart of Bangalore, on the northwestern side of Cubbon Park.""",
        font=("Great Vibes", 10),
        fg="maroon",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    # Example: Display multiple images
    image_paths = [
        r"images\Bengaluru’s-Vidhana-Soudha-1.jpg",
        r"images\VS 2.jpg",
        r"images\vidhana soudha 5.jpg",
        r"images\vidhana soudha 3.jpg"
    ]

    # Display images one after the other
    current_image_index = 0
    current_image_label = None

    def show_next_image():
        nonlocal current_image_index, current_image_label
        # Destroy the previous image label if it exists
        if current_image_label:
            current_image_label.destroy()
        current_image_index = (current_image_index + 1) % len(image_paths)
        update_image()

    def update_image():
        nonlocal current_image_index, current_image_label
        img = Image.open(image_paths[current_image_index])
        img = ImageTk.PhotoImage(img)
        current_image_label = tk.Label(canvas, image=img)
        current_image_label.image = img
        canvas.create_window(260, 50, anchor=tk.NW, window=current_image_label)  # Adjust the coordinates

        # Schedule to show the next image after 2000 milliseconds (2 seconds)
        vidhana_soudha_window.after(2000, show_next_image)

    # Initial image display
    update_image()

    # Pack the Canvas and Scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y", expand=False)

###Wonderla Amusement Park###

def show_wonderla_Amusement_Park_page():
    wonderla_Amusement_Park_window = Toplevel(root)
    wonderla_Amusement_Park_window.title("Wonderla")

    # Create a Canvas with a Scrollbar
    canvas = Canvas(wonderla_Amusement_Park_window, width=600, height=400, scrollregion=(0, 0, 2000, 2000))
    scrollbar = Scrollbar(wonderla_Amusement_Park_window, command=canvas.yview, troughcolor="light gray", activerelief=tk.GROOVE, width=20, orient="vertical")
    canvas.config(yscrollcommand=scrollbar.set)

    # Add widgets to display detailed information about Cubbon Park
    heading_label = tk.Label(
        canvas,
        text="Discover the Beauty of Wonderla",
        font=("Great vibes", 40),
        fg="purple",
        
    )
    heading_label.pack(padx=20, pady=20)

    info_label = tk.Label(
        canvas,
        text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWonderLa is one of India’s largest amusement and water theme parks. Located on the outskirts of Bengaluru in Ramanagara district, Wonderla Bangalore is spread across 82 acres and has over 60 thrill-packed rides offering entertainment and fun for all age groups. It also has a resort inside the amusement park – making it the first amusement park in India to have a resort built right inside it.",
        font=("Great Vibes", 16),
        fg="red",
        wraplength=1000,
        justify=tk.LEFT
    )
    info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="\n\n\n\n\n\n\nWeather : 15.8 - 27.9°C\nLabel : Must Visit\nTags : Dry and Water games\nTimings : Weekdays (Monday to Friday): The park is open from 11:00 AM to 06:00 PM. The water park operates from 12:30 PM to 05:00 PM.\n          Weekends and Holidays: The park is open from 11:00 AM to 07:00 PM. The water park operates from 12:00 PM to 06:00 PM.\nTime Required : 5 - 7 hours\nEntry Fee : Weekdays (Monday to Friday):\nRegular Tickets:\nAdult: Rs.1249/-\nChild: Rs.999/-\nSenior Citizen: Rs.937/-\nAdult (with College ID): Rs.999/-\nFastrack Tickets:\nAdult: Rs.2498/-\nChild: Rs.1998/-\nWeekends and Holidays:\nRegular Tickets:\nAdult: Rs.1499/-\nChild: Rs.1199/-\nSenior Citizen: Rs.1124/-\nAdult (with College ID): Rs.1199/-\nFastrack Tickets:\nAdult: Rs.2998/-\nChild: Rs.2398/-\nPlease note that child ticket rates are applicable for children with a height ranging between 85 to 140 cm. For senior citizen tickets, photo ID with age proof is mandatory. For college students, original college ID needs to be displayed at the gate during check-in.\n",
        font=("Great Vibes", 12),
        fg="DARK GREEN",
        wraplength=500,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="Things To Do In Wonderla:\nExplore the Park: Take a stroll throughout its various areas to explore the attractions and games.\nEnjoy the Rides: The park features a diverse variety of fun electric games. Highlights include Recoil, a reverse-loop roller coaster; the free-fall Flash Tower; and the topsy-turvy Hurricane.\nKids' Games: The park has a number of kids' games that provide an alluring experience for the whole family.\nYoungster Games: There are games designed to fit the taste of youngsters such as rise and fall games, flying chairs, and rollercoasters.\nMazes Game: Spend an enjoyable time trying out the mazes game.\nWater Games: Enjoy a variety of water games.\nUnique Games: Try out some unique games such as Drop Tower Game, Ferris Wheel Game, Bumper Car Game, and Swinging Ship Game.",
        font=("Great Vibes", 12),
        fg="blue",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="""LOCATION :\nWonderla Amusement Park in Bangalore is located on Mysore Road, 28 km from Bengaluru city. The exact address is 28th km, Mysore Road, Before Bidadi, Bengaluru, Karnataka, 562109, India.""",
        font=("Great Vibes", 10),
        fg="maroon",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    # Example: Display multiple images
    image_paths = [
        r"images\Bengaluru’s-Vidhana-Soudha-1.jpg",
        r"images\VS4.jpg",
        r"images\VS 2.jpg",
        r"images\vidhana soudha 5.jpg",
        r"images\vidhana soudha 3.jpg"
    ]

    # Display images one after the other
    current_image_index = 0
    current_image_label = None

    def show_next_image():
        nonlocal current_image_index, current_image_label
        # Destroy the previous image label if it exists
        if current_image_label:
            current_image_label.destroy()
        current_image_index = (current_image_index + 1) % len(image_paths)
        update_image()

    def update_image():
        nonlocal current_image_index, current_image_label
        img = Image.open(image_paths[current_image_index])
        img = ImageTk.PhotoImage(img)
        current_image_label = tk.Label(canvas, image=img)
        current_image_label.image = img
        canvas.create_window(260, 50, anchor=tk.NW, window=current_image_label)  # Adjust the coordinates

        # Schedule to show the next image after 2000 milliseconds (2 seconds)
        wonderla_Amusement_Park_window.after(2000, show_next_image)

    # Initial image display
    update_image()

    # Pack the Canvas and Scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y", expand=False)

###Banglore fort###

def show_banglore_palace_page():
    banglore_palace_window = Toplevel(root)
    banglore_palace_window.title("Banglore Fort")

    # Create a Canvas with a Scrollbar
    canvas = Canvas(banglore_palace_window, width=600, height=400, scrollregion=(0, 0, 2000, 2000))
    scrollbar = Scrollbar(banglore_palace_window, command=canvas.yview, troughcolor="light gray", activerelief=tk.GROOVE, width=20, orient="vertical")
    canvas.config(yscrollcommand=scrollbar.set)

    # Add widgets to display detailed information about Banglore Fort
    heading_label = tk.Label(
        canvas,
        text="Discover the Beauty of Banglore Fort",
        font=("Great Vibes", 40),
        fg="purple",
        
    )
    heading_label.pack(padx=20, pady=20)

    info_label = tk.Label(
        canvas,
        text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nOriginally built as a mud fort by Kempe Gowda I in 1537, Bangalore Fort was transformed into a stone fort by Haider Ali in 1761. Unfortunately, 20 years later, Bangalore Fort fell into the hands of the British and the entire fort was dismantled and reconstructed into schools, hospitals and roads etc. Today, only the ruins remain of what was once a stronghold of Tipu Sultan i.e. the Delhi Gate and two primary bastions. However, these ruins also reek of glory, splendour and magnificence. The fort premises include several structures which include Tipu Sultan’s Summer Palace. Standing tall as an ancient heritage structure, the monument is one of the most popular attractions of the city.",
        font=("Great Vibes", 16),
        fg="red",
        wraplength=1000,
        justify=tk.LEFT
    )
    info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="\n\n\n\n\n\n\nWeather : 20 - 27°C\nLabel : Must Visit\nTags : Forts and Palaces\nTimings : 10:00 AM - 6:00 PM\nClosed on Sundays.\nTime Required : 1 - 2 hours\nEntry Fee :\nFor Indians: INR 15 per person.\nFor Foreigners: INR 200 per person.\n",
        font=("Great Vibes", 12),
        fg="DARK GREEN",
        wraplength=500,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="Things To Do In Banglore Fort:\nExplore the Ganesh Temple: The Ganesh Temple is one of the most significant structures within the fort and is dedicated to Lord Ganesha.\nVisit the Bangalore Palace: The Bangalore Palace is a stunning example of Tudor and Scottish architecture, surrounded by beautiful gardens and a lake.\nWalk along the fort walls: The fort walls provide a glimpse into the history and architecture of the fort.\nLearn about Bangalore’s history: The fort is a great place to learn about the rich history of Bangalore.\nTake a guided tour: A guided tour can provide in-depth information about the fort and its history.\nAttend cultural events: The fort often hosts various cultural events.",
        font=("Great Vibes", 12),
        fg="blue",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="""LOCATION :\nBangalore Fort is located in the city of Bangalore, India. The exact coordinates are 12.962875°N latitude and 77.575956°E longitude1. It’s situated within city limits at New Tharagupet.""",
        font=("Great Vibes", 10),
        fg="maroon",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    # Example: Display multiple images
    image_paths = [
        r"images\BP 5.jpg",
        r"images\Bangalore-Palace-2.jpg",
        r"images\BP 3.jpg",
        r"images\BP 4.jpg"
    ]

    # Display images one after the other
    current_image_index = 0
    current_image_label = None

    def show_next_image():
        nonlocal current_image_index, current_image_label
        # Destroy the previous image label if it exists
        if current_image_label:
            current_image_label.destroy()
        current_image_index = (current_image_index + 1) % len(image_paths)
        update_image()

    def update_image():
        nonlocal current_image_index, current_image_label
        img = Image.open(image_paths[current_image_index])
        img = ImageTk.PhotoImage(img)
        current_image_label = tk.Label(canvas, image=img)
        current_image_label.image = img
        canvas.create_window(260, 50, anchor=tk.NW, window=current_image_label)  # Adjust the coordinates

        # Schedule to show the next image after 2000 milliseconds (2 seconds)
        banglore_palace_window.after(2000, show_next_image)

    # Initial image display
    update_image()

    # Pack the Canvas and Scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y", expand=False)

###Iskcon Temple###

def show_iskcon_page():
    iskcon_window = Toplevel(root)
    iskcon_window.title("Iskcon Temple")

    # Create a Canvas with a Scrollbar
    canvas = Canvas(iskcon_window, width=600, height=400, scrollregion=(0, 0, 2000, 2000))
    scrollbar = Scrollbar(iskcon_window, command=canvas.yview, troughcolor="light gray", activerelief=tk.GROOVE, width=20, orient="vertical")
    canvas.config(yscrollcommand=scrollbar.set)

    # Add widgets to display detailed information about Iskcon Temple
    heading_label = tk.Label(
        canvas,
        text="Welcome to Iskcon Temple",
        font=("Great Vibes", 40),
        fg="purple"
    )
    heading_label.pack(padx=20, pady=20)

    info_label = tk.Label(
        canvas,
        text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nISKCON Sri Radha Krishna temple was inaugurated in the year 1997. It is not just a temple, but a cultural complex housing the temples dedicated to the Deities of Sri Sri Radha Krishnachandra, Sri Sri Krishna Balarama, Sri Sri Nitai Gauranga, Sri Srinivasa Govinda, Sri Prahlada Narasimha, Bhakta Hanuman, Garudadeva and Srila Prabhupada, Founder Acharya of ISKCON. ISKCON Bangalore is a charitable society with the objective of propagating Krishna Consciousness all over the world, as explained by Srila Prabhupada, whose teachings are based on Bhagavad-gita and Srimad Bhagavatam.",
        font=("Great Vibes", 12),
        fg="green",
        wraplength=900,
        justify=tk.LEFT
    )
    info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="\n\n\n\n\n\n\nWeather : 17 - 26°C\nLabel : Must Visit\nTags : Shrine and Temple\nTimings : Weekdays: 7.15 AM to 1 PM, 4.15 PM to 8.20 PM\n Weekends: 7.15 AM till 8.30 PM.\nPhotography is NOT allowed inside temple premises and modest dress code is recommended. Locker rooms are available to store bags and cameras.\nOpen everyday\nTime Required : 1 - 3 hours\nEntry Fee :Free\n",
        font=("Great Vibes", 10),
        fg="red",
        wraplength=500,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="""Things to do in Iskcon Temple:\nDarshan: You can have darshan of the deities of Sri Sri Radha Krishnachandra, Sri Sri Krishna Balarama, Sri Sri Nitai Gauranga, Sri Srinivasa Govinda, and Sri Prahlada Narasimha.\nKirtan and Chanting: The temple organizes kirtan (devotional songs) and chanting sessions.\nPhilosophy Talks: You can attend talks on philosophy.\nFestivals: The temple conducts special programs for Hindu festivals and other important holidays.\nShopping: There are various shops within the temple complex where you can buy snacks and religious materials.""",
        font=("Great Vibes", 10),
        fg="dark blue",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="Location :\nThe ISKCON temple in Bangalore is located at Hare Krishna Hill, Chord Road, Rajajinagar, Bangalore 560010. It’s one of the largest Krishna-Hindu temples in the world.",
        font=("Great Vibes", 8),
        fg="green",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    # Example: Display multiple images
    image_paths = [
        r"images\ISCON1.jpg",
        r"images\ISCON2.jpg",
        r"images\ISKCON3.jpg",
        r"images\ISCON4.jpg",
    ]

    # Display images one after the other
    current_image_index = 0
    current_image_label = None

    def show_next_image():
        nonlocal current_image_index, current_image_label
        # Destroy the previous image label if it exists
        if current_image_label:
            current_image_label.destroy()
        current_image_index = (current_image_index + 1) % len(image_paths)
        update_image()

    def update_image():
        nonlocal current_image_index, current_image_label
        img = Image.open(image_paths[current_image_index])
        img = ImageTk.PhotoImage(img)
        current_image_label = tk.Label(canvas, image=img)
        current_image_label.image = img
        canvas.create_window(260, 50, anchor=tk.NW, window=current_image_label)  # Adjust the coordinates

        # Schedule to show the next image after 2000 milliseconds (2 seconds)
        iskcon_window.after(2000, show_next_image)

    # Initial image display
    update_image()

    # Pack the Canvas and Scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y", expand=False)

##Bannerghatta Zoo###

def show_bannerghatta_zoo_page():
    bannerghatta_zoo_window = Toplevel(root)
    bannerghatta_zoo_window.title("Bannerghatta National Park")

    # Create a Canvas with a Scrollbar
    canvas = Canvas(bannerghatta_zoo_window, width=600, height=400, scrollregion=(0, 0, 2000, 2000))
    scrollbar = Scrollbar(bannerghatta_zoo_window, command=canvas.yview, troughcolor="light gray", activerelief=tk.GROOVE, width=20, orient="vertical")
    canvas.config(yscrollcommand=scrollbar.set)

    # Add widgets to display detailed information about Bannerghatta Zoo
    heading_label = tk.Label(
        canvas,
        text="Discover the Beauty of Bannerghatta Nationak Park",
        font=("Great vibes", 40),
        fg="purple",
        
    )
    heading_label.pack(padx=20, pady=20)

    info_label = tk.Label(
        canvas,
        text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThe Bannerghatta National Park is a sanctuary for a large variety of flora and fauna. Spread over a massive area of around 104.27 sq. km, this national park was established in the year 1971. The park itself has a number of establishments within its confines, which includes the country's first butterfly park as well.",
        font=("Great Vibes", 16),
        fg="red",
        wraplength=1000,
        justify=tk.LEFT
    )
    info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="\n\n\n\n\n\n\\n\n\n\n\n\n\n\n\n\nWeather : 20 - 27°C\nLabel : Must Visit\nTags : National Park\nTimings :\nButterfly park and boating: 9:30 AM - 5:00 PM\nGrand Safari: 10:00 AM - 4:30 PM\nClosed on Tuesdays\nTime Required : 5 - 6 hours\nEntry Fee :\nIndians:\n Adults: INR 80,Kids (6 - 12 years): INR 40\n Senior citizens: INR 50\nForeigners:\n Adults: INR 400\n Kids: INR 300\n",
        font=("Great Vibes", 12),
        fg="DARK GREEN",
        wraplength=500,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="Things To Do In Bannerghatta National Park:\nZoo: The zoo is spread over 12 hectares and houses several wild animals such as King Cobra, Panthers, Crocodiles, Bears, Deer, and birds.\nLion Safari: You can spot lions from close quarters during the Lion Safari.\nTiger Safari: The park houses 33 tigers, including 7 white tigers. Tigers are maintained in three groups.\nButterfly Park: The park has a dedicated butterfly park consisting of a butterfly garden which is a dedicated 7.5 acres, a butterfly conservatory, a museum, a research laboratory, and a curio shop.\nBoating: Boating is another activity that you can enjoy.\nHiking and Trekking: The park is also a popular hiking and trekking site.",
        font=("Great Vibes", 12),
        fg="blue",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    additional_info_label = tk.Label(
        canvas,
        text="""LOCATION :\nThe Bannerghatta National Park is located at Bannerghatta Road, Bannerghatta, Bengaluru, Karnataka 560083. It’s situated almost midway between the city center of Bengaluru and the Anekal town, at about 25 km from Vidhana Soudha and at about 20 km to the North West of Anekal town. It’s well connected by adequate transport facilities (in the form of city buses and cabs) from various locations in Bangalore. """,
        font=("Great Vibes", 10),
        fg="maroon",
        wraplength=800,
        justify=tk.LEFT
    )
    additional_info_label.pack(padx=20, pady=20)

    # Example: Display multiple images
    image_paths = [
        r"images\bannerghatta 2.jpg",
        r"images\Bannerghatta-NationalPark-4.jpg",
        r"images\bannerghattanationalpark3.jpg",
        r"images\BG1.jpg"
    ]

    # Display images one after the other
    current_image_index = 0
    current_image_label = None

    def show_next_image():
        nonlocal current_image_index, current_image_label
        # Destroy the previous image label if it exists
        if current_image_label:
            current_image_label.destroy()
        current_image_index = (current_image_index + 1) % len(image_paths)
        update_image()

    def update_image():
        nonlocal current_image_index, current_image_label
        img = Image.open(image_paths[current_image_index])
        img = ImageTk.PhotoImage(img)
        current_image_label = tk.Label(canvas, image=img)
        current_image_label.image = img
        canvas.create_window(260, 50, anchor=tk.NW, window=current_image_label)  # Adjust the coordinates

        # Schedule to show the next image after 2000 milliseconds (2 seconds)
        bannerghatta_zoo_window.after(2000, show_next_image)

    # Initial image display
    update_image()

    # Pack the Canvas and Scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y", expand=False)


root = tk.Tk()
root.title("BON VOYAGE")
root.geometry("600x400")

background_image = PhotoImage(file=r"images\bonvoyage.png")  # Replace with your image file

# Create a label with the image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

heading_label = tk.Label(
    root,
    text="Welcome to Our Website - Bon Voyage to an Exciting Journey",
    font=("Great Vibes", 32),
    fg="white",
    bg="maroon"
)
heading_label.pack()

destination_var = tk.StringVar()
destination_var.set(destination_options[0])

destination_combobox = ttk.Combobox(root, textvariable=destination_var, values=destination_options)
destination_combobox.pack(pady=20)


people_label = tk.Label(root, text="Number of People:")
people_label.pack()
people_var = tk.StringVar()
people_var.set(people_options[0])
people_combobox = ttk.Combobox(root, textvariable=people_var, values=people_options)
people_combobox.pack(pady=5)

budget_label = tk.Label(root, text="Budget:")
budget_label.pack()
budget_var = tk.StringVar()
budget_var.set(budget_options[0])
budget_combobox = ttk.Combobox(root, textvariable=budget_var, values=budget_options)
budget_combobox.pack(pady=5)

select_button = tk.Button(root, text="EXPLORE", command=on_select_destination)
select_button.pack(pady=20)

root.mainloop()
