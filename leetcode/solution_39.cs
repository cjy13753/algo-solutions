// Time Complexity: ??
// Space Complexity: ??

public class Solution {
    public IList<IList<int>> CombinationSum(int[] candidates, int target) {
        var result = new List<IList<int>>();

        void dfs(int index, int newTarget, List<int> accumulated)
        {
            if (newTarget == 0)
            {
                result.Add(accumulated);
                return;
            }
            
            for (int i = index; i < candidates.Length; i++)
            {
                var candidate = candidates[i];
                if (candidate <= newTarget)
                {
                    var newList = new List<int>(accumulated);
                    newList.Add(candidate);
                    dfs(i, newTarget - candidate, newList);
                }
            }
        }

        dfs(0, target, new List<int>());

        return result;
    }
}