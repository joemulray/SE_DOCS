public class EmailService implements Service{

	String message;

	public void update(String message){
		
		/* Open file containing all users registered for email
     		notification. Open connection to the Email server.
    		For all registered clients, notify them via email. */	

		this.message = message;
		System.out.println("NOTIFYING USERS BY EMAIL");
	}
		
	public String toString(){
	
	//To String method to print status of Email message	
	String str = "EmailService Message: " + message ;
	return str;
	
	}


}
