import streamlit as st
from langraph.graph import StateGraph
import google.generativeai as genai
from datetime import date

#Gemini API key 
genai.configure(api_key="AIzaSyAnn_UrQdTnTi5LMy1H7CG_w-77QwRA7ZI")
model = genai.GenerativeModel("gemini-2.5-pro")

#Multiple agents for specific task
#Agent A is Extract user Intent

def extract_user_intent(state):
  return{
      "location":state["location"], #'location':'paris'
      "budget":state["budget"],
      "days":state["days"],
      "date":state["date"]
  }

# Agent B - suggest places
def suggest_places(state):
  location = state["location"] #location = 'Dubai'
  prompt = f"Suggest top 5 tourist attractions in {location} for a family trip"
  response = model.generate_content(prompt)
  return{**state,"places":response.text}

def suggest_budget_options(state):
  raw_budget = str(state["budget"]).lower().replace(",","").strip()
  if "lakh" in raw_budget:
    try:
      number_part = float(raw_budget.split("lakh")[0].strip())
      budget = int(number_part * 100000)
    except:
      budget = 0  

  elif "k" in raw_budget:
    try:
      number_part = float(raw_budget.replace("k",""))
      budget = int(number_part * 1000)
    except:
      budget = 0  

  else:
    try:
      budget = int(raw_budget)
    except:
      budget = 0  
state["numeric_budget"] = budget

#suggestion
if budget < 10000:
  options = "Budget stay, street food, shared transport"
elif budget < 30000:
  options = "3-star hotels, local restro, guided tours"  
elif budget < 100000:
  options = "luxury hotels, private tours, flights" 
else:
  options = "premium vacation with custom experiences"

return {**state,"budget_tips":options}  

def recommend_hotels(state):
  location = state["location"]
  budget = state["numeric_budget"]

  prompt = f"""
  Recommend 3 good hotels in {location} for a family trip.
  Budget is around {budget}. Include hotel name, price per night, and a short
  description."""

  response = model.generate_content(prompt)
  return {**state,"hotels":response.text}

  def create_itinerary(state):
  location = state["location"]
  days = int(state["days"])

  prompt = f"""
  Create a unique {days}-day itinerary for a family trip to {location}.
  Each day should include morning, afternoon and evening activities.
  Highlight fun,food,culture and relaxations.
  """
  response = model.generate_content(prompt)
  return {**state,"itinerary":response.text}

  def get_google_map(state):
  location = state["location"].replace(" ","+")  
  map_link = f"https://www.google.com/maps/search/?api=1&query={location}"
  return{**state,"map_link":map_link}

  def get_flights(state):
  location = state["location"]
  date_str = state["date"] 

  source = "Delhi"

  flight_url= (f”https://www.google.com/travel/flights?q=flights%20from%20{source}%20to%20{location}%20on%20{date_str}”) 
  return{**state,"flight_link":flight_url}

  state_schema = dict
builder = StateGraph(state_schema)  

builder.add_node("UserIntent",extract_user_intent) 
builder.add_node("DestinationAgent",suggest_places) 
builder.add_node("BudgetAgent",suggest_budget_options) 
builder.add_node("HotelAgent",recommend_hotels) 
builder.add_node("ItineraryAgent",create_itinerary) 
builder.add_node("ChecklistAgent",generate_checklist)   
builder.add_node("MapAgent",get_google_map) 
builder.add_node("FlightAgent",get_flights)

builder.set_entry_point("UserIntent")
builder.add_edge("UserIntent", "DestinationAgent")
builder.add_edge("DestinationAgent", "BudgetAgent")
builder.add_edge("BudgetAgent", "HotelAgent")
builder.add_edge("HotelAgent", "ItineraryAgent")
builder.add_edge("ItineraryAgent", "ChecklistAgent")
builder.add_edge("ChecklistAgent", "MapAgent")
builder.add_edge("MapAgent", "FlightAgent")

builder.set_finish_point("FlightAgent")

travel_graph = builder.compile()


# --- Streamlit Frontend ---
st.set_page_config(page_title="AI Travel Planner", page_icon="🌍")
st.title("🌍 AI Travel Booking Planner (Agentic AI)")
st.markdown("Let **Agentic AI** plan your dream trip with smart itineraries, hotels, flights & maps!")


with st.form("travel_form"):
    location = st.text_input("📍 Enter Destination:")
    budget = st.text_input("💸 Enter Budget (e.g., 5 lakhs, 30000):")
    days = st.number_input("📅 Number of Days:", min_value=1, max_value=15, step=1)
    date_plan = st.date_input("🗓️ Start Date", min_value=date.today())
    submitted = st.form_submit_button("🚀 Plan My Trip")


if submitted:
    state = {
        "location": location,
        "budget": budget,
        "days": days,
        "date": str(date_plan)
    }

    st.info("⏳ Letting Agentic AI craft your trip...")
    result = travel_graph.invoke(state)

    st.success("✅ Trip Planned Successfully!")

    st.subheader("📌 Top Places to Visit")
    st.markdown(result["places"])

    st.subheader("🏨 Hotel Recommendations")
    st.markdown(result["hotels"])

    st.subheader("💰 Budget Suggestions")
    st.markdown(result["budget_tips"])

    st.subheader("🗓️ Day-wise Itinerary")
    st.code(result["itinerary"], language="markdown")

    st.subheader("📋 Travel Checklist")
    st.code(result["checklist"], language="markdown")

    st.subheader("🗺️ Open in Google Maps")
    st.markdown(f"[📍 View Map]({result['map_link']})")

    st.subheader("✈️ Flight Search Link")
    st.markdown(f"[🔍 Find Flights Here]({result['flight_link']})")
