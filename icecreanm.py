import streamlit as st

st.set_page_config(page_title="Sweet Scoop Ice cream",page_icon="🍨",layout="centered",
                   initial_sidebar_state="collapsed",
                   menu_items={'Get Help' : 'https://example.com/help','About':'Made by Freddy'})

st.title("🍦Sweet scoop ice cream parlour")
st.subheader("Design your ice cream and place the order!")

#choosing your base
base = st.radio("Choose your base", ["Cone", "Cup"])

#How many scoops?
scoops = st.slider("How many scoops do you want?", min_value=1,max_value=5)

#pick flavors
flavors = st.multiselect("Choose your flavors", ["Vanila","Strawberry","Chocolate","Mango"])

#Add toppings
toppings = st.multiselect("Add toppings", ["Nuts","Cherry","Choco Chips","Sprinkles"])

st.markdown("##  Your Ice cream ")

flavor_preview = "..".join(flavors) if flavors else "No flavors"
topping_preview = "**".join(toppings) if toppings else "No Toppings"

st.markdown("##  Your Ice cream ")

flavor_preview = "..".join(flavors) if flavors else "No flavors"
topping_preview = "**".join(toppings) if toppings else "No Toppings"

col1,col2 = st.columns(2)

with col1:
  st.markdown(f"### Base: {base}")
  st.markdown(f"### Scoops: {scoops}")

  #Calculate price
price = 20
price = price + (scoops * 10)
price = price + len(toppings) * 5

st.markdown(f"## Total price : {price}")

#place the order
if st.button("Place Order"):
  st.success(f"Your {base} with {scoops} scoop(s) is being prepared")


name = st.text_input("Enter your name")

# Generate Receipt button
if st.button("Generate Receipt"):
  receipt = f"""
  Name: {name if name else "Guest"}
  _________________________________
  Flavors : {flavor_preview}
  Toppings : {topping_preview}
  _________________________________
  Thank you for your order
  """
  st.text_area("Your Receipt:",receipt,height=200)
  st.download_button("Download Receipt",receipt,file_name = "ice_cream_receipt.txt")
