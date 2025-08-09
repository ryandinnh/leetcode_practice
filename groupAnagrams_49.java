import java.util.*;

public class groupAnagrams_49 {
    public List<List<String>> groupAnagrams(String[] strs) {
        // so im thinking we can use a frequency map to count the frequency of each character in the string and compare it with other strings in the array and group it like that
        Map <String, List<String>> map = new HashMap<>();

        //iterate through the array of strings turning each string into a frequency array
        for (String s : strs) {
            int[] count = new int[26]; // 26 bc a-z
            for (char c : s.toCharArray()){ //turns the string into an array of characters
                count[c - 'a']++; //you do -'a' to get the index of the current character it's like subtracting the ASCII value of 'a' from the current character's ASCII value 0-26.
            }

            // convert count[] to a key string to use in the map
            StringBuilder key = new StringBuilder();
            for (int num: count){
                key.append(num).append('#'); // use '#' as a separator to avoid confusion between different counts
            }

            String k = key.toString(); // convert StringBuilder to String

            map.putIfAbsent(k, new ArrayList<>()); // if the key is not present in the map, create a new ArrayList
            map.get(k).add(s); // add the string to the list corresponding to the key
        }

        return new ArrayList<>(map.values()); // return the values of the map as a list of lists
    }
    
    public static void main(String[] args) {
        groupAnagrams_49 solution = new groupAnagrams_49();
        String[] strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
        List<List<String>> result = solution.groupAnagrams(strs);
        System.out.println(result); // Output: [[eat, tea, ate], [tan, nat], [bat]]
    }
}