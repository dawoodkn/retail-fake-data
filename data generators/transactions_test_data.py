from faker import Faker
import random
from datetime import date, timedelta
fake = Faker()


transaction_header = ['transaction_id', 'customer_id','transaction_date', 'total_amount', \
            'discount_amount','payment_method', 'channel', 'is_return', 'return_reason', 'store_id', 'tax_amount', \
                'discount_percentage', 'net_amount' ]
transactions =[]

def generate_transaction_data(num_records):
    for _ in range(num_records):
        transaction = {
            'transaction_id': fake.uuid4(),
            'customer_id': fake.uuid4(),  # Foreign key
            'transaction_date': fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d'),        
            'total_amount':  fake.pyfloat(left_digits=3, right_digits=2, positive=True),
            'discount_percentage': fake.pyfloat(left_digits=2, right_digits=2, positive=True, max_value=35),
            'payment_method': fake.random_element(elements=('Credit Card', 'Debit Card', 'Cash')),
            'channel':fake.random_element(elements=('Online', 'In-Store', 'Phone')),
            'is_return': fake.boolean(chance_of_getting_true=10),
            'return_reason':fake.random_element(elements=('Damaged', 'Expired', 'Incorrect Item'))
        }
        if transaction['channel'] == 'In-Store':
            transaction['store_id'] = str(fake.random_int(min=1, max=10, step=1))
        else:
            transaction['store_id'] = 'NULL'
        transaction['tax_amount'] =  transaction['total_amount'] * 0.15
        transaction['discount_amount'] = transaction['discount_percentage']/100 * transaction['total_amount']
        transaction['net_amount']= transaction['total_amount'] - transaction['discount_amount'] + transaction['tax_amount']
        
        transactions.append(transaction)