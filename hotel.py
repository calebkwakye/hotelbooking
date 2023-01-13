#
#Names:Caleb Kwakye
#Title: Hotel Booking App
#Description:a program that allows guests to make a hotel reservation and sends confirmation details via email
#



#imports needed modules for the hotel booking app
import streamlit as st
import streamlit.components.v1 as com
import base64
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



#sets the webpage configuration
image= Image.open('https://github.com/calebkwakye/hotelbooking/blob/main/images/sh.jpeg')
st.set_page_config(page_title="SpiderHub Oceanfront Hotel", page_icon=image, layout="wide")



#a function that changes the deafult background of the page to an image from the local storage
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
        
        
    }}
    .css-18ni7ap {{
           background: rgba(0,0,0,0)

    }}
    
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('/Users/calebkwakye/Desktop/ECON_242Project/images/r_-r-2_BZuGgkP4k-unsplash.jpg')    


#a function that gets a lottie animation from a url source
def getLottieAnimation(url):
    animation = requests.get(url)
    if animation.status_code != 200:
        return None
    return animation.json()




#Loads animation file
lottie_coding = getLottieAnimation("https://assets4.lottiefiles.com/packages/lf20_JXUInT.json")


# ------------------- ABOUT US SECTION --------------------
with st.container():
    st.title("WELCOME TO SPIDERHUB OCEANFRONT HOTEL")
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("ABOUT US")
        st.write("##")
        st.write(
            """
            The story of SpiderHub Hotels and Resorts, which opened its first hotel in 1961, is a tale of continual innovation, remarkable expansion and a single-minded dedication to the highest of standards. The Virginia Beach-based company has, for 60 years, transformed the hospitality industry by combining personalised, genuine care with an unwavering commitment to excellence. In the process, SpiderHub has redefined luxury for the modern traveller.
            Acclaimed as a North American leader in hospitality, the SpiderHub brand is unrivaled. Anticipating the demand for a new generation of leisure experiences – offering exceptional service and facilities in exotic destinations – the company focuses on expanding its portfolio of resorts. It also plans to introduce the brand to Asia.
            
            SpiderHub will continue its focus on global expansion, while maintaining its emphasis on creativity and innovation, both through the introduction of new properties and technologies, ultimately enhancing its leadership in luxury travel.
            Entering a new era, SpiderHub and the hospitality industry continue to work through the unprecedented challenges hitting the hotel industry, continuing to build upon the trust, care and flexibility that the company has long-established with its guests and residents. SpiderHub continues to focus on exceptional service, maintaining its development momentum with new projects in key markets and solidifying its place in the future of luxury hospitality.
            (Adapted from Four Seasons)
            
            """
        )
    with right_column:
        image = Image.open('/Users/calebkwakye/Desktop/ECON_242Project/images/tholaal-mohamed-8sKTHeGgrUM-unsplash.jpg')
        st.image(image)
  

# ------------------ SERVICE DESCRIPTION ---------------------
with st.container():
    st.write("---")
    st.header("DISCOVER LUXURY IN ITS EPIC PROPORTIONS")
    left_column, right_column = st.columns(2)
    with left_column:
     
        st.write("##")
        st.write(
            """
            With an unshakeable credo and corporate philosophy of un-wavering commitment to service, both in our hotels and in our communities, SpiderHub has been recognized with numerous awards for being the gold standard of hospitality.
            Our Credo:
            SpiderHub is a place where the genuine care and comfort of our guests is our highest mission.
            We pledge to provide the finest personal service and facilities for our guests who will always enjoy a warm, relaxed, yet refined ambience.
            The SpiderHub experience enlivens the senses, instills well-being, and fulfills even the unexpressed wishes and needs of our guests.
            
            What we can promise:
            - Private bath in each guest room
            - Lighter fabrics in the guest room to allow for more thorough washing
            - White tie and apron uniforms for the waitstaff, black tie for the Maître d’ and morning suits for all other staff, conducive to a formal, professional appearance
            - Extensive fresh flowers throughout the public areas
            - A la carte dining, providing choices for diners
            - Gourmet cuisine, utilizing the genius and cooking methods of Auguste Escoffier
            - Intimate, smaller lobbies for a more personalized guest experience
            (Adapted from Ritz-Carlton)
            
            """
        )
        image = Image.open('/Users/calebkwakye/Desktop/ECON_242Project/images/edvin-johansson-rlwE8f8anOc-unsplash.jpg')
        st.image(image)

    with right_column:
        image = Image.open('/Users/calebkwakye/Desktop/ECON_242Project/images/anmol-seth-hDbCjHNdF48-unsplash.jpg')
        st.image(image)


