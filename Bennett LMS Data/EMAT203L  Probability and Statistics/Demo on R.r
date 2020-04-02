rr=read.csv("/home/tanveer/Desktop/rel.csv")

library(Quandl)

install.packages(Quandl)

for (i in 1:length(rr))
{
  
  x <- 5
  if(x > 0){
    print("Positive number")
  }
  
  
}


subset(rr,rr$Prev.Close==981.30)



check <- function(x) {
  if (x > 0) {
    result <- "Positive"
  }
  else if (x < 0) {
    result <- "Negative"
  }
  else {
    result <- "Zero"
  }
  return(result)
}



check <- function(x) {
  if (x > 0) {
    result <- "Positive"
  }
  else if (x < 0) {
    result <- "Negative"
  }
  else {
    result <- "Zero"
  }
  result
}


sample(1:9000,100,replace=T)

runif(1000)

sample(c("H","T"),10,replace=TRUE)


sample(c("Hat","Tan","asdf","asder"),10,replace=TRUE)


vector1 <- c(5,9,3)
vector2 <- c(10,11,12,13,14,15)






