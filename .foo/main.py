population =  332_510_877.0
total_cases = 31_870_727.0
new_cases = 67_511.0
new_deaths = 702.0
active_cases = 6_871_585.0
total_recovered = 24_423_589.0
serious_critical = 9_218.0
total_deaths = 575_553.0
deaths_from_cases = total_deaths/total_cases*100
total_cases = total_cases/population*100
deaths_from_recoveries = (total_deaths / total_recovered) * 100.0
new_cases = new_cases/population*(365/12)*100
new_deaths = new_deaths/population*(365/12)*100
active_cases = active_cases/population*100
total_deaths = total_deaths/population*100

print("[...] as a percentage of population")
print(f'Total cases: {total_cases:.2f}%')
print(f'Total deaths: {total_deaths:.2f}%')
print(f'Monthly new cases: {new_cases:.2f}%')
print(f'Monthly deaths: {new_deaths:.2f}%')
print(f'Number of active cases: {active_cases:.2f}%')
print("---")
print('[...]as a percentage of total cases')
print(f"Total Deaths: {deaths_from_cases:.2f}%")
print("---")
print('[...]as a percentage of closed cases')
print(f"Total Deaths: {deaths_from_recoveries:.2f}%")

