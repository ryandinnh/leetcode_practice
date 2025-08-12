public class indexOfFirstOccurenceInString_28{
    public int strStr(String haystack, String needle){
        // brute force approach : 
        // iterate through haystack seeing if needle.charAt(0) matches current haystack.charAt(i)
        // if it does, then check if the rest of needle matches the substring of haystack starting at i
        // if it does, return i
        // continue until we reach end of haystack and return -1 at the end for no match

        if (needle.length() == 0 || haystack.length() < needle.length()) {
            return -1;
        }

        if (haystack.equals(needle)){ // .equals() for string comparison
            return 0;
        }

        for (int i = 0; i <= haystack.length() - needle.length(); i++){
            if (haystack.charAt(i) == needle.charAt(0)){
                //run a nested loop to check if the rest of the needle matches
                for (int j = 1; j < needle.length(); j++){
                    if(haystack.charAt(i+j) != needle.charAt(j) || i + j >= haystack.length()){
                        break; // not a full match
                    }
                    if (j == needle.length() - 1) {
                        return i;
                    }
                }
            }
        }
        return -1; // default return value if no match is found
    }

    public int strStrFast(String haystack, String needle){
        return haystack.indexOf(needle); // built in method
    }

    public static void main(String[] args){
        indexOfFirstOccurenceInString_28 solution = new indexOfFirstOccurenceInString_28();
        String haystack = "runsomewhere";
        String needle = "some";
        int result = solution.strStr(haystack, needle);
        System.out.println(result); // Output should be 3
    }
}