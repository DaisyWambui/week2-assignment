#Given an array of integers, find the sum of its elements.
arr = [1, 2, 3, 4, 5]
def sum_array(arr):
    return sum(arr)

result = sum_array(arr)
print(result) 








#SQL  HACKERRANK QUIZ
SELECT h.hacker_id, h.name, COUNT(s.submission_id), MAX(s.submission_date) as latest_submission_date
FROM Hackers h
INNER JOIN Submissions s ON h.hacker_id = s.hacker_id
GROUP BY h.hacker_id, h.name
HAVING COUNT(s.submission_id) >= 1
  AND COUNT(s.submission_id) = (
    SELECT COUNT(s2.submission_id)
    FROM Submissions s2
    GROUP BY s2.submission_date
    ORDER BY COUNT(s2.submission_id) DESC
    LIMIT 1
  )
ORDER BY latest_submission_date ASC;

