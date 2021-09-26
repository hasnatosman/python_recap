public class Login{
	public static String password_generator(String num){
		return num.toUpperCase()+Math.floor(Math.random()*1000);
	}
}