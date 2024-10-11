import faker
fake = faker.Faker()

events =[]
events_header = ['event_id','event_name', 'start_date', 'end_date', 'location', 'expected_attendance']

def generate_local_event_data(num_records):
    for _ in range(num_records):
        event = {
            'event_id': fake.uuid4(),
            'event_name': fake.catch_phrase(),
            'start_date': fake.date_between(start_date='-30d', end_date='+30d').strftime('%Y-%m-%d'),
            'end_date': fake.date_between(start_date='+30d', end_date='+60d').strftime('%Y-%m-%d'),
            'location': fake.random_element(elements=('London', 'Paris', 'Rome', 'New York')),
            #'location': fake.city(),
            'expected_attendance': fake.random_int(min=20, max=1000, step=5)
        }
    
        events.append(event)
