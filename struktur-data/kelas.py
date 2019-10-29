import numpy

# a = [1,2,3,4,5]
# b = [6,7,8,9,10]

# # c = a+b

# # print('pakai list',c)

# a = numpy.array([1,2,3,4,5])
# b = numpy.array([6,7,8,9,10])

# c = a+b
# print('pakai numpy',c)

# a = numpy.array([a,b])
# print(a)


# berat =  numpy.array([50,52,60,90])
# tinggi = numpy.array([160,150,165,175])

# BMI = (berat) / ((tinggi/100) ** 2)

# print(BMI[BMI>25])

x = numpy.array([[ 0,  1,  2],
              [ 3,  4,  5],
              [ 6,  7,  8],
              [ 9, 10, 11]])
print(x[1:2,1:4])