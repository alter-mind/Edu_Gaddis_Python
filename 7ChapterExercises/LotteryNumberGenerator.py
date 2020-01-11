import random
def generate():
    lottery_ticket = []
    for i in range(10):
        lottery_ticket.append(random.randrange(0,10))
    return lottery_ticket
def print_ticket(lottery_ticket):
    print(lottery_ticket)
def print_ticket_cicle(lottery_ticket):
    for i in lottery_ticket:
        print(i)

def start():
    print_ticket(generate())
   
