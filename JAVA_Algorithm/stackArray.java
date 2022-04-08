import java.util.Arrays;

public class stackArray {

	public static void main(String[] args) {
		int intArray[]= {1,2,3,4,5,6};
		int sum=0; // 누적합
		
		for (int i=0; i<6; i++) {
			sum+=intArray[i]; // sum에 배열값들을 더해줌
			intArray[i]= sum; // i 인덱스에 sum을 할당
		}
		
		for (int i=0; i<6; i++) {
			System.out.println(intArray[i]);
		}
		
		System.out.println(Arrays.toString(intArray));
	}

}