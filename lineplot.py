import matplotlib.pyplot as plt
students = ['Anu', 'Balu', 'Chitra', 'David', 'Esha']
marks = [78,85,62,90,74]
plt.plot(students, marks, color='blue', marker='^', linestyle='-')
plt.title("Student Marks - Line Plot")
plt.xlabel("Students")
pkt.ylabel("Marks")
#plt.grid(True)
plt.show()
