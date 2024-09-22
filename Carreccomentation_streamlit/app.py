import streamlit as st
import requests

# Set your Gemini API key here
API_KEY = 'AIzaSyBX7FjwaAgFT4-kBWw78U8nZ_D1YkyWdWs'  # Replace with your actual API key
API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'

# Bootstrap-based CSS styling with black car background
st.markdown("""
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
    .main {
        background-image: url('https://wallpapercrafter.com/th800/14002-car-sunset-night-movement-speed-4k.jpg'); /* Replace with a black car image URL */
        background-size: cover;
        background-color: black;
        padding: 30px;
        color: white;
        font-family: 'Dancing Script', cursive;
        font-size: 18px;
    }
    .title {
        font-size: 60px;
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.9);
    }
    .stTextArea textarea {
        font-size: 20px;
        padding: 15px;
        border-radius: 5px;
        border: 2px solid rgba(255, 255, 255, 0.7);
        background: rgba(0, 0, 0, 0.8);
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
    }
    .stButton>button {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 5px;
        border: 2px solid rgba(255, 255, 255, 0.7);
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
        transition: none;
    }
    .stButton>button:hover {
        background-color: rgba(255, 255, 255, 0.2);
        color: white;
    }
    .stAlert {
        font-size: 18px;
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.7);
        border-radius: 5px;
    }
    .stSpinner {
        color: rgba(0, 123, 255, 0.7);
    }
    </style>
    """, unsafe_allow_html=True)

def generate_content(prompt):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'contents': [{
            'parts': [{
                'text': prompt
            }]
        }]
    }
    
    response = requests.post(f"{API_URL}?key={API_KEY}", headers=headers, json=data)
    
    print("Response Status Code:", response.status_code)
    print("Response Body:", response.json())

    if response.status_code == 200:
        response_data = response.json()
        if 'candidates' in response_data and len(response_data['candidates']) > 0:
            return response_data['candidates'][0]['content']['parts'][0]['text']
        else:
            return 'No candidates found in response.'
    else:
        return f"Error: {response.status_code} - {response.text}"

def main():
    st.markdown("<div class='title'>CAR for me</div>", unsafe_allow_html=True)
    
    # Default prompt
    default_prompt = (
        "Please provide the following details for car rental:\n\n"
        "1. Trip Details:\n"
        "   - Where are you going? (City, state, or region) : \n"
        "   - How long will you be renting the car for? (Days or weeks) :\n"
        "   - What kind of roads will you be driving on? (Highway, city, off-road) :\n\n"
        "2. Travel Style:\n"
        "   - How many people are you travelling with? :\n"
        "   - Do you need a lot of luggage space? :\n"
        "   - Are you on a budget or willing to spend more for comfort/features? :\n\n"
        "3. Driving Preferences:\n"
        "   - Do you prefer a manual or automatic transmission? :\n"
        "   - Do you need a car with air conditioning? :\n"
        "   - Are you looking for a fuel-efficient car? :\n\n"
        "4. Budget:\n"
        "   - What is your budget per day in rupees? :"
    )
    
    st.write("Welcome to the Car Rental Chatbot! Please answer the questions below:")
    
    # Use the default prompt
    prompt = st.text_area("Prompt", default_prompt, height=300)
    
    if st.button("Generate Recommendations"):
        if prompt:
            with st.spinner("Generating recommendations..."):
                content = generate_content(prompt)
                st.success("Recommendations generated successfully!")
                st.write(content)
        else:
            st.warning("Please enter your details.")

if __name__ == "__main__":
    main()
