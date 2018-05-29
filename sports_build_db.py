
#database name sports_db
#table name sports_stats
#team_name(30)
#wins (3)
#loses (3)
#points (3)

import records

#connect to the DB
db = records.Database("postgres://localhost/sports_db")

db.query("DROP TABLE IF EXISTS sports_stats;")
db.query("""CREATE TABLE sports_stats (
        team_name varchar(30),
        wins numeric(3),
        losses numeric(3),
        points numeric(3)
);""")

team_names = ["Man. City", "Man United", "Tottenham", "liverpool", "Chelsea", "Arsenal",
            "Burnley FC", "Everton", "Leicester City", "Newcastle", "Crystal Palace", "Bournemouth",
            "West Ham", "Watford", "Brighton", "Huddersfield", "Southhampton", "Swansea City",
            "Stoke City", "West Brom"]

wins = [32, 25, 23, 21, 21, 19, 14, 13, 12, 12, 11, 11, 10, 11, 9, 9, 7, 8, 7, 6]

losses = [2, 7, 7, 5, 10, 13, 12, 15, 15, 18, 16, 16, 16, 19, 16, 19, 16, 21, 19, 19]

points = [100, 81, 77, 75, 70, 63, 54, 49, 47, 44, 44, 44, 42, 41, 40, 37, 36, 33, 33, 31]

for count in range(20):
    db.query("INSERT INTO sports_stats VALUES (:team_name, :wins, :losses, :points);",
    team_name=team_names[count],
    wins=wins[count],
    losses=losses[count],
    points=points[count])

rows = db.query("SELECT * FROM sports_stats")

for row in rows:
    print(row)
