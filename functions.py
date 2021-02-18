
from scipy.stats import *
import numpy as np

# t-test (mean difference)
## test whether the means of two independent samples are different
def t_test():
    data1 = []
    data2 = []

    alphaVal = int(input('Enter the significance level (%): '))
    numData = int(input('Enter the amount of data for each sample: '))

    for i in range(numData):
        n1 = float(input('Enter the data for sample 1: '))
        data1.append(n1)

    for i in range(numData):
        n2 = float(input('Enter the data for sample 2: '))
        data2.append(n2)

    stat, p = ttest_ind(data1, data2)
    print('Test Statistics:%.3f, T-Value:%.3f' % (stat, p))

    trueVal = alphaVal/100
    if p > trueVal:
        print('Do not reject null hypothesis')
    else:
        print('Reject null hypothesis')

# paired t-test
## tests whether the means of two paired samples are significantly different
def paired_t_test():
    data1 = []
    data2 = []

    alphaVal = int(input('Enter the significance level (%): '))
    numData = int(input('Enter the amount of data for each sample: '))

    for i in range(numData):
        n1 = float(input('Enter the data for sample 1: '))
        data1.append(n1)

    for i in range(numData):
        n2 = float(input('Enter the data for sample 2: '))
        data2.append(n2)

    stat, p = ttest_rel(data1, data2)
    print('Test Statistics:%.3f, T-Value:%.3f' % (stat, p))

    trueVal = alphaVal / 100
    if p > trueVal:
        print('Do not reject null hypothesis')
    else:
        print('Reject null hypothesis')

# wilcoxon rank sum test / mann-whitney u test
## tests whether the distributions of two independent samples are equal or not
def rank_sum():
    data1 = []
    data2 = []

    alphaVal = int(input('Enter the significance level (%): '))
    numData = int(input('Enter the amount of data for each sample: '))

    for i in range(numData):
        n1 = float(input('Enter the data for sample 1: '))
        data1.append(n1)

    for i in range(numData):
        n2 = float(input('Enter the data for sample 2: '))
        data2.append(n2)

    stat, p = mannwhitneyu(data1, data2)
    print('Test Statistics:%.3f, T-Value:%.3f' % (stat, p))

    trueVal = alphaVal / 100
    if p > trueVal:
        print('Do not reject null hypothesis')
    else:
        print('Reject null hypothesis')

# wilcoxon signed-rank test
## tests wheter the distribution of two paired samples are equal or not
def w_signed_rank():
    data1 = []
    data2 = []

    alphaVal = int(input('Enter the significance level (%): '))
    numData = int(input('Enter the amount of data for each sample: '))

    for i in range(numData):
        n1 = float(input('Enter the data for sample 1: '))
        data1.append(n1)

    for i in range(numData):
        n2 = float(input('Enter the data for sample 2: '))
        data2.append(n2)

    stat, p = wilcoxon(data1, data2)
    print('Test Statistics:%.3f, T-Value:%.3f' % (stat, p))

    trueVal = alphaVal / 100
    if p > trueVal:
        print('Do not reject null hypothesis')
    else:
        print('Reject null hypothesis')

# chi squared test (contigency table)
## tests whether two categorical variables are related or independent
def chi_test():

    noRow = int(input('Enter the number of row: '))
    noColumn = int(input('Enter the number of column: '))
    alphaVal = int(input('Enter the significance level (%): '))

    trueVal = alphaVal/100

    numList = [[0 for i in range(noColumn)] for j in range(noRow)] #data position is strange!

    for i in range(noRow):
        for j in range(noColumn):
            numAdd = float(input('Enter the data continously: '))
            numList[i-1][j-1] = numAdd

    stat, p, dof, expected = chi2_contingency(numList)
    print('Test statistics:%.3f, Chi Value:%.3f' % (stat, p)) #error printing p

    if p > trueVal:
        print('Do not reject null hypothesis')

    else:
        print('Reject null hypothesis')
