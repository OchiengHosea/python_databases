import psycopg2

conn = psycopg2.connect(database='rough_db', user='postgres', password='postgres', host="localhost", port="5432")
cur = conn.cursor()

def insert_sale(sale):
    cur.execute(
        """INSERT INTO Sales (ORDER_NUM, ORDER_TYPE, CUST_NAME, PROD_NUMBER, PROD_NAME, QUANTITY, PRICE, DISCOUNT, ORDER_TOTAL)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        (sale['order_num'], sale['order_type'], sale['cust_name'], sale['prod_name'], sale['quantity'], sale['price'], sale['discount'], sale['order_total'], sale['order_total'])
        )
    conn.commit()


# insert_sale({
#     'order_num': 1,
#     'order_type': 'Mobile',
#     'cust_name': 'Hosea Ochieng',
#     'prod_name': 'Router',
#     'quantity': 1,
#     'price': 299.99,
#     'discount': 20.00,
#     'order_total': 279.99
# })

cur.execute("SELECT * FROM Sales")
print(cur.fetchone())