print("Hello welcome to the gradebook")
total = int
avg = int

def calc_average(total):
    return total / 5

scores = []
for i in range(1, 6):
    score = int(input('Enter score {0}: '.format(i)))
    if score <= 100 and score >= 0:
        print('The score that you recorded is: ' + str(score))
        scores.append(score)
    else:
        while (score > 100 or score < 0):
            print('The score you entered is incorrect')
            score = int(input('Enter score {0}: '.format(i)))
            if score <= 100 and score >= 0:
                print('The score that you recorded is: ' + str(score))
                scores.append(score)
        
        
        

total = sum(scores)
avg = calc_average(total)
print('The average grade is: ' + str(avg))
