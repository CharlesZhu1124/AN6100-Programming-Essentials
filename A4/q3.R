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

#How many entries are there in this reminder CSV?
dim(out_df)[1] #65
#What is the Country of person whose Lastname is Jackson?
out_df[which(out_df$'Lastname'=='Jackson'),'Country'] #Czechia
#How many entries are above 30 years of age?
dim(out_df[out_df$Age>30,])[1] #22

