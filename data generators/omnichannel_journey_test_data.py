import faker

fake = faker.Faker()

journeys = []
journeys_header = ['journey_id', 'customer_id', 'journey_date', 'touchpoint_sequence', 'conversion', 'total_duration', 'channel_switches']

def generate_omnichanel_journey_data(num_records):
    for _ in range(num_records):
        journey = {
            'journey_id': fake.uuid4(),
            'customer_id': fake.uuid4(),
            'journey_date': fake.date_time_between(start_date="-30d", end_date="now").strftime("%Y-%m-%d"),
            'touchpoint_sequence': [fake.word() for _ in range(fake.random_int(min=1, max=10))],
            'conversion': fake.boolean(),
            'total_duration': fake.random_int(min=1, max=120),
            'channel_switches': fake.random_int(min=0, max=5)
        }
        
        journeys.append(journey)

