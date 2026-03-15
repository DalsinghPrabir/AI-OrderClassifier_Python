import pandas as pd
from classifier import OrderClassifier
from machine_router import assign_machine

orders = pd.read_csv("orders/orders.csv")

classifier = OrderClassifier()

print("\nSMART MANUFACTURING ORDER CLASSIFIER\n")

for index, row in orders.iterrows():

    description = row["description"]

    category = classifier.predict(description)

    machine = assign_machine(category)

    print("Order:", row["order_id"])
    print("Description:", description)
    print("Category:", category)
    print("Assigned Machine:", machine)
    print("-----------------------------------")