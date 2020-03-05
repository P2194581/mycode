#!/usr/bin/env python3
import uuid
howmany = int(input("how many uuids should be generated"))
print("generating UUIDs...")

for rando in range(howmany):
    print (uuid.uuid4())

