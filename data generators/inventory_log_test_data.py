import faker

fake = faker.Faker()

logs =[]
log_header = ['log_id', 'product_id', 'store_id', 'date', 'quantity_change', 'reason']

def generate_logs(num_logs):
    for _ in range(num_logs):
        log = {
            'log_id': fake.uuid4(),
            'product_id': fake.uuid4(),
            'store_id': fake.uuid4(),
            'date': fake.date_time_between(start_date="-30d", end_date="now").strftime("%Y-%m-%d %H:%M:%S"),
            'quantity_change': fake.random_int(min=1, max=100),
            'reason': fake.random_element(elements=('restock', 'sale', 'return', 'transfer'))
        }
        logs.append(log)
    