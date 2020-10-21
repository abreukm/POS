# Salon POS program
Salon point of sale (POS) program using Python 3.4.3 and SQLite
To use this program successfully you must run it on Python 3.4.3 and you must also have SQLite installed. 

There are two types of transactions that can be completed on the system: charge for services or enter expenses/inventory items. 
The user would start by make a selection (either Service or Expenses) using the radio button on the top right-hand side.

Service Transactions 

Steps:
  1. enter the prices and quantities to be charged for each service performed
      if the service performed is not on the list, use the blank textboxes to enter the name of the service
  2. click "Total" to get the total price
      a copy of all services and prices entered will display in the receipt textbox
  3. enter the cash amount the customer has given to pay for their services
  4. hit the "Enter" key on the keyboard to calculate the change. The change amount will be displayed in the Change textbox
  5. click "Complete" to finish the transaction
      this button does two things: 
        clear the page so it is ready for a new transaction
        write the transaction to the SQLite database
        
Expenses Transactions 
       
  1. enter the prices and quantities of products purchased for inventory 
      if the product purchased is not on the list, use the blank textboxes to enter the name of the product
  2. click "Total" to get the total price
      a copy of all products and prices entered will display in the receipt textbox
  3. click "Complete" to finish the transaction
      this button does two things: 
        clear the page so it is ready for a new transaction
        write the transaction to the SQLite database

