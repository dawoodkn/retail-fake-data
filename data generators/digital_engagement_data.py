import faker

fake = faker.Faker() 
    
engagements =[]
engagements_header = ['engagement_id', 'customer_id', 'engagement_date', 'platform', 'session_duration', 'pages_viewed', 'features_used', 'conversion', 'bounce']

def generate_digital_engagement_data(num_rows):
    for _ in range(num_rows):
        engagement = {
            'engagement_id': fake.uuid4(),
            'customer_id': fake.uuid4(),
            'engagement_date': fake.date_between(start_date='-30d', end_date='today').isoformat(),
            'platform': fake.random_element(elements=('Web', 'Mobile', 'Desktop')),
            'session_duration': fake.random_int(min=60, max=3600, step=60),
            'pages_viewed': fake.random_int(min=1, max=100),
            'features_used': fake.random_int(min=1, max=10),
            'conversion': fake.boolean(),
            'bounce': fake.boolean()
        }
        engagements.append(engagement)
        
