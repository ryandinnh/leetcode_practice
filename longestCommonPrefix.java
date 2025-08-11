public class longestCommonPrefix {
    public String LongestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) {
            return "";
        }

        String first = strs[0];

        for (int i =0; i < first.length(); i++) {// string is .length() array is .length
            char c = first.charAt(i);
            for (int j = 1; j < strs.length; j++) { // compare character by character
                if (i >= strs[j].length() || strs[j].charAt(i) != c) {
                    return first.substring(0, i); // return the common prefix found so far
                }
            }
        }
        return first; // if we reach here, the entire first string is a common prefix
    }

    public static void main(String[] args) {
        longestCommonPrefix lcp = new longestCommonPrefix();
        String[] strs = {"flower", "flow", "flight"}; // should return "fl"
        String result = lcp.LongestCommonPrefix(strs);
        System.out.println("Longest Common Prefix: " + result); // Output: "fl"
    }
}
