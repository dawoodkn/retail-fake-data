import faker

fake = faker.Faker()

trends= []
trends_header= ['trend_id', 'trend_name', 'category', 'start_date', 'impact_score', 'description']
def generate_trend_data(num_records):
    for _ in range(num_records):
        trend = {
            'trend_id': fake.uuid4(),
            'trend_name': fake.catch_phrase(),
            'category': fake.random_element(elements=('Technology', 'Finance', 'Healthcare', 'Retail', 'Manufacturing')),
            'start_date': fake.date_between(start_date='-30d', end_date='+30d').strftime('%Y-%m-%d'),
            'impact_score': fake.random_int(min=1, max=10, step=1),
            'description': fake.text(),
        }
        trends.append(trend)
