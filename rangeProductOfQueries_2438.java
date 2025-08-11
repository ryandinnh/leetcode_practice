import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class rangeProductOfQueries_2438 {
    public int[] rangeProductQueries(int n, int[][] queries) {
        // given n, calculate the powers of 2 up to n and then apply querie operations on them
        List<Integer> powers = new ArrayList<>(); // use arrayList because we don't know the limitations of n
        int power = 1;
        while (n > 0) {
            powers.add(power);
            n /= 2; // divide n by 2 to get the next power of 2
            power *= 2;
        }

        // iterate over queries and calculate the product for each range
        int[] results = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            long cur = 1;
            int product = 1;
            int start = queries[i][0], end = queries[i][1];

            for (int j = start; j <= end; j ++){ // calculate the product of powers in the range
                cur = (cur * powers.get(j)) % 1000000007; // calculate the product modulo 10^9 + 7
            }
            results[i] = (int) cur; // store the result for the current query
        }
        return results; // return the array of results for all queries
    }

    public static void main(String[] args) {
        rangeProductOfQueries_2438 rpq = new rangeProductOfQueries_2438();
        int n = 5; // powers of 2: 1, 2, 4
        int[][] queries = {{0, 1}, {1, 2}, {0, 2}}; // should return products of ranges
        int[] results = rpq.rangeProductQueries(n, queries);
        System.out.println("Range Product Results: " + Arrays.toString(results)); // Output: [2, 8, 8]
    }
}
