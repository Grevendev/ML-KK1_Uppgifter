import streamlit as st
import pandas as pd
import joblib


# ============================================================
# 1. Ladda datasetet och den tränade modellen
# ============================================================

df = pd.read_csv("car_price_dataset.csv", sep=";")



model = joblib.load("car_price_linear_regression.joblib")


# ============================================================
# 2. Titel och information
# ============================================================

st.title("🚗 Car Price Predictor")

st.write(
    "Ange information om bilen nedan för att få ett predikterat pris."
)


# ============================================================
# 3. Välj bilmärke
#    Vi hämtar märkena direkt från CSV-filen.
# ============================================================

brands = sorted(df["Brand"].dropna().unique())

brand = st.selectbox(
    "Brand",
    brands
)


# ============================================================
# 4. Välj bilmodell
#    Här visar vi endast modeller som tillhör det valda märket.
# ============================================================

models = sorted(
    df[df["Brand"] == brand]["Model"].dropna().unique()
)

model_name = st.selectbox(
    "Model",
    models
)


# ============================================================
# 5. Årsmodell
#    Min/max hämtas automatiskt från datasetet.
# ============================================================

year = st.number_input(
    "Year",
    min_value=int(df["Year"].min()),
    max_value=int(df["Year"].max()),
    value=int(df["Year"].max()),
    step=1
)


# ============================================================
# 6. Motorstorlek
# ============================================================

engine_size = st.number_input(
    "Engine Size",
    min_value=float(df["Engine_Size"].min()),
    max_value=float(df["Engine_Size"].max()),
    value=float(df["Engine_Size"].median()),
    step=0.1
)


# ============================================================
# 7. Bränsletyp
#    Alternativen hämtas direkt från CSV-filen.
# ============================================================

fuel_types = sorted(
    df["Fuel_Type"].dropna().unique()
)

fuel_type = st.selectbox(
    "Fuel Type",
    fuel_types
)


# ============================================================
# 8. Växellåda
# ============================================================

transmissions = sorted(
    df["Transmission"].dropna().unique()
)

transmission = st.selectbox(
    "Transmission",
    transmissions
)


# ============================================================
# 9. Mileage
# ============================================================

mileage = st.number_input(
    "Mileage",
    min_value=float(df["Mileage"].min()),
    max_value=float(df["Mileage"].max()),
    value=float(df["Mileage"].median()),
    step=1000.0
)


# ============================================================
# 10. Antal dörrar
# ============================================================

doors = st.number_input(
    "Doors",
    min_value=int(df["Doors"].min()),
    max_value=int(df["Doors"].max()),
    value=int(df["Doors"].median()),
    step=1
)


# ============================================================
# 11. Antal tidigare ägare
# ============================================================

owner_count = st.number_input(
    "Owner Count",
    min_value=int(df["Owner_Count"].min()),
    max_value=int(df["Owner_Count"].max()),
    value=int(df["Owner_Count"].median()),
    step=1
)


# ============================================================
# 12. Prediktion
# ============================================================

if st.button("Predict Price"):

    # Skapa en DataFrame med exakt samma kolumner
    # som användes när ML-modellen tränades.
    new_car = pd.DataFrame({
        "Brand": [brand],
        "Model": [model_name],
        "Year": [year],
        "Engine_Size": [engine_size],
        "Fuel_Type": [fuel_type],
        "Transmission": [transmission],
        "Mileage": [mileage],
        "Doors": [doors],
        "Owner_Count": [owner_count]
    })


    # Skicka bilen till den sparade ML-modellen.
    predicted_price = model.predict(new_car)


    # Hämta det predikterade priset.
    price = predicted_price[0]


    # Visa resultatet för användaren.
    st.success(
        f"Predicted price: ${price:,.2f}"
    )