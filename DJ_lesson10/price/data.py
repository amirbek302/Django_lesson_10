from faker import Faker
from .models import Price_data


faker = Faker('en_US')

cars = {
    'BMW': {
        'X5': 'https://example.com/bmw-x5.jpg',
        'M5': 'https://example.com/bmw-m5.jpg'
    },
    'Toyota': {
        'Camry': 'https://example.com/toyota-camry.jpg',
        'Corolla': 'https://example.com/toyota-corolla.jpg'
    }
}

cars_to_create = []

for make, models in cars.items():
    for model in models:
        cars_to_create.append(
            Price_data(
                car_model=model,
                car_description=faker.sentence(),
                car_make=make,
                car_image=models[model]
            )
        )

Price_data.objects.bulk_create(cars_to_create)