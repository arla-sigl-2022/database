import csv
from random import randrange, sample, random

def comments_base_from_csv(comments_base_csv_path):
    comments = []
    with open(comments_base_csv_path, 'r') as comment_base_csv:
        fieldnames = (["comment"])
        reader = csv.DictReader(comment_base_csv, fieldnames)
        next(reader, None) # skip header
        for row in reader:
            comments.append(row['comment'])
    return comments

def orders_with_contractor_from_csv(orders_with_contractor_csv_path):
    orders = []
    with open(orders_with_contractor_csv_path, 'r') as orders_csv:
        fieldnames = (["order_id","order_date","ressource","contractor","username"])
        reader = csv.DictReader(orders_csv, fieldnames)
        next(reader, None) # skip header
        for row in reader:
            orders.append(row)
    return orders

def generate_contractor_comments(comments_base, orders_with_contractor, comments_csv_file_path): 
    with open(comments_csv_file_path, 'w') as comments_csv:
        comments_csv_object = csv.writer(comments_csv, delimiter='\t')
        comments_csv_object.writerow([
            "order_id",
            "order_date",
            "ressource",
            "contractor",
            "username",
            "comment"
        ])
        for order in orders_with_contractor:
            number_of_comment_for_order = randrange(0, 4) # between 0 and 3 comments per order
            comment_list = sample(comments_base, k=number_of_comment_for_order)
            for comment in comment_list:
                comments_csv_object.writerow([
                    order['order_id'],
                    order['order_date'],
                    order['ressource'],
                    order['contractor'],
                    order['username'],
                    comment
                ])

if __name__ == '__main__':
    comments_base = comments_base_from_csv('data/comments-base.csv')
    orders = orders_with_contractor_from_csv('data/orders_with_contractor.csv')
    generate_contractor_comments(comments_base, orders, 'data/comments.tsv')
