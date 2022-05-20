package Dictionary;

import java.util.Arrays;

public class Dictionary extends PairMap {
	private int now=0;
	
	public Dictionary(int size) {
		keyArray = new String[size]; // 배열 생성
		valueArray = new String[size];
	}
	
	@Override
	String get(String key) {
		// TODO Auto-generated method stub
		for(int i=0; i<now; i++) {
			if(keyArray[i].equals(key)) {
				return valueArray[i];
			}
		}
		return null;
	}

	@Override
	void put(String key, String value) {
		// TODO Auto-generated method stub
		if (now==0) {
			keyArray[now]=key;
			valueArray[now]=value;
			now++;
		}
		
		if (Arrays.asList(keyArray).contains(key)) {
			valueArray[Arrays.asList(keyArray).indexOf(key)]=value; // key의 인덱스에 value값 갱신
		} else {
			keyArray[now]=key;
			valueArray[now]=value;
			now++;
		}
	}

	@Override
	String delete(String key) {
		// TODO Auto-generated method stub
		for(int i=0; i<now; i++) {
			if(keyArray[i].equals(key)) {
				keyArray[i]=null;
				valueArray[i]=null;
			} // 중간값을 삭제했을 때 한칸씩 땡기기
			for(int k=i; k<now-1; k++) {
				keyArray[k]=keyArray[k+1];
				valueArray[k]=valueArray[k+1];
			}
		}
		now--;
		return null;
	}

	@Override
	int length() {
		// TODO Auto-generated method stub
		return now;
	}

}
