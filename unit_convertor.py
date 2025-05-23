import streamlit as st

conversion_factors = {
    '🔗 Length': {
        'Foot': 0.3048, 'Miles': 1609.34, 'Inch': 0.0254, 'Kilometer': 1000,
        'Meter': 1, 'Centimeter': 0.01, 'Millimeter': 0.001,
        'Micrometer': 1e-6, 'Nanometer': 1e-9
    },
    '🌐 Area': {
        'Square Meter': 1, 'Square Kilometer': 1e6, 'Square Foot': 0.092903,
        'Square Mile': 2.59e6, 'Acre': 4046.86
    },
    '💾 Digital Transfer Rate': {
        'Bps': 1, 'Kbps': 1e3, 'Mbps': 1e6, 'Gbps': 1e9, 'Tbps': 1e12
    },
    '🔋 Electric Current': {
        'Ampere': 1, 'Milliampere': 1e-3, 'Microampere': 1e-6
    },
    '⚡ Energy': {
        'Joule': 1, 'Kilojoule': 1e3, 'Calorie': 4.184,
        'Kilocalorie': 4184, 'Watt-hour': 3600
    },
    '🧲 Force': {
        'Newton': 1, 'Kilonewton': 1e3, 'Pound-force': 4.44822
    },
    '📡 Frequency': {
        'Hertz': 1, 'Kilohertz': 1e3, 'Megahertz': 1e6, 'Gigahertz': 1e9
    },
    '⚖️ Mass': {
        'Kilogram': 1, 'Gram': 1e-3, 'Milligram': 1e-6,
        'Metric Ton': 1000, 'Pound': 0.453592
    },
    '📐 Plane Angle': {
        'Degree': 1, 'Radian': 57.2958
    },
    '🚀 Power': {
        'Watt': 1, 'Kilowatt': 1e3, 'Megawatt': 1e6, 'Horsepower': 745.7
    },
    '🌡️ Temperature': {
        'Celsius': 'C', 'Fahrenheit': 'F', 'Kelvin': 'K'
    },
    '💧 Volume': {
        'Liter': 1, 'Milliliter': 1e-3, 'Cubic Meter': 1000,
        'Gallon': 3.78541
    },
    '⏱️ Time': {
        'Second': 1, 'Minute': 60, 'Hour': 3600,
        'Day': 86400, 'Week': 604800
    }
}

st.title('Unit Converter 🌍')

category = st.sidebar.selectbox('📂 Select Conversion Category', list(conversion_factors.keys()))

message_displayed = False  # Flag to control the message display

if category == '🌡️ Temperature':
    from_unit = st.selectbox('From 🌡️', conversion_factors[category].keys())
    to_unit = st.selectbox('To 🔄', conversion_factors[category].keys())
    value = st.number_input('🔢 Enter value', format='%f')

    if st.button('🚦 Convert'):
        message_displayed = True  # Set flag to True after button click
        if from_unit == to_unit:
            result = value
        elif from_unit == 'Celsius':
            if to_unit == 'Fahrenheit':
                result = (value * 9/5) + 32
            elif to_unit == 'Kelvin':
                result = value + 273.15
        elif from_unit == 'Fahrenheit':
            if to_unit == 'Celsius':
                result = (value - 32) * 5/9
            elif to_unit == 'Kelvin':
                result = (value - 32) * 5/9 + 273.15
        elif from_unit == 'Kelvin':
            if to_unit == 'Celsius':
                result = value - 273.15
            elif to_unit == 'Fahrenheit':
                result = (value - 273.15) * 9/5 + 32

        st.success(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")

else:
    from_unit = st.selectbox('From 🎯', conversion_factors[category].keys())
    to_unit = st.selectbox('To 🔄', conversion_factors[category].keys())
    value = st.number_input('🔢 Enter value', format='%f')

    if st.button('🚦 Convert'):
        message_displayed = True  # Set flag to True after button click
        result = value * conversion_factors[category][from_unit] / conversion_factors[category][to_unit]
        st.success(f'🎯 {value} {from_unit} = {result:.3f} {to_unit}' if result % 1 != 0 else f'🎯 {value} {from_unit} = {int(result)} {to_unit}')