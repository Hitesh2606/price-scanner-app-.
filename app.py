import streamlit as st

# Function to simulate fetching product prices from APIs
def fetch_product_prices(product_name):
    prices = [
        {'store': 'Amazon', 'price': 199.99},
        {'store': 'Flipkart', 'price': 189.50},
        {'store': 'Walmart', 'price': 205.00},
    ]
    
    best_price = min(prices, key=lambda x: x['price'])
    
    return best_price, prices

# Streamlit app UI
st.title("Product Price Comparison App")

product_name = st.text_input("Enter product name:")
if product_name:
    best_price, all_prices = fetch_product_prices(product_name)

    st.subheader("Best Price Found:")
    st.write(f"**{best_price['store']}**: ${best_price['price']:.2f}")

    st.subheader("All Available Prices:")
    for price in all_prices:
        st.write(f"**{price['store']}**: ${price['price']:.2f}")

