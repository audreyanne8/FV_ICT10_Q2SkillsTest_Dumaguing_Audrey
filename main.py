from pyscript import document, display


# these are dictionaries and are basically data structures that'll help me store info 

clubs = {
    "CommArts": {
        "name": "Comm Arts Club",
        "description": "A club for students interested in communication and arts, focusing on media production, journalism, and creative expression.",
        "meeting_time": "Every Wednesday & Friday, 3:00-4:00 PM",
        "location": "Room 406",
        "moderator": "Ms. Yanis Fernandez",
        "members": 28,
        "category": "Academic"
    },
    "SocSci": {
        "name": "SocSci Club",
        "description": "A club for students interested in debate, social problems, and politics.",
        "meeting_time": "Every Tuesday & Thursday, 3:00-4:00 PM",
        "location": "Room 409",
        "moderator": "Mr. Roberto Lim",
        "members": 28,
        "category": "Academic"
    },
    "Science": {
        "name": "Science Club",
        "description": "A club for students interested in scientific concepts and science competitions",
        "meeting_time": " Tuesdays (3:00 - 4:00 PM), Fridays (2:00-3:00 PM)",
        "location": "Science Laboratory",
        "moderator": "Ms. Maria Santos",
        "members": 35,
        "category": "Academic"
    },
    "Math": {
        "name": "Math Club",
        "description": "A club for students interested in math and joining math competitions.",
        "meeting_time": "Mondays 2:30-4:30 PM",
        "location": "Room 305",
        "moderator": "Mr. Gabuya",
        "members": 30,
        "category": "Academic"
    },
    "Band": {
        "name": "Band Club",
        "description": "A club for students interested in musical instruments and performing in school events.",
        "meeting_time": "Every Monday, Wednesday & Friday, 4-5:30 PM",
        "location": "Music Room",
        "moderator": "Mr. Emillio Alumno",
        "members": 42,
        "category": "Non-Academic"
    },
    "Dance": {
        "name": "Dance Club",
        "description": "A club for students interested in dancing and joining dance competitions.",
        "meeting_time": "Every Tuesday & Thursday, 4-5:30 PM",
        "location": "5th Floor",
        "moderator": "Mr. Cases",
        "members": 38,
        "category": "Non-Academic"
    },
    "Glee": {
        "name": "Glee Club",
        "description": "A club for students interested in singing and performing in school events.",
        "meeting_time": "Every Wednesday & Friday, 4-5 PM",
        "location": "Music Room",
        "moderator": "Sir Denver Martin",
        "members": 33,
        "category": "Non-Academic"
    }
}

def display_club_info(event): #this function helps displays the club info when a club is selected

    document.querySelector("#output").innerHTML = ""
    
    selected = document.querySelector("#clubSelect").value
    
    if not selected: # if no club is selected, nothing will happen 
        return
    
    club = clubs[selected] #this gets the selected club's info from the clubs dictionary
    
    profile = f"""˖ ִ𐙚  {club["name"]} ⋆.˚ ᡣ𐭩 
        Description: {club["description"]} 
        Meeting Time: {club["meeting_time"]}
        Location: {club["location"]}
        Moderator: {club["moderator"]}
        Members: {club["members"]}
        Category: {club["category"]}
"""
    
    display(profile, target="output")  #this displays the club info in the output div