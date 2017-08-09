import json
import re

from dateutil import parser

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from company.models import Company, Employee, Food


# This is just the beginning part to make this program intelligent
# We have some fruits and vegetables names for now
# We will add other names as we move further in the future
FOOD_DATA = {
    'fruits': ['orange', 'apple', 'banana', 'strawberry', 'pears',
               'blackberry', 'watermelon', 'grape', 'mango'],
    'vegetables': ['potato', 'cabbage', 'maize', 'cucumber', 'beetroot',
                   'celery', 'broccoli', 'turnip', 'lettuce']
}


class Command(BaseCommand):
    help = 'Loads people and companies json file into database'

    def add_food(self, foods, employee):
        for food in foods:
            existing_food = Food.objects.filter(name=food)
            if existing_food.exists():
                employee.favorite_foods.add(existing_food[0])
            else:
                food_type = 'F' if food in FOOD_DATA['fruits'] else 'V'
                new_food = Food.objects.create(name=food, food_type=food_type)
                employee.favorite_foods.add(new_food)

    def load_company_data(self):
        try:
            with open('resources/companies.json') as companies:
                for company in json.load(companies):
                    company = company['company']
                    try:
                        Company.objects.create(name=company)
                        self.stdout.write(
                            self.style.SUCCESS('{} company created').format(
                                company))
                    except IntegrityError:
                        self.stdout.write(
                            self.style.ERROR(
                                '{} company already exists').format(company))
        except FileNotFoundError:
            raise CommandError("Missing company resources file!")

    def load_people_data(self):
        try:
            with open('resources/people.json') as people:
                people = json.load(people)
                for person in people:
                    has_died = bool(person['has_died'])
                    # Remove currency sign and comma from balance
                    balance = re.sub("[^\d\.]", "", person['balance'])
                    eye_color = person['eyeColor'].lower()
                    registered = parser.parse(person['registered'])
                    company = Company.objects.get(pk=person['company_id'])
                    gender = 'F' if person['gender'] == 'female' else 'M'
                    # Split the email and create username from the word
                    # before @
                    username = person['email'].split('@')[0]
                    # Create Employee Instance
                    try:
                        emp = Employee.objects.create(_id=person['_id'],
                                                      guid=person['guid'],
                                                      has_died=has_died,
                                                      balance=balance,
                                                      picture_url=person[
                                                          'picture'],
                                                      age=person['age'],
                                                      eye_color=eye_color,
                                                      name=person['name'],
                                                      gender=gender,
                                                      username=username,
                                                      email=person['email'],
                                                      phone=person['phone'],
                                                      address=person[
                                                          'address'],
                                                      about=person['about'],
                                                      registered=registered,
                                                      greeting=person[
                                                          'greeting'],
                                                      company=company
                                                      )
                        # Add favorite foods
                        self.add_food(person['favouriteFood'], emp)
                        # Add tags
                        for tag in person['tags']:
                            emp.tags.add(tag)
                        self.stdout.write(
                            self.style.SUCCESS('{} employee created').format(
                                emp.name))
                    except IntegrityError:
                        self.stdout.write(self.style.ERROR(
                            '{} already exists'.format(person['name'])))

                # Add Friends of the employee
                self.stdout.write(self.style.SUCCESS(
                    "Matchmaking friends. This won't take long :)"))
                for person in people:
                    emp = Employee.objects.get(_id=person['_id'])
                    for friend in person['friends']:
                        hey = Employee.objects.get(pk=friend['index'] + 1)
                        emp.friends.add(hey)
        except FileNotFoundError:
            raise CommandError("Missing people resources file!")

    def handle(self, *args, **options):
        self.load_company_data()
        self.load_people_data()

        self.stdout.write(self.style.SUCCESS(
            'Successfully loaded companies and their respective employees.'))
