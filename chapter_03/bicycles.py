bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
bicycles[0] = 'schwin'
message = f"My next bicycle was a {bicycles[0].title()}."
print(message)
