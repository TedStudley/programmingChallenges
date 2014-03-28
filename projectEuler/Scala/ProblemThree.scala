object AllDone extends Exception { }
object ProblemThree {
  def divides (m: BigInt, n: BigInt) = (n % m  == 0);
  
  def sqrt(number: BigInt) = {
    def next(n: BigInt, i: BigInt): BigInt = (n + i/n) >> 1

    val one = BigInt(1)

    var n = one
    var n1 = next(n, number)

    while ((n1 - n).abs > one) {
      n = n1
      n1 = next(n, number)
    }

    while (n1 * n1 > number) {
      n1 -= one
    }

    n1
  }

  def main (args: Array[String]) {
    var magicNum = BigInt("600851475143")
    
    var bigPrime = BigInt(0);

    while (magicNum > 1) {
      try {
        for (i <- BigInt(2) to bigPrime) {
          if (divides(i, bigPrime)) {
            magicNum /= i;
            if (i > bigPrime) bigPrime = i;
            throw AllDone;
          }
        }
      } catch {
        case AllDone =>
      }
    }
  }
}
