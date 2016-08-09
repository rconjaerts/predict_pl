# We're going to create a dataset to calculate how many goals a player will score in the following EPL 
# season, based on performance in his career. Features we will use:
#
# player_name
# DONE competition (based on points in UEFA ranking)
# DONE season (last 5 years)
# DONE team (ranking end of season)
# position
# age
# minutes played
# amount of goals (as our continuous-valued attribute)

data <- data.frame(
   name=character(),
   position=character(),
   age=numeric(),
   team=character(),
   minutes=numeric(),
   competition=character(),
   season=numeric(),
   goals=numeric(),
   stringsAsFactors=FALSE
)