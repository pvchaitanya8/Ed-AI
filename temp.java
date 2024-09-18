public class FactorialRecursive {

    public static int factorialRecursive(int n) {
        if (n == 0) {
            return 1;
        } else {
            return n * factorialRecursive(n - 1);
        }
    }

    public static void main(String[] args) {
        int num = 88;
        int factorial = factorialRecursive(num);
        System.out.println("Factorial of " + num + " is " + factorial);
    }
}