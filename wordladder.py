# J.Dovala
# C3400
# Word Ladder
# 5th April 2022

# 
def bfs(start, end, list_):
  queue = []
  #lists of path
  queue =[[start]]
  found = False
  #loop run until queue empty or target word is found
  while len(queue)>0:
    curr_list = queue[0]
    if curr_list.count(end) > 0:
      found = True
      break
    else:
      curr_word = curr_list[len(curr_list)-1]
      neighbors = FindNeighbor(curr_word, list_)
      for y in neighbors:
        temp_list = curr_list.copy()
        temp_list.append(y)
        queue.append(temp_list)
    queue.pop(0)    
  if found:
    return curr_list
  else:
    return None

#updates list with same length words
def SameLength(target,list_):
  result = []
  length = len(target)
  for x in list_:
    if len(x) == length:
      result.append(x)
  return result


def FindNeighbor (word, WordList):
  result1  =[]
  
  if(WordList.count(word) > 0):    
    WordList.remove(word)
  #checking for mismatch with target
  for x in WordList:
    mismatched = 0
    matched = True
    index = 0
    #go through each character in a word
    while index < len(word):
      if word[index] != x[index]:
        mismatched+=1
      if mismatched > 1:
        matched = False
      index +=1
    if matched:
      result1.append(x)
      WordList.remove(x)
  
  return result1

def parse_pair(pair):
  return pair.split()

def main():
  WordList = []
  PairList = []

  
  with open("pairs.txt","r") as myPairs:
    mp = myPairs.readlines()
    for x in mp:
      PairList.append(x)
    myPairs.close()

 
  with open("words.txt", "r") as WordFile:
    wf =WordFile.readlines()
    for x in wf:
      x=x[:-1]
      WordList.append(x)
    WordFile.close()

  #look at each pair in pair list
  for x in PairList:
    temp = parse_pair(x)
    start = temp[0]
    end = temp[1]
    if(len(start)!= len(end)):
     print("Two different size words %s  %s"%(start,end))
    else:
      update_list = SameLength(start, WordList)
      result = bfs(start, end, update_list)
      if result != None:
          print('->',result)
      else:
        print("No ladder found from %s to %s"%(start,end))
  pass



if __name__ == "__main__":
    main()