#------------ EXPLORE OUR ROOMS SECTION------------
with st.container():
    st.write("---")
    left_column, right_column = st.columns((10,1))
    with left_column:
        st.header("EXPLORE OUR ROOMS")
        st.write("##")
        image = Image.open('/Users/calebkwakye/Desktop/ECON_242Project/images/suites.png')
        st.image(image)
  


#------------ EXPLORE OUR SERVICE AND FACILITIES SECTION------------
with st.container():
    st.write("---")
    st.header("EXPLORE OUR SERVICES AND FACILITIES")
    column1, column2,column3,column4, column5 = st.columns(5)
    with column1:
        
        st.write("##")
        image=Image.open("/Users/calebkwakye/Desktop/ECON_242Project/images/160502155618-terranea-vista-pool.jpg")
        st.image(image,caption="Pool")

    with column2:
        
        st.write("##")
        image=Image.open("/Users/calebkwakye/Desktop/ECON_242Project/images/gym.jpeg")
        st.image(image,caption="Gym")

    with column3:
        
        st.write("##")
        image=Image.open("/Users/calebkwakye/Desktop/ECON_242Project/images/restaurant.webp")
        st.image(image,caption="Restaurants")


    with column4:
        
        st.write("##")
        image=Image.open("/Users/calebkwakye/Desktop/ECON_242Project/images/spa.jpeg")
        st.image(image,caption="SPA And Health Center")

    with column5:
        
        st.write("##")
        image=Image.open("/Users/calebkwakye/Desktop/ECON_242Project/images/catering.webp")
        st.image(image,caption="Catering Services")



#----------------- TESTIMONIALS SECTION--------------------
with st.container():
    st.write("---")
    left_column, right_column = st.columns((10,1))
    with left_column:
        st.header("TESTIMONIALS")
        st.write("##")
        image = Image.open('/Users/calebkwakye/Desktop/ECON_242Project/images/testimonials.png')
        st.image(image)


