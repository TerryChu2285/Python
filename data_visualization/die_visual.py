from die import Die
import pygal

#  创建一个D6、一个D8、一个D10
die_1 = Die(6)
die_2 = Die(6)

#  掷多次骰子，并将结果存储到一个列表中
results = []
for roll_num in range(100):
    result = die_1.roll() * die_2.roll()
    results.append(result)

#  分析结果
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#  对数据结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = list(range(2, max_result + 1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * D6', frequencies)
hist.render_to_file('dicess_visual.svg')
