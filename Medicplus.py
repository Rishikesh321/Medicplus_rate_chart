import streamlit as st


header = st.container()
body = st.container()

with header:
    from PIL import Image
    image = Image.open('icon.png')

    st.image(image,width=100)
    st.title("Welcome to Medicplus Pharma Merchants")
    st.write("Medicplus Empowering Micro Phramacys to grow & establish their bussiness. Now get credit with a single tap, within 10 hours.")
    st.write("Medicplus is on a mission to make healthcare facilities more affordable & accessible for over a million Indians. We believe in empowering our users, with the most accurate & curated information, enabling them to take better healthcare decision")

with body:
    st.header("Calculate your Installment Credit")
    #Components
    r = 2
    
    col1,col2 = st.columns(2)
    with col1:
     P = st.slider('Please Enter your Loan Amount ₹', 1000, 100000)
    with col2:
     t = st.slider('Please Enter your Time Period in months',1,36)
    
    #Calculation
    CI = round(float(P*(1 + (r/1200))**(12*t)),2)
    EDI = round(float(CI/(t*30)),2)
    
    
    #Infobox

    col3, col4, col5 = st.columns(3)
    
    with col3:
     st.metric(label="Total Amount Payable ₹", value = CI)
    with col4:
     st.metric(label="Interest Rate", value= "2%")
    with col5:
     st.metric(label = "Equal Daily Installment ₹", value = EDI)



