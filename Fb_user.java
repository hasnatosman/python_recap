public class Fb_user{
	public static void main(String args[]){
		Facebook hasnat = new Facebook();
		hasnat.first_name = "Hasnat";
		hasnat.last_name = "Osman";
		hasnat.email = "has@gmail.com";
		hasnat.password = Login.password_generator(hasnat.first_name);
		
		System.out.println(hasnat.first_name);
		System.out.println(hasnat.last_name);
		System.out.println(hasnat.email);
		System.out.println(hasnat.password);
	}
}