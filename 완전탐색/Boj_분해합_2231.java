package 완전탐색;

import java.util.Scanner;

public class Boj_분해합_2231 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.close();

        int result = 0;
        for (int i=1; i<n; i++) {
            int sum = i;
            int tmp = i;

            while (tmp > 0) {
                sum += tmp % 10;
                tmp /=  10;
            }

            if (sum == n) {
                result = i;
                break;
            }
        }

        System.out.println(result);
    }
}
