score = []
n = int(input("학생 수:"))

total = 0

for i in range(0, n):
    jumsu = int(input("[%d] 영어시험 성적: "% (i+1)))
    total += jumsu
    score.append(jumsu)

def printResult(list, total):
    num = len(list)
    printResult(score, total)
    printResult(total, total)
    printResult(total, total/n)

