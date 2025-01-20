class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int time = 0;
        int maxHealth = health;

        for (int[] attack : attacks) {
            int diffTime = attack[0] - time - 1;

            if (diffTime > 0) {
                health += diffTime * bandage[1];
                health += (diffTime / bandage[0]) * bandage[2];
                health = Math.min(health, maxHealth);
            }

            health -= attack[1];
            if (health <= 0) {
                return -1;
            }

            time = attack[0];
        }

        return health;
    }
}