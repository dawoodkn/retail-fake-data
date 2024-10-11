import faker

fake = faker.Faker()

prod_reviews =[]
prod_reviews_header = ['review_id', 'product_id', 'customer_id', 'review_date', 'rating', 'review_text', 'helpful_votes', 'sentiment']

def generate_product_reviews(num_records):
    for _ in range(num_records):
        review = {
            'review_id': fake.uuid4(),
            'product_id': fake.uuid4(),
            'customer_id': fake.uuid4(),
            'review_date': fake.date_between(start_date='-30d', end_date='today').strftime('%Y-%m-%d'),
            'rating': fake.random_int(min=1, max=5, step=1),
            'review_text': fake.text(),
            'helpful_votes': fake.random_int(min=0, max=100, step=1),
            'sentiment': fake.random_element(elements=('positive', 'negative', 'neutral'))
        }
        prod_reviews.append(review)

