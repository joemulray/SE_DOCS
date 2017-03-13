public class PhoneService implements Service{

	String message;

	public void update(String message){
		/* Open file containing all users registered for phone
     		notification. Open connection to the Phone server.
    		For all registered clients, notify them via Phone message. */	
		this.message = message;	

		System.out.println("NOTIFYING USERS BY PHONE");
		
	}


		
	public String toString(){
	
	//toString method to check status of Phone message	
	String str = "PhoneService Message: " + message ;
	return str;
	
	}


}
