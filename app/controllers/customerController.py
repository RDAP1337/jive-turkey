from app.models.customerModel import Customer


def get_all_customer_names():

    customers = Customer.query.all()
    customer_names = []
    for customer in customers:
        customer_names.append(customer.customer_name)

    return customer_names