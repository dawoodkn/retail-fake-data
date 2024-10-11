import faker

fake = faker.Faker()

history = []
history_header = ['price_id', 'product_id', 'start_date', 'end_date', 'price', 'promotion_id']

def generate_price_history(num_records):
    for _ in range(num_records):
        history_record = {
            'price_id': fake.uuid4(),
            'product_id': fake.uuid4(),
            'start_date': fake.date_between(start_date='-30d', end_date='today').strftime('%Y-%m-%d'),
            'end_date': fake.date_between(start_date='+1d', end_date='+30d').strftime('%Y-%m-%d'),
            'price': fake.random_number(digits=2, fix_len=False),
            'promotion_id': fake.uuid4()
        }
        history.append(history_record)


