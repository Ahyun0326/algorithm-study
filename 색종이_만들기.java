import java.util.Scanner;

public class 색종이_만들기 {

    public static int white = 0;
    public static int blue = 0;
    public static int[][] arr;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        arr = new int[n][n];

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                arr[i][j] = sc.nextInt();
            }
        }

        divide(0, 0, n);

        System.out.println(white);
        System.out.println(blue);
    }

    /*
     * 분할 정복
     * 1. 현재 상태의 문제를 풀 수 없는 경우 문제를 분할 할 수 있는지를 확인한다.
     * 2. 문제를 분할하여 각각 풀이한다. (풀이할 수 없는 경우 1번으로 간다.)
     * 3. 풀린 문제들을 합친다.
     */
    public static void divide(int row, int col, int n) {
        // 범위 내 색상이 같은지 확인
        if (colorCheck(row, col, n)) {
            if (arr[row][col] == 1) {
                blue++;
            } else {
                white++;
            }
            return;
        }

        int tmpSize = n/2;

        divide(row, col, tmpSize);
        divide(row+tmpSize, col, tmpSize);
        divide(row, col+tmpSize, tmpSize);
        divide(row+tmpSize, col+tmpSize, tmpSize);
    }

    public static boolean colorCheck(int row, int col, int n) {
        
        int color = arr[row][col];
        
        for(int i=row; i<row+n; i++) {
            for(int j=col; j<col+n; j++) {
                if (arr[i][j] != color) {
                    return false;
                }
            }
        }

        return true;
    }
}