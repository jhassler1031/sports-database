
import records

db = records.Database("postgres://localhost/sports_db")

while True:
    user_choice = input("""
What would you like to do?
Enter 1 to search for a team
Enter 2 to add a new team to the database:
""")
    if user_choice == "1" or user_choice == "2":
        break

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
