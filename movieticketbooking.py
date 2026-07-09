# movie ticket booking program

print("---Movie Ticket Booking---")
print("1.Jananayagan")
print("2.Spiderman")

selected_movie = int(input("Select a movie (1 or 2): "))
ticket_count = int(input("Enter the number of tickets: "))
ticket_price = 150

if selected_movie == 1:
    movie = "Jananayagan"
    print("Selected_movie is: ",movie)
elif selected_movie == 2:
    movie = "Spiderman"
    print("Selected_movie is: ",movie)
else:
    print("Invalid movie selection. choose a valid one.")
    exit()

total = ticket_count*ticket_price
print("---Booking Details---")
print("Movie: ",movie)
print("No.of Tickets: ",ticket_count)
print("Price per Ticket: ",ticket_price)
print("Total Amount: ",total)
