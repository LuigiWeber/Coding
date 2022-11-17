import ex2

points = 0

#Test 1
try:
    assert ex2.EvenOdd([1,1,2,1]) == [2,1,1,1]
    points += 2
except:
    print("Test 1 failed")
    points += 0

#Test 2
try:
    assert ex2.EvenOdd([1,2,3,4]) == [4,2,1,3]
    points += 2
except:
    print("Test 2 failed")
    points += 0

#Test 3
try:
    assert ex2.EvenOdd([-1,5,-24,2]) == [2,-24,-1,5]
    points += 2
except:
    print("Test 3 failed")
    points += 0

print("You got: " + str(points) + "/6 points")