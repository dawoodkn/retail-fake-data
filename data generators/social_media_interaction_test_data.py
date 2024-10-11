import faker

fake = faker.Faker() 

soc_med_interactions=[]
soc_med_interactions_header = ['interaction_id', 'customer_id', 'platform', 'interaction_date', 'interaction_type', 'post_id', 'sentiment']


def generate_soc_med_interactions(num_rows):
    for _ in range(num_rows):
        soc_med_interactions.append({
            'interaction_id': fake.uuid4(),
            'customer_id': fake.random_int(min=1, max=1000, step=1),
            'platform': fake.random_element(elements=('facebook', 'twitter', 'instagram', 'linkedin')),
            'interaction_date': fake.date_between(start_date='-30d', end_date='today').strftime('%Y-%m-%d'),
            'interaction_type': fake.random_element(elements=('like', 'comment', 'share')),
            'post_id': fake.uuid4(),
            'sentiment': fake.random_element(elements=('positive', 'negative', 'neutral'))
        })


