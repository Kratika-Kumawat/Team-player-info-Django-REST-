from django.db import models

TEAM_CHOICES =( 
    ("batsmen", "Batsmen"), 
    ("bowler", "Bowler"), 
    ("wk_batsmen", "Wk_Batsmen"), 
    ("batting_all_rounder", "Batting_All_Rounder"), 
    ("bowling_all_rounder", "Bowling_All_Rounder"),
)
class Teams(models.Model):
    player_name=models.CharField(max_length=50)
    nationality=models.CharField(max_length=30)
    born=models.CharField(max_length=30)
    birthplace=models.CharField(max_length=50)
    height=models.CharField(max_length=50)
    role=models.CharField(max_length = 50,choices = TEAM_CHOICES)
    batting_avg=models.IntegerField()
    bowling_avg=models.IntegerField()
    batting_style=models.CharField(max_length=50)
    bowling_style=models.CharField(max_length=50)
    teams=models.TextField()
    total_innings=models.IntegerField()
    total_runs=models.IntegerField()
    total_avg=models.FloatField()
    total_hundreds=models.IntegerField()
    total_fif=models.IntegerField()
# 15.	Total  bowling ing
    total_wickets=models.IntegerField()
    total_economy=models.FloatField()
# 18.	Total avg
    profile=models.TextField()
    img = models.ImageField(upload_to='pic')
