pen_number = int(input())
marker_number = int(input())
detergent = int(input())
reduction = int(input())

pen = 5.80
marker = 7.20
detergent_liter = 1.20

all_pen = pen * pen_number
all_marker = marker * marker_number
all_detergent = detergent_liter * detergent
sum_for_all = all_pen + all_marker + all_detergent
reduction_for_all = sum_for_all * (reduction/100)
sum = sum_for_all - reduction_for_all

print(sum)
