
from cProfile import label
from tokenize import Number      # import lable
import streamlit as st     #import streamlit ---> pip install streamlit 
from PIL import Image     # import image
import time      #import time
import datetime         #import datetime



add_selectbox = st.sidebar.selectbox("Home",("Home","Login", "Register", "Ticket Booking","About")) # using selectbar and side bars 
if add_selectbox =="Home": # if condition
    st.title("Covai Cinemas") # tish is itle
   
    img = Image.open(r"C:\Users\elcot\Downloads\imax.jpg")  # opening image  use image path

    st.image(img)
    
    st.subheader("Welcome to Covai cinemas!") # tish is subheader
    
    st.text("Covai Cinemas provides: High Class, In house Air-Condition, DTS Sound Experience,\nDigital Video Projection, Excellent Parking Facility, Executive Seats Available,\n1555 Seating Capacity, Advance Booking, 24 Hours Online Ticketing.")

    st.markdown("Location : Ghandhipuram Bus stand,Ramnagar,coimbatore") # markdown - display string formatted
    
    img = Image.open(r"C:\Users\elcot\Downloads\telebooking_2.png")
    
    
    with st.form(key="book"): #form to use add elements to a form object
        
        st.header("Telephone Booking") #header
        st.image(img, width =200,caption ="")
        
        submission=st.form_submit_button(label="Call") #To create a submission button
        if submission == True : #if Condition
            st.success("Calling... 9940015553 ") #Display the success message
            
            
    st.subheader("Telephone / Ph Booking")
    st.subheader("Telephone No : 0422 01234")
    st.subheader("   Mobile No : 9940015553")
    st.subheader("Booking Open")
    
    
    img = Image.open(r"C:\Users\elcot\Downloads\beast.jpg")
    st.image(img)
    occ = st.selectbox("Beast",["  ","Overview","Movie Cast"])     #Display the select widget
    
    if occ=='Overview':
        st.text("Beast is a 2022 Indian Tamil-language action film written and directed by Nelson.\nThe film stars Vijay, Pooja Hegde and Selvaraghavan. It revolves around an ex-RAW agent's quest to rescue people held hostage in a shopping mall by terrorists.")
    
    if occ=='Movie Cast':
        st.text("Director : Nelson Dilipkumar\nMusic : Anirudh Ravichander\nProducer : Kalanithi Maran\nStarring \nJoseph Vijay\nSelvaraghavan\nPooja Hegde\nVtv Ganesh\nAparna Das\nSathish Krishnan")
    st.subheader("Upcomming Movie")
    img = Image.open(r"C:\Users\elcot\Downloads\vikram.jpg")
    st.image(img)

    occ = st.selectbox("Vikram",["  ","Overview","Movie Cast"])     #Display the select widget
    
    if occ=='Overview':
        st.text("Vikram is a 2022 Indian Tamil-language action thriller film written and directed by Lokesh Kanagaraj and produced by Raaj Kamal Films International.[5]\nThe film stars Kamal Haasan, Vijay Sethupathi and Fahadh Faasil.[6][7] Kalidas Jayaram,[8] Narain and Chemban Vinod Jose play supporting roles while Suriya makes a cameo appearance as Rolex.")
    
    if occ=='Movie Cast':
        st.text("Director : Lokesh Kanagaraj\nProducer : Kamal Haasan\nMusic : Anirudh Ravichander\nDialogue by : Rathna Kumar\nstarring\nKamal Haasan\nFahadh Faasil\nVijay Sethupathi\nSuriya")
    
if add_selectbox =="Login":
    
    with st.form(key="Login"):
        st.title("Covai Cinemas")
        st.subheader("UserName & Password")
        u_name=st.text_input("Enter a user Name")
        pwd=st.text_input("Enter a password", type="password")
        
        if pwd=='Soundhar@123':
            if u_name=='Soundhar4792': 
                submission=st.form_submit_button(label="Submit 👈")
        
                if submission == True:
                    with st.spinner("wait"):
                        time.sleep(2)
                    st.success("Login Successfully")
            else:
                submission=st.form_submit_button(label="Submit 👈")
                if submission == True:
                    st.error("Wrong User Name or Password ")
        else:
            submission=st.form_submit_button(label="Submit 👈")
            if submission == True:
                st.error("Wrong User Name or Password")            
                
                