with st.container():
    st.write("---")
    st.header("OUR PERFORMANCE OVER THE YEARS")

    left_column, right_column = st.columns((1,11))

    with right_column:
        HtmlFile = open("/Users/calebkwakye/Desktop/ECON_242Project/images/hotel satisfaction.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        com.html(source_code,height=400)
        



#---------------- OUR TEAM SECTION--------------------
with st.container():
    st.write("---")
    left_column, right_column = st.columns((10,1))
    with left_column:
        st.header("OUR TEAM")
        st.write("##")
        image = Image.open('/Users/calebkwakye/Desktop/ECON_242Project/images/team.png')
        st.image(image)


#----------------- BOOKING SECTION ----------------------
with st.container():
    st.write("---")
    st.header("Book Your Reservation")

    left_column, right_column = st.columns(2)

    with left_column:
        st.write("##")
   

        # Create Fields:
        firstname = st.text_input("First Name(required): ")
        lastname = st.text_input("Last Name(required): ")
        username= firstname +" "+ lastname

        email = st.text_input("Your Email Address(required): ")
        phonenumber= st.text_input("Your phone number: ")
        wantsToBook = st.radio("Do you want to book now(required):",["No","Yes"],horizontal=True)

        # If they rsvp yes, show the room types, number of people and the check-in/check-out dates
        if wantsToBook == "Yes":
            roomChoice = st.selectbox("Room type (required):",["", "Junior Suite", "Executive Suite","Super Deluxe"])
            numberOfAdults = st.selectbox("Adults (required):",["", 1,2,3,4])
            numberOfChildren = st.selectbox("Children (required):",["", 1,2,3,4])
            checkIn = st.date_input("Check-in")
            checkOut = st.date_input("Check-out")
            specialRequests = st.text_input("Special Requests: ")
            
        # If they have filled out all the information correctly, show the book button
        if (((username != "") and (email != "") and (wantsToBook == "No")) or
            ((username != "") and (email != "") and (wantsToBook == "Yes") and 
            (roomChoice != ""))):    
            bookButton = st.button("Make A Reservation")

            # If they click the book button connect to the email server and send an email
            #confirming the reservation
            if (bookButton == True):
                # Server Information
                port = 465 # For SSL
                smtp_server = "smtp.gmail.com"
                sender_email = "booking.spiderhubhotel@gmail.com" # Enter your address (also the username)
                password = "lllwrdxlmdvxbzoy"

                # Create the body of the email (as the variable messagebody)
                messagebody="""

                """
                if wantsToBook=="Yes":
                    messagebody+=f"""Hi {username},<br>
                    <br>
                    Thank you for choosing SpiderHub Hotel.<br>
                    <br>
                    Below is a confirmation of your booking details:<br>
                    <b>Room choice:</b> {roomChoice}<br>
                    <b>Date of Arrival:</b> {checkIn}<br>
                    <b>Date of Departure:</b> {checkOut}<br>
                    <b>Number of Adults:</b> {numberOfAdults}<br>
                    <b>Number of children:</b> {numberOfChildren}<br>
                    <b>Special Requests</b>: {specialRequests}<br>
                    <br>
                    We look forward to welcoming you on {checkIn}.<br>
                    <br>
                    Regards,<br>
                    SpiderHub Management 
                    """
                else:
                    messagebody+= f"""Hi {username},<br>
                    <br>
                    It looks like you have an incomplete reservation with us.
                    Kindly visit our website to complete your booking when you're ready.<br>
                    <br>
                    We appreciate your interest and look forward to serving you in the future.<br>
                    <br>
                    Regards,<br>
                    SpiderHub Management
                    """

                # Create the actual message
                message = MIMEMultipart("alternative")
                message["Subject"] = "Booking Confirmation"
                message["From"] = sender_email
                message["To"] = email.strip()
                message["Cc"] = sender_email
                message.attach(MIMEText(messagebody, "html"))

                # Login and send the email
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.send_message(message)

                # Write confirmation
                st.write("Your Reservation Request has been submitted!")

    with right_column:
        st_lottie(lottie_coding, height=400, key="odings")

        



#--------------------------LOCATION SECTION -------------------------
with st.container():
    st.write("---")
    st.header("Location")
    st.write("##")
    image_column, text_column = st.columns((2, 3))
    with image_column:
        st.write(
            """
            The vibrant coastal city of Virginia Beach is home to a flourishing local culinary scene, rich history, a variety of arts and entertainment and family-friendly attractions that keeps visitors entertained year-round. Located in the Coastal Virginia region, the unique districts are open and thriving year-round. From the lively oceanfront areato remote Sandbridge, the calming Chesapeake Bay to bustling Town Center, or the eclectic ViBe creative district to our surrounding inland areas, your well-earned Virginia Beach vacation awaits you. 
            
            Virginia Beach is at its best this time of year, when the pace slows down just enough for you find your stride without missing a step. With pleasant weather and an unmistakably more local vibe, there's no better season to discover the vibrancy of this coastal city.
            Known for its flourishing local dining scene, arts and entertainment, maritime history, and family-friendly attractions, Virginia Beach features its own unique experiences for everyone to enjoy.
            We can't wait to share our favorite time of year with you and your family.

            """)
        
    with text_column:
        HtmlFile = open("/Users/calebkwakye/Desktop/ECON_242Project/images/hotel_map (1).html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        print(source_code)
        com.html(source_code,height=400)
       
        

      




