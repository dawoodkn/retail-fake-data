import faker
fake = faker.Faker()

transaction_item_header = [
    'transaction_item_id',
    'transaction_id',
    'product_id',
    'quantity',
    'unit_price',
    'total_price',
    'discount_amount'
] 

transaciton_items = []
def generate_transaction_item_data(num_records):
    for _ in range(num_records):
        transaction_item = {
            'transaction_item_id': fake.uuid4(),
            'transaction_id': fake.uuid4(),  # Foreign key
            'product_id': fake.uuid4(),  # Foreign key
            'quantity': fake.pyint(min_value=1, max_value=100),
            'unit_price': fake.pyfloat(left_digits=3, right_digits=2, positive=True),
            'total_price': fake.pyfloat(left_digits=3, right_digits=2, positive=True),
            'discount_amount': fake.pyfloat(left_digits=2, right_digits=2, positive=True, max_value=35),
        }
        transaciton_items.append(transaction_item)


