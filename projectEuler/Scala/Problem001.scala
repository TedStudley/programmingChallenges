object ProblemOne {
  def divides(m: Int, n: Int) = (n % m == 0)
  
  def main(args: Array[String]) {
    var a = 0;
    var sum = 0;
    for (a <- 1 to 999 if (divides(3, a) || divides(5, a))){
      sum += a;
    }
    println("The sum is: " + sum);
  }
}
