import faker

fake = faker.Faker()

products = []

product_header = [
    "product_id",
    "product_name",
    "category",
    "subcategory",
    "brand",
    "supplier_id",
    "unit_cost",
    "unit_price",
    "current_stock",
    "reorder_level",
    "is_active"
]


def generate_product_data(num_records):
    for _ in range(num_records):
        product = {
            'product_id': fake.uuid4(),
            'product_name': fake.word(),
            'category': fake.word(),
            'subcategory': fake.word(),
            'brand': fake.word(),
            'supplier_id': fake.uuid4(),
            'unit_cost': fake.pyfloat(left_digits=3, right_digits=2, positive=True),
            'unit_price': fake.pyfloat(left_digits=3, right_digits=2, positive=True),
            'current_stock': fake.pyint(),
            'reorder_level': fake.pyint(),
            'is_active': fake.boolean()
        }
        products.append(product)