if add_selectbox =="Register":
    with st.form(key="Register"):
        st.title("Covai Cinemas")
        st.subheader("Register")
        location = st.selectbox("location",["Covai","Chennai","Salem"])
        name=st.text_input("Enter your name ")
        mobile_no= st.number_input("Enter Mobile number")
        email=st.text_input("Enter Email id")
        dob=st.date_input('Date of birth')
        gender = st.selectbox("Gender",["Select","Male","Female","Other"])
        pwd_1=st.text_input("Enter a New Password", type="password")
        pwd_2=st.text_input("Enter a Confirm password", type="password")

        if pwd_1==pwd_2:
            submission=st.form_submit_button(label="Submit 👈")
        
            if submission== True:
                with st.spinner("wait"):
                    time.sleep(2)
                st.success("Successfully Registered")

        else:
            submission=st.form_submit_button(label="Submit 👈")
            if submission == True:
                st.error("Password Missmatch")
                
    print("CUSTOMER DETAILS")
    print("\nLocation:",location)
    print("Name    :",name)
    print("Mbile no:",int(mobile_no))
    print("Email   :",email)
    print("Dob     :",dob)
    print("Gender  :",gender)



if add_selectbox =="Ticket Booking":
    st.title("Covai Cinemas")
    st.subheader("Online Ticket Booking")
    
    
    with st.form(key="Booking2"):
        movie_name=st.selectbox("Select Movie",["Select Movie","BEAST ","KGF 2","VALIMAI","RRR"])
        laguage=st.selectbox("Select Language",["Tamil","Telugu","Malayalam","Kannadam","Hindhi"])
        date=st.date_input('Date')
        movie_time=st.selectbox("Show Time",["Select time","10.00 AM ","02.00 PM","06.00 PM","10.00 PM"])
        ticket= st.number_input("No of tickets")
        seat = st.selectbox("Select Row",["Select Row","A","B","C","D","E","F","G","H"])
        seat_1 = st.text_input("Enter Seat No")
        price = st.selectbox("Price Rs",[60 ,100,200])
        submission=st.form_submit_button(label="Submit 👈")
        
        
        
        if submission== True:
            with st.spinner("wait"):
                    time.sleep(5)
            st.success("Booking Confirmed")
            st.success("Your Tickets are send to your Phone No / Email")
            st.balloons()
            
            
            print("\n\n\nWELCOME TO COVAI CINEMAS\nTicket Details\n\nMovie Name  :",movie_name,"\nDate        :",date,"\nTime        :",movie_time,"\nLanguage    :",laguage,"\nTickets     :",int(ticket),"\nSeat Row No :",seat,"-",seat_1,"\nprice       :",price,"\nTotal Amount:",int(ticket)* price,"\n(Include tax)","\n\nTHANKYOU FOR BOOKING")



if add_selectbox == "About":
    st.title("Welcome To Covai Cinemas")
    
    img = Image.open(r"C:\Users\elcot\Downloads\cinema.jpg")
    st.image(img)
    
    st.subheader("Welcome to Covai cinemas!")
    st.text("Covai Cinemas provides: High Class, In house Air-Condition, DTS Sound Experience,\nDigital Video Projection, Excellent Parking Facility, Executive Seats Available,\n1555 Seating Capacity, Advance Booking, 24 Hours Online Ticketing.")
    st.markdown("Location : Ghandhipuram Bus stand,Ramnagar,coimbatore")
    img = Image.open(r"C:\Users\elcot\Downloads\telebooking_2.png")
    st.header("Telephone Booking")
    st.image(img, width =200,caption ="")
    st.button("Call Booking")
    st.subheader("Telephone / Ph Booking")
    st.subheader("Telephone No : 0422 01234")
    st.subheader("   Mobile No : 9940015553")
    st.subheader("Booking Open")
    
    img = Image.open(r"C:\Users\elcot\Downloads\beast.jpg")
    st.image(img)
    st.subheader("Upcomming Movie")
    
    img = Image.open(r"C:\Users\elcot\Downloads\vikram.jpg")
    st.image(img)
    st.text("Covai Cinemas provides: High Class, In house Air-Condition, DTS Sound Experience,\nDigital Video Projection,Excellent Parking Facility, Executive Seats Available,\n1555 Seating Capacity, Advance Booking, 24 Hours Online Ticketing.")

