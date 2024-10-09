from db_utils import get_stock_level, update_stock_level, add_order, get_cost
import requests
import json


def display_menu():
    try:
        response = requests.get('http://127.0.0.1:5000/sweets')
        if response.status_code == 200:
            sweets = response.json()
            print()
            print("************************************************************************************")
            print("                                 Sweet Shop Menu                                    ")
            print("************************************************************************************")
            for sweet in sweets:
                print(f" Name: {sweet['name'].title():<35} Price per sweet: £{float(sweet['price']):.2f}")
                print(f" Description: {sweet['description']:<25}")
                print(f" Stock level: {sweet['stock_quantity']} sweets")
                print("************************************************************************************")
            print()
            return sweets
        else:
            print("Failed to fetch sweets from the API. Please try again later.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching sweets: {e}")
        return None

def fetch_and_display_ingredients(sweet_name):
    try:
        response = requests.get(f'http://127.0.0.1:5000/sweets/name/{sweet_name}')
        if response.status_code == 200:
            sweet = response.json()
            print(f"\nIngredients for {sweet['name'].title()}: {sweet['ingredients']}")
        else:
            print("Sweet not found. Please check the name and try again.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching ingredients: {e}")

def place_order(customer_name, sweet_order_name, order_quantity, total_cost):
    order_data = {
        "customer_name": customer_name,
        "sweet_ordered": sweet_order_name,
        "total_cost": total_cost
    }
    try:
        response = requests.post('http://127.0.0.1:5000/orders', json=order_data)
        if response.status_code == 201:
            print("Order added successfully!")
        else:
            print(f"Failed to add order: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while placing the order: {e}")

def run():
    print('##################################################')
    print('#                                                #')
    print('#       🍭  Welcome to the Sweet Shop!  🍭       #')
    print('#                                                #')
    print('#    From fizzy sherbets to rich toffees,        #')
    print('#    we have something for every sweet tooth!    #')
    print('#                                                #')
    print('#                                                #')
    print('##################################################')
    print()

    # Show menu
    see_menu = input('Would you like to see our menu? (y/n): ').lower()
    if see_menu == "y":
        display_menu()

        see_ingredients = input("Would you like to see the ingredients for any sweet? (y/n): ").lower()
        if see_ingredients == 'y':
            sweet_name = input("Which sweet's ingredients would you like to see? Enter the name: ").strip().lower()
            # Fetch and display ingredients
            fetch_and_display_ingredients(sweet_name)
    else:
        print("Thank you, come again!")
        return

    # Place order
    start_order = input('Would you like to place an order (y/n)? ').lower()
    if start_order != 'y':
        print('Thank you, come again!')
        return

    customer_name = input('Please enter your name: ').strip()
    sweet_order_name = input('What sweet would you like to order? Enter sweet name: ').lower()

    try:
        order_quantity = int(input('Enter quantity: '))
        stock_info = get_stock_level(sweet_order_name)

        if stock_info is None:
            print("Sorry, that sweet does not exist. Please check the name and try again.")
            return

        # Ensure stock_quantity is converted to float
        stock_quantity = float(stock_info['stock_quantity'])

        if order_quantity > stock_quantity:
            print(f"Sorry, we only have {stock_quantity} of {sweet_order_name.title()} in stock.")
            return

        # Calculate total cost of order
        cost = get_cost(order_quantity, sweet_order_name)

        # Ensure cost is converted to float
        cost = float(cost)

        print(f"Your total is: £{cost:.2f}")
        accept_cost = input("Do you wish to proceed (y/n)? ").lower()

        if accept_cost != 'y':
            print('Order cancelled. Thank you, come again!')
            return

        # Handle payment
        buyer_cash = float(input("Please enter how much money you are paying with: £"))

        # Calculate change
        change = buyer_cash - cost
        print(f"Payment successful! Your change is £{change:.2f}.")
        print(f"You have successfully ordered {order_quantity} of {sweet_order_name.title()}. Enjoy your sweets!")

        # Make an API call to add the order
        place_order(customer_name, sweet_order_name, order_quantity, cost)

        # Update stock level (convert to float if necessary)
        update_stock_level(sweet_order_name, float(stock_quantity - order_quantity))

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    run()
