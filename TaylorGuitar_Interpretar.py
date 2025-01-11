import streamlit as st

# Function to interpret the serial number
def interpret_serial(serial_number):
    # Ensure the serial number is valid (9, 10, or 11 digits)
    if len(serial_number) not in [9, 10, 11] or not serial_number.isdigit():
        return {"error": "Invalid serial number. It should be 9, 10, or 11 digits. Please try again."}

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
    background-size: contain;
    background-position: center center;
    background-attachment: fixed;
    height: 100vh;
}
[data-testid="stSidebar"] {
    background-color: rgba(255, 255, 255, 0.5);
}
div[role="alert"] {
    background-color: rgba(255, 0, 0, 0.8) !important;
    color: white !important;
    font-weight: bold;
    border-radius: 5px;
    padding: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Main title
st.markdown("<h1 style='text-align: center;'>Taylor Guitar</h1>", unsafe_allow_html=True)

# Subtitle
st.markdown("<h3 style='text-align: center;'>Serial Number Interpreter</h3>", unsafe_allow_html=True)

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

# Button to show pre-1993 information
if st.button("Show Pre-1993 Serial Numbers"):
    st.write("### Taylor Guitars Pre-1993 Serial Numbers")
    st.table({
        "Serial Numbers": [
            "[No serial numbers]", "00108 and 10109 to 10146", "20147 to 20315",
            "30316 to 450", "451 to 900", "901 to 1300", "1301 to 1400",
            "1401 to 1670", "1671 to 1951", "1952 to 2445", "2446 to 3206",
            "3207 to 3888", "3889 to 4778", "4779 to 5981", "5982 to 7831",
            "7832 to 10070", "10071 to 12497", "12498 to 15249", "15250 to 17947"
        ],
        "Year": [
            "1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981",
            "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989",
            "1990", "1991", "1992"
        ]
    })

# Footer
st.markdown("""
    <div style='position: fixed; bottom: 10px; width: 100%; text-align: center;'>
        Developed by: EagleOne Originals, Sweden, January 2025.
    </div>
""", unsafe_allow_html=True)





