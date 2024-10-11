import faker

fake = faker.Faker()

promotions = []
promotions_header = ['promotion_id', 'promotion_name', 'start_date', 'end_date', 'discount_type', 'discount_value', 'min_purchase_amount', 'applicable_products']


def generate_promotions(num_records):
    for _ in range(num_records):
        promotion = {
            'promotion_id': fake.uuid4(),
            'promotion_name': fake.catch_phrase(),
            'start_date': fake.date_between(start_date='-30d', end_date='today').strftime('%Y-%m-%d'),
            'end_date': fake.date_between(start_date='+1d', end_date='+30d').strftime('%Y-%m-%d'),
            'discount_type': fake.random_element(elements=('percentage', 'fixed_amount')),
            'discount_value': fake.random_number(digits=2, fix_len=False),
            'min_purchase_amount': fake.random_number(digits=2, fix_len=False),
            'applicable_products': [fake.word() for _ in range(fake.random_int(min=1, max=5))]
        }
        promotions.append(promotion)

