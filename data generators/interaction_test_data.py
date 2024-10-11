import faker

fake = faker.Faker()

interaction_header = [
    "interaction_id",
    "customer_id",
    "interaction_type",
    "interaction_date",
    "channel",
    "duration",
    "page_views",
    "conversion",
]

interactions = []


def generate_interactions(num_rows):
    for _ in range(num_rows):
        interaction = {
            "interaction_id": fake.uuid4(),
            "customer_id": fake.uuid4(),  # Assuming customer IDs are UUIDs
            "interaction_type": fake.random_element(
                elements=("website visit", "phone", "in-person", "email opened")
            ),
            "interaction_date": fake.date_between(
                start_date="-30d", end_date="today"
            ).strftime("%Y-%m-%d"),
            "channel": fake.random_element(
                elements=("email", "phone", "web", "social media")
            ),
            "duration": fake.time(pattern="%H:%M:%S"),
            "page_views": fake.random_int(min=1, max=100, step=1),
            "conversion": fake.boolean(chance_of_getting_true=25),
        }
        interactions.append(interaction)
