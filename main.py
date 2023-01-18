# Import the necessary libraries
import json
import requests

# Define the function to track the ATM card
def track_atm_card(card_number):
    # Call the API to get the location of the ATM card
    url = "https://api.example.com/atm/location/" + card_number
    response = requests.get(url)
    data = json.loads(response.text)

    # Check if the card was found
    if "error" in data:
        print("Card not found.")
    else:
        # Print the location of the ATM card
        print("Card found at: " + data["location"])
        
# Example usage
track_atm_card("1234567890")
