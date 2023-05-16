#Q1
set.seed(2398)
r1=rnorm(60000,mean=5,sd=4)
r2=rpois(60000,0.7)
r3=r1[r2>0]
#How many values are in r3?
length(r3) #30242
#Give the mean and sample standard deviation of r3.
mean(r3) #5.012628
sd(r3) #3.989222
