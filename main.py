import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from vehicle_module import Vehicle, PremiumVehicle


# =========================================================
# FUNCTION 1
# Register Customer and Vehicle
# =========================================================
def register_customer_vehicle(
    name,
    phone,
    vehicle_number,
    model
):
    vehicle = Vehicle(
        name,
        phone,
        vehicle_number,
        model
    )

    return vehicle


# =========================================================
# FUNCTION 2
# Calculate Service Charge
# =========================================================
def calculate_service_charge(services):
    total = sum(services.values())
    return total


# =========================================================
# FUNCTION 3
# Display Customer and Vehicle Information
# =========================================================
def display_customer_vehicle(vehicle):

    return (
        f"Owner Name: {vehicle.owner_name}\n"
        f"Phone: {vehicle.phone}\n"
        f"Vehicle Number: {vehicle.vehicle_number}\n"
        f"Vehicle Model: {vehicle.model}\n"
        f"Service Total: RM{vehicle.service_total:.2f}"
    )


# =========================================================
# SERVICE LIST
# =========================================================

service_prices = {
    "Oil Change": 80,
    "Brake Service": 150,
    "Air Conditioning Service": 120,
    "Battery Service": 200,
    "Engine Service": 300
}


# =========================================================
# STREAMLIT PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="AutoCare Service Centre",
    page_icon="🚗",
    layout="centered"
)


# =========================================================
# TITLE
# =========================================================

st.title("🚗 AutoCare Service Centre")

st.subheader(
    "Smart Car Service Centre Management and Analysis System"
)

st.info(
    "Welcome to AutoCare Service Centre. "
    "Enter customer and vehicle information, "
    "select the required services, and calculate "
    "the total service charge."
)


# =========================================================
# CUSTOMER INFORMATION
# =========================================================

st.header("👤 Customer Information")

name = st.text_input(
    "Customer Name"
)

phone = st.text_input(
    "Phone Number"
)


# =========================================================
# VEHICLE INFORMATION
# =========================================================

st.header("🚘 Vehicle Information")

vehicle_number = st.text_input(
    "Vehicle Number"
)

model = st.text_input(
    "Vehicle Model"
)


# =========================================================
# VEHICLE TYPE
# =========================================================

vehicle_type = st.selectbox(
    "Vehicle Type",
    [
        "Regular Vehicle",
        "Premium Vehicle"
    ]
)


# =========================================================
# SERVICE SELECTION
# =========================================================

st.header("🔧 Select Service")

selected_services = st.multiselect(
    "Choose one or more services",
    list(service_prices.keys())
)


# =========================================================
# AUTOMATIC SERVICE CHARGE DISPLAY
# =========================================================

if selected_services:

    st.subheader("Selected Services")

    preview_total = 0

    for service in selected_services:

        charge = service_prices[service]

        st.write(
            f"**{service}** — RM{charge:.2f}"
        )

        preview_total += charge

    st.info(
        f"Current Service Total: RM{preview_total:.2f}"
    )


# =========================================================
# CALCULATE BUTTON
# =========================================================

