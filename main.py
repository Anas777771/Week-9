from ticket import create_ticket
from display import display_ticket


def main():
    ticket = create_ticket()

    if ticket:
        display_ticket(ticket)
    else:
        print("Ticket could not be created.")


main()