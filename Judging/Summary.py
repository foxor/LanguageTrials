#!/usr/bin/env python3

_projects = ["Python", "Java"]
_scores = {}
_properNames = {
  "strLen": "Total character length score",
  "longLen": "Length of longest line",
}

class Score(object):
  def __init__(self, project):
    fptr = open("%s/%s" % ("Judging", project), 'r')
    self.strLen = int(fptr.readline().strip())
    self.longLen = int(fptr.readline().strip())
    self.name = project

def loadScores():
  for project in _projects:
    _scores[project] = Score(project);

def lerpScore(category, ascending=True):
  high = None
  low = None
  for project in _scores.values():
    if high == None or project.__dict__[category] > high:
      high = project.__dict__[category]
    if low == None or project.__dict__[category] < low:
      low = project.__dict__[category]
  categoryRange = (high - low) * 1.0
  for project in _scores.values():
    lerpPct = (project.__dict__[category] - low) / categoryRange
    rating = lerpPct if ascending else (1 - lerpPct)
    project.__dict__[category] = int(rating * 100.0)

def totalScores():
  for project in _scores.values():
    project.totalScore = project.strLen + project.longLen

def dumpData():
  winner = max(_scores.values(), key= lambda project: project.totalScore)
  print("\n" * 3)
  print("%s is the best language for simple projects" % winner.name)
  print("\n" * 3)
  languageNameFormatString = "{:8s}"
  languageScoreFormatString = "{:8d}"
  tableTop = "{:40s}  " + (languageNameFormatString * len(_projects))
  tableRow = "{:40s}  " + (languageScoreFormatString * len(_projects))
  print(tableTop.format(*([" "] + _projects)))
  for category in _properNames:
    print(tableRow.format(*([_properNames[category]] + [_scores[x].__dict__[category] for x in _projects])))

if __name__ == '__main__':
  loadScores()
  lerpScore("strLen", False)
  lerpScore("longLen", False)
  totalScores()
  dumpData()
