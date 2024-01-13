import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from employees.models import Employees, Positions
from django.db.models import Max


class Command(BaseCommand):
    help = "Generate employees"

    def handle(self, *args, **options):
        seeder = Seed.seeder()

        count_employees = Employees.objects.count()
        max_employees = 10000
        max_weight = Positions.objects.aggregate(max_weight=Max('weight'))['max_weight']
        
        has_gen_director = Employees.objects.filter(manager__isnull=True, position__weight=0).exists()

        if not has_gen_director:
            seeder.add_entity(Employees, 1, {
                'full_name': lambda x: seeder.faker.name(),
                'position': lambda x: Positions.objects.get(weight = 0),
                'manager': lambda x: None
            })
            seeder.execute()

        for i in range(count_employees, max_employees):
            rand_emp = random.choice(Employees.objects.all())
            position_weight = random.randint(max(rand_emp.position.weight - 1, 1), min(rand_emp.position.weight + 1, max_weight))
            seeder.add_entity(Employees, 1, {
                'full_name': seeder.faker.name(),
                'position': Positions.objects.get(weight = position_weight),
                'manager': lambda x: random.choice(Employees.objects.filter(position__weight=position_weight - 1))
            })
            print(f"{i}/{max_employees}")
        seeder.execute()
        self.stdout.write(self.style.SUCCESS('Successfully generated employees'))