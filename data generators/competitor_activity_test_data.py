import faker
fake = faker.Faker()

activities = []
activities_header = ['activity_id', 'competitor_name', 'activity_type', 'start_date', 'end_date', 'description']   

def generate_competitior_activity_data(num_records):
    for _ in range(num_records):
        activity ={
            'activity_id': fake.uuid4(),
            'competitor_name': fake.company(),
            'activity_type': fake.random_element(elements=('Product Launch', 'Marketing Campaign', 'Sales Event', 'Conference')),
            'start_date': fake.date_between(start_date='-30d', end_date='+30d').strftime('%Y-%m-%d'),
            'end_date': fake.date_between(start_date='+30d', end_date='+60d').strftime('%Y-%m-%d'),
            'description': fake.random_element(elements=('London', 'Paris', 'Rome', 'New York', 'Madrid')),
        }
        activities.append(activity)