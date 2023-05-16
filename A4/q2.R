#Q2
set.seed(9877)
n=100
first_period=rbinom(40,n,0.4)
total_period=c(first_period)
while(length(total_period)<200){
  n=n+15
  temp_period=rbinom(20,n,0.4)
  total_period=c(total_period,temp_period)
}
#Give the mean and sample standard deviation of prices.
mean(total_period) #61.505
sd(total_period) #16.84604

instVec=c()
for (i in (1:199)){
  if(total_period[i+1]>total_period[i]){
    instVec=c(instVec,'buy')
  }else if(total_period[i+1]<total_period[i]){
    instVec=c(instVec,'SELL')
  }else{
    instVec=c(instVec,'-')
  }
}

#Give the number of “buy”, and number of “SELL” in instVec.
length(instVec[instVec=='buy']) #93
length(instVec[instVec=='SELL']) #97
#length(instVec[instVec=='-']) #9
#What are the instructions on days 62, 112, and 190?
print(instVec[62]) #buy
print(instVec[112]) #-
print(instVec[190]) #SELL

