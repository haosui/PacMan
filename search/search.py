# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    from util import Stack

    stackState = Stack()
    visit = []
    path = []
    if problem.isGoalState(problem.getStartState()):
        return []
    stackState.push((problem.getStartState(), [])) #luu duong di den diem hien tai va node problem.getStartState() tra ve (x,y)
    
    while(True):
        if stackState.isEmpty() :
            return [] #k tim dc duong

        currentt,path = stackState.pop() #lay node tiep theo
        
        visit.append(currentt)   # them vao visited
        if(problem.isGoalState(currentt)): #neu la dich thi tra ve path 
            return path
        successorr = problem.getSuccessors(currentt) #laymang cac nut xung quanh
        if successorr:
            for node in successorr: #node ((x,y),[...])
                if node[0]  not in visit:
                    pathnode = path +[node[1]]
                    stackState.push((node[0],pathnode))
            


    
   
                    


        





              
           

def breadthFirstSearch(problem):
    from util import Queue

    stackState = Queue()
    visit = []
    add = []
    path = []
    if problem.isGoalState(problem.getStartState()):
        return []
    stackState.push((problem.getStartState(), [])) #luu duong di den diem hien tai va node problem.getStartState() tra ve (x,y)
    
    while(True):
        if stackState.isEmpty() :
            return [] #k tim dc duong

        currentt,path = stackState.pop() #lay node tiep theo
        
        visit.append(currentt)   # them vao visited
        if(problem.isGoalState(currentt)): #neu la dich thi tra ve path 
            return path
        successorr = problem.getSuccessors(currentt) #laymang cac nut xung quanh
        if successorr:
            for node in successorr: #node ((x,y),[...])
                if node[0]  not in visit and node[0] not in add:
                    pathnode = path +[node[1]]
                    stackState.push((node[0],pathnode))
                    add.append(node[0])
    

def uniformCostSearch(problem):
    from util import PriorityQueue
    pque = PriorityQueue()
    
    pque.push((problem.getStartState(),[]),0)
    visit = []
    while(True):
        if pque.isEmpty():
            return[]
        currentt,path  = pque.pop()
        if(problem.isGoalState(currentt)):
            return path
        visit.append(currentt)
        successorr = problem.getSuccessors(currentt)
        if successorr:
            for node in successorr:
                if node[0] not in visit:
                    flag = False
                    oldnumber = 0
                    newnumber = 0
                    newpath = path +[node[1]]
                    newnumber = problem.getCostOfActions(newpath)
                    for state in pque.heap:
                        if state[2][0] == node[0]: #check xem co trong priqueeu ko
                            flag = True
                            oldnumber = problem.getCostOfActions(state[2][1])
                    if flag and oldnumber > newnumber:
                        pque.update((node[0],newpath),newnumber)
                    if not flag:
                        pque.push((node[0],newpath),newnumber)      
                    


      



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    from util import PriorityQueue
    pque = PriorityQueue()
    
    pque.push((problem.getStartState(),[]),heuristic( problem.getStartState(),problem))
    visit = []
    while(True):
        if pque.isEmpty():
            return[]
        currentt,path  = pque.pop()
        if(problem.isGoalState(currentt)):
            return path
        visit.append(currentt)
        successorr = problem.getSuccessors(currentt)
        if successorr:
            for node in successorr:
                if node[0] not in visit:
                    
                     
                    flag = False
                    oldnumber = 0
                    newnumber = 0
                    newpath = path +[node[1]]
                    newnumber = problem.getCostOfActions(newpath) +heuristic(node[0],problem)
                    for state in pque.heap:
                        if state[2][0] == node[0]: #check xem co trong priqueeu ko
                            flag = True
                            oldnumber = problem.getCostOfActions(state[2][1])+ heuristic(node[0],problem)
                    if flag and oldnumber > newnumber:
                        pque.update((node[0],newpath),newnumber)
                    if not flag:
                        pque.push((node[0],newpath),newnumber)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
