

import static java.lang.Math.max;

class Solution {
    public int jump(int[] nums) {
        int answer = 0;
        int l = 0;
        int r = 0;

        while(r < nums.length - 1) {
            int farthest = 0;
            for(int i = l; i <= r; i++) {
                farthest = max(farthest, i + nums[i]);
            }
            l =  r + 1;
            r = farthest;
            answer++;
        }

        return answer;
    }
}