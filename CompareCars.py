import pygame
import shelve

"""
Cars in order of numbers: 
(Engine, Gearbox, Aero
Chassis, Clutch, Exhaust, Suspension
Supercharger, Fuel, Tyres)
"""


def PreStartCompareCars(tier):
    user_upgrade_stats = shelve.open("Data/Upgrades/part_upgrades")
    user_upgrade_stats = list(user_upgrade_stats["tier" + str(tier)])
    d_values = shelve.open("Data/Staff/driver_values")  # driver values
    c_values = shelve.open("Data/Staff/crew_values")  # crew values
    m_values = shelve.open("Data/Staff/mechanic_values")  # mechanic values
    driver = d_values["currentdriver"]
    crew = c_values["currentcrew"]
    mechanic = m_values["currentmechanic"]
    maintenance_costs = d_values[driver]["cost"] + c_values[crew]["cost"] + m_values[mechanic]["cost"]
    user_value = 0
    """Calculate the initial stats of the car"""
    for value in range(10):
        if 0 <= value <= 2:
            user_value += (5 + user_upgrade_stats[value] * 0.5)
        if 3 <= value <= 6:
            user_value += (2.5 + user_upgrade_stats[value] * 0.25)
        if 7 <= value <= 9:
            user_value += (1.25 + user_upgrade_stats[value] * 0.125)

    """Calculate extra bonuses"""
    user_value += m_values[mechanic]["value_bonus"]
    user_value += d_values[driver]["value_bonus"]
    user_value * (m_values[mechanic]["value_multiplier"] + d_values[driver]["value_multiplier"] - 1)

    return user_value, maintenance_costs


def AfterStartCompareCars(user_value, start_multiplier, opponent_value):
    user_value = user_value * start_multiplier
    final_value = user_value - opponent_value
    return final_value

