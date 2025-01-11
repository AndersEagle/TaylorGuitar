import streamlit as st

# Function to interpret the serial number
def interpret_serial(serial_number):
    # Ensure the serial number is valid (9, 10, or 11 digits)
    if len(serial_number) not in [9, 10, 11] or not serial_number.isdigit():
        return {"error": "Invalid serial number. It should be 9, 10, or 11 digits."}

    # Process based on the serial number length
    if len(serial_number) == 10:
        # Handle 10-digit serial numbers
        factory_code = int(serial_number[0])  # First digit for factory code
        year = "20" + serial_number[1] + serial_number[6]  # 2nd digit + 7th digit for the year
        month = serial_number[2:4]  # 3rd & 4th digits for the month
        day = serial_number[4:6]  # 5th & 6th digits for the day
        production_sequence = serial_number[7:]  # Last three digits for production sequence
        factory_location = "El Cajon, California, USA" if factory_code == 1 else "Tecate, Baja California, Mexico"

        # Create the result
        return {
            "Serial Number": serial_number,
            "Factory Location": factory_location,
            "Year of Production": year,
            "Month of Production": month,
            "Day of Production": day,
            "Production Sequence Number": production_sequence,
        }

    elif len(serial_number) == 9:
        # Handle 9-digit serial numbers
        year = "19" + serial_number[:2]  # First two digits for the year
        month = serial_number[2:4]  # 3rd & 4th digits for the month
        day = serial_number[4:6]  # 5th & 6th digits for the day
        series_code = serial_number[6]  # 7th digit for series code
        production_sequence = serial_number[7:]  # Last two digits for production sequence

        # Map series code to series
        series_mapping = {
            "0": "300 or 400 Series",
            "1": "500 through Presentation Series",
            "2": "200 Series",
            "3": "Baby or Big Baby (through 2002)",
            "4": "Big Baby (2004-2009)",
            "5": "T5",
            "7": "Nylon Series",
            "8": "100 Series",
            "9": "SolidBody Series",
        }
        series = series_mapping.get(series_code, "Unknown Series")

        # Create the result
        return {
            "Serial Number": serial_number,
            "Year of Production": year,
            "Month of Production": month,
            "Day of Production": day,
            "Series": series,
            "Production Sequence Number": production_sequence,
        }

    elif len(serial_number) == 11:
        # Handle 11-digit serial numbers
        year = serial_number[:4]  # First four digits for the year
        month = serial_number[4:6]  # 5th & 6th digits for the month
        day = serial_number[6:8]  # 7th & 8th digits for the day
        series_code = serial_number[8]  # 9th digit for series code
        production_sequence = serial_number[9:]  # Last two digits for production sequence

        # Map series code to series
        series_mapping = {
            "0": "300 or 400 Series",
            "1": "500 through Presentation Series",
            "2": "200 Series",
            "3": "Baby or Big Baby (through 2002)",
            "4": "Big Baby (2004-2009)",
            "5": "T5",
            "6": "T3",
            "7": "Nylon Series",
            "8": "100 Series",
            "9": "SolidBody Series",
        }
        series = series_mapping.get(series_code, "Unknown Series")

        # Create the result
        return {
            "Serial Number": serial_number,
            "Year of Production": year,
            "Month of Production": month,
            "Day of Production": day,
            "Series": series,
            "Production Sequence Number": production_sequence,
        }

# Streamlit application interface
# Background customization
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://raw.githubusercontent.com/AndersEagle/TaylorGuitar/main/Taylor_Background2.jpg");
    background-size: cover;  /* Ensures the image always covers the entire container */
    background-position: center center;  /* Centers the image in the container */
    background-attachment: fixed;  /* Ensures the background stays fixed when scrolling */
    height: 100vh;  /* Ensures the background fills the entire viewport height */
}
[data-testid="stSidebar"] {
    background-color: rgba(255, 255, 255, 0.5);
}

/* Styling for the boxes around text */
div.stMarkdown, div.stText {
    background-color: rgba(211, 211, 211, 0.8);  /* Light grey background */
    color: #333333;  /* Dark grey text */
    padding: 10px;
    border-radius: 5px;  /* Rounded corners */
    margin-bottom: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);  /* Slight shadow for 3D effect */
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Taylor Guitar Serial Number Interpreter")
st.write("Enter the serial number of your Taylor guitar to learn about its details.")

# User input for serial number
serial_number = st.text_input("Enter the Taylor guitar serial number (9, 10, or 11 digits):", "")

# Display result when serial number is entered
if serial_number:
    result = interpret_serial(serial_number)

    # Check for errors in the result
    if "error" in result:
        st.error(result["error"])
    else:
        st.write("### Serial Number Details:")
        for key, value in result.items():
            st.write(f"**{key}:** {value}")