if st.button(
    "Calculate Service",
    type="primary"
):

    try:

        # =================================================
        # INPUT VALIDATION
        # =================================================

        # Customer name
        if name.strip() == "":
            raise ValueError(
                "Customer name cannot be empty."
            )


        # Phone empty
        if phone.strip() == "":
            raise ValueError(
                "Phone number cannot be empty."
            )


        # Phone must contain numbers only
        if not phone.isdigit():
            raise ValueError(
                "Phone number must contain numbers only."
            )


        # Phone length
        if len(phone) < 10 or len(phone) > 11:
            raise ValueError(
                "Phone number must contain 10 or 11 digits."
            )


        # Vehicle number
        if vehicle_number.strip() == "":
            raise ValueError(
                "Vehicle number cannot be empty."
            )


        # Vehicle model
        if model.strip() == "":
            raise ValueError(
                "Vehicle model cannot be empty."
            )


        # Service selection
        if not selected_services:
            raise ValueError(
                "Please select at least one service."
            )


        # =================================================
        # CREATE SERVICE DATA
        # =================================================

        selected_service_data = {}

        for service in selected_services:

            selected_service_data[service] = (
                service_prices[service]
            )


        # =================================================
        # CALCULATE TOTAL
        # =================================================

        total = calculate_service_charge(
            selected_service_data
        )


        # =================================================
        # CREATE VEHICLE OBJECT
        # =================================================

        if vehicle_type == "Premium Vehicle":

            vehicle = PremiumVehicle(
                name,
                phone,
                vehicle_number,
                model,
                total
            )

        else:

            vehicle = register_customer_vehicle(
                name,
                phone,
                vehicle_number,
                model
            )

            vehicle.service_total = total


        # =================================================
        # SUCCESS MESSAGE
        # =================================================

        st.success(
            "Service information processed successfully!"
        )


        # =================================================
        # CUSTOMER & VEHICLE INFORMATION
        # =================================================

        st.header(
            "📋 Customer & Vehicle Information"
        )

        st.text(
            display_customer_vehicle(vehicle)
        )


        # =================================================
        # SELECTED SERVICES
        # =================================================

        st.header(
            "🔧 Selected Services"
        )

        for service in selected_services:

            charge = service_prices[service]

            st.write(
                f"**{service}**: RM{charge:.2f}"
            )


        # =================================================
        # TOTAL SERVICE CHARGE
        # =================================================

        st.header(
            "💰 Total Service Charge"
        )

        st.metric(
            "Total",
            f"RM{total:.2f}"
        )


        # =================================================
        # PREMIUM VEHICLE
        # =================================================

        if vehicle_type == "Premium Vehicle":

            st.info(
                vehicle.premium_service()
            )


        # =================================================
        # NUMPY ANALYSIS
        # =================================================

        st.header(
            "📊 NumPy Analysis"
        )

        charge_array = np.array(
            list(
                selected_service_data.values()
            )
        )


        # Array
        st.subheader(
            "Service Charge Array"
        )

        st.write(
            charge_array
        )


        # Array attributes
        st.subheader(
            "Array Attributes"
        )

        st.write(
            "Shape:",
            charge_array.shape
        )

        st.write(
            "Size:",
            charge_array.size
        )

        st.write(
            "Data Type:",
            charge_array.dtype
        )


        # Indexing
        st.subheader(
            "NumPy Indexing"
        )

        st.write(
            "First Service Charge:",
            charge_array[0]
        )


        # Slicing
        st.subheader(
            "NumPy Slicing"
        )

        st.write(
            "First Two Service Charges:",
            charge_array[:2]
        )


        # Mathematical analysis
        st.subheader(
            "Mathematical Analysis"
        )

        st.write(
            f"Total: RM{np.sum(charge_array):.2f}"
        )

        st.write(
            f"Average: RM{np.mean(charge_array):.2f}"
        )

        st.write(
            f"Highest: RM{np.max(charge_array):.2f}"
        )

        st.write(
            f"Lowest: RM{np.min(charge_array):.2f}"
        )


        # =================================================
        # PANDAS ANALYSIS
        # =================================================

        st.header(
            "🐼 Pandas Data Analysis"
        )


        analysis_data = {

            "Service": selected_services,

            "Charge": [
                service_prices[service]
                for service in selected_services
            ]
        }


        df = pd.DataFrame(
            analysis_data
        )


        # DataFrame
        st.subheader(
            "Service DataFrame"
        )

        st.dataframe(
            df,
            use_container_width=True
        )


        # Filtering
        st.subheader(
            "Services Above RM100"
        )

        filtered_df = df[
            df["Charge"] > 100
        ]

        st.dataframe(
            filtered_df,
            use_container_width=True
        )


        # Sorting
        st.subheader(
            "Services Sorted by Charge"
        )

        sorted_df = df.sort_values(
            by="Charge",
            ascending=False
        )

        st.dataframe(
            sorted_df,
            use_container_width=True
        )


        # =================================================
        # MATPLOTLIB GRAPH
        # =================================================

        st.header(
            "📈 Service Charge Graph"
        )

        fig, ax = plt.subplots()

        ax.bar(
            df["Service"],
            df["Charge"]
        )

        ax.set_title(
            "Service Charges"
        )

        ax.set_xlabel(
            "Service"
        )

        ax.set_ylabel(
            "Charge (RM)"
        )

        plt.xticks(
            rotation=30
        )

        plt.tight_layout()

        st.pyplot(
            fig
        )


    # =====================================================
    # EXCEPTION HANDLING
    # =====================================================

    except ValueError as e:

        st.error(
            f"❌ Error: {e}"
        )


    except Exception as e:

        st.error(
            f"❌ Unexpected error: {e}"
        )