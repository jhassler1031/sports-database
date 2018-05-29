
import records

db = records.Database("postgres://localhost/sports_db")

while True:
    user_choice = input("""
What would you like to do?
Enter 1 to search for a team
Enter 2 to add a new team to the database
Enter 3 to show top performers by a certain stat
Enter 4 to adjust stats for a certain team:
""")
    if user_choice == "1" or user_choice == "2" or user_choice == "3" or user_choice == "4":
        break
    else:
        print("Invalid input.")

if user_choice == "1":
    team_name = input("Enter team name: ")
    team_data = db.query("SELECT * FROM sports_stats WHERE team_name=:team;", team=team_name)
    for row in team_data:
        print(row)
elif user_choice == "2":
    new_team_name = input("Enter the new team name: ")
    new_team_wins = input("Enter number of wins: ")
    new_team_losses = input("Enter number of losses: ")
    new_team_points = input("Enter number of points: ")
    db.query("INSERT INTO sports_stats VALUES (:team_name, :wins, :losses, :points);",
    team_name=new_team_name,
    wins=new_team_wins,
    losses=new_team_losses,
    points=new_team_points)
elif user_choice == "3":
    while True:
        stat_to_compare = input("""
Which stat would you like to see?
Enter 1 for wins
Enter 2 for points:
""")
        if stat_to_compare == "1" or stat_to_compare == "2":
            break
        else:
            print("Invalid input.")
    if stat_to_compare == "1":
        team_sort = db.query("SELECT * FROM sports_stats ORDER BY wins DESC;")
        for row in team_sort[:5]:
            print(row)
    elif stat_to_compare == "2":
        team_sort = db.query("SELECT * FROM sports_stats ORDER BY points DESC;")
        for row in team_sort[:5]:
            print(row)
elif user_choice == "4":
    team_name = input("Enter team name whose stats you wish to edit: ")
    #print the team values so you can see what you want to change
    team_data = db.query("SELECT * FROM sports_stats WHERE team_name=:team;", team=team_name)
    for row in team_data:
        print(row)
    while True:
        stat_to_adjust = input("""
Select which value to adjust,
Enter 1 for team name
Enter 2 for wins
Enter 3 for losses
Enter 4 for points
""")
        if stat_to_adjust == "1" or stat_to_adjust == "2" or stat_to_adjust == "3" or stat_to_adjust =="4":
            break
        else:
            print("Invalid input.")
    if stat_to_adjust == "1":
        adjustment = input("Enter new team name: ")
        db.query("UPDATE sports_stats SET team_name=:name WHERE team_name=:team;",
        name=adjustment,
        team=team_name)
    elif stat_to_adjust == "2":
        adjustment = input("Enter new number of wins: ")
        db.query("UPDATE sports_stats SET wins=:num_wins WHERE team_name=:team;",
        num_wins=adjustment,
        team=team_name)
    elif stat_to_adjust == "3":
        adjustment = input("Enter new number of losses: ")
        db.query("UPDATE sports_stats SET losses=:num_losses WHERE team_name=:team;",
        num_losses=adjustment,
        team=team_name)
    elif stat_to_adjust == "4":
        adjustment = input("Enter new number of points: ")
        db.query("UPDATE sports_stats SET points=:num_points WHERE team_name=:team;",
        num_points=adjustment,
        team=team_name)

    #Reprint the team info showing new values
    team_data = db.query("SELECT * FROM sports_stats WHERE team_name=:team;", team=team_name)
    for row in team_data:
        print(row)
