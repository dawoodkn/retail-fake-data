import faker

fake = faker.Faker()

fulfillments = []
fulfillment_header = ['fulfillment_id', 'order_id', 'fulfillment_date', 'fulfillment_method', 'shipping_carrier', 'tracking_number', 'estimated_delivery_date', 'actual_delivery_date']

def generate_fulfillments(num_fulfillments):
    for _ in range(num_fulfillments):
        fulfillment = {
            'fulfillment_id': fake.uuid4(),
            'order_id': fake.uuid4(),
            'fulfillment_date': fake.date_time_between(start_date="-30d", end_date="now").strftime("%Y-%m-%d %H:%M:%S"),
            'fulfillment_method': fake.random_element(elements=('ship to home', 'in-store pickup', 'ups', 'usps', 'fedex')),
            'shipping_carrier': fake.company(),
            'tracking_number': fake.uuid4(),
            'estimated_delivery_date': fake.date_between(start_date="today", end_date="+30d").strftime("%Y-%m-%d"),
            'actual_delivery_date': fake.date_between(start_date="today", end_date="+30d").strftime("%Y-%m-%d")
        }
        fulfillments.append(fulfillment)
        
