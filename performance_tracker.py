def calc_avg(marks):
    return sum(marks) / len(marks)

def track_perform(students):
    avgs = {name: calc_avg(marks) for name, marks in students.items()}
    top_performer = max(avgs, key=avgs.get)
    return avgs, top_performer

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
avgs, top_performer = track_perform(students)
print("Average Marks:", avgs)
print("Top Performer:", top_performer)
