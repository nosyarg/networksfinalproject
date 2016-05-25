p <- .5
parr <- p
lowerarr <- numeric()
for (i in seq(1,21))
{
        parr <- c(parr,p*parr[i]+(1-p)*parr[i]^2)
        lowerarr <- c(lowerarr,1-(1-p)*(1-p^2)^(i-1))
}
1-parr -> parr
jpeg("upperlower.jpg")
plot(parr,ylim = c(0,1), xlim = c(0,20),col = "red",main = "Minimum and Maximum Bounds on Probability Subproblem",ylab="Probability of Success",xlab = "Number of Vertices")
points(lowerarr,col = "blue")
legend("bottomright",legend = c("Upper Bound","Lower Bound"),col = c("red","blue"),pch=1)
lines(parr,col = "red")
lines(lowerarr, col = "blue")
dev.off()
