public class soup_servings_808 {
    public double soupServings(int N) {
        // so theres 4 different pours 25, 50, 75, 100 you end once a soup is empty or both are empty
        // use a recursive function to calculate the probability of each pour, recording the results in a memoization map to avoid recomputation
        // state: (a, b) where a is the amount of soup A and b is the amount of soup B
        // Base case (breaks recursion):
        // if a <= 0 and b <= 0, return 0.5 (both soups empty)
        // if a <= 0, return 1 (soup A empty, soup B still has soup)
        // if b <= 0, return 0 (soup B empty, soup A still has soup)
        // Memoization: store results in a 2d array so each state is only solved once
        // order: solve(a,b) -> check memo -> check base case -> compute average -> store in memo -> return result

        // prune large values of n
        if (N >= 4800) {
            return 1.0;
        }

        // scale to 25-ml units for easy calculation
        int n = (N + 24) / 25;

        // memoization array (-1.0 means not computed)
        double[][] memo = new double[n + 1][n + 1];
        for (int i = 0; i <= n; i++) {
            java.util.Arrays.fill(memo[i], -1.0);
        }

        return dfs(n, n, memo);
    }

    // top down recursive function with dfs
    private double dfs(int a, int b, double[][] memo) {
        // memo hit
        if (memo[a][b] >= 0.0) return memo[a][b];

        // base cases
        if (a == 0 && b == 0) return memo[a][b] = 0.5;
        if (a == 0) return memo[a][b] = 1.0;
        if (b == 0) return memo[a][b] = 0.0;

        //helper to clamp to zero (stops index from going negative)
        int a1 = Math.max(a - 4, 0), b1 = Math.max(b - 0, 0);
        int a2 = Math.max(a - 3, 0), b2 = Math.max(b - 1, 0);
        int a3 = Math.max(a - 2, 0), b3 = Math.max(b - 2, 0);
        int a4 = Math.max(a - 1, 0), b4 = Math.max(b - 3, 0);

        // calculate the average of the four possible pours
        double ans = 0.25 * (dfs(a1, b1, memo) + dfs(a2, b2, memo) + dfs(a3, b3, memo) + dfs(a4, b4, memo));

        // store the result in memo
        memo[a][b] = ans;
        return ans;
    }
    public static void main(String[] args) {
        soup_servings_808 solver = new soup_servings_808();
        System.out.println(solver.soupServings(50));   // Example test case
        System.out.println(solver.soupServings(100));  // Another test case
    }
}
