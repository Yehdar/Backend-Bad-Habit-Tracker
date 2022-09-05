from datetime import datetime
from habit_tool import break_habit
import pandas as pd
from tabulate import tabulate

# there are habits that do not cost money like sleeping in. Therefore, for those habits, make the cost_per_day equal 0
# Note that the minutes_saved and money_saved is distributed over 24 hours in a day. For example, suppose you stated that the minutes_wasted was 30. Well, 
# after an hour, it would be 1.25 minutes_saved. However, after 24 hours, you would get your 30 minutes_saved.
habits = [
    break_habit('Sleeping In', datetime(2022, 7, 29, 7, 20), cost_per_day=0, minutes_wasted=30),
    break_habit('Instagram', datetime(2022, 7, 29, 7, 20), cost_per_day=0, minutes_wasted=30),
    break_habit('Coffee', datetime(2022, 7, 29, 7, 20), cost_per_day=2, minutes_wasted=15),
    break_habit('Video Games', datetime(2022, 7, 29, 7, 20), cost_per_day=0, minutes_wasted=120),
    break_habit('18+ Content', datetime(2022, 7, 29, 7, 20), cost_per_day=0, minutes_wasted=30),
]

df = pd.DataFrame(habits)

print(tabulate(df, headers='keys', tablefmt='psql'))