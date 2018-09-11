import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


plt.switch_backend('agg')

tips = sns.load_dataset('tips')
# print(tips.head())

# fig = sns.distplot(tips['total_bill'],kde=False,bins=30)

#### Joint Plotter 

# sns.jointplot(x='total_bill',y='tip',data=tips, kind='hex')
# sns.jointplot(x='total_bill',y='tip',data=tips, kind='kde')

# plt.savefig('sns_03c')

#### Pair Plotter 

# sns.pairplot(tips, hue='sex', palette='coolwarm')


# plt.savefig('sns_04b')

#### Rug Plot

# sns.rugplot(tips['total_bill'])

# plt.savefig('sns_05')

#### KDE --> kernel density estimation 


# Create dataset
dataset = np.random.randn(25)

# Create another rugplot
sns.rugplot(dataset);

# Set up the x-axis for the plot
x_min = dataset.min() - 2
x_max = dataset.max() + 2

# 100 equally spaced points from x_min to x_max
x_axis = np.linspace(x_min,x_max,100)

# Set up the bandwidth, for info on this:
url = 'http://en.wikipedia.org/wiki/Kernel_density_estimation#Practical_estimation_of_the_bandwidth'

bandwidth = ((4*dataset.std()**5)/(3*len(dataset)))**.2


# Create an empty kernel list
kernel_list = []

# Plot each basis function
for data_point in dataset:
    
    # Create a kernel for each point and append to list
    kernel = stats.norm(data_point,bandwidth).pdf(x_axis)
    kernel_list.append(kernel)
    
    #Scale for plotting
    kernel = kernel / kernel.max()
    kernel = kernel * .4
    plt.plot(x_axis,kernel,color = 'grey',alpha=0.5)

plt.ylim(0,1)

# plt.savefig('sns_06')

# To get the kde plot we can sum these basis functions.

# Plot the sum of the basis function
sum_of_kde = np.sum(kernel_list,axis=0)

# Plot figure
fig = plt.plot(x_axis,sum_of_kde,color='indianred')

# Add the initial rugplot
sns.rugplot(dataset,c = 'indianred')

# Get rid of y-tick marks
plt.yticks([])

# Set title
plt.suptitle("Sum of the Basis Functions")

plt.savefig('sns_06a')
