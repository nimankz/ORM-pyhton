from simple_orm import Model

class User(Model):
    name: str
    age: int

# Create and save
# u1 = User()
# u1.name = "Alice"
# u1.age = 30
# u1.save()

# u2 = User()
# u2.name = "Bob"
# u2.age = 25
# u2.save()

# Fetch all
print(User.all())

u1= User()
# u1.delete_by_ID(1)

# u1.name = "Abbas"
# u1.age = 67
# u1.update_by_ID(5)

# print(User.all())

User.empty_table()
print(User.all())


