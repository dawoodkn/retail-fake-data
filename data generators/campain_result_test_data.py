import faker

fake = faker.Faker()


campaign_results = []
campaign_results_header = ['result_id', 'campaign_id', 'customer_id', 'interaction_date', 'action', 'revenue_generated']

def generate_campaign_results(num_rows):
    for _ in range(num_rows):
        campaign_results.append({
            'result_id': fake.uuid4(),
            'campaign_id': fake.uuid4(),
            'customer_id': fake.uuid4(),
            'interaction_date': fake.date_between(start_date='-30d', end_date='today').strftime('%Y-%m-%d'),
            'action': fake.random_element(elements=('impression', 'click', 'conversion')),
            'revenue_generated': fake.pyfloat(left_digits=2, right_digits=2, positive=True)
        })
