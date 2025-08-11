public class removeDuplicates {
    public int removeDuplicates(int[] nums) {
        // turn nums into a set as it will remove duplicates and then compare length of nums to the set.
        // k = nums.length - set.length
        // modify nums to have the set first?
        //HashSet<Integer> set = new HashSet<>(Arrays.asList(nums)); // only works on objects though need to cast as Integer[]

        // could brute force by iterating over nums as its already in order
        // have two values a read and write index
        // the write index is used to keep track of the previous value in place so you can replace it if there is a duplciate

        if (nums.length == 0){
            return 0;
        }

        int writeIndex = 1;

        for (int readIndex = 1; readIndex < nums.length; readIndex++) {
            if(nums[readIndex] != nums[readIndex - 1]) {
                nums[writeIndex] = nums[readIndex];
                writeIndex++;
            }
        }
        return writeIndex;
    }
}
