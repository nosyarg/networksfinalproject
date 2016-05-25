data <- rbind(read.csv("writefile.csv"),read.csv("junmo.csv"),read.csv("luke.csv"))
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
jpeg('plot.jpg')
plot(y = k,x = nums,main = "Probability of Successful Transmission V.S. Number of Edges", xlab = "Number of Edges", ylab = "Probability of Successful Transmission")
dev.off()
