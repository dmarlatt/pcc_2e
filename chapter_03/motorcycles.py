motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f"\nA {too_expensive.title()} is too expensive for me.")

motorcycles.append(too_expensive)
print(motorcycles)
print(sorted(motorcycles))

motorcycles.insert(0, 'harley')
print(f"After insert()\t {motorcycles}")
popped_motorcycle = motorcycles.pop()
print(f"After pop()\t\t {motorcycles}")
motorcycles.append(popped_motorcycle)
print(f"After append()\t {motorcycles}, so, push if you will")

print(f"{too_expensive}, index: {motorcycles.index(too_expensive)}")
motorcycles.sort()
print(motorcycles)
print(f"{too_expensive}, index: {motorcycles.index(too_expensive)}")
del motorcycles[motorcycles.index(too_expensive)]
print(motorcycles)
print(len(motorcycles))
print(f"too_expensive: {too_expensive}")
