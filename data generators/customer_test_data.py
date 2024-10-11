from faker import Faker
import random
from datetime import date, timedelta


fake = Faker()

customer_header = ['customer_id', 'first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'gender', 'address_line1', \
    'address_line2', 'city', 'state', 'country', 'postal_code', 'registration_date', 'customer_type', \
        'preferred_contact_method', 'occupation', 'income_bracket']
customers = []
def generate_customer_data(num_records):
    for _ in range(num_records):
        customer = {
            'customer_id': fake.uuid4(),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'phone': fake.phone_number(),
            'date_of_birth': fake.date_between(start_date='-80y', end_date='-18y').strftime('%Y-%m-%d'),
            'gender': random.choice(['Male', 'Female']),
            'address_line1': fake.street_address(),
            'address_line2': fake.secondary_address(),
            'city': fake.city(),
            'state': fake.state(),
            'country': fake.country(),
            'postal_code': fake.postcode(),
            'registration_date': fake.date_between(start_date='-2y', end_date='today').strftime('%Y-%m-%d'),     
            'customer_type': fake.random_element(elements=('Individual', 'Business')),
            'preferred_contact_method': fake.random_element(elements=('Email', 'Phone', 'Mail')),
            'occupation': fake.random_element(elements=('Lawyer', 'Construction Worker', 'Nurse', 'Manager')),
            'income_bracket': fake.random_element(elements=('Low', 'Medium', 'High')),
        }
        customers.append(customer)