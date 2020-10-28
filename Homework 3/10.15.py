# Tianhao Shao
# 1781421

class Team:
	def __init__(self):
		self.team_name = 'none'
		self.team_wins = 0
		self.team_losses = 0

	def get_win_percentage(self):
		precentage = self.team_wins / (self.team_wins+self.team_losses)
		return precentage


if __name__ == "__main__":
	
	team = Team()
	
	team.team_name = input()
	team.team_wins = int(input())
	team.team_losses = int(input())
	
	if team.get_win_percentage() >= 0.5:
		print('Congratulations, Team', team.team_name,'has a winning average!')
	else:
		print('Team', team.team_name, 'has a losing average.')
