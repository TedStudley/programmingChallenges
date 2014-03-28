object ProblemTwo {
  def fib(n: BigInt): BigInt = {
    def fibs(n: BigInt): (BigInt, BigInt) = if (n == 1) (1, 0) else {
      val (a, b) = fibs(n/2)
      val p = (2*b+a)*a
      val q = a*a + b*b
      if(n % 2 == 0) (p, q) else (p+q, p)
    }
    fibs(n)._1
  }

  def divides(m: BigInt, n: BigInt) = (n % m == 0);

  def main(args: Array[String]) {
    var sum = 0 : BigInt;
    for (x <- 1 to 100 if (divides(2, fib(x)) && fib(x) < 4000000)) {
      sum += fib(x)
    }
    println("The sum is: " + sum);
  }
}
