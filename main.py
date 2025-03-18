from category import Category
from client import Client
from clientSocialnetwork import ClientSocialnetwork
from order import Order
from orderitem import OrderItem
from product import Product
from socialnetwork import Socialnetwork

def main():
    c1 = Client("Gabriel", "Matos", "Rua a", 51999587799, "gabriel@gmail.com", "Male")
    cat1 = Category("Tec", "Tecno products")
    prod1 = Product("mouse", "Gamer mouse", "04/05/1997", True, cat1)
    or1 = Order(150.99, "Waiting payment", c1)
    oi1 = OrderItem(5, 30.19, or1, prod1)
    sntw1 = Socialnetwork("network", "Internal network")
    csntw1 = ClientSocialnetwork(c1, sntw1)

    or1.add_item(oi1)
    print(or1.verifica_total())    


if __name__ == "__main__": 
    main()