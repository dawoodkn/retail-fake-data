import faker
import random

fake = faker.Faker()
campaigns =[]
campaign_header = ['campaign_id', 'campaign_name', 'campaign_type', 'start_date', 'end_date', 'target_audience', 'channel', 'total_budget', 'total_spend']

def generate_campaign_data(num_records):
    for _ in range(num_records):
        campaign = {
            'campaign_id': fake.uuid4(),
            'campaign_name': fake.catch_phrase(),
            'campaign_type': random.choice(['Brand', 'Product', 'Service']),
            'start_date': fake.date_between(start_date='-30d', end_date='+30d').strftime('%Y-%m-%d'),
            'end_date': fake.date_between(start_date='+30d', end_date='+60d').strftime('%Y-%m-%d'),
            'target_audience': random.choice(['Men', 'Women', 'Children', 'Teens', 'Adults']),
            'channel': random.choice(['Online', 'In-Store', 'Phone']),
            'total_budget': fake.pyfloat(left_digits=5, right_digits=2, positive=True),
            'total_spend': fake.pyfloat(left_digits=5, right_digits=2, positive=True)
        }
        campaigns.append(campaign)

