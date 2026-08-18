class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        double[][] pairs = new double[n][2];
        for (int i = 0; i<n; i++ ) {
            pairs[i][0] = position[i];
            pairs[i][1] = (double)(target - position[i]) / speed[i];
        }

        Arrays.sort(pairs, (a,b) -> Double.compare(b[0], a[0]));
        Stack<Double> stack = new Stack<>();
        for (double[] pair: pairs) {
            stack.push(pair[1]);
            if(stack.size() >= 2 && stack.peek() <= stack.get(stack.size() - 2)) {
                stack.pop();
            }
        }
        return stack.size();
    }
}
