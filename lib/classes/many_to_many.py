class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if not hasattr(self, 'name') and isinstance(name, str) and len(name) >= 3:
            self._name = name 
        
    def orders(self):
        customer_orders = Order.all
        return [order for order in customer_orders if order.coffee == self] 
        #coffee_orders = []
        #for order in Order.all:
        #    if (order.coffee == self):
        #        coffee_orders.append(order)
        #return coffee_orders
        
    
    def customers(self):
        customer_set = set()
        coffee_orders = Order.all

        for order in coffee_orders:
            if order.coffee == self:
                customer_set.add(order.customer)
        return list(customer_set)
        

    def num_orders(self):
        if len(self.orders()) > 0:
            return len(self.orders())
        else:
            return 0
    
    def average_price(self):
        """
        total_orders = self.orders()
        total_price = sum(order.price for order in total_orders)
        average = total_price/ len(total_orders)

        if not total_orders:
            return 0
        else:
            return average 
        """
        orders = self.orders()
        if not orders:
            return 0  

        total_price = sum(order.price for order in orders)
        return total_price / len(orders)


class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name 
        
    def orders(self):
        #return [order.customer for order in Order.all if order.coffee == self] 
        #customer_orders = []
        #for order in Order.all:
        #    if order.customer == self:
        #        customer_orders.append(order)
        #return customer_orders
        customer_orders = Order.all
        return [order for order in customer_orders if order.customer == self]
    
    def coffees(self):
        return list(set(order.coffee for order in self.orders()))
    
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        return new_order


    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        if isinstance (customer, Customer):
            self.customer = customer
        if isinstance (coffee, Coffee):
            self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if not hasattr(self, 'price') and isinstance(price, float) and 1 <= price <= 10:
            self._price = price 