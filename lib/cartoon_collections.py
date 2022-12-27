def roll_call_dwarves(dwarves):
    [print(f"{index + 1}. {dwarf}") for index, dwarf in enumerate(dwarves)]

def summon_captain_planet(planeteers):
    return [f"{planeteer.capitalize()}!" for planeteer in planeteers]

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)

def find_the_cheese(words):
    sol = [word for word in words if word in ["cheddar", "gouda", "camembert"]]
    return sol[0] if len(sol) > 0 else None
