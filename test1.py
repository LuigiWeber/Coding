import ex1

points = 0

#Test 1
try:
    assert ex1.SwapEl([0,1,2], 1, 2) == [0,2,1]
    points += 2
except:
    print("Test 1 failed")
    points += 0

#Test 2
try:
    assert ex1.SwapEl(['a',2,2,4,5], 0, 4) == [5,2,2,4,'a']
    points += 2
except:
    print("Test 2 failed")
    points += 0

#Test 3
try:
    assert ex1.SwapEl([1], 0, 4) == False
    points += 2
except:
    print("Test 3 failed")
    points += 0

print("You got: " + str(points) + "/6 points")