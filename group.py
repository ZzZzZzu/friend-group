"""An example of how to represent a group of acquaintances in Python."""

my_group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "Zalika": "friend",
            "John": "partner"
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend"
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "Jill": "partner"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}


print (f"Nash is {my_group['Nash']['age']}")
print(",".join(my_group.keys()))
print(f"{my_group['Jill']['relations']}")



def average_age():
    age = 0
    for person in my_group:
         age += person["age"]
    return age / len(my_group)

def add_person(name, age, job, relations):
    my_group.append({"name":name, "age":age, "job":job, "relations":relations})
    return my_group

def forget(person1, person2):
     my_group[person1]["relations"][person2] = ""
     my_group[person2]["relations"][person1] = ""
     return my_group




# Homework
def mean(data):
    return sum(data) / len(data)


print(max(person["age"] for person in my_group.values()))  # 34
print(mean([len(person["relations"]) for person in my_group.values()]))  # 1.5
print(max(person["age"] for person in my_group.values() if person["relations"]))  # 34
print(max(person["age"] for person in my_group.values() if "friend" in person["relations"].values()))  # 28