from simple_orm import Model
import datetime


class Personels(Model):
    name: str
    age: int
    salary_per_hour: float
    job: str
    hired_year: datetime.datetime

class Menu(Model):
    food_name: str
    price: float
    type: str

class Ingredient(Model):
    name: str
    price: float
    stock: int
    provider_ID: int

class Providers(Model):
    name: str
    phone_number: str
    address: str

class Costumers(Model):
    name: str
    phone_number: str
    address: str
    debt: float


def main():
    try:
        for cls in [Personels, Menu, Ingredient, Providers, Costumers]:
            cls.empty_table()

        sponge = Personels()
        sponge.name = "SpongeBob"
        sponge.age = 20
        sponge.salary_per_hour = 8.5
        sponge.job = "Cook"
        sponge.hired_year = datetime.datetime(2020, 1, 1)
        sponge.save()

        squidward = Personels()
        squidward.name = "Squidward Tentacles"
        squidward.age = 40
        squidward.salary_per_hour = 10.0
        squidward.job = "Cashier"
        squidward.hired_year = datetime.datetime(2019, 5, 1)
        squidward.save()

        sandy = Personels()
        sandy.name = "Sandy Cheeks"
        sandy.age = 30
        sandy.salary_per_hour = 9.0
        sandy.job = "Waitress"
        sandy.hired_year = datetime.datetime(2018, 3, 15)
        sandy.save()

        krabs = Personels()
        krabs.name = "Mr. Krabs"
        krabs.age = 50
        krabs.salary_per_hour = 15.0
        krabs.job = "Owner"
        krabs.hired_year = datetime.datetime(1990, 1, 1)
        krabs.save()

        krabby_patty = Menu()
        krabby_patty.food_name = "Krabby Patty"
        krabby_patty.price = 5.99
        krabby_patty.type = "Lunch"
        krabby_patty.save()

        chum_burger = Menu()
        chum_burger.food_name = "Chum Burger"
        chum_burger.price = 4.99
        chum_burger.type = "Lunch"
        chum_burger.save()

        kelpo = Menu()
        kelpo.food_name = "Kelpo"
        kelpo.price = 3.99
        kelpo.type = "Breakfast"
        kelpo.save()

        seaweed_salad = Menu()
        seaweed_salad.food_name = "Seaweed Salad"
        seaweed_salad.price = 6.99
        seaweed_salad.type = "Lunch"
        seaweed_salad.save()

        pizza = Menu()
        pizza.food_name = "Pizza"
        pizza.price = 8.99
        pizza.type = "Dinner"
        pizza.save()


        sea_supplies = Providers()
        sea_supplies.name = "Sea Supplies"
        sea_supplies.phone_number = "555-1234"
        sea_supplies.address = "123 Ocean Ave"
        sea_supplies.save()

        assady = Providers()
        assady.name = "Assady"
        assady.phone_number = "555-5678"
        assady.address = "456 Coral St"
        assady.save()

        molaee = Providers()
        molaee.name = "Molaee"
        molaee.phone_number = "555-8765"
        molaee.address = "789 Seaweed St"
        molaee.save()

        jellyfish = Ingredient()
        jellyfish.name = "Jellyfish"
        jellyfish.price = 2.0
        jellyfish.stock = 50
        jellyfish.provider_ID = 1
        jellyfish.save()

        patty = Ingredient()
        patty.name = "Patty"
        patty.price = 1.5
        patty.stock = 100
        patty.provider_ID = 2
        patty.save()

        bubble_tea = Ingredient()
        bubble_tea.name = "Bubble Tea"
        bubble_tea.price = 3.0
        bubble_tea.stock = 75
        bubble_tea.provider_ID = 3
        bubble_tea.save()

        patrick = Costumers()
        patrick.name = "Patrick Star"
        patrick.phone_number = "555-5678"
        patrick.address = "124 Conch St"
        patrick.debt = 10.0
        patrick.save()

        plankton = Costumers()
        plankton.name = "Plankton"
        plankton.phone_number = "555-8765"
        plankton.address = "101 Chum Bucket Ln"
        plankton.debt = 5.0
        plankton.save()

        pery = Costumers()
        pery.name = "Perry the Platypus"
        pery.phone_number = "555-4321"
        pery.address = "789 Secret St"
        pery.debt = 15.0
        pery.save()

        print(Personels.all())
        print(Menu.all())
        print(Ingredient.all())
        print(Providers.all())
        print(Costumers.all())

        print(f"who have more than 7$ debt:{Costumers.show_by_fiter("debt > 7")}")
        sandy.update_by_ID(3,"salary_per_hour", 12.0)
        print(f"Updated Sandy's salary: {sandy.show_row(3)}")
        sandy.delete_by_ID(3)
        print(f"Deleted Sandy's record: {Personels.all()}")
        print(f"inner join providers and ingredients: {Providers.inner_join(Ingredient, 'Providers.id = Ingredient.provider_ID')}")
        Costumers.empty_table()
        print(f"empty costumers: {Costumers.all()},")

    except Exception as error:
        print(f"the main function failed! {error}")


main()