import faker

fake = faker.Faker()

feedback =[]
feedback_header = ['feedback_id', 'customer_id', 'feedback_date', 'feedback_type', 'score', 'comments', 'context']

def generate_feedback_data(num_rows):
    for _ in range(num_rows):
        feedback.append({
            'feedback_id': fake.uuid4(),
            'customer_id': fake.uuid4(),  # Assuming customer IDs are UUIDs
            'feedback_date': fake.date_time_between(start_date='-30d', end_date='now').strftime('%Y-%m-%d'),
            'feedback_type': fake.random_element(elements=('NPS', 'CSAT', 'CES')),
            'score': fake.random_int(min=1, max=5),
            'comments': fake.text(),
            'context': fake.random_element(elements=('Web', 'App', 'Store'))
        })
