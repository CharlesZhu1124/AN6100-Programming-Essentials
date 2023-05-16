#Q1
set.seed(2398)
r1=rnorm(60000,mean=5,sd=4)
r2=rpois(60000,0.7)
r3=r1[r2>0]
length(r3) #30242
mean(r3) #5.012628
sd(r3) #3.989222


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
length(instVec[instVec=='buy']) #93
length(instVec[instVec=='SELL']) #97
length(instVec[instVec=='-']) #9
print(instVec[62]) #buy
print(instVec[112]) #-
print(instVec[190]) #SELL


#Q3
fname = 'AN6100-Data-3A.csv'
ddir = '/Users/apple/Desktop/NTU_Tri1/AN6100/Assignment/A4/'
setwd(ddir)

df = read.csv(fname)
head(df)
df['BMI']=df$Weight/(df$Height*df$Height)
temp_df=df[df$BMI>=22 & df$Num.Covid.Shots==0,]
out_df=temp_df[,c('Lastname','Country','BMI','Age')]
write.csv(out_df,"Reminder.csv", row.names = FALSE)

dim(out_df)[1] #65
out_df[which(out_df$'Lastname'=='Jackson'),'Country'] #Czechia
dim(out_df[out_df$Age>30,])[1] #22


#Q4
req_df=df[df$Num.Covid.Shots==2,c('Age','Height','Weight')]
library(cluster)
clusAg=diana(req_df,metric = 'euclidean')
clusAg
clusAg3=cutree(clusAg,k=3)
clusAg3
req_df['cluster_type']=clusAg3
table(req_df$cluster_type)
print('Based on the table function, we know that cluster 3 is smallest. There are 58 people in the largest cluster, and 9 people in the smallest cluster.')

colors = c("red", "green", "purple") 
x = req_df[['Age']]
y = req_df[['Weight']]
plot(x=x, y=y, col=colors[clusAg3])
print('The characteristic of the smallest cluster is that they have large age and heavy weight.')

