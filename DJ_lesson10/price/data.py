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


# https://imgd.aeplcdn.com/1920x1080/n/cw/ec/152681/x5-exterior-right-front-three-quarter-6.jpeg?isig=0&q=80&q=80
# https://bmw.scene7.com/is/image/BMW/g90_driving-dynamics_fb?qlt=80&wid=1024&fmt=webp
# https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSY5KFcf2JFkjoEBmmHo8qY3sH06IbJtBXKZbC7v_F8NdNggHxPG6mrMz-M&s=10
# https://www.usnews.com/object/image/00000199-c8c4-d7cb-abdb-efe4ff790000/usnpx-2026toyotacorolla-angularfront-zd.jpg?update-time=1760009977538&size=responsiveGallery&format=webp



# from .models import Price_data
# car = Price_data.objects.get(car_make='BMW', car_model='X5')
# car.car_image = 'https://imgd.aeplcdn.com/1920x1080/n/cw/ec/152681/x5-exterior-right-front-three-quarter-6.jpeg?isig=0&q=80&q=80'
# car.save()
#
# car = Price_data.objects.get(car_make='BMW', car_model='M5')
# car.car_image = 'https://bmw.scene7.com/is/image/BMW/g90_driving-dynamics_fb?qlt=80&wid=1024&fmt=webp'
# car.save()
#
# car = Price_data.objects.get(car_make='Toyota', car_model='Camry')
# car.car_image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSY5KFcf2JFkjoEBmmHo8qY3sH06IbJtBXKZbC7v_F8NdNggHxPG6mrMz-M&s=10'
# car.save()
#
# car = Price_data.objects.get(car_make='Toyota', car_model='Corolla')
# car.car_image = 'https://www.usnews.com/object/image/00000199-c8c4-d7cb-abdb-efe4ff790000/usnpx-2026toyotacorolla-angularfront-zd.jpg?update-time=1760009977538&size=responsiveGallery&format=webp'
# car.save()