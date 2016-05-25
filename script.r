data <- read.csv("writefile.csv")
attach(data)
print(cor(prob,edge))
#plot(y=prob,x=edge)
#hist(prob)
nums = seq(0,200)
f <- function(x)
{
        mean(prob[edge == x])
}
lapply(nums,f) -> k
plot(y=k,x=nums)
