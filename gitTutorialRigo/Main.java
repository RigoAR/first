public class Main {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};
        System.out.println("The average is: " + average(numbers));
    }

    // Fixed average function with explanation this time
    public static double average(int[] nums) {
        double sum = 0; // Initialize sum
        for (int num : nums) {
            sum += num; // Add each number to the sum
        }
        return sum / nums.length; // Return the average
    }
}

