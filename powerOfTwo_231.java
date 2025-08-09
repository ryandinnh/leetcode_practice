public class powerOfTwo_231 {
    public boolean isPowerOfTwo(int n) {
        // brute force solution can't you recursively divide n by 2 until it is less than or equal to 1 and if it is 1 then it is a power of two
        if (n <= 0) return false; // if n is less than or equal to 0, it cannot be a power of two
        while (n > 1) {
            if (n % 2 != 0) return false;
            n /= 2;
        }
        return true;
    }

    public boolean isPowerOfTwoNoLoop(int n) {
        // using bit manipulation to check if n is a power of two
        // a number is a power of two if it has exactly one bit set in its binary representation (1000, 100, 10 etc.)
        // this can be checked using the expression (n > 0 && (n & (n - 1)) == 0) its a special property of powers of two where if you AND n and n-1 as bits they should all clear to 0.
        return n > 0 && (n & (n - 1)) == 0;
        
    }
    
    public static void main(String[] args) {
        powerOfTwo_231 solution = new powerOfTwo_231();
        int n = 16; // Example input
        boolean result = solution.isPowerOfTwoNoLoop(n);
        System.out.println(result); // Output: true, since 16 is a power of two (2^4)
        
        n = 18; // Another example input
        result = solution.isPowerOfTwoNoLoop(n);
        System.out.println(result); // Output: false, since 18 is not a power of two
    }
}
