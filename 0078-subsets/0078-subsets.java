class Solution {
    public void backtrack(int[] nums, int index, List<Integer> subset, List<List<Integer>> answer) {
        if (index >= nums.length) {
            answer.add(new ArrayList<>(subset));
            return;
        }
        subset.add(nums[index]);
        backtrack(nums, index + 1, subset, answer);

        subset.removeLast();
        backtrack(nums, index + 1, subset, answer);
        
        return;
    }

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> answer = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();

        backtrack(nums, 0, subset, answer);

        return answer;
    }
}