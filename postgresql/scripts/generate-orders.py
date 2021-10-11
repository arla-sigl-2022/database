import csv
from random import randrange, sample, random

def users_from_csv(users_csv_path):
    users = []
    with open(users_csv_path, 'r') as users_csv:
        fieldnames = (["username"])
        reader = csv.DictReader(users_csv, fieldnames)
        next(reader, None) # skip header
        for row in reader:
            users.append(row['username'])
    return users

def delivery_status_from_csv(delivery_status_path):
    delivery_status = []
    with open(delivery_status_path, 'r') as delivery_status_csv:
        fieldnames = (["name"])
        reader = csv.DictReader(delivery_status_csv, fieldnames)
        next(reader, None) # skip header
        for row in reader:
            delivery_status.append(row['name'])
    return delivery_status


def ressource_list_from_csv(ressource_csv_path):
    ressources = []
    with open(ressource_csv_path, 'r') as ressource_csv:
        fieldnames = ("planet_id", "name", "price")
        reader = csv.DictReader(ressource_csv, fieldnames)
        next(reader, None) # skip header
        for row in reader:
            ressources.append(row)
    print('resources are', ressources)
    return ressources

def contractor_list_from_csv(contractor_csv_path):
    contractors = []
    with open(contractor_csv_path, 'r') as contractor_csv:
        fieldnames = ("name", "location", "about", "email", "phone")
        reader = csv.DictReader(contractor_csv, fieldnames)
        next(reader, None) # skip header
        for row in reader:
            contractors.append(row)
    return contractors


def contractor_sells_ressource_csv(contractors, number_of_ressources,csv_file_path):
    contractor_sells_ressource = []
    with open(csv_file_path, 'w') as csv_file:
        csv_object = csv.writer(csv_file)
        csv_object.writerow([
            "contractor_id",
            "ressource_id"
        ])
        contractor_id = 1
        for contractor in contractors:
            number_of_ressource_to_sell = randrange(1, 4)
            ressource_sample = sample(range(1, number_of_ressources + 1), k=number_of_ressource_to_sell)
            for ressource_id in ressource_sample:
                contractor_sells_ressource.append(dict(contractor_id=contractor_id, ressource_id=ressource_id))
                csv_object.writerow([contractor_id, ressource_id])
            contractor_id += 1

    return contractor_sells_ressource

def generate_orders(ressources, contractor_sells_ressource_list, delivery_status_list, number_of_order, order_csv_path, ordered_to_contractor_csv_path):
    ordered_to_contractor = []
    orders = []
    with open(order_csv_path, 'w') as order_csv_file:
        order_csv_object = csv.writer(order_csv_file)
        order_csv_object.writerow([
            "price",
            "created_at",
            "delivery_status"
        ])
        with open(ordered_to_contractor_csv_path, 'w') as order_to_contractor_csv_file:
            order_to_contractor_csv_object = csv.writer(order_to_contractor_csv_file)
            order_to_contractor_csv_object.writerow([
                "order_id",
                "contractor_id",
                "ressource_id",
                "quantity"
            ])
            for order_id in range(1, number_of_order + 1):
                number_of_order_to_contractor = randrange(1, 7)
                contractor_selected_list = sample(contractor_sells_ressource_list, k=number_of_order_to_contractor)
                order_price = 0
                for contractor_selected in contractor_selected_list:
                    qty = round(random() * 20, 2) 
                    ressource_selected = ressources[contractor_selected['ressource_id'] - 1]
                    print("ressource selected: ", ressource_selected)
                    ressource_price = round(float(ressource_selected['price']), 2)
                    order_price += qty * ressource_price
                    ordered_to_contractor.append(dict(order_id=order_id, contractor_id=contractor_selected['contractor_id'], resource_id=contractor_selected['ressource_id'], quantity=qty))
                    order_to_contractor_csv_object.writerow([
                        order_id,
                        contractor_selected['contractor_id'],
                        contractor_selected['ressource_id'],
                        qty
                    ])
                order_price = round(order_price + (order_price / 10), 2) # 10% of delivery fee
                order_created_at = randrange(1619827200000, 1633937330066)
                order_status = randrange(1, len(delivery_status_list) + 1)
                orders.append(dict(price=order_price, created_at=order_created_at, delivery_status=order_status))
                order_csv_object.writerow([order_price, order_created_at, order_status])

    return orders

def attach_user_to_order(number_of_users, orders, user_orders_csv_path):
    with open(user_orders_csv_path, 'w') as user_orders_csv:
        order_csv_object = csv.writer(user_orders_csv)
        order_csv_object.writerow([
            "user_id",
            "order_id"
        ])
        order_id = 1
        for order in orders:
            user_id = randrange(1, number_of_users + 1)
            order_csv_object.writerow([
                user_id,
                order_id
            ])
            order_id += 1

if __name__ == '__main__':
    users = users_from_csv('data/users.csv')
    contractors = contractor_list_from_csv('data/contractors.csv')
    ressources = ressource_list_from_csv('data/ressources.csv')
    contractor_sells_list = contractor_sells_ressource_csv(contractors, len(ressources), 'data/contractor_sells_ressource.csv')
    delivery_status_list = delivery_status_from_csv('data/delivery_status.csv')
    orders = generate_orders(ressources, contractor_sells_list, delivery_status_list, 100000, 'data/orders.csv', 'data/ordered_to_contractor.csv')
    attach_user_to_order(len(users), orders, 'data/user_orders.csv')
