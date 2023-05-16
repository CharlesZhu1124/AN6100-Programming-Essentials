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
#Which cluster number is the smallest?How many people are in the largest cluster? How many in the smallest cluster?
print('Based on the table function, we know that cluster 3 is smallest. There are 59 people in the largest cluster, and 9 people in the smallest cluster.')

colors = c("red", "green", "purple") 
x = req_df[['Age']]
y = req_df[['Weight']]
plot(x=x, y=y, col=colors[clusAg3])
#assess the characteristics of people in the smallest cluster.
print('The characteristic of the smallest cluster is that they have large age and heavy weight.')

