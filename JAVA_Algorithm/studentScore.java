import java.util.Scanner;

public class studentScore {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		String student[] = new String[5];
		int studentScore[] = new int[5];
		
		for (int i=0; i<5; i++) {
			student[i]=scanner.next(); // [경희, 진수, 민수, 영희, 윤희]
			studentScore[i]=scanner.nextInt(); // [100,  67,  92, 74,  50]
		}
		
		for (int i=0; i<5; i++) {
			switch (studentScore[i]/10) {
			case 10:
			case 9:
				System.out.print(student[i]+" ");
				System.out.print(studentScore[i]+" ");
				System.out.println("A");
				break;
			case 8:
				System.out.print(student[i]+" ");
				System.out.print(studentScore[i]+" ");
				System.out.println("B");
				break;
			case 7:
				System.out.print(student[i]+" ");
				System.out.print(studentScore[i]+" ");
				System.out.println("C");
				break;
			case 6:
				System.out.print(student[i]+" ");
				System.out.print(studentScore[i]+" ");
				System.out.println("D");
				break;
			default:
				System.out.print(student[i]+" ");
				System.out.print(studentScore[i]+" ");
				System.out.println("F");
			}
		}
		scanner.close();
	}
}